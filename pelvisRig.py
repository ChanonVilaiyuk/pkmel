# Pelvis rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class PelvisRig( object ) :
	
	def __init__( self ,
				parent = 'root_jnt' ,
				animGrp = 'anim_grp' ,
				skinGrp = 'skin_grp' ,
				charSize = 1 ,
				tmpJnt = 'pelvis_tmpJnt' ) :
		
		# Checking parent
		rootJnt = pc.Dag( parent )
		if not rootJnt.exists :
			rootJnt = pc.Null()
			rootJnt.parent( skinGrp )
		
		# Template objects
		pelvis = pc.Dag( tmpJnt )
		
		# Skin joint
		self.pelvis_jnt = rigTools.jointAt( pelvis )
		self.pelvisSca_jnt = rigTools.jointAt( pelvis )
		
		self.pelvisSca_jnt.parent( self.pelvis_jnt )
		self.pelvis_jnt.parent( rootJnt )
		
		mc.parentConstraint( self.pelvisSca_jnt , pelvis )
		
		# Main group
		self.pelvisRig_grp = pc.Null()
		self.pelvisRigGrp_parCons = pc.parentConstraint( rootJnt , self.pelvisRig_grp )
		
		# Control
		self.pelvis_ctrl = rigTools.jointControl( 'square' )
		self.pelvisCtrlZro_grp = rigTools.zeroGroup( self.pelvis_ctrl )
		
		# Parenting and positioning
		self.pelvisCtrlZro_grp.snapPoint( self.pelvis_jnt )
		self.pelvis_ctrl.snapOrient( self.pelvis_jnt )
		self.pelvis_ctrl.freeze()
		self.pelvisCtrlZro_grp.parent( self.pelvisRig_grp )
		
		self.pelvisGmbl_ctrl = pc.addGimbal( self.pelvis_ctrl )
		
		# shape adjustment
		self.pelvis_ctrl.color = 'red'
		self.pelvis_ctrl.scaleShape( 3 * charSize )
		
		# Connect to joint
		self.pelvisJnt_parCons = pc.parentConstraint( self.pelvisGmbl_ctrl , self.pelvis_jnt )
		self.pelvisJnt_scaCons = pc.scaleConstraint( self.pelvisGmbl_ctrl , self.pelvisSca_jnt )
		
		# rotate order adjustment
		self.pelvis_ctrl.rotateOrder = 'xzy'
		self.pelvisGmbl_ctrl.rotaeOrder = 'xzy'
		
		# local/world setup
		# orientLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , oriGrp = '' )
		# return locGrp , worGrp , worGrpOriCons , oriGrpOriCons , oriGrpOriConsRev
		self.pelvisLoc_grp , self.pelvisWor_grp , self.pelvisWorGrp_oriCons , self.pelvisZroGrp_oriCons , self.pelvisZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( self.pelvis_ctrl , self.pelvisRig_grp , animGrp , self.pelvisCtrlZro_grp )
		
		# Group
		self.pelvisRig_grp.parent( animGrp )
		
		# Rig cleanup
		rigTools.lockUnusedAttrs( self )
		
		self.pelvis_ctrl.attr('v').lockHide()

