# Arm rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
import pkmel.ribbon as pr
reload( pc )
reload( rigTools )
reload( pr )

class ArmRig( object ) :
	
	def __init__( self ,
				parent = 'clav2LFT_jnt' ,
				side = 'LFT' ,
				animGrp = 'anim_grp' ,
				jntGrp = 'jnt_grp' ,
				ikhGrp = 'ikh_grp' ,
				skinGrp = 'skin_grp' ,
				stillGrp = 'still_grp' ,
				ribbon = True ,
				charSize = 1 ,
				tmpJnt = ( 'upArmLFT_tmpJnt' ,
							'forearmLFT_tmpJnt' ,
							'wristLFT_tmpJnt' ,
							'handLFT_tmpJnt' ,
							'elbowIkLFT_tmpJnt' )
				) :
		
		# Checking parent
		clav2Jnt = pc.Dag( parent )
		if not clav2Jnt.exists :
			clav2Jnt = pc.Null()
			clav2Jnt.parent( skinGrp )
		
		# Template objects
		upArm = pc.Dag( tmpJnt[0] )
		forearm = pc.Dag( tmpJnt[1] )
		wrist = pc.Dag( tmpJnt[2] )
		hand = pc.Dag( tmpJnt[3] )
		
		elbowIkCtrl = pc.Dag( tmpJnt[4] )
		
		# Skin joints
		self.upArm_jnt = rigTools.jointAt( upArm )
		self.forearm_jnt = rigTools.jointAt( forearm )
		self.wrist_jnt = rigTools.jointAt( wrist )
		self.hand_jnt = rigTools.jointAt( hand )
		
		# Skin joints - parenting
		self.hand_jnt.parent( self.wrist_jnt )
		self.wrist_jnt.parent( self.forearm_jnt )
		self.forearm_jnt.parent( self.upArm_jnt )
		self.upArm_jnt.parent( clav2Jnt )

		self.hand_jnt.attr('ssc').v = 0
		
		mc.parentConstraint( self.upArm_jnt , upArm )
		mc.parentConstraint( self.forearm_jnt , forearm )
		mc.parentConstraint( self.wrist_jnt , wrist )
		mc.parentConstraint( self.hand_jnt , hand )
		
		# Main group
		self.armRig_grp = pc.Null()
		self.armRigGrp_parCons = pc.parentConstraint( clav2Jnt , self.armRig_grp )
		
		self.armJnt_grp = pc.Null()
		self.armJntGrp_parCons = pc.parentConstraint( clav2Jnt , self.armJnt_grp )
		
		# Length
		self.upArmLen = pc.distance( upArm , forearm )
		self.forearmLen = pc.distance( forearm , wrist )
		
		# Joint - rotate order
		self.upArm_jnt.rotateOrder = 'yzx'
		self.forearm_jnt.rotateOrder = 'yzx'
		self.wrist_jnt.rotateOrder = 'yzx'
		self.hand_jnt.rotateOrder = 'yzx'
		
		# Arm control
		self.arm_ctrl = pc.Control( 'stick' )
		self.armCtrl_grp = pc.group( self.arm_ctrl )
		self.armCtrlGrp_parCons = pc.parentConstraint( self.wrist_jnt , self.armCtrl_grp )
		self.armCtrl_grp.parent( self.armRig_grp )
		
		# Arm control - hand scale attribute
		self.arm_ctrl.add( ln='handScale' , dv=1 , k=True )
		self.arm_ctrl.attr( 'handScale' ) >> self.wrist_jnt.attr( 'sx' )
		self.arm_ctrl.attr( 'handScale' ) >> self.wrist_jnt.attr( 'sy' )
		self.arm_ctrl.attr( 'handScale' ) >> self.wrist_jnt.attr( 'sz' )
		
		# Arm control - shape adjustment
		self.arm_ctrl.color = 'green'
		self.arm_ctrl.scaleShape( 3 * charSize )
		
		# ----- FK -----
		# FK main groups
		self.armFkCtrl_grp = pc.Null()
		self.armFkJnt_grp = pc.Null()
		
		self.armFkCtrl_grp.snap( clav2Jnt )
		self.armFkJnt_grp.snap( clav2Jnt )
		self.armFkCtrl_grp.parent( self.armRig_grp )
		self.armFkJnt_grp.parent( self.armJnt_grp )
		
		# FK joints
		self.upArmFk_jnt = rigTools.jointAt( upArm )
		self.forearmFk_jnt = rigTools.jointAt( forearm )
		self.wristFk_jnt = rigTools.jointAt( wrist )
		self.handFk_jnt = rigTools.jointAt( hand )
		
		self.handFk_jnt.parent( self.wristFk_jnt )
		self.wristFk_jnt.parent( self.forearmFk_jnt )
		self.forearmFk_jnt.parent( self.upArmFk_jnt )
		self.upArmFk_jnt.parent( self.armFkJnt_grp )
		
		self.upArmFk_jnt.rotateOrder = 'yzx'
		self.forearmFk_jnt.rotateOrder = 'yzx'
		self.wristFk_jnt.rotateOrder = 'yzx'
		self.handFk_jnt.rotateOrder = 'yzx'
		
		# FK controls
		self.upArmFk_ctrl = rigTools.jointControl( 'circle' )
		self.upArmFkCtrlZro_grp = rigTools.zeroGroup( self.upArmFk_ctrl )
		
		self.forearmFk_ctrl = rigTools.jointControl( 'circle' )
		self.forearmFkGmbl_ctrl = pc.addGimbal( self.forearmFk_ctrl )
		self.forearmFkCtrlZro_grp = rigTools.zeroGroup( self.forearmFk_ctrl )
		
		self.wristFk_ctrl = rigTools.jointControl( 'circle' )
		self.wristFkGmbl_ctrl = pc.addGimbal( self.wristFk_ctrl )
		self.wristFkCtrlZro_grp = rigTools.zeroGroup( self.wristFk_ctrl )
		
		# FK control - parenting and positioning
		self.upArmFk_ctrl.snapOrient( upArm )
		self.upArmFk_ctrl.freeze( r = True , t = False , s = False )
		
		self.upArmFkGmbl_ctrl = pc.addGimbal( self.upArmFk_ctrl )
		
		self.wristFkCtrlZro_grp.snap( wrist )
		self.forearmFkCtrlZro_grp.snap( forearm )
		self.upArmFkCtrlZro_grp.snapPoint( upArm )
		
		self.wristFkCtrlZro_grp.parent( self.forearmFkGmbl_ctrl )
		self.forearmFkCtrlZro_grp.parent( self.upArmFkGmbl_ctrl )
		self.upArmFkCtrlZro_grp.parent( self.armFkCtrl_grp )
		
		# FK control - shape adjustment
		self.upArmFk_ctrl.color = 'red'
		self.forearmFk_ctrl.color = 'red'
		self.wristFk_ctrl.color = 'red'
		
		self.upArmFk_ctrl.scaleShape( 3 * charSize )
		self.forearmFk_ctrl.scaleShape( 3 * charSize )
		self.wristFk_ctrl.scaleShape( 3 * charSize )
		
		# FK control - rotate order adjustment
		self.upArmFk_ctrl.rotateOrder = 'yxz'
		self.upArmFkGmbl_ctrl.rotateOrder = 'yxz'
		self.forearmFk_ctrl.rotateOrder = 'yxz'
		self.forearmFkGmbl_ctrl.rotateOrder = 'yxz'
		self.wristFk_ctrl.rotateOrder = 'yxz'
		self.wristFkGmbl_ctrl.rotateOrder = 'yxz'
		
		# FK control - stretch control
		( self.upArmFkStretch_add ,
		self.upArmFkStretch_mul ) = rigTools.fkStretch( ctrl = self.upArmFk_ctrl ,
													target = self.forearmFkCtrlZro_grp
													)
		( self.forearmFkStretch_add ,
		self.forearmFkStretch_mul ) = rigTools.fkStretch( ctrl = self.forearmFk_ctrl ,
													target = self.wristFkCtrlZro_grp
													)
		
		# FK control - Adjusting stretch amplitude
		self.upArmFkStretchAmp_mul = rigTools.attrAmper( self.upArmFk_ctrl.attr('stretch') , self.upArmFkStretch_mul.attr('i2') , dv = 0.1 )
		self.forearmFkStretchAmp_mul = rigTools.attrAmper( self.forearmFk_ctrl.attr('stretch') , self.forearmFkStretch_mul.attr('i2') , dv = 0.1 )
		
		# FK control - connect to joint
		self.upArmFkJnt_parCons = pc.parentConstraint( self.upArmFkGmbl_ctrl , self.upArmFk_jnt )
		self.forearmFkJnt_parCons = pc.parentConstraint( self.forearmFkGmbl_ctrl , self.forearmFk_jnt )
		self.wristFkJnt_parCons = pc.parentConstraint( self.wristFkGmbl_ctrl , self.wristFk_jnt )
		
		# FK control - local/world setup
		self.upArmFkCtrlLoc_grp,self.upArmFkCtrlWor_grp,self.upArmFkCtrlWorGrp_oriCons,self.upArmFkCtrlZroGrp_oriCons,self.upArmFkCtrlZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( self.upArmFk_ctrl , self.armFkCtrl_grp , animGrp , self.upArmFkCtrlZro_grp )
		
		# ----- IK -----
		# IK main groups
		self.armIkCtrl_grp = pc.Null()
		self.armIkJnt_grp = pc.Null()
		
		self.armIkCtrl_grp.snap( clav2Jnt )
		self.armIkJnt_grp.snap( clav2Jnt )
		self.armIkCtrl_grp.parent( self.armRig_grp )
		self.armIkJnt_grp.parent( self.armJnt_grp )
		
		# IK joints
		self.upArmIk_jnt = rigTools.jointAt( upArm )
		self.forearmIk_jnt = rigTools.jointAt( forearm)
		self.wristIk_jnt = rigTools.jointAt( wrist )
		self.handIk_jnt = rigTools.jointAt( hand )
		
		self.handIk_jnt.parent( self.wristIk_jnt )
		self.wristIk_jnt.parent( self.forearmIk_jnt )
		self.forearmIk_jnt.parent( self.upArmIk_jnt )
		self.upArmIk_jnt.parent( self.armIkJnt_grp )
		
		self.upArmIk_jnt.rotateOrder = 'yzx'
		self.forearmIk_jnt.rotateOrder = 'yzx'
		self.wristIk_jnt.rotateOrder = 'yzx'
		self.handIk_jnt.rotateOrder = 'yzx'
		
		# IK controls
		self.armIkRoot_ctrl = rigTools.jointControl( 'cube' )
		self.armIkRootCtrlZro_grp = pc.group( self.armIkRoot_ctrl )
		
		self.armIk_ctrl = rigTools.jointControl( 'cube' )
		self.armIkCtrlLock_grp = pc.group( self.armIk_ctrl )
		self.armIkCtrlZro_grp = pc.group( self.armIkCtrlLock_grp )
		
		self.elbowIk_ctrl = pc.Control( 'plus' )
		self.elbowIkCtrlZro_grp = pc.group( self.elbowIk_ctrl )
		
		# IK control - parenting and positioning
		self.armIkRootCtrlZro_grp.snapPoint( upArm )
		self.armIkCtrlZro_grp.snapPoint( wrist )
		self.elbowIkCtrlZro_grp.snapPoint( elbowIkCtrl )
		
		self.armIk_ctrl.snapOrient( wrist )
		self.armIk_ctrl.freeze( t = False , r = True , s = False )
		self.armIkCon_ctrl = pc.addConCtrl( self.armIk_ctrl )
		self.armIkGmbl_ctrl = pc.addGimbal( self.armIk_ctrl )
		
		self.armIkRootCtrlZro_grp.parent( self.armIkCtrl_grp )
		self.armIkCtrlZro_grp.parent( self.armIkRoot_ctrl )
		self.elbowIkCtrlZro_grp.parent( self.armIkRoot_ctrl )
		self.armIkRootCtrlZroGrp_oriCons = pc.orientConstraint( animGrp , self.armIkRootCtrlZro_grp )
		
		# IK control - shape adjustment
		self.armIkRoot_ctrl.color = 'blue'
		self.armIk_ctrl.color = 'blue'
		self.elbowIk_ctrl.color = 'blue'
		self.armIkRoot_ctrl.scaleShape( 3 * charSize )
		self.armIk_ctrl.scaleShape( 3 * charSize )
		self.elbowIk_ctrl.scaleShape( 3 * charSize )
		
		# IK control - elbow curve
		self.elbowIkCtrl_crv , self.elbowIkCtrl1_clstr , self.elbowIkCtrl2_clstr = rigTools.crvGuide( ctrl = self.elbowIk_ctrl , target = self.forearmIk_jnt )
		
		self.elbowIkCtrl_crv.attr('inheritsTransform').value = 0
		self.elbowIkCtrl_crv.attr('overrideEnabled').value = 1
		self.elbowIkCtrl_crv.attr('overrideDisplayType').value = 2
		
		self.elbowIkCtrl_crv.parent( self.armIkCtrl_grp )
		self.elbowIkCtrl_crv.attr('t').value = (0,0,0)
		self.elbowIkCtrl_crv.attr('r').value = (0,0,0)
		
		# IK control - rotate order adjustment
		self.armIk_ctrl.rotateOrder = 'zxy'
		self.armIkGmbl_ctrl.rotateOrder = 'zxy'
		
		# IK control - local/world setup
		# parentLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , oriGrp = '' )
		# return locGrp , worGrp , worGrpParCons , parGrpParCons , parGrpParConsRev
		self.armIkCtrlLoc_grp,self.armIkCtrlWor_grp,self.armIkCtrlWorGrp_oriCons,self.armIkCtrlZroGrp_oriCons,self.armIkCtrlZroGrpOriCons_rev = rigTools.parentLocalWorldCtrl( self.armIk_ctrl , self.armIkRoot_ctrl , animGrp , self.armIkCtrlZro_grp )
		self.elbowIkCtrlLoc_grp,self.elbowIkCtrlWor_grp,self.elbowIkCtrlWorGrp_oriCons,self.elbowIkCtrlZroGrp_oriCons,self.elbowIkCtrlZroGrpOriCons_rev = rigTools.parentLocalWorldCtrl( self.elbowIk_ctrl , self.armIk_ctrl , animGrp , self.elbowIkCtrlZro_grp )
		
		# IK handles
		self.armIk_ikh = pc.IkRp( sj = self.upArmIk_jnt , ee = self.wristIk_jnt )
		self.handIk_ikh = pc.IkRp( sj = self.wristIk_jnt , ee = self.handIk_jnt )
		self.armIkIkh_polCons = pc.poleVectorConstraint( self.elbowIk_ctrl , self.armIk_ikh )
		
		self.armIkIkh_grp = pc.Null()
		self.armIkIkhZro_grp = rigTools.zeroGroup( self.armIk_ikh )
		self.handIkIkhZro_grp = rigTools.zeroGroup( self.handIk_ikh )
		
		self.armIkIkhZro_grp.parent( self.armIkIkh_grp )
		self.handIkIkhZro_grp.parent( self.armIkIkh_grp )
		self.armIkIkh_grp.parent( ikhGrp )
		
		# IK handles - pivot
		self.handIkPiv_grp = pc.Null()
		self.armIkIkhPiv_grp = pc.Null()
		self.handIkIkhPiv_grp = pc.Null()
		
		# IK handles - pivots - positioning and parenting
		self.handIkPiv_grp.snapPoint( wrist )
		self.armIkIkhPiv_grp.snap( self.armIkIkhZro_grp )
		self.handIkIkhPiv_grp.snap( self.handIkIkhZro_grp )
		
		self.upArmIkJnt_pntCons = pc.pointConstraint( self.armIkRoot_ctrl , self.upArmIk_jnt )
		self.armIkIkhPiv_grp.parent( self.handIkPiv_grp )
		self.handIkIkhPiv_grp.parent( self.handIkPiv_grp )
		self.handIkPiv_grp.parent( self.armIkGmbl_ctrl )
		
		self.armIkIkhZroGrp_parCons = pc.parentConstraint( self.armIkIkhPiv_grp , self.armIkIkhZro_grp )
		self.handIkIkhZroGrp_parCons = pc.parentConstraint( self.handIkIkhPiv_grp , self.handIkIkhZro_grp )
		
		# IK twist
		self.armIk_ctrl.add( ln = 'twist' , k = True )
		self.armIk_ctrl.attr('twist') >> self.armIk_ikh.attr('twist')
		
		# IK stretch - Attributes
		self.armIk_ctrl.add( ln = '__stretch__' , k = True )
		self.armIk_ctrl.attr('__stretch__').set( l = True )
		self.armIk_ctrl.add( ln = 'autoStretch' , min = 0 , max = 1 , k = True )
		self.armIk_ctrl.add( ln = 'upArmStretch' , k = True )
		self.armIk_ctrl.add( ln = 'forearmStretch' , k = True )
		
		# IK Auto stretch
		self.upArmIkJntPnt_grp = pc.Null()
		self.upArmIkJntPntGrp_pntCons = pc.pointConstraint( self.armIkRoot_ctrl , self.upArmIkJntPnt_grp )
		self.armIkCtrlPnt_grp = pc.Null()
		self.armIkCtrlPntGrp_pntCons = pc.pointConstraint( self.armIkIkhZro_grp , self.armIkCtrlPnt_grp )
		self.elbowIkCtrlPnt_grp = pc.Null()
		self.elbowIkCtrlPntGrp_pntCons = pc.pointConstraint( self.elbowIk_ctrl , self.elbowIkCtrlPnt_grp )
		
		self.upArmIkJntPnt_grp.parent( self.armIkCtrl_grp )
		self.armIkCtrlPnt_grp.parent( self.armIkCtrl_grp )
		self.elbowIkCtrlPnt_grp.parent( self.armIkCtrl_grp )
		
		self.armIkAutoStretch_dist = pc.DistanceBetween()
		self.upArmIkLock_dist = pc.DistanceBetween()
		self.forearmIkLock_dist = pc.DistanceBetween()
		
		self.upArmIkJntPnt_grp.attr('t') >> self.armIkAutoStretch_dist.attr('p1')
		self.armIkCtrlPnt_grp.attr('t') >> self.armIkAutoStretch_dist.attr('p2')
		self.upArmIkJntPnt_grp.attr('t') >> self.upArmIkLock_dist.attr('p1')
		self.elbowIkCtrlPnt_grp.attr('t') >> self.upArmIkLock_dist.attr('p2')
		self.elbowIkCtrlPnt_grp.attr('t') >> self.forearmIkLock_dist.attr('p1')
		self.armIkCtrlPnt_grp.attr('t') >> self.forearmIkLock_dist.attr('p2')
		
		self.armIkAutoStretch_cnd = pc.Condition()
		self.armIkAutoStretch_mul = pc.MultDoubleLinear()
		
		self.upArmIkAutoStretch_mul = pc.MultDoubleLinear()
		self.upArmIkStretch_mul = pc.MultDoubleLinear()
		self.upArmIkAutoStretch_add = pc.AddDoubleLinear()
		self.upArmIkAutoStretch_blnd = pc.BlendTwoAttr()
		
		self.forearmIkAutoStretch_mul = pc.MultDoubleLinear()
		self.forearmIkStretch_mul = pc.MultDoubleLinear()
		self.forearmIkAutoStretch_add = pc.AddDoubleLinear()
		self.forearmIkAutoStretch_blnd = pc.BlendTwoAttr()
		
		# IK Stretch - Auto stretch
		ikCtrlDist = self.armIkAutoStretch_dist.attr('d').value
		upArmDist = self.forearmIk_jnt.attr('ty').value
		forearmDist = self.wristIk_jnt.attr('ty').value
		
		self.armIkAutoStretch_dist.attr('d') >> self.armIkAutoStretch_cnd.attr('ft')
		self.armIkAutoStretch_cnd.attr('st').value = ikCtrlDist
		self.armIkAutoStretch_cnd.attr('op').value = 2
		self.armIkAutoStretch_cnd.attr('cfr').value = 1
		self.armIkAutoStretch_dist.attr('d') >> self.armIkAutoStretch_mul.attr('i1')
		self.armIkAutoStretch_mul.attr('i2').value = 1/ikCtrlDist
		self.armIkAutoStretch_mul.attr('o') >> self.armIkAutoStretch_cnd.attr('ctr')
		
		# IK Stretch - Auto stretch, upper arm
		self.armIkAutoStretch_cnd.attr('ocr') >> self.upArmIkAutoStretch_mul.attr('i1')
		self.upArmIkAutoStretch_mul.attr('i2').value = upArmDist
		
		self.armIk_ctrl.attr('autoStretch') >> self.upArmIkAutoStretch_blnd.attr('ab')
		self.upArmIkAutoStretch_blnd.add( ln = 'default' , dv = upArmDist , k = True )
		self.upArmIkAutoStretch_blnd.attr('default') >> self.upArmIkAutoStretch_blnd.last()
		self.upArmIkAutoStretch_mul.attr('o') >> self.upArmIkAutoStretch_blnd.last()
		self.upArmIkAutoStretch_blnd.attr('o') >> self.upArmIkAutoStretch_add.attr('i1')
		
		self.armIk_ctrl.attr('upArmStretch') >> self.upArmIkStretch_mul.attr('i1')
		self.upArmIkStretch_mul.attr('i2').value = upArmDist
		self.upArmIkStretch_mul.attr('o') >> self.upArmIkAutoStretch_add.attr('i2')
		
		# IK Stretch - Auto stretch, forearm
		self.armIkAutoStretch_cnd.attr('ocr') >> self.forearmIkAutoStretch_mul.attr('i1')
		self.forearmIkAutoStretch_mul.attr('i2').value = forearmDist
		
		self.armIk_ctrl.attr('autoStretch') >> self.forearmIkAutoStretch_blnd.attr('ab')
		self.forearmIkAutoStretch_blnd.add( ln = 'default' , dv = forearmDist , k = True )
		self.forearmIkAutoStretch_blnd.attr('default') >> self.forearmIkAutoStretch_blnd.last()
		self.forearmIkAutoStretch_mul.attr('o') >> self.forearmIkAutoStretch_blnd.last()
		self.forearmIkAutoStretch_blnd.attr('o') >> self.forearmIkAutoStretch_add.attr('i1')
		
		self.armIk_ctrl.attr('forearmStretch') >> self.forearmIkStretch_mul.attr('i1')
		self.forearmIkStretch_mul.attr('i2').value = forearmDist
		self.forearmIkStretch_mul.attr('o') >> self.forearmIkAutoStretch_add.attr('i2')
		
		# IK Stretch - Adjusting stretch amplitude
		self.upArmIkStretchAmp_mul = rigTools.attrAmper( self.armIk_ctrl.attr('upArmStretch') , self.upArmIkStretch_mul.attr('i1') , dv = 0.1 )
		self.forearmIkStretchAmp_mul = rigTools.attrAmper( self.armIk_ctrl.attr('forearmStretch') , self.forearmIkStretch_mul.attr('i1') , dv = 0.1 )
		
		# IK lock - Controls
		self.elbowIk_ctrl.add( ln = 'lock' , min = 0 , max = 1 , k = True )
		
		# IK lock - Stretch, upper arm stretch
		self.upArmIkLockLen_mul = pc.MultDoubleLinear()
		self.upArmIkLock_mul = pc.MultDoubleLinear()
		self.upArmIkLock_blnd = pc.BlendTwoAttr()
		
		self.forearmIkLockLen_mul = pc.MultDoubleLinear()
		self.forearmIkLock_mul = pc.MultDoubleLinear()
		self.forearmIkLock_blnd = pc.BlendTwoAttr()
		
		self.upArmIkLock_dist.attr('d') >> self.upArmIkLockLen_mul.attr('i1')
		self.upArmIkLockLen_mul.attr('i2').value = abs( 1/upArmDist )
		self.upArmIkLockLen_mul.attr('o') >> self.upArmIkLock_mul.attr('i1')
		self.upArmIkLock_mul.attr('i2').value = upArmDist
		self.upArmIkAutoStretch_add.attr('o') >> self.upArmIkLock_blnd.last()
		self.upArmIkLock_mul.attr('o') >> self.upArmIkLock_blnd.last()
		self.elbowIk_ctrl.attr('lock') >> self.upArmIkLock_blnd.attr('ab')
		self.upArmIkLock_blnd.attr('o') >> self.forearmIk_jnt.attr('ty')
		
		self.forearmIkLock_dist.attr('d') >> self.forearmIkLockLen_mul.attr('i1')
		self.forearmIkLockLen_mul.attr('i2').value = abs( 1/forearmDist )
		self.forearmIkLockLen_mul.attr('o') >> self.forearmIkLock_mul.attr('i1')
		self.forearmIkLock_mul.attr('i2').value = forearmDist
		self.forearmIkAutoStretch_add.attr('o') >> self.forearmIkLock_blnd.last()
		self.forearmIkLock_mul.attr('o') >> self.forearmIkLock_blnd.last()
		self.elbowIk_ctrl.attr('lock') >> self.forearmIkLock_blnd.attr('ab')
		self.forearmIkLock_blnd.attr('o') >> self.wristIk_jnt.attr('ty')
		
		# FK/IK blending
		self.armFkIk_rev = pc.Reverse()
		self.arm_ctrl.add( ln = 'fkIk' , min = 0 , max = 1 , k = True )
		self.arm_ctrl.attr( 'fkIk' ) >> self.armFkIk_rev.attr( 'ix' )
		self.arm_ctrl.attr( 'fkIk' ) >> self.armIkCtrl_grp.attr( 'v' )
		self.armFkIk_rev.attr( 'ox' ) >> self.armFkCtrl_grp.attr( 'v' )
		
		# # FK/IK blending - Using blendColors
		# self.upArmJntT_bc = rigTools.blend2Vectors( 't' , self.upArmIk_jnt , self.upArmFk_jnt , self.upArm_jnt )
		# self.forearmJntT_bc = rigTools.blend2Vectors( 't' , self.forearmIk_jnt , self.forearmFk_jnt , self.forearm_jnt )
		# self.wristJntT_bc = rigTools.blend2Vectors( 't' , self.wristIk_jnt , self.wristFk_jnt , self.wrist_jnt )
		# self.handJntT_bc = rigTools.blend2Vectors( 't' , self.handIk_jnt , self.handFk_jnt , self.hand_jnt )

		# self.upArmJntR_bc = rigTools.blend2Vectors( 'r' , self.upArmIk_jnt , self.upArmFk_jnt , self.upArm_jnt )
		# self.forearmJntR_bc = rigTools.blend2Vectors( 'r' , self.forearmIk_jnt , self.forearmFk_jnt , self.forearm_jnt )
		# self.wristJntR_bc = rigTools.blend2Vectors( 'r' , self.wristIk_jnt , self.wristFk_jnt , self.wrist_jnt )
		# self.handJntR_bc = rigTools.blend2Vectors( 'r' , self.handIk_jnt , self.handFk_jnt , self.hand_jnt )
		
		# self.arm_ctrl.attr( 'fkIk' ) >> self.upArmJntT_bc.attr( 'blender' )
		# self.arm_ctrl.attr( 'fkIk' ) >> self.forearmJntT_bc.attr( 'blender' )
		# self.arm_ctrl.attr( 'fkIk' ) >> self.wristJntT_bc.attr( 'blender' )
		# self.arm_ctrl.attr( 'fkIk' ) >> self.handJntT_bc.attr( 'blender' )
		# self.arm_ctrl.attr( 'fkIk' ) >> self.upArmJntR_bc.attr( 'blender' )
		# self.arm_ctrl.attr( 'fkIk' ) >> self.forearmJntR_bc.attr( 'blender' )
		# self.arm_ctrl.attr( 'fkIk' ) >> self.wristJntR_bc.attr( 'blender' )
		# self.arm_ctrl.attr( 'fkIk' ) >> self.handJntR_bc.attr( 'blender' )
		
		# FK/IK blending - Using parentConstraint
		self.upArmJnt_parCons = pc.parentConstraint( self.upArmFk_jnt , self.upArmIk_jnt , self.upArm_jnt )
		self.forearmJnt_parCons = pc.parentConstraint( self.forearmFk_jnt , self.forearmIk_jnt , self.forearm_jnt )
		self.wristJnt_parCons = pc.parentConstraint( self.wristFk_jnt , self.wristIk_jnt , self.wrist_jnt )
		self.handJnt_parCons = pc.parentConstraint( self.handFk_jnt , self.handIk_jnt , self.hand_jnt )
		
		self.arm_ctrl.attr( 'fkIk' ) >> self.upArmJnt_parCons.attr( 'w1' )
		self.arm_ctrl.attr( 'fkIk' ) >> self.forearmJnt_parCons.attr( 'w1' )
		self.arm_ctrl.attr( 'fkIk' ) >> self.wristJnt_parCons.attr( 'w1' )
		self.arm_ctrl.attr( 'fkIk' ) >> self.handJnt_parCons.attr( 'w1' )
		
		self.armFkIk_rev.attr( 'ox' ) >> self.upArmJnt_parCons.attr( 'w0' )
		self.armFkIk_rev.attr( 'ox' ) >> self.forearmJnt_parCons.attr( 'w0' )
		self.armFkIk_rev.attr( 'ox' ) >> self.wristJnt_parCons.attr( 'w0' )
		self.armFkIk_rev.attr( 'ox' ) >> self.handJnt_parCons.attr( 'w0' )
		
		# Group
		self.armRig_grp.parent( animGrp )
		self.armJnt_grp.parent( jntGrp )
		
		# Ribbon
		self.armRbnAnim_grp = pc.Null()
		self.armRbnAnim_grp.snap( self.armRig_grp )
		
		if side == 'RGT' :
			rbnAx = 'x-'
			rbnAim = (-1,0,0)
			rbnUp = (0,0,-1)
		else :
			rbnAx = 'x+'
			rbnAim = (1,0,0)
			rbnUp = (0,0,1)
		
		# Ribbon control
		self.armRbn_ctrl 		= pc.Control( 'plus' )
		self.armRbnCtrlZro_grp 	= pc.group( self.armRbn_ctrl )
				
		# Ribbon control - shape adjustment
		self.armRbn_ctrl.color = 'yellow'
		self.armRbn_ctrl.scaleShape( 3 * charSize )
		
		# Ribbon control - parenting and positioning
		self.armRbnCtrlZroGrp_pntCons = pc.pointConstraint( self.forearm_jnt , self.armRbnCtrlZro_grp )
		self.armRbnCtrlZroGrp_oriCons = pc.orientConstraint( self.upArm_jnt , self.armRbnCtrlZro_grp , mo = True )
		
		# Ribbon upper arm
		if ribbon :
			self.upArmRbn = pr.RibbonIkHi( size = self.upArmLen , ax = rbnAx )
		else :
			self.upArmRbn = pr.RibbonIkLow( size = self.upArmLen , ax = rbnAx )
		
		# Ribbon upper arm - adjust position
		self.upArmRbn.rbnAnim_grp.snapPoint( upArm )
		mc.delete( pc.aimConstraint( forearm ,
									self.upArmRbn.rbnAnim_grp ,
									aim = rbnAim , u = rbnUp ,
									wut = 'objectrotation' ,
									wuo = upArm ,
									wu = (0,0,1)
									)
				)
		self.upArmRbn_parCons 			= pc.parentConstraint( self.upArm_jnt , self.upArmRbn.rbnAnim_grp , mo = True )
		self.upArmRbnRootCtrl_pntCons 	= pc.pointConstraint( self.upArm_jnt , self.upArmRbn.rbnRoot_ctrl )
		self.upArmRbnEndCtrl_pntCons 	= pc.pointConstraint( self.armRbn_ctrl , self.upArmRbn.rbnEnd_ctrl )

		# Ribbon upper arm - space
		self.upArmRbn.rbnRootTwstZro_grp.snap( upArm )
		self.upArmRbnRootTwstZroGrp_parCons	= pc.parentConstraint( parent ,
												self.upArmRbn.rbnRootTwstZro_grp ,
												mo = True
												)
		self.upArmRbnRootTwstGrp_parCons	= pc.parentConstraint( self.upArm_jnt ,
												self.upArmRbn.rbnRootTwst_grp
												)

		self.upArmRbn.rbnEndTwstZro_grp.snap( forearm )
		self.upArmRbnEndTwstZroGrp_parCons	= pc.parentConstraint( self.upArm_jnt ,
												self.upArmRbn.rbnEndTwstZro_grp,
												mo = True
												)
		self.upArmRbnEndTwstGrp_parCons		= pc.parentConstraint( self.forearm_jnt ,
												self.upArmRbn.rbnEndTwst_grp
												)

		self.upArmRbn.rbnRootTwst_grp.rotateOrder = 'yzx'
		self.upArmRbn.rbnEndTwst_grp.rotateOrder = 'yzx'
		self.upArmRbn.rbnRootTwst_grp.attr('ry') 	>> self.upArmRbn.rbnRootTwstAmp_mul.attr('i1')
		self.upArmRbn.rbnEndTwst_grp.attr('ry') 	>> self.upArmRbn.rbnEndTwstAmp_mul.attr('i1')

		# Ribbon upper arm - twist distributetion
		upArmRbnShp = pc.Dag( self.upArmRbn.rbn_ctrl.shape )
		upArmRbnShp.attr('rootTwistAmp').value 	= -1
		upArmRbnShp.attr('endTwistAmp').value 	= 1
		
		# Ribbon forearm
		if ribbon :
			self.forearmRbn = pr.RibbonIkHi( size = self.forearmLen , ax = rbnAx )
		else :
			self.forearmRbn = pr.RibbonIkLow( size = self.forearmLen , ax = rbnAx )
		
		self.forearmRbn.rbnAnim_grp.snapPoint( forearm )
		mc.delete( pc.aimConstraint( wrist ,
										self.forearmRbn.rbnAnim_grp ,
										aim = rbnAim , u = rbnUp ,
										wut = 'objectrotation' ,
										wuo = forearm ,
										wu = (0,0,1)
									)
				)
		self.forearmRbn_parCons = pc.parentConstraint( self.forearm_jnt , self.forearmRbn.rbnAnim_grp , mo = True )
		self.forearmRbnRootCtrl_pntCons = pc.pointConstraint( self.armRbn_ctrl , self.forearmRbn.rbnRoot_ctrl )
		self.forearmRbnEndCtrl_pntCons = pc.pointConstraint( self.wrist_jnt , self.forearmRbn.rbnEnd_ctrl )
		
		# Ribbon forearm - space
		self.forearmRbn.rbnRootTwstZro_grp.snap( forearm )
		# self.forearmRbnRootTwstZroGrp_parCons	= pc.parentConstraint( self.upArm_jnt ,
		# 										self.forearmRbn.rbnRootTwstZro_grp
		# 										)
		# self.forearmRbnRootTwstGrp_parCons		= pc.parentConstraint( self.forearm_jnt ,
		# 										self.forearmRbn.rbnRootTwst_grp
		# 										)

		self.forearmRbn.rbnEndTwstZro_grp.snap( wrist )
		self.forearmRbnEndTwstZroGrp_parCons	= pc.parentConstraint( self.forearm_jnt ,
												self.forearmRbn.rbnEndTwstZro_grp ,
												mo = True
												)
		self.forearmRbnEndTwstGrp_parCons		= pc.parentConstraint( self.wrist_jnt ,
												self.forearmRbn.rbnEndTwst_grp ,
												mo = True
												)
		self.forearmRbn.rbnRootTwst_grp.attr('ry') 	>> self.forearmRbn.rbnRootTwstAmp_mul.attr('i1')
		self.forearmRbn.rbnEndTwst_grp.attr('ry') 	>> self.forearmRbn.rbnEndTwstAmp_mul.attr('i1')
		self.forearmRbn.rbnRootTwst_grp.rotateOrder = 'yzx'
		self.forearmRbn.rbnEndTwst_grp.rotateOrder = 'yzx'

		# Ribbon forearm - twist distributetion
		forearmRbnShp = pc.Dag( self.forearmRbn.rbn_ctrl.shape )
		forearmRbnShp.attr('rootTwistAmp').value = 0
		forearmRbnShp.attr('endTwistAmp').value = 1
		
		# Ribbon - group
		self.armRbnCtrlZro_grp.parent( self.armRbnAnim_grp )
		self.upArmRbn.rbnAnim_grp.parent( self.armRbnAnim_grp )
		self.upArmRbn.rbnSkin_grp.parent( skinGrp )
		self.upArmRbn.rbnStill_grp.parent( stillGrp )
		self.forearmRbn.rbnAnim_grp.parent( self.armRbnAnim_grp )
		self.forearmRbn.rbnSkin_grp.parent( skinGrp )
		self.forearmRbn.rbnStill_grp.parent( stillGrp )
		self.armRbnAnim_grp.parent( self.armRig_grp )
		
		if ribbon :
			self.upArmRbn.rbnJnt_grp.parent( self.armJnt_grp )
			self.forearmRbn.rbnJnt_grp.parent( self.armJnt_grp )
		
		# Ribbon - cleanup
		self.armRbn_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		
		self.upArmRbn.rbnRoot_ctrl.hide()
		self.upArmRbn.rbnEnd_ctrl.hide()
		self.forearmRbn.rbnRoot_ctrl.hide()
		self.forearmRbn.rbnEnd_ctrl.hide()
		
		# Rig cleanup
		self.armIk_ctrl.attr('localWorld').value 	= 1
		self.upArmFk_ctrl.attr('localWorld').value 	= 1
		
		# rigTools.lockUnusedAttrs( self )
		self.armIkRoot_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' )
		self.armIkRoot_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.armIk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.arm_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.elbowIk_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.forearmFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.upArmFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.wristFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.elbowIkCtrl_crv.lockHideKeyableAttrs()


