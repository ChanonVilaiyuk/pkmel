# Spine rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
import pkmel.ribbon as pr
reload( pc )
reload( rigTools )
reload( pr )

class SpineRig( object ) :
	
	def __init__(
						self ,
						parent = 'root_jnt' ,
						animGrp = 'anim_grp' ,
						jntGrp = 'jnt_grp' ,
						ikhGrp = 'ikh_grp' ,
						skinGrp = 'skin_grp' ,
						stillGrp = 'still_grp' ,
						ribbon = True ,
						ax = 'y' ,
						charSize = 1 ,
						tmpJnt = (
										'spine1_tmpJnt' ,
										'spine2_tmpJnt' ,
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
		
		# Skin joints
		self.spine1_jnt = rigTools.jointAt( spine1 )
		self.spine2_jnt = rigTools.jointAt( spine2 )
		self.spine3_jnt = pc.Joint()
		
		self.spine3_jnt.snapPoint( spine3 )
		self.spine3_jnt.snapOrient( spine2 )
		self.spine3_jnt.freeze( r = True , t = True )
		self.spine3_jnt.parent( self.spine2_jnt )
		self.spine2_jnt.parent( self.spine1_jnt )
		self.spine1_jnt.parent( rootJnt )
		
		mc.parentConstraint( self.spine1_jnt , spine1 )
		mc.parentConstraint( self.spine2_jnt , spine2 )
		
		# Skin joint - rotate order adjustment
		self.spine1_jnt.rotateOrder = 'yzx'
		self.spine2_jnt.rotateOrder = 'yzx'
		self.spine3_jnt.rotateOrder = 'yzx'
		
		# Main group
		self.spineRig_grp = pc.Null()
		self.spineRigGrp_parCons = pc.parentConstraint( rootJnt , self.spineRig_grp )
		
		self.spineJnt_grp = pc.Null()
		self.spineJntGrp_parCons = pc.parentConstraint( rootJnt , self.spineJnt_grp )
		
		# Length
		self.upSpineLen = pc.distance( spine2 , spine3 )
		self.lowSpineLen = pc.distance( spine1 , spine2 )
		
		# Spine control
		self.spine_ctrl = pc.Control( 'stick' )
		self.spineCtrl_grp = pc.group( self.spine_ctrl )
		self.spineCtrlGrp_parCons = pc.parentConstraint( self.spine1_jnt , self.spineCtrl_grp )
		
		self.spineCtrl_grp.parent( self.spineRig_grp )
		
		self.spine_ctrl.color = 'green'
		self.spine_ctrl.scaleShape( 3 * charSize )
		
		# ----- FK -----
		# FK group
		self.spineFkCtrl_grp = pc.Null()
		self.spineFkCtrl_grp.snap( rootJnt )
		self.spineFkCtrl_grp.parent( self.spineRig_grp )
		
		self.spineFkJnt_grp = pc.Null()
		self.spineFkJnt_grp.snap( rootJnt )
		self.spineFkJnt_grp.parent( self.spineJnt_grp )
		
		# FK joint
		self.spine1Fk_jnt = rigTools.jointAt( self.spine1_jnt )
		self.spine2Fk_jnt = rigTools.jointAt( self.spine2_jnt )
		self.spine3Fk_jnt = rigTools.jointAt( self.spine3_jnt )
		
		self.spine3Fk_jnt.parent( self.spine2Fk_jnt )
		self.spine2Fk_jnt.parent( self.spine1Fk_jnt )
		self.spine1Fk_jnt.parent( self.spineFkJnt_grp )
		
		# Fk joint - rotate order adjustment
		self.spine1Fk_jnt.rotateOrder = 'yzx'
		self.spine2Fk_jnt.rotateOrder = 'yzx'
		self.spine3Fk_jnt.rotateOrder = 'yzx'
		
		# FK control
		self.spine1Fk_ctrl = rigTools.jointControl( 'circle' )
		self.spine1FkGmbl_ctrl = pc.addGimbal( self.spine1Fk_ctrl )
		self.spine1FkCtrlZro_grp = rigTools.zeroGroup( self.spine1Fk_ctrl )
		
		self.spine2Fk_ctrl = rigTools.jointControl( 'circle' )
		self.spine2FkGmbl_ctrl = pc.addGimbal( self.spine2Fk_ctrl )
		self.spine2FkCtrlZro_grp = rigTools.zeroGroup( self.spine2Fk_ctrl )
		
		# FK control - parenting and positioning
		self.spine1FkCtrlZro_grp.snapPoint( self.spine1Fk_jnt )
		self.spine1Fk_ctrl.snapOrient( self.spine1Fk_jnt )
		self.spine1Fk_ctrl.freeze( r=True )
		
		self.spine2FkCtrlZro_grp.snapPoint( self.spine2Fk_jnt )
		self.spine2Fk_ctrl.snapOrient( self.spine2Fk_jnt )
		self.spine2Fk_ctrl.freeze( r=True )
		
		self.spine2FkCtrlZro_grp.parent( self.spine1FkGmbl_ctrl )
		self.spine1FkCtrlZro_grp.parent( self.spineFkCtrl_grp )
		
		# FK control - shape adjustment
		self.spine1Fk_ctrl.color = 'red'
		self.spine2Fk_ctrl.color = 'red'
		self.spine1Fk_ctrl.scaleShape( 3 * charSize )
		self.spine2Fk_ctrl.scaleShape( 3 * charSize )
		
		# FK control - Rotate order adjustment
		self.spine1Fk_ctrl.rotateOrder = 'xzy'
		self.spine1FkGmbl_ctrl.rotateOrder = 'xzy'
		self.spine2Fk_ctrl.rotateOrder = 'xzy'
		self.spine2FkGmbl_ctrl.rotateOrder = 'xzy'
		
		# FK control - stretch setup
		self.spine1FkStretch_add , self.spine1FkStretch_mul = rigTools.fkStretch( ctrl = self.spine1Fk_ctrl ,
									target = self.spine2FkCtrlZro_grp ,
									ax = ax )
		self.spine2FkStretch_add , self.spine2FkStretch_mul = rigTools.fkStretch( ctrl = self.spine2Fk_ctrl ,
									target = self.spine3Fk_jnt ,
									ax = ax )
		
		# FK control - adjusting stretch amplitude
		self.spine1FkStretchAmp_mul = rigTools.attrAmper( self.spine1Fk_ctrl.attr('stretch') , self.spine1FkStretch_mul.attr('i2') , dv = 0.1 )
		self.spine2FkStretchAmp_mul = rigTools.attrAmper( self.spine2Fk_ctrl.attr('stretch') , self.spine2FkStretch_mul.attr('i2') , dv = 0.1 )
		
		# FK control - local/world setup
		# parentLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , oriGrp = '' )
		# return locGrp , worGrp , worGrpParCons , parGrpParCons , parGrpParConsRev
		self.spine1FkCtrlLoc_grp,self.spine1FkCtrlWor_grp,self.spine1FkCtrlWorGrp_oriCons,self.spine1FkCtrlZroGrp_oriCons,self.spine1FkCtrlZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( self.spine1Fk_ctrl , self.spineFkCtrl_grp , animGrp , self.spine1FkCtrlZro_grp )
		self.spine2FkCtrlLoc_grp,self.spine2FkCtrlWor_grp,self.spine2FkCtrlWorGrp_oriCons,self.spine2FkCtrlZroGrp_oriCons,self.spine2FkCtrlZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( self.spine2Fk_ctrl , self.spine1FkGmbl_ctrl , animGrp , self.spine2FkCtrlZro_grp )
		
		# FK control - connect to joint
		self.spine1Jnt_parCons = pc.parentConstraint( self.spine1FkGmbl_ctrl , self.spine1Fk_jnt)
		self.spine2Jnt_parCons = pc.parentConstraint( self.spine2FkGmbl_ctrl , self.spine2Fk_jnt)
		
		# ----- IK -----
		# IK group
		self.spineIkCtrl_grp = pc.Null()
		self.spineIkCtrl_grp.snap( rootJnt )
		self.spineIkCtrl_grp.parent( self.spineRig_grp )
		
		self.spineIkJnt_grp = pc.Null()
		self.spineIkJnt_grp.snap( rootJnt )
		self.spineIkJnt_grp.parent( self.spineJnt_grp )
		
		# IK joint
		self.spine1Ik_jnt = rigTools.jointAt( spine1 )
		self.spine2Ik_jnt = rigTools.jointAt( spine2 )
		self.spine3Ik_jnt = rigTools.jointAt( spine3 )
		
		# IK joint - parenting
		self.spine3Ik_jnt.parent( self.spine2Ik_jnt )
		self.spine2Ik_jnt.parent( self.spine1Ik_jnt )
		self.spine1Ik_jnt.parent( self.spineIkJnt_grp )
		
		# IK joint - rotate order adjustment
		self.spine1Ik_jnt.rotateOrder = 'yzx'
		self.spine2Ik_jnt.rotateOrder = 'yzx'
		self.spine3Ik_jnt.rotateOrder = 'yzx'
		
		# IK control
		self.spineIk_ctrl = rigTools.jointControl( 'circle' )
		self.spineIkOff_ctrl = pc.group( self.spineIk_ctrl )
		self.spineIkCtrlZro_grp = pc.group( self.spineIkOff_ctrl )
		
		self.spineIkRoot_ctrl = rigTools.jointControl( 'circle' )
		self.spineIkRootCtrlZro_grp = pc.group( self.spineIkRoot_ctrl )
		
		self.spine1IkPol_grp = pc.Null()
		
		# IK control - parenting and positioning
		self.spineIkCtrlZro_grp.snapPoint( spine2 )
		self.spineIk_ctrl.snapOrient( spine2 )
		self.spineIk_ctrl.freeze( r = True )
		
		self.spineIkCon_ctrl = pc.addConCtrl( self.spineIk_ctrl )
		self.spineIkGmbl_ctrl = pc.addGimbal( self.spineIk_ctrl )
		
		self.spineIkRootCtrlZro_grp.snapPoint( self.spine1Ik_jnt )
		
		self.spine1IkPol_grp.snap( self.spineIkRoot_ctrl )
		self.spine1IkPol_grp.parent( self.spineIkRoot_ctrl )
		# self.spine1IkPol_grp.attr('tz').v = -1
		
		self.spineIkCtrlZro_grp.parent( self.spineIkRoot_ctrl )
		self.spineIkRootCtrlZro_grp.parent( self.spineIkCtrl_grp )
		
		self.spineIkRootCtrlZroGrp_oriCons = pc.orientConstraint( animGrp , self.spineIkRootCtrlZro_grp )
		self.spine1IkJnt_parCons = pc.pointConstraint( self.spineIkRoot_ctrl , self.spine1Ik_jnt )
		
		# IK control - polvector adjustment
		ikCtrlShp = pc.Dag( self.spineIk_ctrl.shape )
		ikCtrlShp.add( ln='polVector' , at='double3' , k=False )
		ikCtrlShp.add( p = 'polVector' , ln = 'polVectorX' , at = 'double' , k = False )
		ikCtrlShp.add( p = 'polVector' , ln = 'polVectorY' , at = 'double' , k = False )
		ikCtrlShp.add( p = 'polVector' , ln = 'polVectorZ' , at = 'double' , k = False )
		
		ikCtrlShp.attr( 'polVectorX' ) >> self.spine1IkPol_grp.attr( 'tx' )
		ikCtrlShp.attr( 'polVectorY' ) >> self.spine1IkPol_grp.attr( 'ty' )
		ikCtrlShp.attr( 'polVectorZ' ) >> self.spine1IkPol_grp.attr( 'tz' )
		
		# IK control - shape adjustment
		self.spineIkRoot_ctrl.color = 'blue'
		self.spineIk_ctrl.color = 'blue'
		
		self.spineIk_ctrl.scaleShape( 3 * charSize )
		self.spineIkRoot_ctrl.scaleShape( 3 * charSize )
		
		# IK control -  rotate order adjustment
		self.spineIk_ctrl.rotateOrder = 'xzy'
		self.spineIkGmbl_ctrl.rotateOrder = 'xzy'
		
		# IK handle
		self.spine1_ikh = pc.IkRp( self.spine1Ik_jnt , self.spine2Ik_jnt )
		self.spine2_ikh = pc.IkRp( self.spine2Ik_jnt , self.spine3Ik_jnt )
		
		self.spine1Ikh_polCons = pc.poleVectorConstraint( self.spine1IkPol_grp , self.spine1_ikh )
		
		self.spineIkh_grp = pc.Null()
		self.spine1IkhZro_grp = rigTools.zeroGroup( self.spine1_ikh )
		self.spine2IkhZro_grp = rigTools.zeroGroup( self.spine2_ikh )
		self.spine1IkhZro_grp.parent( self.spineIkh_grp )
		self.spine2IkhZro_grp.parent( self.spineIkh_grp )
		self.spineIkh_grp.parent( ikhGrp )
		
		# IK handle - pivots
		self.spine1IkhPiv_grp = pc.Null()
		self.spine2IkhPiv_grp = pc.Null()
		
		# IK handle - pivots - positioning and parenting
		self.spine1IkhPiv_grp.snap( self.spine1IkhZro_grp )
		self.spine2IkhPiv_grp.snap( self.spine2IkhZro_grp )
		
		self.spine1IkhPiv_grp.parent( self.spineIkGmbl_ctrl )
		self.spine2IkhPiv_grp.parent( self.spineIkGmbl_ctrl )
		
		self.spine1IkhZroGrp_parCons = pc.parentConstraint( self.spine1IkhPiv_grp , self.spine1IkhZro_grp )
		self.spine2IkhZroGrp_parCons = pc.parentConstraint( self.spine2IkhPiv_grp , self.spine2IkhZro_grp )
		
		# IK control - local/world setup
		self.spineIkCtrlLoc_grp,self.spineIkCtrlWor_grp,self.spineIkCtrlWorGrp_parCons , self.spineIkCtrlZroGrp_parCons , self.spineIkCtrlZroGrpParCons_rev = rigTools.parentLocalWorldCtrl( self.spineIk_ctrl , self.spineIkRoot_ctrl , animGrp , self.spineIkCtrlZro_grp )

		# IK handle - twist control
		self.spineIk_ctrl.add( ln = 'twist' , k = True )
		self.spineIkTwist_add = pc.AddDoubleLinear()
		self.spineIk_ctrl.attr( 'twist' ) >> self.spineIkTwist_add.attr( 'i1' )
		self.spineIkTwist_add.attr( 'o' ) >> self.spine1_ikh.attr( 'twist' )
		
		# IK stretch
		self.spineIk_ctrl.add( ln = '__stretch__' , k = True )
		self.spineIk_ctrl.attr('__stretch__').set( l = True )
		
		# IK stretch - lower auto stretch setup
		spiLen = self.spine2_jnt.attr( 't%s' % ax ).value
		# spiLen = distance( self.spine1_jnt , self.spine2_jnt )
		self.spine1IkStrtPnt1_grp = pc.Null()
		self.spine1IkStrtPnt2_grp = pc.Null()
		self.spine1IkStrtPnt1Grp_pntCons = pc.pointConstraint( self.spine1IkhPiv_grp , self.spine1IkStrtPnt1_grp )
		self.spine2IkStrtPnt1Grp_pntCons = pc.pointConstraint( self.spineIkRoot_ctrl , self.spine1IkStrtPnt2_grp )
		self.spine1IkStrt_mdv = pc.MultiplyDivide()
		self.spine1IkStrt_mul = pc.MultDoubleLinear()
		self.spine1IkStrt_blen = pc.BlendTwoAttr()
		self.spine1IkStrt_dist = pc.DistanceBetween()
		
		self.spineIk_ctrl.add( ln = 'autoStretch' , k = True , min = 0 , max = 1 )
		self.spineIk_ctrl.attr( 'autoStretch' ) >> self.spine1IkStrt_blen.attr( 'attributesBlender' )
		
		self.spine1IkStrtPnt1_grp.attr( 't' ) >> self.spine1IkStrt_dist.attr( 'point1' )
		self.spine1IkStrtPnt2_grp.attr( 't' ) >> self.spine1IkStrt_dist.attr( 'point2' )
		
		self.spine1IkStrt_mdv.attr('operation').value = 2
		self.spine1IkStrt_dist.attr( 'distance' ) >> self.spine1IkStrt_mdv.attr( 'i1x' )
		# self.spine1IkStrt_mdv.attr( 'i2x' ).value = spiLen
		self.spine1IkStrt_mdv.attr( 'i2x' ).value = pc.distance( self.spine1_jnt , self.spine2_jnt )
		
		self.spine1IkStrt_mdv.attr('ox') >> self.spine1IkStrt_mul.attr( 'i1' )
		self.spine1IkStrt_mul.attr('i2').value = spiLen
		self.spine1IkStrt_blen.add( ln = 'default' , dv = spiLen , k = True )
		self.spine1IkStrt_blen.attr( 'default' ) >> self.spine1IkStrt_blen.attr( 'i[0]' )
		self.spine1IkStrt_mul.attr( 'o' ) >> self.spine1IkStrt_blen.attr( 'i[1]' )
		self.spine1IkStrtPnt1_grp.parent( self.spineIkCtrl_grp )
		self.spine1IkStrtPnt2_grp.parent( self.spineIkCtrl_grp )
		
		# IK stretch - lower and upper stretch
		self.spineIk_ctrl.add( ln = 'lowerStretch' , k = True )
		self.spineIk_ctrl.add( ln = 'upperStretch' , k = True )
		
		self.spineIkLowerStretch_add , self.spineIkLowerStretch_mul = rigTools.fkStretch( ctrl = self.spineIk_ctrl , attr = 'lowerStretch' , target = self.spine2Ik_jnt ,  ax=ax )
		self.spine1IkStrt_blen.attr( 'o' ) >> self.spineIkLowerStretch_add.attr( 'default' )
		
		# self.spineIkUpperStretch_add , self.spineIkUpperStretch_mul = rigTools.fkStretch( ctrl = self.spineIk_ctrl , attr = 'upperStretch' , target = self.spine2IkhZro_grp , ax=ax )
		self.spineIkUpperStretch_add , self.spineIkUpperStretch_mul = rigTools.fkStretch( ctrl = self.spineIk_ctrl , attr = 'upperStretch' , target = self.spine3Ik_jnt , ax=ax )
		# self.spineIkUpperStretch_add.attr( 'o' ) >> self.spine3Ik_jnt.attr( 't%s' % ax )
		
		# IK stretch - Adjusting stretch amplitude
		self.spineIkLowerStretchAmp_mul = rigTools.attrAmper( self.spineIk_ctrl.attr('lowerStretch') , self.spineIkLowerStretch_mul.attr('i2') , dv = 0.1 )
		self.spineIkUpperStretchAmp_mul = rigTools.attrAmper( self.spineIk_ctrl.attr('upperStretch') , self.spineIkUpperStretch_mul.attr('i2') , dv = 0.1 )
		
		# FK/IK blending
		self.spineFkIk_rev = pc.Reverse()
		self.spine_ctrl.add( ln = 'fkIk' , min = 0 , max = 1 , k = True )
		self.spine_ctrl.attr( 'fkIk' ) >> self.spineFkIk_rev.attr( 'ix' )
		self.spine_ctrl.attr( 'fkIk' ) >> self.spineIkCtrl_grp.attr( 'v' )
		self.spineFkIk_rev.attr( 'ox' ) >> self.spineFkCtrl_grp.attr( 'v' )
		
		# FK/IK blending - Using blendColors
		# self.spine1JntT_bc = rigTools.blend2Vectors( 't' , self.spine1Ik_jnt , self.spine1Fk_jnt , self.spine1_jnt )
		# self.spine2JntT_bc = rigTools.blend2Vectors( 't' , self.spine2Ik_jnt , self.spine2Fk_jnt , self.spine2_jnt )
		# self.spine3JntT_bc = rigTools.blend2Vectors( 't' , self.spine3Ik_jnt , self.spine3Fk_jnt , self.spine3_jnt )
		# self.spine1JntR_bc = rigTools.blend2Vectors( 'r' , self.spine1Ik_jnt , self.spine1Fk_jnt , self.spine1_jnt )
		# self.spine2JntR_bc = rigTools.blend2Vectors( 'r' , self.spine2Ik_jnt , self.spine2Fk_jnt , self.spine2_jnt )
		# self.spine3JntR_bc = rigTools.blend2Vectors( 'r' , self.spine3Ik_jnt , self.spine3Fk_jnt , self.spine3_jnt )
		
		# self.spine_ctrl.attr( 'fkIk' ) >> self.spine1JntT_bc.attr( 'blender' )
		# self.spine_ctrl.attr( 'fkIk' ) >> self.spine2JntT_bc.attr( 'blender' )
		# self.spine_ctrl.attr( 'fkIk' ) >> self.spine3JntT_bc.attr( 'blender' )
		# self.spine_ctrl.attr( 'fkIk' ) >> self.spine1JntR_bc.attr( 'blender' )
		# self.spine_ctrl.attr( 'fkIk' ) >> self.spine2JntR_bc.attr( 'blender' )
		# self.spine_ctrl.attr( 'fkIk' ) >> self.spine3JntR_bc.attr( 'blender' )
		
		# FK/IK blending - Using parentConstraint
		self.spine1Jnt_parCons = pc.parentConstraint( self.spine1Fk_jnt , self.spine1Ik_jnt , self.spine1_jnt )
		self.spine2Jnt_parCons = pc.parentConstraint( self.spine2Fk_jnt , self.spine2Ik_jnt , self.spine2_jnt )
		self.spine3Jnt_parCons = pc.parentConstraint( self.spine3Fk_jnt , self.spine3Ik_jnt , self.spine3_jnt )
		
		self.spine_ctrl.attr( 'fkIk' ) >> self.spine1Jnt_parCons.attr( 'w1' )
		self.spine_ctrl.attr( 'fkIk' ) >> self.spine2Jnt_parCons.attr( 'w1' )
		self.spine_ctrl.attr( 'fkIk' ) >> self.spine3Jnt_parCons.attr( 'w1' )
		
		self.spineFkIk_rev.attr( 'ox' ) >> self.spine1Jnt_parCons.attr( 'w0' )
		self.spineFkIk_rev.attr( 'ox' ) >> self.spine2Jnt_parCons.attr( 'w0' )
		self.spineFkIk_rev.attr( 'ox' ) >> self.spine3Jnt_parCons.attr( 'w0' )
		
		# Group
		self.spineRig_grp.parent( animGrp )
		self.spineJnt_grp.parent( jntGrp )
		
		# Ribbon
		self.spineRbnAnim_grp = pc.Null()
		self.spineRbnAnim_grp.snap( self.spineRig_grp )
		
		# Ribbon - Space
		self.spineRbnSpc_grp = pc.Null()
		self.spineRbnSpc_grp.snap( self.spineRbnAnim_grp )
		
		self.spine1RbnSpc_grp = pc.Null()
		self.spine1RbnSpcZro_grp = pc.group( self.spine1RbnSpc_grp )
		
		self.spine1RbnSpc_grp.rotateOrder = 'yzx'
		
		self.spine1RbnSpcZro_grp.snap( spine1 )
		self.spine2RbnSpcZroGrp_parCons = pc.parentConstraint( rootJnt , self.spine1RbnSpcZro_grp , mo = True )
		self.spine1RbnSpcGrp_parCons = pc.parentConstraint( self.spine1_jnt , self.spine1RbnSpc_grp )
		
		self.spine2RbnSpc_grp = pc.Null()
		self.spine2RbnSpcZro_grp = pc.group( self.spine2RbnSpc_grp )
		
		self.spine2RbnSpc_grp.rotateOrder = 'yzx'
		
		self.spine2RbnSpcZro_grp.snap( spine2 )
		self.spine2RbnSpcZroGrp_parCons = pc.parentConstraint( self.spine1_jnt , self.spine2RbnSpcZro_grp , mo = True )
		self.spine2RbnSpcGrp_parCons = pc.parentConstraint( self.spine2_jnt , self.spine2RbnSpc_grp )
		
		self.spine3RbnSpc_grp = pc.Null()
		self.spine3RbnSpcZro_grp = pc.group( self.spine3RbnSpc_grp )
		
		self.spine3RbnSpc_grp.rotateOrder = 'yzx'
		
		self.spine3RbnSpcZro_grp.snap( spine3 )
		self.spine3RbnSpcZroGrp_parCons = pc.parentConstraint( self.spine2_jnt , self.spine3RbnSpcZro_grp , mo = True )
		self.spine3RbnSpcGrp_parCons = pc.parentConstraint( self.spine3_jnt , self.spine3RbnSpc_grp )
		
		# Ribbon - Space - group
		self.spine1RbnSpcZro_grp.parent( self.spineRbnSpc_grp )
		self.spine2RbnSpcZro_grp.parent( self.spineRbnSpc_grp )
		self.spine3RbnSpcZro_grp.parent( self.spineRbnSpc_grp )
		self.spineRbnSpc_grp.parent( self.spineRbnAnim_grp )
		
		# Ribbon control
		self.spineRbn_ctrl = pc.Control( 'plus' )
		self.spineRbnCtrlZro_grp = pc.group( self.spineRbn_ctrl )
		
		# Ribbon control - parenting and positioning
		self.spineRbnCtrlZroGrp_pntCons = pc.pointConstraint( self.spine2RbnSpc_grp , self.spineRbnCtrlZro_grp )
		self.spineRbnCtrlZroGrp_oriCons = pc.orientConstraint( self.spine2RbnSpc_grp , self.spineRbnCtrlZro_grp , mo = True )
		
		# Ribbon control - shape adjustment
		self.spineRbn_ctrl.color = 'yellow'
		self.spineRbn_ctrl.scaleShape( 3 * charSize )
		
		# Ribbon - Lower spine
		if ribbon :
			self.lowSpineRbn = pr.RibbonIkHi( size = self.lowSpineLen , ax = '%s+' % ax )
		else :
			self.lowSpineRbn = pr.RibbonIkLow( size = self.lowSpineLen , ax = '%s+' % ax )
		
		aimVec = (0,1,0)
		upVec = (1,0,0)
		
		if ax == 'z' :
			aimVec = (0,0,1)
			upVec = (1,0,0)
		
		self.lowSpineRbn.rbnAnim_grp.snap( spine1 )
		mc.delete( pc.aimConstraint( self.spine2_jnt , self.lowSpineRbn.rbnAnim_grp , aim = aimVec , u = upVec , wut = 'vector' , wu = upVec ) )
		self.lowSpineRbn_parCons = pc.parentConstraint( self.spine1RbnSpc_grp , self.lowSpineRbn.rbnAnim_grp , mo = True )
		self.lowSpineRbnEndCtrl_pntCons = pc.pointConstraint( self.spineRbn_ctrl , self.lowSpineRbn.rbnEnd_ctrl )
		
		# Ribbon - Lower spine - twist
		lowSpineRbnShp = pc.Dag( self.lowSpineRbn.rbn_ctrl.shape )
		self.spine2RbnSpc_grp.attr('ry') >> lowSpineRbnShp.attr('endTwist')
		
		# Ribbon - Upper spine
		if ribbon :
			self.upSpineRbn = pr.RibbonIkHi( size = self.upSpineLen , ax = '%s+' % ax )
		else :
			self.upSpineRbn = pr.RibbonIkLow( size = self.upSpineLen , ax = '%s+' % ax  )
		
		upSpineRbnShp = pc.Dag( self.upSpineRbn.rbn_ctrl.shape )
		
		self.upSpineRbn.rbnAnim_grp.snapPoint( spine2 )
		mc.delete( pc.aimConstraint( self.spine3RbnSpc_grp , self.upSpineRbn.rbnAnim_grp , aim = aimVec , u = upVec , wut = 'vector' , wu = (1,0,0) ) )
		self.upSpineRbn_parCons = pc.parentConstraint( self.spine2RbnSpc_grp , self.upSpineRbn.rbnAnim_grp , mo = True )
		self.upSpineRbnRootCtrl_pntCons = pc.pointConstraint( self.spineRbn_ctrl , self.upSpineRbn.rbnRoot_ctrl )
		self.upSpineRbnEndCtrl_pntCons = pc.pointConstraint( self.spine3RbnSpc_grp , self.upSpineRbn.rbnEnd_ctrl )
		
		# Ribbon - Upper spine - twist
		upSpineRbnShp = pc.Dag( self.upSpineRbn.rbn_ctrl.shape )
		self.spine3RbnSpc_grp.attr('ry') >> upSpineRbnShp.attr('endTwist')
		
		# Ribbon - group
		self.spineRbnCtrlZro_grp.parent( self.spineRbnAnim_grp )
		self.lowSpineRbn.rbnAnim_grp.parent( self.spineRbnAnim_grp )
		# self.lowSpineRbn.rbnStill_grp.parent( stillGrp )
		self.lowSpineRbn.rbnSkin_grp.parent( skinGrp )
		self.upSpineRbn.rbnAnim_grp.parent( self.spineRbnAnim_grp )
		# self.upSpineRbn.rbnStill_grp.parent( stillGrp )
		self.upSpineRbn.rbnSkin_grp.parent( skinGrp )
		self.spineRbnAnim_grp.parent( self.spineRig_grp )
		
		if ribbon :
			self.lowSpineRbn.rbnJnt_grp.parent( jntGrp )
			self.upSpineRbn.rbnJnt_grp.parent( jntGrp )
			self.lowSpineRbn.rbnStill_grp.parent( stillGrp )
			self.upSpineRbn.rbnStill_grp.parent( stillGrp )
		
		# Ribbon - cleanup
		# for attr in ('rootTwist','endTwist') :
		# 	upSpineRbnShp.attr( attr ).l = True
		# 	lowSpineRbnShp.attr( attr ).l = True
		
		for attr in ('tx','ty','tz') :
			self.lowSpineRbn.rbnRoot_ctrl.attr( attr ).lockHide()
			self.lowSpineRbn.rbnEnd_ctrl.attr( attr ).lockHide()
			self.upSpineRbn.rbnRoot_ctrl.attr( attr ).lockHide()
			self.upSpineRbn.rbnEnd_ctrl.attr( attr ).lockHide()
		
		for attr in ('rx','ry','rz','sx','sy','sz','v') :
			self.spineRbn_ctrl.attr( attr ).lockHide()
		
		self.lowSpineRbn.rbnRoot_ctrl.hide()
		self.lowSpineRbn.rbnEnd_ctrl.hide()
		self.upSpineRbn.rbnRoot_ctrl.hide()
		self.upSpineRbn.rbnEnd_ctrl.hide()
		
		# Rig cleanup
		rigTools.lockUnusedAttrs( self )
		for attr in ('tx','ty','tz','rx','ry','rz','sx','sy','sz','v') :
			self.spine_ctrl.attr( attr ).lockHide()
		
		for attr in ('sx','sy','sz','v') :
			self.spine1Fk_ctrl.attr( attr ).lockHide()
			self.spine2Fk_ctrl.attr( attr ).lockHide()
			self.spineIk_ctrl.attr( attr ).lockHide()
			self.spineIkOff_ctrl.attr( attr ).lockHide()
		
		for attr in ('rx','ry','rz','sx','sy','sz','v') :
			self.spineIkRoot_ctrl.attr( attr ).lockHide()
		
