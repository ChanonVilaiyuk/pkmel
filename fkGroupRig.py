 # Simple fk group rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class FkGroupRig( object ) :
	
	def __init__(
					self ,
					parent = 'spine3_jnt' ,
					animGrp = 'anim_grp' ,
					charSize = 1 ,
					tmpJnt = [] ,
					name = ''  ,
					side = '' ,
					shape = 'circle'
				) :

		# Create group of FK controller.
		# Script will create a master controller that will be placed
		# at the middle of input joints.
		# If only one input joint script will generate only one controller.
		
		# Main group
		self.rigGrp = pc.Null()
		self.rigGrp.name = '%sRig%s_grp' % ( name , side )

		if parent :
			mc.parentConstraint( parent , self.rigGrp )
			mc.scaleConstraint( parent , self.rigGrp )
		
		self.ctrl = rigTools.jointControl( shape )
		self.ctrl.scaleShape( 3 * charSize )
		self.gmbl = pc.addGimbal( self.ctrl )
		self.ori = pc.group( self.ctrl )
		self.ofst = pc.group( self.ori )
		self.zGrp = pc.group( self.ofst )
		
		self.ctrl.name = '%s%s_ctrl' % ( name , side )
		self.gmbl.name = '%sGmbl%s_ctrl' % ( name , side )
		self.ori.name = '%sCtrlOri%s_grp' % ( name , side )
		self.ofst.name = '%sCtrlOfst%s_grp' % ( name , side )
		self.zGrp.name = '%sCtrlZro%s_grp' % ( name , side )
		self.ctrl.color = 'blue'
		
		self.ctrl.lockHideAttrs( 'v' )
		self.ofst.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )

		self.zGrp.snapPoint( tmpJnt )
		self.ctrl.snapOrient( tmpJnt )
		self.ctrl.freeze( r=True )
		self.zGrp.parent( self.rigGrp )

		# Add local/world parent
		# ( locGrp ,
		# worGrp ,
		# worGrpParCons ,
		# oriGrpParCons ,
		# oriGrpParConsRev ) = rigTools.parentLocalWorldCtrl(
		# 														ctrl = self.ctrl ,
		# 														localObj = self.ofst ,
		# 														worldObj = animGrp ,
		# 														parGrp = self.ori
		# 													)
		( locGrp ,
		worGrp ,
		worGrpParCons ,
		oriGrpParCons ,
		oriGrpParConsRev ) = rigTools.orientLocalWorldCtrl(
																ctrl = self.ctrl ,
																localObj = self.ofst ,
																worldObj = animGrp ,
																oriGrp = self.ori
															)
		locGrp.name = '%sCtrlLoc%s_grp' % ( name , side )
		worGrp.name = '%sCtrlWor%s_grp' % ( name , side )
		worGrpParCons.name = '%s_parentConstraint1' % worGrp
		oriGrpParCons.name = '%s_parentConstraint1' % self.ori
		oriGrpParConsRev.name = '%sCtrlLocWorOri%s_rev' % ( name , side )

		if len( tmpJnt ) == 1 :

			mc.parentConstraint( self.gmbl , tmpJnt[0] )
			mc.scaleConstraint( self.gmbl , tmpJnt[0] )

		else :

			self.ctrls = []
			self.gmbls = []
			self.ofsts = []
			self.zgrps = []
			
			for ix in range( 0 , len( tmpJnt ) ) :
				
				currCtrl = rigTools.jointControl( shape )
				currCtrl.scaleShape( charSize )
				currGmbl = pc.addGimbal( currCtrl )
				currOri = pc.group( currCtrl )
				currOfst = pc.group( currOri )
				currZGrp = pc.group( currOfst )

				self.ctrls.append( currCtrl )
				self.gmbls.append( currGmbl )
				self.ofsts.append( currOfst )
				self.zgrps.append( currZGrp )

				currCtrl.name = '%s%d%s_ctrl' % ( name , ( ix+1 ) , side )
				currGmbl.name = '%s%dGmbl%s_ctrl' % ( name , ( ix+1 ) , side )
				currOri.name = '%s%dCtrlOri%s_grp' % ( name , ( ix+1 ) , side )
				currOfst.name = '%s%dCtrlOfst%s_grp' % ( name , ( ix+1 ) , side )
				currZGrp.name = '%s%dCtrlZro%s_grp' % ( name , ( ix+1 ) , side )
				currCtrl.color = 'red'

				currCtrl.lockHideAttrs( 'v' )
				currOfst.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )

				currZGrp.snapPoint( tmpJnt[ix] )
				currCtrl.snapOrient( tmpJnt[ix] )
				currCtrl.freeze( r=True )

				currZGrp.parent( self.gmbl )

				mc.parentConstraint( currGmbl , tmpJnt[ix] )
				mc.scaleConstraint( currGmbl , tmpJnt[ix] )

				# Add local/world parent
				# ( locGrp ,
				# worGrp ,
				# worGrpParCons ,
				# oriGrpParCons ,
				# oriGrpParConsRev ) = rigTools.parentLocalWorldCtrl( ctrl = currCtrl ,
				# 													localObj = currOfst ,
				# 													worldObj = animGrp ,
				# 													parGrp = currOri
				# 													)
 				( locGrp ,
				worGrp ,
				worGrpParCons ,
				oriGrpParCons ,
				oriGrpParConsRev ) = rigTools.orientLocalWorldCtrl(
																		ctrl = currCtrl ,
																		localObj = currOfst ,
																		worldObj = animGrp ,
																		oriGrp = currOri
																	)
				locGrp.name = '%s%dCtrlLoc%s_grp' % ( name , ( ix+1 ) , side )
				worGrp.name = '%s%dCtrlWor%s_grp' % ( name , ( ix+1 ) , side )
				worGrpParCons.name = '%s_parentConstraint1' % worGrp
				oriGrpParCons.name = '%s_parentConstraint1' % self.ori
				oriGrpParConsRev.name = '%s%dCtrlLocWorOri%s_rev' % ( name , ( ix+1 ) , side )

		# Group
		self.rigGrp.parent( animGrp )