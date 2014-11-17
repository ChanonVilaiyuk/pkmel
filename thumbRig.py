# Thumb rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class ThumbRig( object ) :
	
	def __init__( self ,
				parent = 'handLFT_jnt' , 
				armCtrl = 'armLFT_ctrl' ,
				side = 'LFT' ,
				animGrp = 'anim_grp' ,
				skinGrp = 'skin_grp' ,
				stillGrp = 'still_grp' ,
				charSize = 1 ,
				tmpJnt = ( 'thumb1LFT_tmpJnt' ,
						'thumb2LFT_tmpJnt' ,
						'thumb3LFT_tmpJnt' ,
						'thumb4LFT_tmpJnt'
						)
				) :
		
		# Checking parent
		wristJnt = pc.Dag( parent )
		if not wristJnt.exists :
			wristJnt = pc.Null()
			wristJnt.parent( skinGrp )
		
		# Template objects
		arm = pc.Dag( armCtrl )
		
		thumb1 = pc.Dag( tmpJnt[0] )
		thumb2 = pc.Dag( tmpJnt[1] )
		thumb3 = pc.Dag( tmpJnt[2])
		thumb4 = pc.Dag( tmpJnt[3] )
		# thumb5 = pc.Dag( tmpJnt[4] )
		
		# Skin joints
		self.thumb1_jnt = rigTools.jointAt( thumb1 )
		self.thumb2_jnt = rigTools.jointAt( thumb2 )
		self.thumb3_jnt = rigTools.jointAt( thumb3 )
		self.thumb4_jnt = rigTools.jointAt( thumb4 )
		
		
		# Skin joint - parenting
		self.thumb1_jnt.parent( wristJnt )
		self.thumb2_jnt.parent( self.thumb1_jnt )
		self.thumb3_jnt.parent( self.thumb2_jnt )
		self.thumb4_jnt.parent( self.thumb3_jnt )
		
		self.thumb1_jnt.attr('segmentScaleCompensate').v = 0
		
		mc.parentConstraint( self.thumb1_jnt , thumb1 )
		mc.parentConstraint( self.thumb2_jnt , thumb2 )
		mc.parentConstraint( self.thumb3_jnt , thumb3 )
		mc.parentConstraint( self.thumb4_jnt , thumb4 )
		
		# Main group
		self.thumbRig_grp = pc.group( em = True )
		self.thumbGrp_parCons = pc.parentConstraint( wristJnt , self.thumbRig_grp )
		self.thumbGrp_scaCons = pc.scaleConstraint( wristJnt , self.thumbRig_grp )
		
		# Thumb control
		self.thumb_ctrl = pc.Control( 'stick' )
		self.thumbCtrlZro_grp = pc.group( self.thumb_ctrl )
		self.thumbCtrlZro_grp.snap( thumb1 )
		self.thumbCtrlZro_grp.parent( self.thumbRig_grp )
		
		# Thumb control - shape adjustment
		self.thumb_ctrl.color = 'blue'
		self.thumb_ctrl.scaleShape( charSize )
		
		# Thumb aim
		self.thumbAim_grp = pc.Null()
		self.thumbAim_grp.snap( thumb2 )
		
		# ----- FK -----
		# FK main group
		self.thumbFk_grp = pc.group( em = True )
		self.thumbFk_grp.snap( self.thumbRig_grp )
		self.thumbFk_grp.parent( self.thumb_ctrl )
		
		# FK controls
		self.thumb1Fk_ctrl = rigTools.jointControl( 'circle' )
		self.thumb1FkCtrlTwst_grp = pc.group( self.thumb1Fk_ctrl )
		self.thumb1FkCtrlSdk_grp = pc.group( self.thumb1FkCtrlTwst_grp )
		self.thumb1FkCtrlZro_grp = pc.group( self.thumb1FkCtrlSdk_grp )
		
		self.thumb2Fk_ctrl = rigTools.jointControl( 'circle' )
		self.thumb2FkCtrlTwst_grp = pc.group( self.thumb2Fk_ctrl )
		self.thumb2FkCtrlSdk_grp = pc.group( self.thumb2FkCtrlTwst_grp )
		self.thumb2FkCtrlZro_grp = pc.group( self.thumb2FkCtrlSdk_grp )
		
		self.thumb3Fk_ctrl = rigTools.jointControl( 'circle' )
		self.thumb3FkCtrlTwst_grp = pc.group( self.thumb3Fk_ctrl )
		self.thumb3FkCtrlSdk_grp = pc.group( self.thumb3FkCtrlTwst_grp )
		self.thumb3FkCtrlZro_grp = pc.group( self.thumb3FkCtrlSdk_grp )
		
		# FK control - parenting and positioning
		self.thumb1FkCtrlZro_grp.snap( thumb1 )
		self.thumb2FkCtrlZro_grp.snap( thumb2 )
		self.thumb3FkCtrlZro_grp.snap( thumb3 )
		
		self.thumb1FkCtrlZro_grp.parent( self.thumbFk_grp )
		self.thumbAim_grp.parent( self.thumb1Fk_ctrl )
		#self.thumbTargetCtrlZro_grp.parent( self.thumb1Fk_ctrl )
		self.thumb2FkCtrlZro_grp.parent( self.thumbAim_grp )
		self.thumb3FkCtrlZro_grp.parent( self.thumb2Fk_ctrl )
		
		# Thumb aim - target local/world orientation
		#self.thumbTargetCtrlLoc_grp,self.thumbTargetCtrlWor_grp,self.thumbTargetCtrlWorGrp_parCons , self.thumbTargetCtrlZroGrp_parCons , self.thumbTargetCtrlZroGrpParCons_rev = rigTools.parentLocalWorldCtrl( self.thumbTarget_ctrl , self.thumb1Fk_ctrl , animGrp , self.thumbTargetCtrlZro_grp )
		
		# FK control - shape adjustment
		self.thumb1Fk_ctrl.color = 'red'
		self.thumb2Fk_ctrl.color = 'red'
		self.thumb3Fk_ctrl.color = 'red'
		self.thumb1Fk_ctrl.scaleShape( 0.5 * charSize )
		self.thumb2Fk_ctrl.scaleShape( 0.5 * charSize )
		self.thumb3Fk_ctrl.scaleShape( 0.5 * charSize )
		
		# FK control - rotate order adjustment
		self.thumb1Fk_ctrl.rotateOrder = 'xzy'
		self.thumb2Fk_ctrl.rotateOrder = 'xzy'
		self.thumb3Fk_ctrl.rotateOrder = 'xzy'
		
		# Thumb aim - aim constraint
		#if side == 'LFT' :
			#self.thumbAimGrp_aimCons = pc.aimConstraint(self.thumbTarget_ctrl,self.thumbAim_grp,aimVector=(0,1,0),upVector=(0,0,1),worldUpType="objectrotation",worldUpVector=(0,0,1),worldUpObject=self.thumb1Fk_ctrl,mo=True)
		#else :
			#self.thumbAimGrp_aimCons = pc.aimConstraint(self.thumbTarget_ctrl,self.thumbAim_grp,aimVector=(0,-1,0),upVector=(0,0,1),worldUpType="objectrotation",worldUpVector=(0,0,1),worldUpObject=self.thumb1Fk_ctrl,mo=True)

		# FK control - stretch control
		self.thumb2FkStretch_add , self.thumb2FkStretch_mul = rigTools.fkStretch( ctrl = self.thumb2Fk_ctrl , target = self.thumb3FkCtrlZro_grp )
		self.thumb3FkStretch_add , self.thumb3FkStretch_mul = rigTools.fkStretch( ctrl = self.thumb3Fk_ctrl , target = self.thumb4_jnt )
		
		# FK control - stretch control - stretch collector
		self.thumb2FkCtrlStretch_pma = pc.PlusMinusAverage()
		self.thumb3FkCtrlStretch_pma = pc.PlusMinusAverage()
		
		self.thumb2FkCtrlStretch_pma.attr('o1') >> self.thumb3FkCtrlZro_grp.attr('ty')
		self.thumb3FkCtrlStretch_pma.attr('o1') >> self.thumb4_jnt.attr('ty')
		
		self.thumb2FkStretch_add.attr('o') >> self.thumb2FkCtrlStretch_pma.last1D()
		self.thumb3FkStretch_add.attr('o') >> self.thumb3FkCtrlStretch_pma.last1D()
		
		# Fk control - adjusting stretch amplitude
		self.thumb2FkStretchAmp_mul = rigTools.attrAmper( self.thumb2Fk_ctrl.attr('stretch') , self.thumb2FkStretch_mul.attr('i2') , dv = 0.1 )
		self.thumb3FkStretchAmp_mul = rigTools.attrAmper( self.thumb3Fk_ctrl.attr('stretch') , self.thumb3FkStretch_mul.attr('i2') , dv = 0.1 )
		
		# FK control - connect to joint
		self.thumb1Jnt_parCons = pc.parentConstraint( self.thumb1Fk_ctrl , self.thumb1_jnt )
		self.thumb2Jnt_parCons = pc.parentConstraint( self.thumb2Fk_ctrl , self.thumb2_jnt )
		self.thumb3Jnt_parCons = pc.parentConstraint( self.thumb3Fk_ctrl , self.thumb3_jnt )
		
		# Attribute control - plusMinusAverage - rotation collector
		self.thumb1FkCtrlSdkRx_pma = pc.PlusMinusAverage()
		self.thumb2FkCtrlSdkRx_pma = pc.PlusMinusAverage()
		self.thumb3FkCtrlSdkRx_pma = pc.PlusMinusAverage()
		
		self.thumb1FkCtrlSdkRy_pma = pc.PlusMinusAverage()
		self.thumb2FkCtrlSdkRy_pma = pc.PlusMinusAverage()
		self.thumb3FkCtrlSdkRy_pma = pc.PlusMinusAverage()
		
		self.thumb1FkCtrlSdkRz_pma = pc.PlusMinusAverage()
		self.thumb2FkCtrlSdkRz_pma = pc.PlusMinusAverage()
		self.thumb3FkCtrlSdkRz_pma = pc.PlusMinusAverage()
		
		self.thumb1FkCtrlSdkRx_pma.attr('o1') >> self.thumb1FkCtrlSdk_grp.attr('rx')
		self.thumb2FkCtrlSdkRx_pma.attr('o1') >> self.thumb2FkCtrlSdk_grp.attr('rx')
		self.thumb3FkCtrlSdkRx_pma.attr('o1') >> self.thumb3FkCtrlSdk_grp.attr('rx')
		
		self.thumb1FkCtrlSdkRy_pma.attr('o1') >> self.thumb1FkCtrlTwst_grp.attr('ry')
		self.thumb2FkCtrlSdkRy_pma.attr('o1') >> self.thumb2FkCtrlTwst_grp.attr('ry')
		self.thumb3FkCtrlSdkRy_pma.attr('o1') >> self.thumb3FkCtrlTwst_grp.attr('ry')
		
		self.thumb1FkCtrlSdkRz_pma.attr('o1') >> self.thumb1FkCtrlSdk_grp.attr('rz')
		self.thumb2FkCtrlSdkRz_pma.attr('o1') >> self.thumb2FkCtrlSdk_grp.attr('rz')
		self.thumb3FkCtrlSdkRz_pma.attr('o1') >> self.thumb3FkCtrlSdk_grp.attr('rz')
		
		# Hand attribute control
		# '__hand__' , 'fist' , 'cup' , 'spread' and 'baseSpread'
		if not arm.attr( '__hand__' ).exists :
			arm.add( ln = '__hand__' , k = True )
			arm.attr( '__hand__' ).set( l = True )
		
		# Hand attribute control - fist
		if not arm.attr( 'fist' ).exists :
			arm.add( ln = 'fist' , k = True )
		
		self.thumb1FistRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb1FkCtrlSdkRx_pma.last1D(),dv=0,ampAttr='thumb1FistRx')
		self.thumb1FistRyAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb1FkCtrlSdkRy_pma.last1D(),dv=0,ampAttr='thumb1FistRy')
		self.thumb1FistRzAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb1FkCtrlSdkRz_pma.last1D(),dv=0,ampAttr='thumb1FistRz')
		
		self.thumb2FistRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb2FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='thumb2FistRx')
		self.thumb2FistRyAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb2FkCtrlSdkRy_pma.last1D(),dv=0,ampAttr='thumb2FistRy')
		self.thumb2FistRzAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb2FkCtrlSdkRz_pma.last1D(),dv=0,ampAttr='thumb2FistRz')
		
		self.thumb3FistRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb3FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='thumb3FistRx')
		self.thumb3FistRyAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb3FkCtrlSdkRy_pma.last1D(),dv=0,ampAttr='thumb3FistRy')
		self.thumb3FistRzAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.thumb3FkCtrlSdkRz_pma.last1D(),dv=0,ampAttr='thumb3FistRz')
		
		# Thumb attribute control
		self.thumb_ctrl.add( ln = '__thumb__' , k = True )
		self.thumb_ctrl.attr( '__thumb__' ).set( l = True )
		
		# Thumb attribute control - fold
		self.thumb_ctrl.add( ln = 'fold' , k = True )
		
		self.thumb2FngrFoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('fold'),targetAttr=self.thumb2FkCtrlSdkRx_pma.last1D(),dv=-9)
		self.thumb3FngrFoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('fold'),targetAttr=self.thumb3FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# Thumb attribute control - stretch
		self.thumb_ctrl.add( ln = 'stretch' , k = True )
		
		self.thumbStretchFngr2_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('stretch'),targetAttr=self.thumb2FkCtrlStretch_pma.last1D(),dv=self.thumb2FkStretch_mul.attr('i1').value)
		self.thumbStretchFngr3_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('stretch'),targetAttr=self.thumb3FkCtrlStretch_pma.last1D(),dv=self.thumb3FkStretch_mul.attr('i1').value)
		
		# fngr attribute control - adjusting stretch amplitude
		self.thumbStretchthumb2Amp_mul = rigTools.attrAmper( self.thumb_ctrl.attr('stretch') , self.thumbStretchFngr2_mul.attr('i2') , dv = 0.1 )
		self.thumbStretchthumb3Amp_mul = rigTools.attrAmper( self.thumb_ctrl.attr('stretch') , self.thumbStretchFngr3_mul.attr('i2') , dv = 0.1 )
		
		# Thumb attribute control - __finger1__
		self.thumb_ctrl.add( ln = '__finger1__' , k = True )
		self.thumb_ctrl.attr( '__finger1__' ).set( l = True )
		
		# Thumb attribute control - __finger1__ - finger1Fold
		self.thumb_ctrl.add( ln = 'finger1Fold' , k = True )
		self.thumb1FoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger1Fold'),targetAttr=self.thumb1FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger1__ - finger1Spread
		self.thumb_ctrl.add( ln = 'finger1Spread' , k = True )
		self.thumb1SpreadAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger1Spread'),targetAttr=self.thumb1FkCtrlSdkRz_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger1__ - finger1Twist
		self.thumb_ctrl.add( ln = 'finger1Twist' , k = True )
		self.thumb1TwistAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger1Twist'),targetAttr=self.thumb1FkCtrlSdkRy_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger2__
		self.thumb_ctrl.add( ln = '__finger2__' , k = True )
		self.thumb_ctrl.attr( '__finger2__' ).set( l = True )
		
		# Thumb attribute control - __finger2__ - finger2Fold
		self.thumb_ctrl.add( ln = 'finger2Fold' , k = True )
		self.thumb2FoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger2Fold'),targetAttr=self.thumb2FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger2__ - finger2Spread
		self.thumb_ctrl.add( ln = 'finger2Spread' , k = True )
		self.thumb2SpreadAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger2Spread'),targetAttr=self.thumb2FkCtrlSdkRz_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger2__ - finger2Twist
		self.thumb_ctrl.add( ln = 'finger2Twist' , k = True )
		self.thumb2TwistAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger2Twist'),targetAttr=self.thumb2FkCtrlSdkRy_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger3__
		self.thumb_ctrl.add( ln = '__finger3__' , k = True )
		self.thumb_ctrl.attr( '__finger3__' ).set( l = True )
		
		# Thumb attribute control - __finger3__ - finger3Fold
		self.thumb_ctrl.add( ln = 'finger3Fold' , k = True )
		self.thumb3FoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger3Fold'),targetAttr=self.thumb3FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger3__ - finger3Spread
		self.thumb_ctrl.add( ln = 'finger3Spread' , k = True )
		self.thumb3SpreadAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger3Spread'),targetAttr=self.thumb3FkCtrlSdkRz_pma.last1D(),dv=-9)
		
		# Thumb attribute control - __finger3__ - finger3Twist
		self.thumb_ctrl.add( ln = 'finger3Twist' , k = True )
		self.thumb3TwistAmp_mul = rigTools.attrAmper(ctrlAttr=self.thumb_ctrl.attr('finger3Twist'),targetAttr=self.thumb3FkCtrlSdkRy_pma.last1D(),dv=-9)
		
		# Group
		self.thumbRig_grp.parent( animGrp )
		
		# Rig cleanup		
		rigTools.lockUnusedAttrs( self )
		self.thumb1Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.thumb2Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.thumb3Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		#self.thumbTarget_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.thumb_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )

