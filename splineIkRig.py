# Spline IK rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

'''
import pkmel.splineIkRig as psir
reload( psir )

ikJnts = ['tailIk1_jnt', 'tailIk2_jnt', 'tailIk3_jnt', 'tailIk4_jnt', 'tailIk5_jnt', 'tailIk6_jnt' ]
ikUpJnts = ['tailIkUp1_jnt', 'tailIkUp2_jnt', 'tailIkUp3_jnt', 'tailIkUp4_jnt', 'tailIkUp5_jnt' ]
ikPosJnts = []
ikCtrlJnts = ['tailIkCtrl1_jnt', 'tailIkCtrl2_jnt', 'tailIkCtrl3_jnt', 'tailIkCtrl4_jnt' ]

ikCrv = 'taiklIkSpline_crv'
ikUpCrv = 'taiklIkUpSpline_crv'
ax = 'z'
aimVec = (0,0,-1)
upVec = (0,1,0)
name = 'tailIk'
side = ''

ikObj = psir.SplineIkRig(ikJnts,ikUpJnts,ikPosJnts,ikCtrlJnts,ikCrv,ikUpCrv,ax,aimVec,upVec,name,side)
'''

class SplineIkRig( object ) :
	
	def __init__(
					self ,
					ikJnts = [] ,
					ikUpJnts = [] ,
					ikPosJnts = [] ,
					ikCtrlJnts = [] ,
					ikCrv = '' ,
					ikUpCrv = '' ,
					ax = 'y' ,
					aimVec = (0,1,0) ,
					upVec = (1,0,0 ) ,
					name = '' ,
					side = ''
				) :
		
		# Info
		self.ik_crv = pc.Dag( ikCrv )
		self.ikUp_crv = pc.Dag( ikUpCrv )
		self.ikJnts = ikJnts
		self.ikUpJnts = ikUpJnts
		self.ikPosJnts = []
		
		self.ikOrig_crv = pc.Dag( mc.duplicate( self.ik_crv , rr=True )[0] )
		self.ikUpOrig_crv = pc.Dag( mc.duplicate( self.ikUp_crv , rr=True )[0] )
		self.ikOrig_crv.name = '%sOrig%s_crv' % ( name , side )
		self.ikUpOrig_crv.name = '%sUpOrig%s_crv' % ( name , side )

		# Pos joints
		if not ikPosJnts :
			# In case of pos joints have not been prepared
			for ix in range( len( self.ikJnts ) ) :
				
				jnt = rigTools.jointAt( self.ikJnts[ix] )
				jnt.name = '%sPos%s%s_jnt' % ( name , (ix+1) , side )
				self.ikPosJnts.append( jnt )
				
				if ix > 0 :
					self.ikPosJnts[ ix ].parent( self.ikPosJnts[ ix - 1 ] )
		else :
			self.ikPosJnts = ikPosJnts

		print self.ikPosJnts
		
		# Main group
		self.rig_grp = pc.group( em=True , n='%sRig%s_grp' % ( name , side ) )
		self.jnt_grp = pc.group( em=True , n='%sJnt%s_grp' % ( name , side ) )
		self.still_grp = pc.group( em=True , n='%sStill%s_grp' % ( name , side ) )
		self.ikh_grp = pc.group( em=True , n='%sIkh%s_grp' % ( name , side ) )
		self.worOri_grp = pc.group( em=True , n='%sWorOri%s_grp' % ( name , side ) )
		
		mc.parent( self.ikPosJnts[0] , self.jnt_grp )
		mc.parent( self.ikUpJnts[0] , self.jnt_grp )
		mc.parent( self.ikJnts[0] , self.jnt_grp )
		mc.parent( self.worOri_grp , self.still_grp )
		
		# IK controller
		self.ikCtrl_grp = pc.group( em=True , n='%sIkCtrl%s_grp' % ( name , side ) )

		self.ctrls = []
		self.gmblCtrls = []
		self.ctrlZros = []

		for ix in range( len( ikCtrlJnts ) ) :
			
			currCtrl = rigTools.jointControl( 'cube' )
			currGmbl = pc.addGimbal( currCtrl )
			currZro = rigTools.zeroGroup( currCtrl )

			currCtrl.color = 'blue'
			currCtrl.name = '%sIk%s%s_ctrl' % ( name , (ix+1) , side )
			currGmbl.name = '%sIk%sGmbl%s_ctrl' % ( name , (ix+1) , side )
			currZro.name = '%sIkCtrl%sZro%s_grp' % ( name , (ix+1) , side )

			currZro.snap( ikCtrlJnts[ix] )

			currCtrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
			mc.parentConstraint( currCtrl , ikCtrlJnts[ix] )
			mc.parent( ikCtrlJnts[ix] , self.jnt_grp )

			self.ctrls.append( currCtrl )
			self.gmblCtrls.append( currGmbl )
			self.ctrlZros.append( currZro )

			if not ix == 0 :
				mc.parent( currZro , self.gmblCtrls[0] )
				locGrp,worGrp,worParCon,zroParCon,locWorRev = rigTools.parentLocalWorldCtrl( currCtrl ,
																								self.gmblCtrls[0] ,
																								self.worOri_grp ,
																								currZro
																							)
				locGrp.name = '%sIk%sCtrlLocOri%s_grp' % ( name , (ix+1) , side )
				worGrp.name = '%sIk%sCtrlWorOri%s_grp' % ( name , (ix+1) , side )
				worParCon.name = '%sIk%sCtrlWorOriGrp%s_parCons' % ( name , (ix+1) , side )
				locWorRev.name = '%sIk%sCtrlLocWorOri%s_rev' % ( name , (ix+1) , side )


		mc.parent( self.ctrlZros[0] , self.ikCtrl_grp )
		mc.parent( self.ikCtrl_grp , self.rig_grp )

		# IK handle
		self.ik_ikh = pc.Ik(
								mc.ikHandle(
												sol='ikSplineSolver' ,
												createCurve=False ,
												parentCurve=False ,
												curve=self.ik_crv ,
												startJoint=self.ikPosJnts[0],
												endEffector=self.ikPosJnts[-1]
											)[0]
							)
		self.ikUp_ikh = pc.Ik( mc.ikHandle(
												sol='ikSplineSolver' ,
												createCurve=False ,
												parentCurve=False ,
												curve=self.ikUp_crv ,
												startJoint=self.ikUpJnts[0],
												endEffector=self.ikUpJnts[-1]
											)[0]
							)
		
		self.ik_ikh.name = '%sPos%s_ikh' % ( name , side )
		self.ikUp_ikh.name = '%sUp%s_ikh' % ( name , side )
		
		self.ik_ikh.parent( self.ikh_grp )
		self.ikUp_ikh.parent( self.ikh_grp )
		
		self.ik_crv.parent( self.still_grp )
		self.ikUp_crv.parent( self.still_grp )
		
		upCrvShp = pc.Dag( self.ikUp_crv )
		# upCrvShp.attr( 'overrideEnabled' ).v = 1
		# upCrvShp.attr( 'overrideDisplayType' ).v = 2
		
		# Ori joints
		self.ikOriJnts = []
		
		for ix in range( len( self.ikPosJnts ) ) :
			jnt = rigTools.jointAt( self.ikPosJnts[ix] )
			# jnt = rigTools.jointAt( self.ikJnts[ix] )
			jnt.name = '%sOri%s%s_jnt' % ( name , (ix+1) , side )
			jnt.parent( self.ikPosJnts[ix] )
			self.ikOriJnts.append( jnt )
		
		# Aim constraints
		for ix in range( len( self.ikOriJnts ) ) :
			if ix <  ( len( self.ikOriJnts ) - 1 ) :
				pc.aimConstraint( self.ikOriJnts[ ix+1 ] ,
									self.ikOriJnts[ ix ] ,
									aim = aimVec , u = upVec ,
									wut = 'object' ,
									wuo = self.ikUpJnts[ ix ] ,
									wu = upVec
								)
		
		# Detail controller
		self.dtlCtrl_grp = pc.group( em=True )
		self.dtlCtrl_grp.name = '%sDtlCtrl%s_grp' % ( name , side )
		self.dtlCtrl_grp.parent( self.rig_grp )
		
		self.dtlCtrls = []
		self.dtlCtrlOriGrps = []
		self.dtlCtrlZroGrps = []
		
		for ix in range( len( self.ikOriJnts ) ) :
			
			ctrl = pc.Control( 'circle' )
			ctrlOriGrp = pc.group( ctrl )
			ctrlZroGrp = pc.group( ctrlOriGrp )
			
			ctrl.color = 'softBlue'
			ctrl.name = '%sDtl%s%s_ctrl' % ( name , (ix+1) , side )
			ctrlOriGrp.name = '%sDtl%sCtrlOri%s_grp' % ( name , (ix+1) , side )
			ctrlZroGrp.name = '%sDtl%sCtrlZro%s_grp' % ( name , (ix+1) , side )
			
			mc.parentConstraint( self.ikOriJnts[ix] , ctrlZroGrp )
			ctrlOriGrp.snap( self.ikJnts[ix] )
			mc.parentConstraint( ctrl , self.ikJnts[ix] )
			mc.scaleConstraint( ctrl , self.ikJnts[ix] )
			ctrlZroGrp.parent( self.dtlCtrl_grp )
			
			self.dtlCtrls.append( ctrl )
			self.dtlCtrlOriGrps.append( ctrlOriGrp )
			self.dtlCtrlZroGrps.append( ctrlZroGrp )
		
		ikCtrlShp = pc.Dag( self.ctrls[0].shape )
		ikCtrlShp.add( ln='detailVis' , k=True , min=0 , max=1 )
		ikCtrlShp.attr( 'detailVis' ) >> self.dtlCtrl_grp.attr('v')
		
		# Auto-Stretch
		self.ctrls[0].add( ln='autoStretch' , min=0 , max=1 , k=True )
		self.ikOrig_crv.parent( self.rig_grp )
		self.ikUpOrig_crv.parent( self.rig_grp )
		self.ikOrig_crv.attr('v').v = 0
		self.ikUpOrig_crv.attr('v').v = 0
		
		self.ikCrvLen_cif = pc.Dag( mc.arclen( self.ik_crv , ch=True ) )
		self.ikUpCrvLen_cif = pc.Dag( mc.arclen( self.ikUp_crv , ch=True ) )
		self.ikOrigCrvLen_cif = pc.Dag( mc.arclen( self.ikOrig_crv , ch=True ) )
		self.ikUpOrigCrvLen_cif = pc.Dag( mc.arclen( self.ikUpOrig_crv , ch=True ) )
		
		self.ikCrvLen_cif.name = '%sCrvLen%s_cif' % ( name , side )
		self.ikUpCrvLen_cif.name = '%sUpCrvLen%s_cif' % ( name , side )
		self.ikOrigCrvLen_cif.name = '%sOrigCrvLen%s_cif' % ( name , side )
		self.ikUpOrigCrvLen_cif.name = '%sUpOrigCrvLen%s_cif' % ( name , side )
		
		self.ikStretch_mdv = pc.MultiplyDivide()
		self.ikUpStretch_mdv = pc.MultiplyDivide()
		self.ikStretch_mdv.name = '%sStretch%s_mdv' % ( name , side )
		self.ikUpStretch_mdv.name = '%sUpStretch%s_mdv' % ( name , side )
		
		self.ikStretch_mdv.attr( 'operation' ).v = 2
		self.ikUpStretch_mdv.attr( 'operation' ).v = 2
		self.ikCrvLen_cif.attr( 'arcLength' ) >> self.ikStretch_mdv.attr( 'i1x' )
		self.ikUpCrvLen_cif.attr( 'arcLength' ) >> self.ikUpStretch_mdv.attr( 'i1x' )
		
		self.ikStretch_bc = pc.BlendColors()
		self.ikUpStretch_bc = pc.BlendColors()
		self.ikStretch_bc.name = '%sStretch%s_bc' % ( name , side )
		self.ikUpStretch_bc.name = '%sUpStretch%s_bc' % ( name , side )
		
		self.ctrls[0].attr( 'autoStretch' ) >> self.ikStretch_bc.attr( 'blender' )
		self.ctrls[0].attr( 'autoStretch' ) >> self.ikUpStretch_bc.attr( 'blender' )
		self.ikCrvLen_cif.attr( 'arcLength' ) >> self.ikStretch_bc.attr( 'color2R' )
		self.ikUpCrvLen_cif.attr( 'arcLength' ) >> self.ikUpStretch_bc.attr( 'color2R' )
		self.ikOrigCrvLen_cif.attr( 'arcLength' ) >> self.ikStretch_bc.attr( 'color1R' )
		self.ikUpOrigCrvLen_cif.attr( 'arcLength' ) >> self.ikUpStretch_bc.attr( 'color1R' )
		
		self.ikStretch_bc.attr( 'outputR' ) >> self.ikStretch_mdv.attr( 'i2x' )
		self.ikUpStretch_bc.attr( 'outputR' ) >> self.ikUpStretch_mdv.attr( 'i2x' )
		
		self.ikPosMdvs = []
		self.ikUpMdvs = []
		
		for ix in range( 1 , len( self.ikPosJnts ) ) :
			
			posJnt = pc.Dag( self.ikPosJnts[ ix ] )
			upJnt = pc.Dag( self.ikUpJnts[ ix ] )
			
			posMdv = pc.MultiplyDivide()
			posMdv.name = '%sStretch%s%s_mdv' % ( name , (ix+1) , side )
			
			upMdv = pc.MultiplyDivide()
			upMdv.name = '%sUpStretch%s%s_mdv' % ( name , (ix+1) , side )
			
			origLen = posJnt.attr( 't%s'%ax ).v
			origUpLen = upJnt.attr( 't%s'%ax ).v
			
			posMdv.attr( 'i2x' ).v = origLen
			upMdv.attr( 'i2x' ).v = origUpLen
			
			self.ikStretch_mdv.attr( 'ox' ) >> posMdv.attr( 'i1x' )
			self.ikUpStretch_mdv.attr( 'ox' ) >> upMdv.attr( 'i1x' )
			
			posMdv.attr( 'ox' ) >> posJnt.attr( 't%s'%ax )
			upMdv.attr( 'ox' ) >> upJnt.attr( 't%s'%ax )
			
			self.ikPosMdvs.append( posMdv )
			self.ikUpMdvs.append( upMdv )





















































