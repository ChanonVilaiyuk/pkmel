# Root rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class RootRig( object ) :
	
	def __init__( self ,
				animGrp = 'anim_grp' ,
				skinGrp = 'skin_grp' ,
				charSize = 1 ,
				tmpJnt = 'root_tmpJnt' ) :
		
		# Template objects
		root = pc.Dag( tmpJnt )
		anim = pc.Dag( animGrp )
		skin = pc.Dag( skinGrp )
		
		# Skin joint
		self.root_jnt = rigTools.jointAt( root )
		
		mc.parentConstraint( self.root_jnt , root )
		
		# Main group
		self.rootRig_grp = pc.Null()
		
		# control
		self.root_ctrl = rigTools.jointControl( 'circle' )
		self.rootGmbl_ctrl = pc.addGimbal( self.root_ctrl )
		self.rootCtrlZro_grp = rigTools.zeroGroup( self.root_ctrl )
		
		# Parenting and positioning
		self.rootCtrlZro_grp.snap( self.root_jnt )
		self.rootCtrlZro_grp.parent( self.rootRig_grp )
		
		# shape adjustment
		self.root_ctrl.color = 'brown'
		self.root_ctrl.scaleShape( 3 * charSize )
		
		# Connect to joint
		self.rootJnt_parCons = pc.parentConstraint( self.rootGmbl_ctrl , self.root_jnt )
		
		# rotate order adjustment
		self.root_ctrl.rotateOrder = 'xzy'
		self.rootGmbl_ctrl.rotaeOrder = 'xzy'
		
		# Group
		self.root_jnt.parent( skin )
		self.rootRig_grp.parent( anim )
		
		# Rig cleanup
		for attr in ('tx','ty','tz','rx','ry','rz','sx','sy','sz','v') :
			self.rootRig_grp.attr( attr ).l = True

			self.rootCtrlZro_grp.attr( attr ).l = True
		
		for attr in ('sx','sy','sz','v') :
			self.rootGmbl_ctrl.attr( attr ).l = True
			self.root_ctrl.attr( attr ).lockHide()
