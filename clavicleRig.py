# Clavicle rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class ClavicleRig( object ) :
	
	def __init__( self ,
					parent = 'spine3_jnt' ,
					side = 'LFT' ,
					animGrp = 'anim_grp' ,
					skinGrp = 'skin_grp' ,
					charSize = 1 ,
					tmpJnt = ( 'clavLFT_tmpJnt' , 'upArmLFT_tmpJnt' )
				) :
		
		# Checking parent
		spine3Jnt = pc.Dag( parent )
		if not spine3Jnt.exists :
			spine3Jnt = pc.Null()
			spine3Jnt.parent( skinGrp )
		
		# Template objects
		clav1 = pc.Dag( tmpJnt[0] )
		clav2 = pc.Dag( tmpJnt[1] )
		
		# Skin joints
		self.clav1_jnt = rigTools.jointAt( clav1 )
		self.clav1Sca_jnt = rigTools.jointAt( clav1 )
		self.clav2_jnt = rigTools.jointAt( clav2 )
		
		mc.parentConstraint( self.clav1Sca_jnt , clav1 )
		
		# Skin joints - parenting
		self.clav2_jnt.parent( self.clav1_jnt )
		self.clav1Sca_jnt.parent( self.clav1_jnt )
		self.clav1_jnt.parent( spine3Jnt )
		
		# Main Group
		self.clavRig_grp = pc.Null()
		self.clavRigGrp_parCons = pc.parentConstraint( spine3Jnt , self.clavRig_grp )
		
		# Clavicle control
		self.clav_ctrl = rigTools.jointControl( 'circle' )
		self.clavCtrlZro_grp = rigTools.zeroGroup( self.clav_ctrl )
		
		# Clavicle control - parenting and positioning
		self.clavCtrlZro_grp.snapPoint( self.clav1_jnt )
		self.clav_ctrl.snapOrient( self.clav1_jnt )
		self.clav_ctrl.freeze( r = True , t = False , s = False )
		self.clavCtrlZro_grp.parent( self.clavRig_grp )
		
		self.clavGmbl_ctrl = pc.addGimbal( self.clav_ctrl )
		
		# Clavicle control - shape adjustment
		self.clav_ctrl.color = 'red'
		self.clav_ctrl.scaleShape( 3 * charSize )
		
		# Clavicle control - rotate order adjustment
		self.clav_ctrl.rotateOrder = 'xyz'
		self.clavGmbl_ctrl.rotateOrder = 'xyz'
		
		# Clavicle control - stretch control
		self.clavStretch_add , self.clavStretch_mul = rigTools.fkStretch( ctrl = self.clav_ctrl , target = self.clav2_jnt )
		
		# Clavicle control - adjusting stretch amplitude
		self.clavStretchAmp_mul = rigTools.attrAmper( self.clav_ctrl.attr('stretch') , self.clavStretch_mul.attr('i2') , dv = 0.1 )
		
		# Clavicle control - connect to joint
		self.clav1Jnt_parCons = pc.parentConstraint( self.clavGmbl_ctrl , self.clav1_jnt )
		self.clav1Jnt_scaCons = pc.scaleConstraint( self.clavGmbl_ctrl , self.clav1Sca_jnt )
		
		# Group
		self.clavRig_grp.parent( animGrp )
		
		# Rig cleanup
		rigTools.lockUnusedAttrs( self )
		self.clav_ctrl.attr( 'v' ).lockHide()

