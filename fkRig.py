 # Simple fk rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
import pkmel.ribbon as pr
reload( pc )
reload( rigTools )
reload( pr )

class FkRig( object ) :
	
	def __init__(
					self ,
					parent = '' ,
					animGrp = 'anim_grp' ,
					charSize = 1 ,
					tmpJnt = [] ,
					name = '' ,
					side = '' ,
					ax='y' ,
					shape='circle'
				) :
		
		# Need to have more than one input tmpJnt
		
		# Main group
		self.rigGrp = pc.Null()
		self.rigGrp.name = '%sFkRig%s_grp' % ( name , side )
		if parent :
			mc.parentConstraint( parent , self.rigGrp )
			mc.scaleConstraint( parent , self.rigGrp )
		
		# Rig
		self.ctrls = []
		self.gmbls = []
		self.ofstGrps = []
		self.oriGrps = []
		self.zGrps = []
		self.adds = []
		self.muls = []
		self.sqAdds = []
		self.stAmps = []
		self.sqAmps = []
		
		for ix in range( 0 , ( len( tmpJnt ) - 1 ) ) :
			
			# name = tmpJnt[ix].split( side )[0]
			
			# Create controllers
			ctrl = rigTools.jointControl( shape )
			ctrl.scaleShape( 3 * charSize )
			gmbl = pc.addGimbal( ctrl )
			ofst = pc.group( ctrl )
			ori = pc.group( ofst )
			zGrp = pc.group( ori )
			
			ctrl.name = '%s%dFk%s_ctrl' % ( name , (ix+1) , side )
			gmbl.name = '%s%dFkGmbl%s_ctrl' % ( name , (ix+1) , side )
			ofst.name = '%s%dFkCtrlOfst%s_grp' % ( name , (ix+1) , side )
			ori.name = '%s%dFkCtrlOri%s_grp' % ( name , (ix+1) , side )
			zGrp.name = '%s%dFkCtrlZro%s_grp' % ( name , (ix+1) , side )
			
			ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
			ofst.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
	
			self.ctrls.append( ctrl )
			self.gmbls.append( gmbl )
			self.ofstGrps.append( ofst )
			self.oriGrps.append( ori )
			self.zGrps.append( zGrp )
	
			ctrl.color = 'red'
	
			ctrl.rotateOrder = 'yzx'
			gmbl.rotateOrder = 'yzx'
	
			zGrp.snapPoint( tmpJnt[ix] )
			ctrl.snap( tmpJnt[ix] )
			ctrl.freeze( r=True )
	
			if not ix == 0 :
				self.zGrps[ix].parent( self.gmbls[ ix - 1 ] )
			else :
				self.zGrps[ix].parent( self.rigGrp )

				# Ori loc/wor
				( locGrp ,
				worGrp ,
				worGrpParCons ,
				oriGrpParCons ,
				oriGrpParConsRev ) = rigTools.orientLocalWorldCtrl(
																		ctrl = ctrl ,
																		localObj = zGrp ,
																		worldObj = animGrp ,
																		oriGrp = ori
																	)

				locGrp.name = '%s%dCtrlLoc%s_grp' % ( name , ( ix+1 ) , side )
				worGrp.name = '%s%dCtrlWor%s_grp' % ( name , ( ix+1 ) , side )
				worGrpParCons.name = '%s_parentConstraint1' % worGrp
				oriGrpParCons.name = '%s_parentConstraint1' % ori
				oriGrpParConsRev.name = '%s%dCtrlLocWorOri%s_rev' % ( name , ( ix+1 ) , side )
			
			# Connect to joint
			mc.parentConstraint( gmbl , tmpJnt[ ix ] )
		
		# Squash and stretch
		for ix in range( 0 , ( len( tmpJnt ) - 1 ) ) :
			
			# name = tmpJnt[ix].split( side )[0]
			
			# Stretch
			if ix < ( len( tmpJnt ) - 2 ) :
				# Connect to next zero group
				currAdd , currMul = rigTools.fkStretch( ctrl = self.ctrls[ix] ,
														target = self.zGrps[ ix + 1 ] ,
														ax = ax
														)
		
			else :
				# Connect to the last joint
				currAdd , currMul = rigTools.fkStretch( ctrl = self.ctrls[ix] ,
														target = tmpJnt[ ix + 1 ] ,
														ax = ax
														)
			
			currAdd.name = '%s%dFkStretch%s_add' % ( name , (ix+1) , side )
			currMul.name = '%s%dFkStretch%s_mul' % ( name , (ix+1) , side )
			self.adds.append( currAdd )
			self.muls.append( currMul )
			
			# Squash
			currJnt = pc.Dag( tmpJnt[ix] )
			self.ctrls[ix].add( ln = 'squash' , k = True )
			
			sqAdd = pc.AddDoubleLinear()
			sqAdd.name = '%s%dFkSquash%s_add' % ( name , (ix+1) , side )
			sqAdd.add( ln = 'default' , dv = 1 , min = 1 , max = 1 , k = True )
			
			sqAdd.attr('default') >> sqAdd.attr('i1')
			self.ctrls[ix].attr('squash') >> sqAdd.attr('i2')
			
			for eachAx in ( 'x' , 'y' , 'z' ) :
				if not ax == eachAx :
					sqAdd.attr('o') >> currJnt.attr( 's%s' % eachAx )
			
			# Adjusting squash and stretch attributes amplitude
			currStAmp = rigTools.attrAmper( self.ctrls[ix].attr('stretch') , currMul.attr('i2') , dv = 0.1 )
			currSqAmp = rigTools.attrAmper( self.ctrls[ix].attr('squash') , sqAdd.attr('i2') , dv = 0.1 )
			currStAmp.name = '%s%dFkStretchAmp%s_mul' % ( name , (ix+1) , side )
			currSqAmp.name = '%s%dFkSquashAmp%s_mul' % ( name , (ix+1) , side )
			
			self.stAmps.append( currStAmp )
			self.sqAmps.append( currSqAmp )

		# Group
		self.rigGrp.parent( animGrp )