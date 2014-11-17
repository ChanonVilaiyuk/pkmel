# Spine rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
import pkmel.ribbon as pr
reload( pc )
reload( rigTools )
reload( pr )

class HumanSpineRig( object ) :
	
	def __init__(
					self ,
					parent = 'root_jnt' ,
					animGrp = 'anim_grp' ,
					jntGrp = 'jnt_grp' ,
					ikhGrp = 'ikh_grp' ,
					skinGrp = 'skin_grp' ,
					stillGrp = 'still_grp' ,
					ax = 'y' ,
					charSize = 1 ,
					tmpJnt = (
									'spine1_tmpJnt' ,
									'spine2_tmpJnt' ,
									'spine3_tmpJnt' ,
									'spine4_tmpJnt' ,
									'neck1_tmpJnt'
								)
				) :
		
		# Checking parent
		rootJnt = pc.Dag( parent )
		if not rootJnt.exists :
			rootJnt = pc.Null()
			rootJnt.parent( skinGrp )
		
		# Template objects
		spine1 = pc.Dag( tmpJnt[ 0 ] )
		spine2 = pc.Dag( tmpJnt[ 1 ])
		spine3 = pc.Dag( tmpJnt[ 2 ] )
		spine4 = pc.Dag( tmpJnt[ 3 ] )
		spine5 = pc.Dag( tmpJnt[ 4 ] )
		
		# Skin joints
		self.spine1_jnt = rigTools.jointAt( spine1 )
		self.spine2_jnt = rigTools.jointAt( spine2 )
		self.spine3_jnt = rigTools.jointAt( spine3 )
		self.spine4_jnt = rigTools.jointAt( spine4 )
		self.spine5_jnt = pc.Joint()
		
		self.spine5_jnt.snapPoint( spine5 )
		self.spine5_jnt.snapOrient( spine4 )
		self.spine5_jnt.freeze( r = True , t = True )
		self.spine5_jnt.parent( self.spine4_jnt )
		self.spine4_jnt.parent( self.spine3_jnt )
		self.spine3_jnt.parent( self.spine2_jnt )
		self.spine2_jnt.parent( self.spine1_jnt )
		self.spine1_jnt.parent( rootJnt )
		
		# Scale joints
		self.spine1Sca_jnt = rigTools.jointAt( spine1 )
		self.spine2Sca_jnt = rigTools.jointAt( spine2 )
		self.spine3Sca_jnt = rigTools.jointAt( spine3 )
		self.spine4Sca_jnt = rigTools.jointAt( spine4 )
		
		self.spine1Sca_jnt.parent( self.spine1_jnt )
		self.spine2Sca_jnt.parent( self.spine2_jnt )
		self.spine3Sca_jnt.parent( self.spine3_jnt )
		self.spine4Sca_jnt.parent( self.spine4_jnt )
		
		mc.parentConstraint( self.spine1Sca_jnt , spine1 )
		mc.parentConstraint( self.spine2Sca_jnt , spine2 )
		mc.parentConstraint( self.spine3Sca_jnt , spine3 )
		mc.parentConstraint( self.spine4Sca_jnt , spine4 )
		
		# Skin joint - rotate order adjustment
		self.spine1_jnt.rotateOrder = 'yzx'
		self.spine2_jnt.rotateOrder = 'yzx'
		self.spine3_jnt.rotateOrder = 'yzx'
		self.spine4_jnt.rotateOrder = 'yzx'
		self.spine5_jnt.rotateOrder = 'yzx'
		
		# Main group
		self.spineRig_grp = pc.Null()
		self.spineRigGrp_parCons = pc.parentConstraint( rootJnt , self.spineRig_grp )
		
		self.spineJnt_grp = pc.Null()
		self.spineJntGrp_parCons = pc.parentConstraint( rootJnt , self.spineJnt_grp )
		
		# Control
		self.spine1_ctrl = rigTools.jointControl( 'circle' )
		self.spine1Gmbl_ctrl = pc.addGimbal( self.spine1_ctrl )
		self.spine1CtrlZro_grp = pc.group( self.spine1_ctrl )
		self.spine1CtrlOfst_grp = pc.group( self.spine1_ctrl )
		
		self.spine2_ctrl = rigTools.jointControl( 'circle' )
		self.spine2Gmbl_ctrl = pc.addGimbal( self.spine2_ctrl )
		self.spine2CtrlZro_grp = pc.group( self.spine2_ctrl )
		self.spine2CtrlOfst_grp = pc.group( self.spine2_ctrl )
		
		self.spine3_ctrl = rigTools.jointControl( 'circle' )
		self.spine3Gmbl_ctrl = pc.addGimbal( self.spine3_ctrl )
		self.spine3CtrlZro_grp = pc.group( self.spine3_ctrl )
		self.spine3CtrlOfst_grp = pc.group( self.spine3_ctrl )
		
		self.spine4_ctrl = rigTools.jointControl( 'circle' )
		self.spine4Gmbl_ctrl = pc.addGimbal( self.spine4_ctrl )
		self.spine4CtrlZro_grp = pc.group( self.spine4_ctrl )
		self.spine4CtrlOfst_grp = pc.group( self.spine4_ctrl )
		
		# Control - parenting and positioning
		self.spine1CtrlZro_grp.snapPoint( self.spine1_jnt )
		self.spine1_ctrl.snapOrient( self.spine1_jnt )
		self.spine1_ctrl.freeze( r=True )
		
		self.spine2CtrlZro_grp.snapPoint( self.spine1_jnt )
		self.spine2CtrlOfst_grp.snapPoint( self.spine2_jnt )
		self.spine2_ctrl.snapOrient( self.spine2_jnt )
		self.spine2_ctrl.freeze( r=True )
		
		self.spine3CtrlZro_grp.snapPoint( self.spine2_jnt )
		self.spine3CtrlOfst_grp.snapPoint( self.spine3_jnt )
		self.spine3_ctrl.snapOrient( self.spine3_jnt )
		self.spine3_ctrl.freeze( r=True )
		
		self.spine4CtrlZro_grp.snapPoint( self.spine3_jnt )
		self.spine4CtrlOfst_grp.snapPoint( self.spine4_jnt )
		self.spine4_ctrl.snapOrient( self.spine4_jnt )
		self.spine4_ctrl.freeze( r=True )
		
		self.spine2CtrlZroGrp_pntCons = pc.pointConstraint( self.spine1Gmbl_ctrl , self.spine2CtrlZro_grp )
		self.spine2CtrlZroGrp_oriCons = pc.orientConstraint( self.spine1Gmbl_ctrl , self.spine2CtrlZro_grp )
		self.spine3CtrlZroGrp_pntCons = pc.pointConstraint( self.spine2Gmbl_ctrl , self.spine3CtrlZro_grp )
		self.spine3CtrlZroGrp_oriCons = pc.orientConstraint( self.spine2Gmbl_ctrl , self.spine3CtrlZro_grp )
		self.spine4CtrlZroGrp_pntCons = pc.pointConstraint( self.spine3Gmbl_ctrl , self.spine4CtrlZro_grp )
		self.spine4CtrlZroGrp_oriCons = pc.orientConstraint( self.spine3Gmbl_ctrl , self.spine4CtrlZro_grp )
		
		self.spine4CtrlZro_grp.parent( self.spineRig_grp )
		self.spine3CtrlZro_grp.parent( self.spineRig_grp )
		self.spine2CtrlZro_grp.parent( self.spineRig_grp )
		self.spine1CtrlZro_grp.parent( self.spineRig_grp )
		
		# Control - shape adjustment
		self.spine1_ctrl.color = 'red'
		self.spine2_ctrl.color = 'red'
		self.spine3_ctrl.color = 'red'
		self.spine4_ctrl.color = 'red'
		self.spine1_ctrl.scaleShape( 3 * charSize )
		self.spine2_ctrl.scaleShape( 3 * charSize )
		self.spine3_ctrl.scaleShape( 3 * charSize )
		self.spine4_ctrl.scaleShape( 3 * charSize )
		
		# Control - rotate order adjustment
		self.spine1_ctrl.rotateOrder = 'yzx'
		self.spine1Gmbl_ctrl.rotateOrder = 'yzx'
		self.spine2_ctrl.rotateOrder = 'yzx'
		self.spine2Gmbl_ctrl.rotateOrder = 'yzx'
		self.spine3_ctrl.rotateOrder = 'yzx'
		self.spine3Gmbl_ctrl.rotateOrder = 'yzx'
		self.spine4_ctrl.rotateOrder = 'yzx'
		self.spine4Gmbl_ctrl.rotateOrder = 'yzx'
		
		# Control - stretch setup
		self.spine1Stretch_add , self.spine1Stretch_mul = rigTools.fkStretch( ctrl = self.spine1_ctrl ,
									target = self.spine2CtrlOfst_grp ,
									ax = ax )
		self.spine2Stretch_add , self.spine2Stretch_mul = rigTools.fkStretch( ctrl = self.spine2_ctrl ,
									target = self.spine3CtrlOfst_grp ,
									ax = ax )
		self.spine3Stretch_add , self.spine3Stretch_mul = rigTools.fkStretch( ctrl = self.spine3_ctrl ,
									target = self.spine4CtrlOfst_grp ,
									ax = ax )
		self.spine4Stretch_add , self.spine4Stretch_mul = rigTools.fkStretch( ctrl = self.spine4_ctrl ,
									target = self.spine5_jnt ,
									ax = ax )
		
		# Control - adjusting stretch amplitude
		self.spine1StretchAmp_mul = rigTools.attrAmper( self.spine1_ctrl.attr('stretch') , self.spine1Stretch_mul.attr('i2') , dv = 0.1 )
		self.spine2StretchAmp_mul = rigTools.attrAmper( self.spine2_ctrl.attr('stretch') , self.spine2Stretch_mul.attr('i2') , dv = 0.1 )
		self.spine3StretchAmp_mul = rigTools.attrAmper( self.spine3_ctrl.attr('stretch') , self.spine3Stretch_mul.attr('i2') , dv = 0.1 )
		self.spine4StretchAmp_mul = rigTools.attrAmper( self.spine4_ctrl.attr('stretch') , self.spine4Stretch_mul.attr('i2') , dv = 0.1 )
		
		# Control - local/world setup
		# parentLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , oriGrp = '' )
		# return locGrp , worGrp , worGrpParCons , parGrpParCons , parGrpParConsRev
		self.spine1CtrlLoc_grp,self.spine1CtrlWor_grp,self.spine1CtrlWorGrp_oriCons,self.spine1CtrlZroGrp_oriCons,self.spine1CtrlZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( self.spine1_ctrl , self.spineRig_grp , animGrp , self.spine1CtrlZro_grp )
		
		# Control - connect to joint
		self.spine1Jnt_parCons = pc.parentConstraint( self.spine1Gmbl_ctrl , self.spine1_jnt )
		self.spine2Jnt_parCons = pc.parentConstraint( self.spine2Gmbl_ctrl , self.spine2_jnt )
		self.spine3Jnt_parCons = pc.parentConstraint( self.spine3Gmbl_ctrl , self.spine3_jnt )
		self.spine4Jnt_parCons = pc.parentConstraint( self.spine4Gmbl_ctrl , self.spine4_jnt )
		
		self.spine1Jnt_scaCons = pc.scaleConstraint( self.spine1Gmbl_ctrl , self.spine1Sca_jnt )
		self.spine2Jnt_scaCons = pc.scaleConstraint( self.spine2Gmbl_ctrl , self.spine2Sca_jnt )
		self.spine3Jnt_scaCons = pc.scaleConstraint( self.spine3Gmbl_ctrl , self.spine3Sca_jnt )
		self.spine4Jnt_scaCons = pc.scaleConstraint( self.spine4Gmbl_ctrl , self.spine4Sca_jnt )
		
		# Group
		self.spineRig_grp.parent( animGrp )
		self.spineJnt_grp.parent( jntGrp )
		
		# Rig cleanup
		rigTools.lockUnusedAttrs( self )
		
		self.spine1_ctrl.attr( 'v' ).lockHide()
		self.spine2_ctrl.attr( 'v' ).lockHide()
		self.spine3_ctrl.attr( 'v' ).lockHide()
		self.spine4_ctrl.attr( 'v' ).lockHide()
		