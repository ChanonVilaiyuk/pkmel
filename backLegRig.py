# Back leg rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
import pkmel.ribbon as pr
reload( pc )
reload( rigTools )
reload( pr )

class BackLegRig( object ) :
	
	def __init__(
						self ,
						parent = 'clav2LFT_jnt' ,
						side = 'LFT' ,
						animGrp = 'anim_grp' ,
						jntGrp = 'jnt_grp' ,
						ikhGrp = 'ikh_grp' ,
						skinGrp = 'skin_grp' ,
						stillGrp = 'still_grp' ,
						ribbon = True ,
						charSize = 1 ,
						tmpJnt = (
									'upLegLFT_tmpJnt' ,
									'midLegLFT_tmpJnt' ,
									'lowLegLFT_tmpJnt' ,
									'ankleLFT_tmpJnt' ,
									'ballLFT_tmpJnt' ,
									'toeLFT_tmpJnt' ,
									'heelLFT_tmpJnt' ,
									'footInLFT_tmpJnt' ,
									'footOutLFT_tmpJnt' ,
									'kneeIkLFT_tmpJnt'
									)
					) :
		
		# Checking parent
		parent = pc.Dag( parent )
		if not parent.exists :
			parent = pc.Null()
			parent.parent( skinGrp )
		
		# Template objects
		upLeg = pc.Dag( tmpJnt[0] )
		midLeg = pc.Dag( tmpJnt[1] )
		lowLeg = pc.Dag( tmpJnt[2] )
		ankle = pc.Dag( tmpJnt[3] )
		ball = pc.Dag( tmpJnt[4] )
		toe = pc.Dag( tmpJnt[5] )
		
		heel = pc.Dag( tmpJnt[6] )
		footIn = pc.Dag( tmpJnt[7] )
		footOut = pc.Dag( tmpJnt[8] )
		
		kneeIkCtrl = pc.Dag( tmpJnt[9] )
		
		# Skin joints
		self.upLeg_jnt = rigTools.jointAt( upLeg )
		self.midLeg_jnt = rigTools.jointAt( midLeg )
		self.lowLeg_jnt = rigTools.jointAt( lowLeg )
		self.ankle_jnt = rigTools.jointAt( ankle )
		self.ball_jnt = rigTools.jointAt( ball )
		self.toe_jnt = rigTools.jointAt( toe )
		
		mc.parentConstraint( self.upLeg_jnt , upLeg )
		mc.parentConstraint( self.midLeg_jnt , midLeg )
		mc.parentConstraint( self.lowLeg_jnt , lowLeg )
		mc.parentConstraint( self.ankle_jnt , ankle )
		mc.parentConstraint( self.ball_jnt , ball )
		mc.parentConstraint( self.toe_jnt , toe )
		
		# Skin joint - parenting
		self.toe_jnt.parent( self.ball_jnt )
		self.ball_jnt.parent( self.ankle_jnt )
		self.ankle_jnt.parent( self.lowLeg_jnt )
		self.midLeg_jnt.parent( self.upLeg_jnt )
		self.lowLeg_jnt.parent( self.midLeg_jnt )
		self.upLeg_jnt.parent( parent )
		self.ball_jnt.attr('ssc').v = 0
		
		# Main group
		self.legAnim_grp = pc.Null()
		self.legAnimGrp_parCons = pc.parentConstraint( parent , self.legAnim_grp )
		
		self.legJnt_grp = pc.Null()
		self.legJntGrp_parCons = pc.parentConstraint( parent , self.legJnt_grp )
		
		# Length
		self.upLegLen = pc.distance( upLeg , lowLeg )
		self.midLegLen = pc.distance( upLeg , midLeg )
		self.lowLegLen = pc.distance( lowLeg , ankle )
		
		# Joint - rotate order
		self.upLeg_jnt.rotateOrder = 'yzx'
		self.midLeg_jnt.rotateOrder = 'yzx'
		self.lowLeg_jnt.rotateOrder = 'yzx'
		self.ankle_jnt.rotateOrder = 'yzx'
		self.ball_jnt.rotateOrder = 'yzx'
		self.toe_jnt.rotateOrder = 'yzx'
		
		# Leg control
		self.leg_ctrl = pc.Control( 'stick' )
		self.legCtrl_grp = pc.group( self.leg_ctrl )
		self.legCtrlGrp_parCons = pc.parentConstraint( self.ankle_jnt , self.legCtrl_grp )
		self.legCtrl_grp.parent( self.legAnim_grp )
		
		# Leg control - shape adjustment
		self.leg_ctrl.color = 'green'
		self.leg_ctrl.scaleShape( 3 * charSize )
		
		# Leg control - foot scale attribute
		self.leg_ctrl.add( ln='footScale' , dv=1 , k=True )
		self.leg_ctrl.attr( 'footScale' ) >> self.ankle_jnt.attr( 'sx' )
		self.leg_ctrl.attr( 'footScale' ) >> self.ankle_jnt.attr( 'sy' )
		self.leg_ctrl.attr( 'footScale' ) >> self.ankle_jnt.attr( 'sz' )
		
		# ----- FK -----
		# FK main group
		self.legFkCtrl_grp = pc.Null()
		self.legFkCtrl_grp.snap( self.legAnim_grp )
		self.legFkCtrl_grp.parent( self.legAnim_grp )
		
		self.legFkJnt_grp = pc.Null()
		self.legFkJnt_grp.snap( self.legAnim_grp )
		self.legFkJnt_grp.parent( self.legJnt_grp )
		
		# FK joints
		self.upLegFk_jnt = rigTools.jointAt( upLeg )
		self.midLegFk_jnt = rigTools.jointAt( midLeg )
		self.lowLegFk_jnt = rigTools.jointAt( lowLeg )
		self.ankleFk_jnt = rigTools.jointAt( ankle )
		self.ballFk_jnt = rigTools.jointAt( ball )
		self.toeFk_jnt = rigTools.jointAt( toe )
		
		self.toeFk_jnt.parent( self.ballFk_jnt )
		self.ballFk_jnt.parent( self.ankleFk_jnt )
		self.ankleFk_jnt.parent( self.lowLegFk_jnt )
		self.lowLegFk_jnt.parent( self.midLegFk_jnt )
		self.midLegFk_jnt.parent( self.upLegFk_jnt )
		self.upLegFk_jnt.parent( self.legFkJnt_grp )
		self.ballFk_jnt.attr('ssc').v = 0
		
		self.upLegFk_jnt.rotateOrder = 'yzx'
		self.midLegFk_jnt.rotateOrder = 'yzx'
		self.lowLegFk_jnt.rotateOrder = 'yzx'
		self.ankleFk_jnt.rotateOrder = 'yzx'
		self.ballFk_jnt.rotateOrder = 'yzx'
		self.toeFk_jnt.rotateOrder = 'yzx'
		
		# FK controls
		self.upLegFk_ctrl = rigTools.jointControl( 'circle' )
		self.upLegFkCtrlZro_grp = rigTools.zeroGroup( self.upLegFk_ctrl )
		
		self.midLegFk_ctrl = rigTools.jointControl( 'circle' )
		self.midLegFkGmbl_ctrl = pc.addGimbal( self.midLegFk_ctrl )
		self.midLegFkCtrlZro_grp = rigTools.zeroGroup( self.midLegFk_ctrl )
		
		self.lowLegFk_ctrl = rigTools.jointControl( 'circle' )
		self.lowLegFkGmbl_ctrl = pc.addGimbal( self.lowLegFk_ctrl )
		self.lowLegFkCtrlZro_grp = rigTools.zeroGroup( self.lowLegFk_ctrl )
		
		self.ankleFk_ctrl = rigTools.jointControl( 'circle' )
		self.ankleFkGmbl_ctrl = pc.addGimbal( self.ankleFk_ctrl )
		self.ankleFkCtrlZro_grp = rigTools.zeroGroup( self.ankleFk_ctrl )
		self.ankleScaOfst_grp = pc.Null()
		self.ankleScaOfst_grp.parent( self.ankleFkGmbl_ctrl )
		
		self.toeFk_ctrl = rigTools.jointControl( 'circle' )
		self.toeFkGmbl_ctrl = pc.addGimbal( self.toeFk_ctrl )
		self.toeFkCtrlZro_grp = rigTools.zeroGroup( self.toeFk_ctrl )
		
		# FK control - parenting and positioning
		self.upLegFkCtrlZro_grp.snapPoint( upLeg )
		self.upLegFk_ctrl.snapOrient( upLeg )
		self.upLegFk_ctrl.freeze( r=True )
		
		self.upLegFkGmbl_ctrl = pc.addGimbal( self.upLegFk_ctrl )

		self.midLegFkCtrlZro_grp.snap( midLeg )
		self.lowLegFkCtrlZro_grp.snap( lowLeg )
		self.ankleFkCtrlZro_grp.snap( ankle )
		self.toeFkCtrlZro_grp.snap( ball )
		
		self.toeFkCtrlZro_grp.parent( self.ankleScaOfst_grp )
		self.ankleFkCtrlZro_grp.parent( self.lowLegFkGmbl_ctrl )
		self.lowLegFkCtrlZro_grp.parent( self.midLegFkGmbl_ctrl )
		self.midLegFkCtrlZro_grp.parent( self.upLegFkGmbl_ctrl )
		self.upLegFkCtrlZro_grp.parent( self.legFkCtrl_grp )
		
		# FK control - shape adjustment
		self.upLegFk_ctrl.color = 'red'
		self.midLegFk_ctrl.color = 'red'
		self.lowLegFk_ctrl.color = 'red'
		self.ankleFk_ctrl.color = 'red'
		self.toeFk_ctrl.color = 'red'
		
		self.upLegFk_ctrl.scaleShape( 3 * charSize )
		self.midLegFk_ctrl.scaleShape( 3 * charSize )
		self.lowLegFk_ctrl.scaleShape( 3 * charSize )
		self.ankleFk_ctrl.scaleShape( 3 * charSize )
		self.toeFk_ctrl.scaleShape( 3 * charSize )
		
		# FK control - rotate order adjustment
		self.upLegFk_ctrl.rotateOrder = 'yzx'
		self.upLegFkGmbl_ctrl.rotateOrder = 'yzx'
		self.midLegFk_ctrl.rotateOrder = 'yzx'
		self.midLegFkGmbl_ctrl.rotateOrder = 'yzx'
		self.lowLegFk_ctrl.rotateOrder = 'yzx'
		self.lowLegFkGmbl_ctrl.rotateOrder = 'yzx'
		self.ankleFk_ctrl.rotateOrder = 'yzx'
		self.ankleFkGmbl_ctrl.rotateOrder = 'yzx'
		self.toeFk_ctrl.rotateOrder = 'yzx'
		self.toeFkGmbl_ctrl.rotateOrder = 'yzx'
		
		# FK control - stretch control
		self.upLegFkStretch_add , self.upLegFkStretch_mul = rigTools.fkStretch( ctrl = self.upLegFk_ctrl , target = self.midLegFkCtrlZro_grp )
		self.midLegFkStretch_add , self.midLegFkStretch_mul = rigTools.fkStretch( ctrl = self.midLegFk_ctrl , target = self.lowLegFkCtrlZro_grp )
		self.lowLegFkStretch_add , self.lowLegFkStretch_mul = rigTools.fkStretch( ctrl = self.lowLegFk_ctrl , target = self.ankleFkCtrlZro_grp )
		self.toeFkStretch_add , self.toeFkStretch_mul = rigTools.fkStretch( ctrl = self.toeFk_ctrl , target = self.toeFk_jnt )
		
		# FK control - Adjusting stretch amplitude
		self.upLefFkStretchAmp_mul = rigTools.attrAmper( self.upLegFk_ctrl.attr('stretch') , self.upLegFkStretch_mul.attr('i2') , dv = 0.1 )
		self.midLefFkStretchAmp_mul = rigTools.attrAmper( self.midLegFk_ctrl.attr('stretch') , self.midLegFkStretch_mul.attr('i2') , dv = 0.1 )
		self.lowLegFkStretchAmp_mul = rigTools.attrAmper( self.lowLegFk_ctrl.attr('stretch') , self.lowLegFkStretch_mul.attr('i2') , dv = 0.1 )
		self.toeFkStretchAmp_mul = rigTools.attrAmper( self.toeFk_ctrl.attr('stretch') , self.toeFkStretch_mul.attr('i2') , dv = 0.1 )
		
		# FK control - connect to joint
		self.upLegFkJnt_parCons = pc.parentConstraint( self.upLegFkGmbl_ctrl , self.upLegFk_jnt )
		self.midLegFkJnt_parCons = pc.parentConstraint( self.midLegFkGmbl_ctrl , self.midLegFk_jnt )
		self.lowLegFkJnt_parCons = pc.parentConstraint( self.lowLegFkGmbl_ctrl , self.lowLegFk_jnt )
		self.ankleFkJnt_parCons = pc.parentConstraint( self.ankleFkGmbl_ctrl , self.ankleFk_jnt )
		self.ballFkJnt_parCons = pc.parentConstraint( self.toeFkGmbl_ctrl , self.ballFk_jnt )
		
		# FK control - local/world setup
		self.upLegFkCtrlLoc_grp,self.upLegFkCtrlWor_grp,self.upLegFkCtrlWorGrp_oriCons,self.upLegFkCtrlZroGrp_oriCons,self.upLegFkCtrlZroGrpOrCons_rev = rigTools.orientLocalWorldCtrl( self.upLegFk_ctrl , self.legFkCtrl_grp , animGrp , self.upLegFkCtrlZro_grp )
		
		# FK control - scale control
		self.leg_ctrl.attr('footScale') >> self.ankleFk_jnt.attr('sx')
		self.leg_ctrl.attr('footScale') >> self.ankleFk_jnt.attr('sy')
		self.leg_ctrl.attr('footScale') >> self.ankleFk_jnt.attr('sz')
		self.leg_ctrl.attr('footScale') >> self.ankleScaOfst_grp.attr('sx')
		self.leg_ctrl.attr('footScale') >> self.ankleScaOfst_grp.attr('sy')
		self.leg_ctrl.attr('footScale') >> self.ankleScaOfst_grp.attr('sz')
		
		# ----- IK -----
		# IK main group
		self.legIkCtrl_grp = pc.Null()
		self.legIkCtrl_grp.snap( self.legAnim_grp )
		self.legIkCtrl_grp.parent( self.legAnim_grp )
		
		self.legIkJnt_grp = pc.Null()
		self.legIkJnt_grp.snap( self.legAnim_grp )
		self.legIkJnt_grp.parent( self.legJnt_grp )
		
		# IK joints
		self.upLegIk_jnt = rigTools.jointAt( upLeg )
		self.midLegIk_jnt = rigTools.jointAt( midLeg )
		self.lowLegIk_jnt = rigTools.jointAt( lowLeg )
		self.ankleIk_jnt = rigTools.jointAt( ankle )
		self.ballIk_jnt = rigTools.jointAt( ball )
		self.toeIk_jnt = rigTools.jointAt( toe )
		
		# IK joint - parenting
		self.toeIk_jnt.parent( self.ballIk_jnt )
		self.ballIk_jnt.parent( self.ankleIk_jnt )
		self.ankleIk_jnt.parent( self.lowLegIk_jnt )
		self.lowLegIk_jnt.parent( self.midLegIk_jnt )
		self.midLegIk_jnt.parent( self.upLegIk_jnt )
		self.upLegIk_jnt.parent( self.legIkJnt_grp )
		self.ballIk_jnt.attr('ssc').v = 0
		
		# IK-L joints
		self.upLegIkL_jnt = rigTools.jointAt( upLeg )
		self.midLegIkL_jnt = rigTools.jointAt( midLeg )
		self.lowLegIkL_jnt = rigTools.jointAt( lowLeg )
		self.ankleIkL_jnt = rigTools.jointAt( ankle )
		
		# IK-L joint - parenting
		self.ankleIkL_jnt.parent( self.lowLegIkL_jnt )
		self.lowLegIkL_jnt.parent( self.midLegIkL_jnt )
		self.midLegIkL_jnt.parent( self.upLegIkL_jnt )
		self.upLegIkL_jnt.parent( self.legIkJnt_grp )
		
		self.upLegIk_jnt.rotateOrder = 'yzx'
		self.midLegIk_jnt.rotateOrder = 'yzx'
		self.lowLegIk_jnt.rotateOrder = 'yzx'
		self.ankleIk_jnt.rotateOrder = 'yzx'
		self.ballIk_jnt.rotateOrder = 'yzx'
		self.toeIk_jnt.rotateOrder = 'yzx'
		
		self.upLegIkL_jnt.rotateOrder = 'yzx'
		self.midLegIkL_jnt.rotateOrder = 'yzx'
		self.lowLegIkL_jnt.rotateOrder = 'yzx'
		self.ankleIkL_jnt.rotateOrder = 'yzx'
		
		# IK controls
		self.legIkRoot_ctrl = rigTools.jointControl( 'cube' )
		self.legIkRootCtrlZro_grp = rigTools.zeroGroup( self.legIkRoot_ctrl )
		
		self.legIk_ctrl = rigTools.jointControl( 'cube' )
		self.legIkCtrlLock_grp = pc.group( self.legIk_ctrl )
		self.legIkCtrlZro_grp = pc.group( self.legIkCtrlLock_grp )
		
		self.kneeIk_ctrl = pc.Control( 'plus' )
		self.kneeIkCtrlZro_grp = pc.group( self.kneeIk_ctrl )
		
		# IK control - parenting and positioning
		self.legIkRootCtrlZro_grp.snapPoint( upLeg )
		
		self.legIkCtrlZro_grp.snapPoint( ankle )
		self.legIk_ctrl.snapOrient( ankle )
		self.legIk_ctrl.freeze( t = False , r = True , s = False )
		
		self.legIkGmbl_ctrl = pc.addGimbal( self.legIk_ctrl )
		
		self.kneeIkCtrlZro_grp.snapPoint( kneeIkCtrl )
		
		self.legIkRootCtrlZro_grp.parent( self.legIkCtrl_grp )
		self.legIkCtrlZro_grp.parent( self.legIkRoot_ctrl )
		self.kneeIkCtrlZro_grp.parent( self.legIkRoot_ctrl )
		
		# IK control - shape adjustment
		self.legIkRoot_ctrl.color = 'blue'
		self.legIk_ctrl.color = 'blue'
		self.kneeIk_ctrl.color = 'blue'
		
		self.legIkRoot_ctrl.scaleShape( 3 * charSize )
		self.legIk_ctrl.scaleShape( 3 * charSize )
		self.kneeIk_ctrl.scaleShape( 3 * charSize )
		
		# IK control - knee curve
		self.kneeIkCtrl_crv , self.kneeIkCtrl1_clstr , self.kneeIkCtrl2_clstr = rigTools.crvGuide( ctrl = self.kneeIk_ctrl , target = self.midLegIk_jnt )
		
		self.kneeIkCtrl_crv.attr('inheritsTransform').value = 0
		self.kneeIkCtrl_crv.attr('overrideEnabled').value = 1
		self.kneeIkCtrl_crv.attr('overrideDisplayType').value = 2
		
		self.kneeIkCtrl_crv.parent( self.legIkCtrl_grp )
		self.kneeIkCtrl_crv.attr('t').value = (0,0,0)
		self.kneeIkCtrl_crv.attr('r').value = (0,0,0)
		
		# IK control - rotate order adjustment
		self.legIk_ctrl.rotateOrder = 'xzy'
		self.legIkGmbl_ctrl.rotateOrder = 'xzy'
		
		# IK control - local/world setup
		# parentLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , oriGrp = '' )
		# return locGrp , worGrp , worGrpParCons , parGrpParCons , parGrpParConsRev
		( self.legIkCtrlLoc_grp ,
		self.legIkCtrlWor_grp ,
		self.legIkCtrlWorGrp_oriCons ,
		self.legIkCtrlZroGrp_oriCons ,
		self.legIkCtrlZroGrpOrCons_rev ) = rigTools.parentLocalWorldCtrl( self.legIk_ctrl ,
																			self.legIkRoot_ctrl ,
																			animGrp ,
																			self.legIkCtrlZro_grp
																			)
		( self.kneeIkCtrlLoc_grp ,
		self.kneeIkCtrlWor_grp ,
		self.kneeIkCtrlWorGrp_oriCons ,
		self.kneeIkCtrlZroGrp_oriCons ,
		self.kneeIkCtrlZroGrpOrCons_rev ) = rigTools.parentLocalWorldCtrl( self.kneeIk_ctrl ,
																			self.legIkGmbl_ctrl ,
																			animGrp ,
																			self.kneeIkCtrlZro_grp
																			)
		
		# IK handles
		self.legIkL_ikh = pc.IkRp( sj = self.upLegIkL_jnt , ee = self.ankleIkL_jnt )
		
		self.lowLegIk_ikh = pc.IkRp( sj = self.upLegIk_jnt , ee = self.lowLegIk_jnt )
		self.ankleIk_ikh = pc.IkRp( sj = self.lowLegIk_jnt , ee = self.ankleIk_jnt )
		self.ballIk_ikh = pc.IkRp( sj = self.ankleIk_jnt , ee = self.ballIk_jnt )
		self.toeIk_ikh = pc.IkRp( sj = self.ballIk_jnt , ee = self.toeIk_jnt )
		self.legIkIkh_polCons = pc.poleVectorConstraint( self.kneeIk_ctrl , self.legIkL_ikh )
		
		self.legIkh_grp = pc.Null()
		self.legIkLIkhZro_grp = rigTools.zeroGroup( self.legIkL_ikh  )
		self.lowLegIkIkhZro_grp = rigTools.zeroGroup( self.lowLegIk_ikh )
		self.ankleIkIkhZro_grp = rigTools.zeroGroup( self.ankleIk_ikh )
		self.ballIkIkhZro_grp = rigTools.zeroGroup( self.ballIk_ikh  )
		self.toeIkIkhZro_grp = rigTools.zeroGroup( self.toeIk_ikh  )
		
		self.legIkLIkhZro_grp.parent( self.legIkh_grp )
		self.lowLegIkIkhZro_grp.parent( self.legIkh_grp )
		self.ankleIkIkhZro_grp.parent( self.legIkh_grp )
		self.ballIkIkhZro_grp.parent( self.legIkh_grp )
		self.toeIkIkhZro_grp.parent( self.legIkh_grp )
		self.legIkh_grp.parent( ikhGrp )
		
		# IK handles - pivots
		self.legFlexIkPiv_grp = pc.Null()
		self.legFlexIkPivZro_grp = pc.group( self.legFlexIkPiv_grp )
		self.ankleRollIkPiv_grp = pc.Null()
		self.ankleRollIk_ctrl = pc.Control( 'circle' )
		self.toeBendIkPiv_grp = pc.Null()
		self.footInIkPiv_grp = pc.Null()
		self.footOutIkPiv_grp = pc.Null()
		self.heelIkPiv_grp = pc.Null()
		self.toeIkPiv_grp = pc.Null()
		self.legIkPiv_grp = pc.Null()
		
		self.legIkLIkhPiv_grp = pc.Null()
		self.lowLegIkIkhPiv_grp = pc.Null()
		self.ankleIkIkhPiv_grp = pc.Null()
		self.ballIkIkhPiv_grp = pc.Null()
		self.toeIkIkhPiv_grp = pc.Null()
		
		self.ankleRollIk_ctrl.rotateOrder = 'xzy'
		self.ankleRollIk_ctrl.color = 'blue'
		self.ankleRollIk_ctrl.scaleShape( 3 * charSize )
		
		# IK handles - positioning and parenting
		self.legFlexIkPivZro_grp.snapPoint( ankle )
		self.ankleRollIkPiv_grp.snapPoint( ball )
		self.ankleRollIk_ctrl.snapPoint( ball )
		self.toeBendIkPiv_grp.snapPoint( ball )
		self.footInIkPiv_grp.snapPoint( footIn )
		self.footOutIkPiv_grp.snapPoint( footOut )
		self.heelIkPiv_grp.snapPoint( heel )
		self.toeIkPiv_grp.snapPoint( toe )
		self.legIkPiv_grp.snapPoint( ankle )
		
		self.legIkLIkhPiv_grp.snap( self.legIkLIkhZro_grp )
		self.lowLegIkIkhPiv_grp.snap( self.lowLegIkIkhZro_grp )
		self.ankleIkIkhPiv_grp.snap( self.ankleIkIkhZro_grp )
		self.ballIkIkhPiv_grp.snap( self.ballIkIkhZro_grp )
		self.toeIkIkhPiv_grp.snap( self.toeIkIkhZro_grp )
		
		self.legFlexIkPivZro_grp.parent( self.lowLegIkL_jnt )
		self.ankleRollIkPiv_grp.parent( self.footInIkPiv_grp )
		self.ankleRollIk_ctrl.parent( self.ankleRollIkPiv_grp )
		self.toeBendIkPiv_grp.parent( self.footInIkPiv_grp )
		self.footInIkPiv_grp.parent( self.footOutIkPiv_grp )
		self.footOutIkPiv_grp.parent( self.heelIkPiv_grp )
		self.heelIkPiv_grp.parent( self.toeIkPiv_grp )
		self.toeIkPiv_grp.parent( self.legIkPiv_grp )
		self.legIkPiv_grp.parent( self.legIkGmbl_ctrl )
		
		# self.legIkLIkhZro_grp.parent( self.ankleRollIk_ctrl )
		# self.ballIkIkhZro_grp.parent( self.ankleRollIk_ctrl )
		# self.toeIkIkhZro_grp.parent( self.toeBendIkPiv_grp )
		# self.lowLegIkIkhZro_grp.parent( self.legFlexIkPiv_grp )
		self.legIkLIkhPiv_grp.parent( self.ankleRollIk_ctrl )
		self.lowLegIkIkhPiv_grp.parent( self.legFlexIkPiv_grp )
		self.ankleIkIkhPiv_grp.parent( self.ankleIkL_jnt )
		self.ballIkIkhPiv_grp.parent( self.ankleRollIk_ctrl )
		self.toeIkIkhPiv_grp.parent( self.toeBendIkPiv_grp )
		
		self.upLegIkJnt_pntCons = pc.pointConstraint( self.legIkRoot_ctrl , self.upLegIk_jnt )
		self.upLegIkJnt_pntCons = pc.pointConstraint( self.legIkRoot_ctrl , self.upLegIkL_jnt )
		
		self.legIk_ctrl.add( ln = 'twist' , k = True )
		self.legIk_ctrl.attr('twist') >> self.legIkL_ikh.attr('twist')
		
		self.legIkLIkhZroGrp_parCons = pc.parentConstraint( self.legIkLIkhPiv_grp , self.legIkLIkhZro_grp )
		self.lowLegIkIkhZroGrp_parCons = pc.parentConstraint( self.lowLegIkIkhPiv_grp , self.lowLegIkIkhZro_grp )
		self.ankleIkIkhZroGrp_parCons = pc.parentConstraint( self.ankleIkIkhPiv_grp , self.ankleIkIkhZro_grp )
		self.ballIkIkhZroGrp_parCons = pc.parentConstraint( self.ballIkIkhPiv_grp , self.ballIkIkhZro_grp )
		self.toeIkIkhZroGrp_parCons = pc.parentConstraint( self.toeIkIkhPiv_grp , self.toeIkIkhZro_grp )
		
		# IK Stretch - Attributes
		self.legIk_ctrl.add( ln = '__stretch__' , k = True )
		self.legIk_ctrl.attr('__stretch__').set( l = True )
		self.legIk_ctrl.add( ln = 'autoStretch' , min = 0 , max = 1 , k = True )
		self.legIk_ctrl.add( ln = 'upLegStretch' , k = True )
		self.legIk_ctrl.add( ln = 'midLegStretch' , k = True )
		self.legIk_ctrl.add( ln = 'lowLegStretch' , k = True )
		self.legIk_ctrl.add( ln = 'toeStretch' , k = True )
		
		# IK handles - leg control attributes
		# '__foot__' , 'heel_roll' , 'ball_roll' , 'toe_roll' , 'heel_twist' , 'toe_twist' , 'foot_rock' , 'toe_bend'
		self.legIk_ctrl.add( ln = '__foot__' , k = True )
		self.legIk_ctrl.attr('__foot__').set( l = True )
		
		attrs = ( 'legFlex' , 'legBend' , 'heelRoll' , 'ballRoll' , 'toeRoll' , 'heelTwist' , 'toeTwist' , 'footRock' , 'toeBend' )
		for attr in attrs :
			self.legIk_ctrl.add( ln = attr , k = True )
		
		self.legIk_ctrl.attr('legFlex') >> self.legFlexIkPiv_grp.attr('rx')
		self.legIk_ctrl.attr('legBend') >> self.legFlexIkPiv_grp.attr('rz')
		self.legIk_ctrl.attr('heelRoll') >> self.heelIkPiv_grp.attr('rx')
		self.legIk_ctrl.attr('ballRoll') >> self.ankleRollIkPiv_grp.attr('rx')
		self.legIk_ctrl.attr('toeRoll') >> self.toeIkPiv_grp.attr('rx')
		self.legIk_ctrl.attr('heelTwist') >> self.heelIkPiv_grp.attr('ry')
		self.legIk_ctrl.attr('toeTwist') >> self.toeIkPiv_grp.attr('ry')
		self.legIk_ctrl.attr('toeBend') >> self.toeBendIkPiv_grp.attr('rx')
		
		self.legIk_ctrl.attr('footRock') >> self.footInIkPiv_grp.attr('rz')
		self.legIk_ctrl.attr('footRock') >> self.footOutIkPiv_grp.attr('rz')
		
		if side == 'LFT' :
			self.footOutIkPiv_grp.attr('xrze').value = 1
			self.footInIkPiv_grp.attr('mrze').value = 1
			self.footOutIkPiv_grp.attr('xrzl').value = 0
			self.footInIkPiv_grp.attr('mrzl').value = 0
		elif side == 'RGT' :
			self.footOutIkPiv_grp.attr('mrze').value = 1
			self.footInIkPiv_grp.attr('xrze').value = 1
			self.footOutIkPiv_grp.attr('mrzl').value = 0
			self.footInIkPiv_grp.attr('xrzl').value = 0
		
		# IK stretch
		self.upLegIkJntPnt_grp = pc.Null()
		self.upLegIkJntPntGrp_pntCons = pc.pointConstraint( self.legIkRoot_ctrl , self.upLegIkJntPnt_grp )
		
		self.legIkCtrlPnt_grp = pc.Null()
		self.legIkCtrlPntGrp_pntCons = pc.pointConstraint( self.legIkLIkhZro_grp , self.legIkCtrlPnt_grp )
		
		#self.kneeIkCtrlPnt_grp = pc.Null()
		#self.kneeIkCtrlPntGrp_pntCons = pc.pointConstraint( self.kneeIkGmbl_ctrl , self.kneeIkCtrlPnt_grp )
		
		self.upLegIkJntPnt_grp.parent( self.legIkRoot_ctrl )
		self.legIkCtrlPnt_grp.parent( self.legIkRoot_ctrl )
		#self.kneeIkCtrlPnt_grp.parent( self.legIkRoot_ctrl )
		
		self.legIkAutoStretch_dist = pc.DistanceBetween()
		#self.upLegIkLock_dist = pc.DistanceBetween()
		#self.lowLegIkLock_dist = pc.DistanceBetween()
		
		self.upLegIkJntPnt_grp.attr('t') >> self.legIkAutoStretch_dist.attr('p1')
		self.legIkCtrlPnt_grp.attr('t') >> self.legIkAutoStretch_dist.attr('p2')
		#self.upLegIkJntPnt_grp.attr('t') >> self.upLegIkLock_dist.attr('p1')
		#self.kneeIkCtrlPnt_grp.attr('t') >> self.upLegIkLock_dist.attr('p2')
		#self.kneeIkCtrlPnt_grp.attr('t') >> self.lowLegIkLock_dist.attr('p1')
		#self.legIkCtrlPnt_grp.attr('t') >> self.lowLegIkLock_dist.attr('p2')
		
		self.legIkAutoStretch_cnd = pc.Condition()
		self.legIkAutoStretch_mdv = pc.MultiplyDivide()
		
		self.upLegIkAutoStretch_mul = pc.MultDoubleLinear()
		self.upLegIkStretch_mul = pc.MultDoubleLinear()
		self.upLegIkAutoStretch_add = pc.AddDoubleLinear()
		self.upLegIkAutoStretch_blnd = pc.BlendTwoAttr()
		
		self.midLegIkAutoStretch_mul = pc.MultDoubleLinear()
		self.midLegIkStretch_mul = pc.MultDoubleLinear()
		self.midLegIkAutoStretch_add = pc.AddDoubleLinear()
		self.midLegIkAutoStretch_blnd = pc.BlendTwoAttr()
		
		self.lowLegIkAutoStretch_mul = pc.MultDoubleLinear()
		self.lowLegIkStretch_mul = pc.MultDoubleLinear()
		self.lowLegIkAutoStretch_add = pc.AddDoubleLinear()
		self.lowLegIkAutoStretch_blnd = pc.BlendTwoAttr()
		
		# IK Stretch - Auto stretch
		upLegDist = self.midLegIk_jnt.attr('ty').value
		midLegDist = self.lowLegIk_jnt.attr('ty').value
		lowLegDist = self.ankleIk_jnt.attr('ty').value
		ikCtrlDist = upLegDist + midLegDist + lowLegDist
		
		self.legIkAutoStretch_dist.attr('d') >> self.legIkAutoStretch_cnd.attr('ft')
		self.legIkAutoStretch_cnd.attr('st').value = abs( ikCtrlDist )
		self.legIkAutoStretch_cnd.attr('op').value = 2
		self.legIkAutoStretch_cnd.attr('cfr').value = 1
		
		self.legIkAutoStretch_mdv.attr('operation').v = 2
		self.legIkAutoStretch_dist.attr('d') >> self.legIkAutoStretch_mdv.attr('i1x')
		self.legIkAutoStretch_mdv.attr('i2x').v = abs( ikCtrlDist )
		# self.legIkAutoStretch_mul.attr('i2').value = 1/ikCtrlDist
		# self.legIkAutoStretch_mul.attr('o') >> self.legIkAutoStretch_cnd.attr('ctr')
		self.legIkAutoStretch_mdv.attr('ox') >> self.legIkAutoStretch_cnd.attr('ctr')
		
		
		self.legIkAutoStretch_cnd.attr('ocr') >> self.upLegIkAutoStretch_mul.attr('i1')
		self.upLegIkAutoStretch_mul.attr('i2').value = upLegDist
		self.legIk_ctrl.attr('autoStretch') >> self.upLegIkAutoStretch_blnd.attr('ab')
		self.upLegIkAutoStretch_blnd.add( ln = 'default' , dv = upLegDist , k = True )
		self.upLegIkAutoStretch_blnd.attr('default') >> self.upLegIkAutoStretch_blnd.last()
		self.upLegIkAutoStretch_mul.attr('o') >> self.upLegIkAutoStretch_blnd.last()
		self.upLegIkAutoStretch_blnd.attr('o') >> self.upLegIkAutoStretch_add.attr('i1')
		self.legIk_ctrl.attr('upLegStretch') >> self.upLegIkStretch_mul.attr('i1')
		self.upLegIkStretch_mul.attr('i2').value = upLegDist
		self.upLegIkStretch_mul.attr('o') >> self.upLegIkAutoStretch_add.attr('i2')
		
		self.legIkAutoStretch_cnd.attr('ocr') >> self.midLegIkAutoStretch_mul.attr('i1')
		self.midLegIkAutoStretch_mul.attr('i2').value = midLegDist
		self.legIk_ctrl.attr('autoStretch') >> self.midLegIkAutoStretch_blnd.attr('ab')
		self.midLegIkAutoStretch_blnd.add( ln = 'default' , dv = midLegDist , k = True )
		self.midLegIkAutoStretch_blnd.attr('default') >> self.midLegIkAutoStretch_blnd.last()
		self.midLegIkAutoStretch_mul.attr('o') >> self.midLegIkAutoStretch_blnd.last()
		self.midLegIkAutoStretch_blnd.attr('o') >> self.midLegIkAutoStretch_add.attr('i1')
		self.legIk_ctrl.attr('midLegStretch') >> self.midLegIkStretch_mul.attr('i1')
		self.midLegIkStretch_mul.attr('i2').value = midLegDist
		self.midLegIkStretch_mul.attr('o') >> self.midLegIkAutoStretch_add.attr('i2')
		
		self.legIkAutoStretch_cnd.attr('ocr') >> self.lowLegIkAutoStretch_mul.attr('i1')
		self.lowLegIkAutoStretch_mul.attr('i2').value = lowLegDist
		self.legIk_ctrl.attr('autoStretch') >> self.lowLegIkAutoStretch_blnd.attr('ab')
		self.lowLegIkAutoStretch_blnd.add( ln = 'default' , dv = lowLegDist , k = True )
		self.lowLegIkAutoStretch_blnd.attr('default') >> self.lowLegIkAutoStretch_blnd.last()
		self.lowLegIkAutoStretch_mul.attr('o') >> self.lowLegIkAutoStretch_blnd.last()
		self.lowLegIkAutoStretch_blnd.attr('o') >> self.lowLegIkAutoStretch_add.attr('i1')
		self.legIk_ctrl.attr('lowLegStretch') >> self.lowLegIkStretch_mul.attr('i1')
		self.lowLegIkStretch_mul.attr('i2').value = lowLegDist
		self.lowLegIkStretch_mul.attr('o') >> self.lowLegIkAutoStretch_add.attr('i2')
		
		# IK Stretch - connect to joint
		self.upLegIkAutoStretch_add.attr('o') >> self.midLegIk_jnt.attr('ty')
		self.midLegIkAutoStretch_add.attr('o') >> self.lowLegIk_jnt.attr('ty')
		self.lowLegIkAutoStretch_add.attr('o') >> self.ankleIk_jnt.attr('ty')
		
		self.upLegIkAutoStretch_add.attr('o') >> self.midLegIkL_jnt.attr('ty')
		self.midLegIkAutoStretch_add.attr('o') >> self.lowLegIkL_jnt.attr('ty')
		self.lowLegIkAutoStretch_add.attr('o') >> self.ankleIkL_jnt.attr('ty')
		
		# IK Stretch - toe stretch
		self.legIkToeStretch_add , self.legIkToeStretch_mul = rigTools.fkStretch( ctrl = self.legIk_ctrl , attr = 'toeStretch' , target = self.toeIk_jnt )
		
		# IK Stretch - Adjusting stretch amplitude
		self.upLegIkStretchAmp_mul = rigTools.attrAmper( self.legIk_ctrl.attr('upLegStretch') , self.upLegIkStretch_mul.attr('i1') , dv = 0.1 )
		self.midLegIkStretchAmp_mul = rigTools.attrAmper( self.legIk_ctrl.attr('midLegStretch') , self.midLegIkStretch_mul.attr('i1') , dv = 0.1 )
		self.lowLegIkStretchAmp_mul = rigTools.attrAmper( self.legIk_ctrl.attr('lowLegStretch') , self.lowLegIkStretch_mul.attr('i1') , dv = 0.1 )
		self.toeIkStretchAmp_mul = rigTools.attrAmper( self.legIk_ctrl.attr('toeStretch') , self.legIkToeStretch_mul.attr('i2') , dv = 0.1 )
		
		# Ik Leg - scale control
		self.leg_ctrl.attr('footScale') >> self.ankleIk_jnt.attr('sx')
		self.leg_ctrl.attr('footScale') >> self.ankleIk_jnt.attr('sy')
		self.leg_ctrl.attr('footScale') >> self.ankleIk_jnt.attr('sz')
		self.leg_ctrl.attr('footScale') >> self.legIkPiv_grp.attr('sx')
		self.leg_ctrl.attr('footScale') >> self.legIkPiv_grp.attr('sy')
		self.leg_ctrl.attr('footScale') >> self.legIkPiv_grp.attr('sz')
		
		# FK/IK blending
		self.legFkIk_rev = pc.Reverse()
		self.leg_ctrl.add( ln = 'fkIk' , min = 0 , max = 1 , k = True )
		self.leg_ctrl.attr( 'fkIk' ) >> self.legFkIk_rev.attr( 'ix' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.legIkCtrl_grp.attr( 'v' )
		self.legFkIk_rev.attr( 'ox' ) >> self.legFkCtrl_grp.attr( 'v' )
		
		# FK/IK blending - Using blendColors
		# self.upLegJntT_bc = rigTools.blend2Vectors( 't' , self.upLegIk_jnt , self.upLegFk_jnt , self.upLeg_jnt )
		# self.midLegJntT_bc = rigTools.blend2Vectors( 't' , self.midLegIk_jnt , self.midLegFk_jnt , self.midLeg_jnt )
		# self.lowLegJntT_bc = rigTools.blend2Vectors( 't' , self.lowLegIk_jnt , self.lowLegFk_jnt , self.lowLeg_jnt )
		# self.ankleJntT_bc = rigTools.blend2Vectors( 't' , self.ankleIk_jnt , self.ankleFk_jnt , self.ankle_jnt )
		# self.ballJntT_bc = rigTools.blend2Vectors( 't' , self.ballIk_jnt , self.ballFk_jnt , self.ball_jnt )
		# self.toeJntT_bc = rigTools.blend2Vectors( 't' , self.toeIk_jnt , self.toeFk_jnt , self.toe_jnt )
		
		# self.upLegJntR_bc = rigTools.blend2Vectors( 'r' , self.upLegIk_jnt , self.upLegFk_jnt , self.upLeg_jnt )
		# self.midLegJntR_bc = rigTools.blend2Vectors( 'r' , self.midLegIk_jnt , self.midLegFk_jnt , self.midLeg_jnt )
		# self.lowLegJntR_bc = rigTools.blend2Vectors( 'r' , self.lowLegIk_jnt , self.lowLegFk_jnt , self.lowLeg_jnt )
		# self.ankleJntR_bc = rigTools.blend2Vectors( 'r' , self.ankleIk_jnt , self.ankleFk_jnt , self.ankle_jnt )
		# self.ballJntR_bc = rigTools.blend2Vectors( 'r' , self.ballIk_jnt , self.ballFk_jnt , self.ball_jnt )
		# self.toeJntR_bc = rigTools.blend2Vectors( 'r' , self.toeIk_jnt , self.toeFk_jnt , self.toe_jnt )
		
		# self.leg_ctrl.attr( 'fkIk' ) >> self.upLegJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.midLegJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.lowLegJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ankleJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ballJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.toeJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.upLegJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.midLegJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.lowLegJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ankleJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ballJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.toeJntR_bc.attr( 'blender' )
		
		# FK/IK blending - Using parentConstraint
		self.upLegJnt_parCons = pc.parentConstraint( self.upLegFk_jnt ,
														self.upLegIk_jnt ,
														self.upLeg_jnt
														)
		self.midLegJnt_parCons = pc.parentConstraint( self.midLegFk_jnt ,
														self.midLegIk_jnt ,
														self.midLeg_jnt
														)
		self.lowLegJnt_parCons = pc.parentConstraint( self.lowLegFk_jnt ,
														self.lowLegIk_jnt ,
														self.lowLeg_jnt
														)
		self.ankleJnt_parCons = pc.parentConstraint( self.ankleFk_jnt ,
														self.ankleIk_jnt ,
														self.ankle_jnt
														)
		self.ballJnt_parCons = pc.parentConstraint( self.ballFk_jnt ,
														self.ballIk_jnt ,
														self.ball_jnt
														)
		self.toeJnt_parCons = pc.parentConstraint( self.toeFk_jnt ,
														self.toeIk_jnt ,
														self.toe_jnt
														)
		
		self.leg_ctrl.attr( 'fkIk' ) >> self.upLegJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.midLegJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.lowLegJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.ankleJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.ballJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.toeJnt_parCons.attr( 'w1' )
		
		self.legFkIk_rev.attr( 'ox' ) >> self.upLegJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.midLegJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.lowLegJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.ankleJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.ballJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.toeJnt_parCons.attr( 'w0' )
		
		# Group
		self.legAnim_grp.parent( animGrp )
		self.legJnt_grp.parent( jntGrp )
		
		# Ribbon
		self.legRbnAnim_grp = pc.Null()
		
		rbnAx = 'y-'
		rbnAim = (0,-1,0)
		if side == 'RGT' :
			rbnUp = (0,0,-1)
			rbnAmp = -1
		else :
			rbnUp = (0,0,1)
			rbnAmp = 1
		
		# Ribbon - Space
		self.legRbnSpc_grp = pc.Null()
		
		self.upLegRbnSpc_grp = pc.Null()
		self.upLegRbnSpcZro_grp = pc.group( self.upLegRbnSpc_grp )
		
		self.upLegRbnSpc_grp.rotateOrder = 'yzx'
		
		self.upLegRbnSpcZro_grp.snap( upLeg )
		self.upLegRbnSpcGrp_parCons = pc.parentConstraint( self.upLeg_jnt , self.upLegRbnSpc_grp )
		
		self.midLegRbnSpc_grp = pc.Null()
		self.midLegRbnSpcZro_grp = pc.group( self.midLegRbnSpc_grp )
		
		self.midLegRbnSpc_grp.rotateOrder = 'yzx'
		
		self.midLegRbnSpcZro_grp.snap( upLeg )
		self.midLegRbnSpcZroGrp_parCons = pc.parentConstraint( self.upLeg_jnt , self.midLegRbnSpcZro_grp , mo = True )
		self.midLegRbnSpcGrp_parCons = pc.parentConstraint( self.midLeg_jnt , self.midLegRbnSpc_grp )
		
		self.lowLegRbnSpc_grp = pc.Null()
		self.lowLegRbnSpcZro_grp = pc.group( self.lowLegRbnSpc_grp )
		
		self.lowLegRbnSpc_grp.rotateOrder = 'yzx'
		
		self.lowLegRbnSpcZro_grp.snap( lowLeg )
		self.lowLegRbnSpcZroGrp_parCons = pc.parentConstraint( self.midLeg_jnt , self.lowLegRbnSpcZro_grp , mo = True )
		self.lowLegRbnSpcGrp_parCons = pc.parentConstraint( self.lowLeg_jnt , self.lowLegRbnSpc_grp )
		
		self.ankleRbnSpc_grp = pc.Null()
		self.ankleRbnSpcZro_grp = pc.group( self.ankleRbnSpc_grp )
		
		self.ankleRbnSpc_grp.rotateOrder = 'yzx'
		
		self.ankleRbnSpcZro_grp.snap( ankle )
		self.ankleRbnSpcZroGrp_parCons = pc.parentConstraint( self.lowLeg_jnt , self.ankleRbnSpcZro_grp , mo = True )
		self.ankleRbnSpcGrp_parCons = pc.parentConstraint( self.ankle_jnt , self.ankleRbnSpc_grp )
		
		# Ribbon - Transform - group
		self.upLegRbnSpcZro_grp.parent( self.legRbnSpc_grp )
		self.midLegRbnSpcZro_grp.parent( self.legRbnSpc_grp )
		self.lowLegRbnSpcZro_grp.parent( self.legRbnSpc_grp )
		self.ankleRbnSpcZro_grp.parent( self.legRbnSpc_grp )
		self.legRbnSpc_grp.parent( self.legRbnAnim_grp )
		
		# Ribbon control
		self.upKneeRbn_ctrl = pc.Control( 'plus' )
		self.upKneeRbnCtrlZro_grp = pc.group( self.upKneeRbn_ctrl )
		
		self.lowKneeRbn_ctrl = pc.Control( 'plus' )
		self.lowKneeRbnCtrlZro_grp = pc.group( self.lowKneeRbn_ctrl )
		
		# Ribbon control - parenting and positioning
		self.upKneeRbnCtrlZroGrp_pntCons = pc.pointConstraint( self.midLegRbnSpc_grp , self.upKneeRbnCtrlZro_grp )
		self.upKneeRbnCtrlZroGrp_oriCons = pc.orientConstraint( self.upLegRbnSpc_grp , self.upKneeRbnCtrlZro_grp , mo = True )
		
		self.lowKneeRbnCtrlZroGrp_pntCons = pc.pointConstraint( self.lowLegRbnSpc_grp , self.lowKneeRbnCtrlZro_grp )
		self.lowKneeRbnCtrlZroGrp_oriCons = pc.orientConstraint( self.lowLegRbnSpc_grp , self.lowKneeRbnCtrlZro_grp , mo = True )
		
		# Ribbon control - shape adjustment
		self.upKneeRbn_ctrl.color = 'yellow'
		self.upKneeRbn_ctrl.scaleShape( 3 * charSize )
		
		self.lowKneeRbn_ctrl.color = 'yellow'
		self.lowKneeRbn_ctrl.scaleShape( 3 * charSize )
		
		# Ribbon upper leg
		if ribbon :
			self.upLegRbn = pr.RibbonIkHi( size = self.upLegLen , ax = rbnAx )
		else :
			self.upLegRbn = pr.RibbonIkLow( size = self.upLegLen , ax = rbnAx )
		
		self.upLegRbn.rbnAnim_grp.snapPoint( upLeg )
		mc.delete( pc.aimConstraint( midLeg ,
										self.upLegRbn.rbnAnim_grp ,
										aim = rbnAim , u = rbnUp ,
										wut = 'objectrotation' ,
										wuo = upLeg ,
										wu = (0,0,1)
									)
				)
		self.upLegRbn_parCons = pc.parentConstraint( self.upLegRbnSpc_grp , self.upLegRbn.rbnAnim_grp , mo = True )
		self.upLegRbnRootCtrl_pntCons = pc.pointConstraint( self.upLegRbnSpc_grp , self.upLegRbn.rbnRoot_ctrl )
		self.upLegRbnEndCtrl_pntCons = pc.pointConstraint( self.upKneeRbn_ctrl , self.upLegRbn.rbnEnd_ctrl )
		
		# Ribbon middle leg
		if ribbon :
			self.midLegRbn = pr.RibbonIkHi( size = self.midLegLen , ax = rbnAx )
		else :
			self.midLegRbn = pr.RibbonIkLow( size = self.midLegLen , ax = rbnAx )
		
		self.midLegRbn.rbnAnim_grp.snapPoint( midLeg )
		mc.delete( pc.aimConstraint( lowLeg ,
										self.midLegRbn.rbnAnim_grp ,
										aim = rbnAim , u = rbnUp ,
										wut = 'objectrotation' ,
										wuo = midLeg , wu = (0,0,1)
									)
				)
		self.midLegRbn_parCons = pc.parentConstraint( self.midLegRbnSpc_grp , self.midLegRbn.rbnAnim_grp , mo = True )
		self.midLegRbnRootCtrl_pntCons = pc.pointConstraint( self.upKneeRbn_ctrl , self.midLegRbn.rbnRoot_ctrl )
		self.midLegRbnEndCtrl_pntCons = pc.pointConstraint( self.lowKneeRbn_ctrl , self.midLegRbn.rbnEnd_ctrl )
		
		# Ribbon lower leg
		if ribbon :
			self.lowLegRbn = pr.RibbonIkHi( size = self.lowLegLen , ax = rbnAx )
		else :
			self.lowLegRbn = pr.RibbonIkLow( size = self.lowLegLen , ax = rbnAx )
		
		self.lowLegRbn.rbnAnim_grp.snapPoint( lowLeg )
		mc.delete( pc.aimConstraint( ankle ,
										self.lowLegRbn.rbnAnim_grp ,
										aim = rbnAim , u = rbnUp ,
										wut = 'objectrotation' ,
										wuo = lowLeg , wu = (0,0,1)
									)
				)
		self.lowLegRbn_parCons = pc.parentConstraint( self.lowLegRbnSpc_grp , self.lowLegRbn.rbnAnim_grp , mo = True )
		self.lowLegRbnRootCtrl_pntCons = pc.pointConstraint( self.lowKneeRbn_ctrl , self.lowLegRbn.rbnRoot_ctrl )
		self.lowLegRbnEndCtrl_pntCons = pc.pointConstraint( self.ankleRbnSpc_grp , self.lowLegRbn.rbnEnd_ctrl )
		
		# Ribbon - group
		self.upKneeRbnCtrlZro_grp.parent( self.legRbnAnim_grp )
		self.lowKneeRbnCtrlZro_grp.parent( self.legRbnAnim_grp )
		
		self.upLegRbn.rbnAnim_grp.parent( self.legRbnAnim_grp )
		self.upLegRbn.rbnSkin_grp.parent( skinGrp )
		# self.upLegRbn.rbnStill_grp.parent( stillGrp )
		
		self.midLegRbn.rbnAnim_grp.parent( self.legRbnAnim_grp )
		self.midLegRbn.rbnSkin_grp.parent( skinGrp )
		# self.midLegRbn.rbnStill_grp.parent( stillGrp )
		
		self.lowLegRbn.rbnAnim_grp.parent( self.legRbnAnim_grp )
		self.lowLegRbn.rbnSkin_grp.parent( skinGrp )
		# self.lowLegRbn.rbnStill_grp.parent( stillGrp )
		
		self.legRbnAnim_grp.parent( self.legAnim_grp )
		
		if ribbon :
			self.upLegRbn.rbnJnt_grp.parent( self.legJnt_grp )
			self.midLegRbn.rbnJnt_grp.parent( self.legJnt_grp )
			self.lowLegRbn.rbnJnt_grp.parent( self.legJnt_grp )
			self.upLegRbn.rbnStill_grp.parent( stillGrp )
			self.midLegRbn.rbnStill_grp.parent( stillGrp )
			self.lowLegRbn.rbnStill_grp.parent( stillGrp )
		
		# Ribbon - cleanup
		upLegRbnShp = pc.Dag( self.upLegRbn.rbn_ctrl.shape )
		midLegRbnShp = pc.Dag( self.midLegRbn.rbn_ctrl.shape )
		lowLegRbnShp = pc.Dag( self.lowLegRbn.rbn_ctrl.shape )
		
		# upLegRbnShp.lockAttrs( 'rootTwist' , 'endTwist' )
		# midLegRbnShp.lockAttrs( 'rootTwist' , 'endTwist' )
		# lowLegRbnShp.lockAttrs( 'rootTwist' , 'endTwist' )
		
		self.upKneeRbn_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.lowKneeRbn_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		
		self.upLegRbn.rbnRoot_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.upLegRbn.rbnEnd_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.midLegRbn.rbnRoot_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.midLegRbn.rbnEnd_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.lowLegRbn.rbnRoot_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.lowLegRbn.rbnEnd_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		
		self.upLegRbn.rbnRoot_ctrl.hide()
		self.upLegRbn.rbnEnd_ctrl.hide()
		self.midLegRbn.rbnRoot_ctrl.hide()
		self.midLegRbn.rbnEnd_ctrl.hide()
		self.lowLegRbn.rbnRoot_ctrl.hide()
		self.lowLegRbn.rbnEnd_ctrl.hide()
		
		# Rig cleanup
		self.leg_ctrl.attr('fkIk').value = 1
		self.legIk_ctrl.attr('localWorld').value = 1
		self.upLegFk_ctrl.attr('localWorld').value = 1
		
		# self.upLegIkL_jnt.attr('v').value = 0
		# self.upLegIk_jnt.attr('v').value = 0
		# self.upLegFk_jnt.attr('v').value = 0
		# self.legIkL_ikh.attr('v').value = 0
		# self.lowLegIk_ikh.attr('v').value = 0
		# self.ankleIk_ikh.attr('v').value = 0
		# self.ballIk_ikh.attr('v').value = 0
		# self.toeIk_ikh.attr('v').value = 0
		
		rigTools.lockUnusedAttrs( self )
		self.legIkRoot_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' )
		self.ankleFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.kneeIk_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.legIk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.ankleRollIk_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.legIkRoot_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.leg_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.midLegFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.lowLegFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.toeFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.upLegFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.kneeIkCtrl_crv.lockHideKeyableAttrs()