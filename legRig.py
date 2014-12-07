# Leg rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
import pkmel.ribbon as pr
reload( pc )
reload( rigTools )
reload( pr )

class LegRig( object ) :
	
	def __init__(
						self ,
						parent = 'pelvis_jnt' ,
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
		pelvisJnt = pc.Dag( parent )
		if not pelvisJnt.exists :
			pelvisJnt = pc.Null()
			pelvisJnt.parent( skinGrp )
		
		# Template objects
		upLeg = pc.Dag( tmpJnt[0] )
		lowLeg = pc.Dag( tmpJnt[1] )
		ankle = pc.Dag( tmpJnt[2] )
		ball = pc.Dag( tmpJnt[3] )
		toe = pc.Dag( tmpJnt[4] )
		
		heel = pc.Dag( tmpJnt[5] )
		footIn = pc.Dag( tmpJnt[6] )
		footOut = pc.Dag( tmpJnt[7] )
		
		kneeIkCtrl = pc.Dag( tmpJnt[8] )
		
		# Skin joints
		self.upLeg_jnt = rigTools.jointAt( upLeg )
		self.lowLeg_jnt = rigTools.jointAt( lowLeg )
		self.ankle_jnt = rigTools.jointAt( ankle )
		self.ball_jnt = rigTools.jointAt( ball )
		self.toe_jnt = rigTools.jointAt( toe )
		
		self.toe_jnt.parent( self.ball_jnt )
		self.ball_jnt.parent( self.ankle_jnt )
		self.ankle_jnt.parent( self.lowLeg_jnt )
		self.lowLeg_jnt.parent( self.upLeg_jnt )
		self.upLeg_jnt.parent( pelvisJnt )
		# self.upLeg_jnt.attr('ssc').v = 0
		self.ball_jnt.attr('ssc').v = 0
		
		self.upLeg_jnt.rotateOrder = 'yzx'
		self.lowLeg_jnt.rotateOrder = 'yzx'
		self.ankle_jnt.rotateOrder = 'yzx'
		self.ball_jnt.rotateOrder = 'yzx'
		self.toe_jnt.rotateOrder = 'yzx'
		
		mc.parentConstraint( self.upLeg_jnt , upLeg )
		mc.parentConstraint( self.lowLeg_jnt , lowLeg )
		mc.parentConstraint( self.ankle_jnt , ankle )
		mc.parentConstraint( self.ball_jnt , ball )
		mc.parentConstraint( self.toe_jnt , toe )
		
		# Main group
		self.legRig_grp = pc.Null()
		self.legRigGrp_parCons = pc.parentConstraint( pelvisJnt , self.legRig_grp )
		self.legRigGrp_scaCons = pc.scaleConstraint( pelvisJnt , self.legRig_grp )
		
		self.legJnt_grp = pc.Null()
		self.legJntGrp_parCons = pc.parentConstraint( pelvisJnt , self.legJnt_grp )
		# self.legJntGrp_scaCons = pc.scaleConstraint( pelvisJnt , self.legJnt_grp )
		
		# Length
		self.upLegLen = pc.distance( upLeg , lowLeg )
		self.lowLegLen = pc.distance( lowLeg , ankle )
		
		# Leg control
		self.leg_ctrl = pc.Control( 'stick' )
		self.legCtrl_grp = pc.group( self.leg_ctrl )
		self.legCtrlGrp_parCons = pc.parentConstraint( self.ankle_jnt , self.legCtrl_grp )
		self.legCtrl_grp.parent( self.legRig_grp )
		
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
		self.legFkCtrl_grp.snap( self.legRig_grp )
		self.legFkCtrl_grp.parent( self.legRig_grp )
		
		self.legFkJnt_grp = pc.Null()
		self.legFkJnt_grp.snap( self.legJnt_grp )
		self.legFkJnt_grp.parent( self.legJnt_grp )
		
		# FK joints
		self.upLegFk_jnt = rigTools.jointAt( upLeg )
		self.lowLegFk_jnt = rigTools.jointAt( lowLeg )
		self.ankleFk_jnt = rigTools.jointAt( ankle )
		self.ballFk_jnt = rigTools.jointAt( ball )
		self.toeFk_jnt = rigTools.jointAt( toe )
		
		self.toeFk_jnt.parent( self.ballFk_jnt )
		self.ballFk_jnt.parent( self.ankleFk_jnt )
		self.ankleFk_jnt.parent( self.lowLegFk_jnt )
		self.lowLegFk_jnt.parent( self.upLegFk_jnt )
		self.upLegFk_jnt.parent( self.legFkJnt_grp )
		self.ballFk_jnt.attr('ssc').v = 0
		
		self.upLegFk_jnt.rotateOrder 	= 'yzx'
		self.lowLegFk_jnt.rotateOrder 	= 'yzx'
		self.ankleFk_jnt.rotateOrder 	= 'yzx'
		self.ballFk_jnt.rotateOrder 	= 'yzx'
		self.toeFk_jnt.rotateOrder 		= 'yzx'
		
		# FK controls
		self.upLegFk_ctrl = rigTools.jointControl( 'circle' )
		self.upLegFkCtrlZro_grp = rigTools.zeroGroup( self.upLegFk_ctrl )
		
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

		self.lowLegFkCtrlZro_grp.snap( lowLeg )
		self.ankleFkCtrlZro_grp.snap( ankle )
		self.toeFkCtrlZro_grp.snap( ball )
		
		self.toeFkCtrlZro_grp.parent( self.ankleScaOfst_grp )
		self.ankleFkCtrlZro_grp.parent( self.lowLegFkGmbl_ctrl )
		self.lowLegFkCtrlZro_grp.parent( self.upLegFkGmbl_ctrl )
		self.upLegFkCtrlZro_grp.parent( self.legFkCtrl_grp )
		
		# FK control - shape adjustment
		self.upLegFk_ctrl.color = 'red'
		self.lowLegFk_ctrl.color = 'red'
		self.ankleFk_ctrl.color = 'red'
		self.toeFk_ctrl.color = 'red'
		self.upLegFk_ctrl.scaleShape( 3 * charSize )
		self.lowLegFk_ctrl.scaleShape( 3 * charSize )
		self.ankleFk_ctrl.scaleShape( 3 * charSize )
		self.toeFk_ctrl.scaleShape( 3 * charSize )
		
		# FK control - rotate order adjustment
		self.upLegFk_ctrl.rotateOrder = 'yzx'
		self.upLegFkGmbl_ctrl.rotateOrder = 'yzx'
		self.lowLegFk_ctrl.rotateOrder = 'yzx'
		self.lowLegFkGmbl_ctrl.rotateOrder = 'yzx'
		self.ankleFk_ctrl.rotateOrder = 'yzx'
		self.ankleFkGmbl_ctrl.rotateOrder = 'yzx'
		self.toeFk_ctrl.rotateOrder = 'yzx'
		self.toeFkGmbl_ctrl.rotateOrder = 'yzx'
		
		# FK control - stretch control
		self.upLegFkStretch_add , self.upLegFkStretch_mul = rigTools.fkStretch( ctrl = self.upLegFk_ctrl , target = self.lowLegFkCtrlZro_grp )
		self.lowLegFkStretch_add , self.lowLegFkStretch_mul = rigTools.fkStretch( ctrl = self.lowLegFk_ctrl , target = self.ankleFkCtrlZro_grp )
		self.toeFkStretch_add , self.toeFkStretch_mul = rigTools.fkStretch( ctrl = self.toeFk_ctrl , target = self.toeFk_jnt )
		
		# FK control - Adjusting stretch amplitude
		self.upLefFkStretchAmp_mul = rigTools.attrAmper( self.upLegFk_ctrl.attr('stretch') , self.upLegFkStretch_mul.attr('i2') , dv = 0.1 )
		self.lowLegFkStretchAmp_mul = rigTools.attrAmper( self.lowLegFk_ctrl.attr('stretch') , self.lowLegFkStretch_mul.attr('i2') , dv = 0.1 )
		self.toeFkStretchAmp_mul = rigTools.attrAmper( self.toeFk_ctrl.attr('stretch') , self.toeFkStretch_mul.attr('i2') , dv = 0.1 )
		
		# FK control - connect to joint
		self.upLegFkJnt_parCons = pc.parentConstraint( self.upLegFkGmbl_ctrl , self.upLegFk_jnt )
		self.lowLegFkJnt_parCons = pc.parentConstraint( self.lowLegFkGmbl_ctrl , self.lowLegFk_jnt )
		self.ankleFkJnt_parCons = pc.parentConstraint( self.ankleFkGmbl_ctrl , self.ankleFk_jnt )
		self.ballFkJnt_parCons = pc.parentConstraint( self.toeFkGmbl_ctrl , self.ballFk_jnt )
		
		# FK control - local/world setup
		( self.upLegFkCtrlLoc_grp ,
		self.upLegFkCtrlWor_grp ,
		self.upLegFkCtrlWorGrp_oriCons ,
		self.upLegFkCtrlZroGrp_oriCons ,
		self.upLegFkCtrlZroGrpOriCons_rev ) = rigTools.orientLocalWorldCtrl( self.upLegFk_ctrl ,
																				self.legFkCtrl_grp ,
																				animGrp ,
																				self.upLegFkCtrlZro_grp
																				)
		
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
		self.legIkCtrl_grp.snap( self.legRig_grp )
		self.legIkCtrl_grp.parent( self.legRig_grp )
		
		self.legIkJnt_grp = pc.Null()
		self.legIkJnt_grp.snap( self.legJnt_grp )
		self.legIkJnt_grp.parent( self.legJnt_grp )
		
		# IK joints
		self.upLegIk_jnt = rigTools.jointAt( upLeg )
		self.lowLegIk_jnt = rigTools.jointAt( lowLeg )
		self.ankleIk_jnt = rigTools.jointAt( ankle )
		self.ballIk_jnt = rigTools.jointAt( ball )
		self.toeIk_jnt = rigTools.jointAt( toe )
		
		self.toeIk_jnt.parent( self.ballIk_jnt )
		self.ballIk_jnt.parent( self.ankleIk_jnt )
		self.ankleIk_jnt.parent( self.lowLegIk_jnt )
		self.lowLegIk_jnt.parent( self.upLegIk_jnt )
		self.upLegIk_jnt.parent( self.legIkJnt_grp )
		self.ballIk_jnt.attr('ssc').v = 0
		
		self.upLegIk_jnt.rotateOrder 	= 'yzx'
		self.lowLegIk_jnt.rotateOrder 	= 'yzx'
		self.ankleIk_jnt.rotateOrder 	= 'yzx'
		self.ballIk_jnt.rotateOrder 	= 'yzx'
		self.toeIk_jnt.rotateOrder 		= 'yzx'
		
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
		
		self.legIkCon_ctrl = pc.addConCtrl( self.legIk_ctrl )
		self.legIkGmbl_ctrl = pc.addGimbal( self.legIk_ctrl )
		
		self.kneeIkCtrlZro_grp.snapPoint( kneeIkCtrl )
		
		self.legIkRootCtrlZro_grp.parent( self.legIkCtrl_grp )
		self.legIkCtrlZro_grp.parent( self.legIkRoot_ctrl )
		self.kneeIkCtrlZro_grp.parent( self.legIkRoot_ctrl )
		self.legIkRootCtrlZroGrp_oriCons = pc.orientConstraint( animGrp , self.legIkRootCtrlZro_grp )
		
		# IK control - shape adjustment
		self.legIkRoot_ctrl.color = 'blue'
		self.legIk_ctrl.color = 'blue'
		self.kneeIk_ctrl.color = 'blue'
		self.legIkRoot_ctrl.scaleShape( 3 * charSize )
		self.legIk_ctrl.scaleShape( 3 * charSize )
		self.kneeIk_ctrl.scaleShape( 3 * charSize )
		
		# IK control - knee curve
		self.kneeIkCtrl_crv , self.kneeIkCtrl1_clstr , self.kneeIkCtrl2_clstr = rigTools.crvGuide( ctrl = self.kneeIk_ctrl , target = self.lowLegIk_jnt )
		
		self.kneeIkCtrl_crv.attr('inheritsTransform').value 	= 0
		self.kneeIkCtrl_crv.attr('overrideEnabled').value 		= 1
		self.kneeIkCtrl_crv.attr('overrideDisplayType').value 	= 2
		
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
		self.legIkCtrlZroGrpOriCons_rev ) = rigTools.parentLocalWorldCtrl( self.legIk_ctrl ,
																			self.legIkRoot_ctrl ,
																			animGrp ,
																			self.legIkCtrlZro_grp
																			)
		( self.kneeIkCtrlLoc_grp ,
		self.kneeIkCtrlWor_grp ,
		self.kneeIkCtrlWorGrp_oriCons ,
		self.kneeIkCtrlZroGrp_oriCons ,
		self.kneeIkCtrlZroGrpOriCons_rev ) = rigTools.parentLocalWorldCtrl( self.kneeIk_ctrl ,
																			self.legIkGmbl_ctrl ,
																			animGrp ,
																			self.kneeIkCtrlZro_grp
																			)
		
		# IK handle
		self.legIk_ikh = pc.IkRp( sj = self.upLegIk_jnt , ee = self.ankleIk_jnt )
		self.ballIk_ikh = pc.IkRp( sj = self.ankleIk_jnt , ee = self.ballIk_jnt )
		self.toeIk_ikh = pc.IkRp( sj = self.ballIk_jnt , ee = self.toeIk_jnt )
		self.legIkIkh_polCons = pc.poleVectorConstraint( self.kneeIk_ctrl , self.legIk_ikh )
		
		self.legIkIkh_grp = pc.Null()
		self.legIkIkhZro_grp = rigTools.zeroGroup( self.legIk_ikh  )
		self.ballIkIkhZro_grp = rigTools.zeroGroup( self.ballIk_ikh  )
		self.toeIkIkhZro_grp = rigTools.zeroGroup( self.toeIk_ikh  )
		
		self.legIkIkhZro_grp.parent( self.legIkIkh_grp )
		self.ballIkIkhZro_grp.parent( self.legIkIkh_grp )
		self.toeIkIkhZro_grp.parent( self.legIkIkh_grp )
		self.legIkIkh_grp.parent( ikhGrp )
		
		# IK handle - pivots
		self.ankleRollIkPiv_grp = pc.Null()
		self.ankleRollIk_ctrl = pc.Control( 'circle' )
		self.toeBendIkPiv_grp = pc.Null()
		self.footInIkPiv_grp = pc.Null()
		self.footOutIkPiv_grp = pc.Null()
		self.heelIkPiv_grp = pc.Null()
		self.toeIkPiv_grp = pc.Null()
		self.legIkPiv_grp = pc.Null()

		self.ankleRollIkPivZro_grp = pc.group( self.ankleRollIkPiv_grp )
		self.ankleRollIkZro_ctrl = pc.group( self.ankleRollIk_ctrl )
		self.toeBendIkPivZro_grp = pc.group( self.toeBendIkPiv_grp )
		self.footInIkPivZro_grp = pc.group( self.footInIkPiv_grp )
		self.footOutIkPivZro_grp = pc.group( self.footOutIkPiv_grp )
		self.heelIkPivZro_grp = pc.group( self.heelIkPiv_grp )
		self.toeIkPivZro_grp = pc.group( self.toeIkPiv_grp )
		self.legIkPivZro_grp = pc.group( self.legIkPiv_grp )
		
		self.legIkIkhPiv_grp = pc.Null()
		self.ballIkIkhPiv_grp = pc.Null()
		self.toeIkIkhPiv_grp = pc.Null()
		
		# IK handle - pivots - positioning and parenting
		# self.legIkPiv_grp.snapPoint( ankle )
		# self.ankleRollIkPiv_grp.snapPoint( ball )
		# self.ankleRollIk_ctrl.snapPoint( ball )
		# self.toeBendIkPiv_grp.snapPoint( ball )
		# self.footInIkPiv_grp.snapPoint( footIn )
		# self.footOutIkPiv_grp.snapPoint( footOut )
		# self.heelIkPiv_grp.snapPoint( heel )
		# self.toeIkPiv_grp.snapPoint( toe )
		self.legIkPiv_grp.snap( ankle )
		self.ankleRollIkPivZro_grp.snap( ball )
		self.ankleRollIkZro_ctrl.snap( ball )
		self.toeBendIkPivZro_grp.snap( ball )
		self.footInIkPivZro_grp.snap( footIn )
		self.footOutIkPivZro_grp.snap( footOut )
		self.heelIkPivZro_grp.snap( heel )
		self.toeIkPivZro_grp.snap( toe )
		
		self.legIkIkhPiv_grp.snap( self.legIkIkhZro_grp )
		self.ballIkIkhPiv_grp.snap( self.ballIkIkhZro_grp )
		self.toeIkIkhPiv_grp.snap( self.toeIkIkhZro_grp )

		# self.ankleRollIkPiv_grp.parent( self.footInIkPiv_grp )
		# self.ankleRollIk_ctrl.parent( self.ankleRollIkPiv_grp )
		# self.toeBendIkPiv_grp.parent( self.footInIkPiv_grp )
		# self.footInIkPiv_grp.parent( self.footOutIkPiv_grp )
		# self.footOutIkPiv_grp.parent( self.heelIkPiv_grp )
		# self.heelIkPiv_grp.parent( self.toeIkPiv_grp )
		# self.toeIkPiv_grp.parent( self.legIkPiv_grp )
		# self.legIkPiv_grp.parent( self.legIkGmbl_ctrl )
		
		self.ankleRollIkPivZro_grp.parent( self.footInIkPiv_grp )
		self.ankleRollIkZro_ctrl.parent( self.ankleRollIkPiv_grp )
		self.toeBendIkPivZro_grp.parent( self.footInIkPiv_grp )
		self.footInIkPivZro_grp.parent( self.footOutIkPiv_grp )
		self.footOutIkPivZro_grp.parent( self.heelIkPiv_grp )
		self.heelIkPivZro_grp.parent( self.toeIkPiv_grp )
		self.toeIkPivZro_grp.parent( self.legIkPiv_grp )
		self.legIkPivZro_grp.parent( self.legIkGmbl_ctrl )
		
		self.ankleRollIk_ctrl.rotateOrder = 'xzy'
		self.ankleRollIk_ctrl.color = 'blue'
		self.ankleRollIk_ctrl.scaleShape( 3 * charSize )
		
		# IK handles - positioning and parenting
		self.legIkIkhPiv_grp.parent( self.ankleRollIk_ctrl )
		self.ballIkIkhPiv_grp.parent( self.ankleRollIk_ctrl )
		self.toeIkIkhPiv_grp.parent( self.toeBendIkPiv_grp )
		self.upLegIkJnt_pntCons = pc.pointConstraint( self.legIkRoot_ctrl , self.upLegIk_jnt )
		
		self.legIkIkhZroGrp_parCons = pc.parentConstraint( self.legIkIkhPiv_grp , self.legIkIkhZro_grp )
		self.ballIkIkhZroGrp_parCons = pc.parentConstraint( self.ballIkIkhPiv_grp , self.ballIkIkhZro_grp )
		self.toeIkIkhZroGrp_parCons = pc.parentConstraint( self.toeIkIkhPiv_grp , self.toeIkIkhZro_grp )
		
		self.legIk_ctrl.add( ln = 'twist' , k = True )
		self.legIk_ctrl.attr('twist') >> self.legIk_ikh.attr('twist')
		
		# IK Stretch - Attributes
		self.legIk_ctrl.add( ln = '__stretch__' , k = True )
		self.legIk_ctrl.attr('__stretch__').set( l = True )
		self.legIk_ctrl.add( ln = 'autoStretch' , min = 0 , max = 1 , k = True )
		self.legIk_ctrl.add( ln = 'upLegStretch' , k = True )
		self.legIk_ctrl.add( ln = 'lowLegStretch' , k = True )
		self.legIk_ctrl.add( ln = 'toeStretch' , k = True )
		
		# IK handles - leg control attributes
		# '__foot__' , 'heel_roll' , 'ball_roll' , 'toe_roll' , 'heel_twist' , 'toe_twist' , 'foot_rock' , 'toe_bend'
		self.legIk_ctrl.add( ln = '__foot__' , k = True )
		self.legIk_ctrl.attr('__foot__').set( l = True )
		
		attrs = (
					'heelRoll' ,
					'ballRoll' ,
					'toeRoll' ,
					'heelTwist' ,
					'toeTwist' ,
					'footRock' ,
					'toeBend'
				)
		for attr in attrs :
			self.legIk_ctrl.add( ln = attr , k = True )
		
		self.legIk_ctrl.attr('heelRoll') >> self.heelIkPiv_grp.attr('rx')
		self.legIk_ctrl.attr('ballRoll') >> self.ankleRollIkPiv_grp.attr('rx')
		self.legIk_ctrl.attr('toeRoll') >> self.toeIkPiv_grp.attr('rx')
		# self.legIk_ctrl.attr('heelTwist') >> self.heelIkPiv_grp.attr('ry')
		# self.legIk_ctrl.attr('toeTwist') >> self.toeIkPiv_grp.attr('ry')
		self.legIk_ctrl.attr('heelTwist') >> self.heelIkPiv_grp.attr('rz')
		self.legIk_ctrl.attr('toeTwist') >> self.toeIkPiv_grp.attr('rz')
		self.legIk_ctrl.attr('toeBend') >> self.toeBendIkPiv_grp.attr('rx')
		
		# self.legIk_ctrl.attr('footRock') >> self.footInIkPiv_grp.attr('rz')
		# self.legIk_ctrl.attr('footRock') >> self.footOutIkPiv_grp.attr('rz')
		self.legIk_ctrl.attr('footRock') >> self.footInIkPiv_grp.attr('ry')
		self.legIk_ctrl.attr('footRock') >> self.footOutIkPiv_grp.attr('ry')
		
		# if side == 'LFT' :
		# 	self.footOutIkPiv_grp.attr('xrze').value = 1
		# 	self.footInIkPiv_grp.attr('mrze').value = 1
		# 	self.footOutIkPiv_grp.attr('xrzl').value = 0
		# 	self.footInIkPiv_grp.attr('mrzl').value = 0
		# elif side == 'RGT' :
		# 	self.footOutIkPiv_grp.attr('mrze').value = 1
		# 	self.footInIkPiv_grp.attr('xrze').value = 1
		# 	self.footOutIkPiv_grp.attr('mrzl').value = 0
		# 	self.footInIkPiv_grp.attr('xrzl').value = 0
		self.footOutIkPiv_grp.attr('xrye').value = 1
		self.footOutIkPiv_grp.attr('xryl').value = 0
		self.footInIkPiv_grp.attr('mrye').value = 1
		self.footInIkPiv_grp.attr('mryl').value = 0

		# IK stretch
		self.upLegIkJntPnt_grp = pc.Null()
		self.upLegIkJntPntGrp_pntCons = pc.pointConstraint( self.legIkRoot_ctrl , self.upLegIkJntPnt_grp )
		self.legIkCtrlPnt_grp = pc.Null()
		self.legIkCtrlPntGrp_pntCons = pc.pointConstraint( self.legIkIkhZro_grp , self.legIkCtrlPnt_grp )
		self.kneeIkCtrlPnt_grp = pc.Null()
		self.kneeIkCtrlPntGrp_pntCons = pc.pointConstraint( self.kneeIk_ctrl , self.kneeIkCtrlPnt_grp )
		
		self.upLegIkJntPnt_grp.parent( self.legIkRoot_ctrl )
		self.legIkCtrlPnt_grp.parent( self.legIkRoot_ctrl )
		self.kneeIkCtrlPnt_grp.parent( self.legIkRoot_ctrl )
		
		self.legIkAutoStretch_dist = pc.DistanceBetween()
		self.upLegIkLock_dist = pc.DistanceBetween()
		self.lowLegIkLock_dist = pc.DistanceBetween()
		
		self.upLegIkJntPnt_grp.attr('t') >> self.legIkAutoStretch_dist.attr('p1')
		self.legIkCtrlPnt_grp.attr('t') >> self.legIkAutoStretch_dist.attr('p2')
		self.upLegIkJntPnt_grp.attr('t') >> self.upLegIkLock_dist.attr('p1')
		self.kneeIkCtrlPnt_grp.attr('t') >> self.upLegIkLock_dist.attr('p2')
		self.kneeIkCtrlPnt_grp.attr('t') >> self.lowLegIkLock_dist.attr('p1')
		self.legIkCtrlPnt_grp.attr('t') >> self.lowLegIkLock_dist.attr('p2')
		
		self.legIkAutoStretch_cnd = pc.Condition()
		self.legIkAutoStretch_mul = pc.MultDoubleLinear()
		self.legIkAutoStretchDiv_mdv = pc.MultiplyDivide()
		
		self.upLegIkAutoStretch_mul = pc.MultDoubleLinear()
		self.upLegIkStretch_mul = pc.MultDoubleLinear()
		self.upLegIkAutoStretch_add = pc.AddDoubleLinear()
		self.upLegIkAutoStretch_blnd = pc.BlendTwoAttr()
		
		self.lowLegIkAutoStretch_mul = pc.MultDoubleLinear()
		self.lowLegIkStretch_mul = pc.MultDoubleLinear()
		self.lowLegIkAutoStretch_add = pc.AddDoubleLinear()
		self.lowLegIkAutoStretch_blnd = pc.BlendTwoAttr()
		
		# IK Stretch - Auto stretch
		ikCtrlDist = self.legIkAutoStretch_dist.attr('d').value
		upLegDist = abs( self.lowLegIk_jnt.attr('ty').value )
		lowLegDist = abs( self.ankleIk_jnt.attr('ty').value )
		
		self.legIkAutoStretch_dist.attr('d') >> self.legIkAutoStretch_cnd.attr('ft')
		self.legIkAutoStretch_cnd.attr('st').value = upLegDist + lowLegDist
		self.legIkAutoStretch_cnd.attr('op').value = 2
		self.legIkAutoStretch_cnd.attr('cfr').value = 1
		self.legIkAutoStretch_dist.attr('d') >> self.legIkAutoStretch_mul.attr('i1')
		self.legIkAutoStretchDiv_mdv.attr('op').v = 2
		self.legIkAutoStretchDiv_mdv.attr('i1x').v = 1
		self.legIkAutoStretchDiv_mdv.attr('i2x').v = upLegDist + lowLegDist
		# self.legIkAutoStretch_mul.attr('i2').value = 1/ikCtrlDist
		self.legIkAutoStretchDiv_mdv.attr('ox') >> self.legIkAutoStretch_mul.attr('i2')
		self.legIkAutoStretch_mul.attr('o') >> self.legIkAutoStretch_cnd.attr('ctr')
		
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
		
		# IK Stretch - toe stretch
		self.legIkToeStretch_add , self.legIkToeStretch_mul = rigTools.fkStretch( ctrl = self.legIk_ctrl , attr = 'toeStretch' , target = self.toeIk_jnt )
		
		# IK Stretch - Adjusting stretch amplitude
		self.upLegIkStretchAmp_mul = rigTools.attrAmper( self.legIk_ctrl.attr('upLegStretch') , self.upLegIkStretch_mul.attr('i1') , dv = 0.1 )
		self.lowLegIkStretchAmp_mul = rigTools.attrAmper( self.legIk_ctrl.attr('lowLegStretch') , self.lowLegIkStretch_mul.attr('i1') , dv = 0.1 )
		self.toeIkStretchAmp_mul = rigTools.attrAmper( self.legIk_ctrl.attr('toeStretch') , self.legIkToeStretch_mul.attr('i2') , dv = 0.1 )
		
		# IK lock - control
		self.kneeIk_ctrl.add( ln = 'lock' , min = 0 , max = 1 , k = True )
		
		self.upLegIkLockLen_mul = pc.MultDoubleLinear()
		self.upLegIkLock_mul = pc.MultDoubleLinear()
		self.upLegIkLock_blnd = pc.BlendTwoAttr()
		
		self.lowLegIkLockLen_mul = pc.MultDoubleLinear()
		self.lowLegIkLock_mul = pc.MultDoubleLinear()
		self.lowLegIkLock_blnd = pc.BlendTwoAttr()
		
		self.upLegIkLock_dist.attr('d') >> self.upLegIkLockLen_mul.attr('i1')
		self.upLegIkLockLen_mul.attr('i2').value = abs( 1/upLegDist )
		self.upLegIkLockLen_mul.attr('o') >> self.upLegIkLock_mul.attr('i1')
		self.upLegIkLock_mul.attr('i2').value = upLegDist
		self.upLegIkAutoStretch_add.attr('o') >> self.upLegIkLock_blnd.last()
		self.upLegIkLock_mul.attr('o') >> self.upLegIkLock_blnd.last()
		self.kneeIk_ctrl.attr('lock') >> self.upLegIkLock_blnd.attr('ab')
		self.upLegIkLock_blnd.attr('o') >> self.lowLegIk_jnt.attr('ty')
		
		self.lowLegIkLock_dist.attr('d') >> self.lowLegIkLockLen_mul.attr('i1')
		self.lowLegIkLockLen_mul.attr('i2').value = abs( 1/lowLegDist )
		self.lowLegIkLockLen_mul.attr('o') >> self.lowLegIkLock_mul.attr('i1')
		self.lowLegIkLock_mul.attr('i2').value = lowLegDist
		self.lowLegIkAutoStretch_add.attr('o') >> self.lowLegIkLock_blnd.last()
		self.lowLegIkLock_mul.attr('o') >> self.lowLegIkLock_blnd.last()
		self.kneeIk_ctrl.attr('lock') >> self.lowLegIkLock_blnd.attr('ab')
		self.lowLegIkLock_blnd.attr('o') >> self.ankleIk_jnt.attr('ty')
		
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
		
		# # FK/IK blending - Using blendColors
		# self.upLegJntT_bc = rigTools.blend2Vectors( 't' , self.upLegIk_jnt , self.upLegFk_jnt , self.upLeg_jnt )
		# self.lowLegJntT_bc = rigTools.blend2Vectors( 't' , self.lowLegIk_jnt , self.lowLegFk_jnt , self.lowLeg_jnt )
		# self.ankleJntT_bc = rigTools.blend2Vectors( 't' , self.ankleIk_jnt , self.ankleFk_jnt , self.ankle_jnt )
		# self.ballJntT_bc = rigTools.blend2Vectors( 't' , self.ballIk_jnt , self.ballFk_jnt , self.ball_jnt )
		# self.toeJntT_bc = rigTools.blend2Vectors( 't' , self.toeIk_jnt , self.toeFk_jnt , self.toe_jnt )
		
		# self.upLegJntR_bc = rigTools.blend2Vectors( 'r' , self.upLegIk_jnt , self.upLegFk_jnt , self.upLeg_jnt )
		# self.lowLegJntR_bc = rigTools.blend2Vectors( 'r' , self.lowLegIk_jnt , self.lowLegFk_jnt , self.lowLeg_jnt )
		# self.ankleJntR_bc = rigTools.blend2Vectors( 'r' , self.ankleIk_jnt , self.ankleFk_jnt , self.ankle_jnt )
		# self.ballJntR_bc = rigTools.blend2Vectors( 'r' , self.ballIk_jnt , self.ballFk_jnt , self.ball_jnt )
		# self.toeJntR_bc = rigTools.blend2Vectors( 'r' , self.toeIk_jnt , self.toeFk_jnt , self.toe_jnt )
		
		# self.leg_ctrl.attr( 'fkIk' ) >> self.upLegJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.lowLegJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ankleJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ballJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.toeJntT_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.upLegJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.lowLegJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ankleJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.ballJntR_bc.attr( 'blender' )
		# self.leg_ctrl.attr( 'fkIk' ) >> self.toeJntR_bc.attr( 'blender' )
		
		# FK/IK blending - Using parentConstraint
		self.upLegJnt_parCons = pc.parentConstraint( self.upLegFk_jnt , self.upLegIk_jnt , self.upLeg_jnt )
		self.lowLegJnt_parCons = pc.parentConstraint( self.lowLegFk_jnt , self.lowLegIk_jnt , self.lowLeg_jnt )
		self.ankleJnt_parCons = pc.parentConstraint( self.ankleFk_jnt , self.ankleIk_jnt , self.ankle_jnt )
		self.ballJnt_parCons = pc.parentConstraint( self.ballFk_jnt , self.ballIk_jnt , self.ball_jnt )
		self.toeJnt_parCons = pc.parentConstraint( self.toeFk_jnt , self.toeIk_jnt , self.toe_jnt )
		
		self.leg_ctrl.attr( 'fkIk' ) >> self.upLegJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.lowLegJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.ankleJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.ballJnt_parCons.attr( 'w1' )
		self.leg_ctrl.attr( 'fkIk' ) >> self.toeJnt_parCons.attr( 'w1' )
		
		self.legFkIk_rev.attr( 'ox' ) >> self.upLegJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.lowLegJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.ankleJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.ballJnt_parCons.attr( 'w0' )
		self.legFkIk_rev.attr( 'ox' ) >> self.toeJnt_parCons.attr( 'w0' )
		
		# Group
		self.legRig_grp.parent( animGrp )
		self.legJnt_grp.parent( jntGrp )
		
		# Ribbon
		self.legRbnAnim_grp = pc.Null()
		self.legRbnAnim_grp.snap( self.legRig_grp )
		
		rbnAx = 'y-'
		rbnAim = (0,-1,0)
		if side == 'RGT' :
			rbnUp = (0,0,-1)
			rbnAmp = -1
		else :
			rbnUp = (0,0,1)
			rbnAmp = 1
			
		# # Ribbon - Space
		# self.legRbnSpc_grp = pc.Null()
		# self.legRbnSpc_grp.snap( self.legRbnAnim_grp )
		
		# self.upLegRbnSpc_grp = pc.Null()
		# self.upLegRbnSpcZro_grp = pc.group( self.upLegRbnSpc_grp )
		
		# self.upLegRbnSpc_grp.rotateOrder = 'yzx'
		
		# self.upLegRbnSpcZro_grp.snap( upLeg )
		# self.upLegRbnSpcGrp_parCons = pc.parentConstraint( self.upLeg_jnt , self.upLegRbnSpc_grp )
		
		# self.lowLegRbnSpc_grp = pc.Null()
		# self.lowLegRbnSpcZro_grp = pc.group( self.lowLegRbnSpc_grp )
		
		# self.lowLegRbnSpc_grp.rotateOrder = 'yzx'
		
		# self.lowLegRbnSpcZro_grp.snap( lowLeg )
		# self.lowLegRbnSpcZroGrp_parCons = pc.parentConstraint( self.upLeg_jnt , self.lowLegRbnSpcZro_grp , mo = True )
		# self.lowLegRbnSpcGrp_parCons = pc.parentConstraint( self.lowLeg_jnt , self.lowLegRbnSpc_grp )
		
		# self.ankleRbnSpc_grp = pc.Null()
		# self.ankleRbnSpcZro_grp = pc.group( self.ankleRbnSpc_grp )
		
		# self.ankleRbnSpc_grp.rotateOrder = 'yzx'
		
		# self.ankleRbnSpcZro_grp.snap( ankle )
		# self.ankleRbnSpcZroGrp_parCons = pc.parentConstraint( self.lowLeg_jnt , self.ankleRbnSpcZro_grp , mo = True )
		# self.ankleRbnSpcGrp_parCons = pc.parentConstraint( self.ankle_jnt , self.ankleRbnSpc_grp )
		
		# # Ribbon - Space - group
		# self.upLegRbnSpcZro_grp.parent( self.legRbnSpc_grp )
		# self.lowLegRbnSpcZro_grp.parent( self.legRbnSpc_grp )
		# self.ankleRbnSpcZro_grp.parent( self.legRbnSpc_grp )
		# self.legRbnSpc_grp.parent( self.legRbnAnim_grp )
		
		# Ribbon control
		self.legRbn_ctrl = pc.Control( 'plus' )
		self.legRbnCtrlZro_grp = pc.group( self.legRbn_ctrl )
		
		# Ribbon control - parenting and positioning
		self.legRbnCtrlZroGrp_pntCons = pc.pointConstraint( self.lowLeg_jnt , self.legRbnCtrlZro_grp )
		self.legRbnCtrlZroGrp_oriCons = pc.orientConstraint( self.upLeg_jnt , self.legRbnCtrlZro_grp , mo = True )
		
		# Ribbon control - shape adjustment
		self.legRbn_ctrl.color = 'yellow'
		self.legRbn_ctrl.scaleShape( 3 * charSize )
		
		# Ribbon upper leg
		if ribbon :
			self.upLegRbn = pr.RibbonIkHi( size = self.upLegLen , ax = rbnAx )
		else :
			self.upLegRbn = pr.RibbonIkLow( size = self.upLegLen , ax = rbnAx )
		
		self.upLegRbn.rbnAnim_grp.snapPoint( upLeg )
		mc.delete( pc.aimConstraint( lowLeg , self.upLegRbn.rbnAnim_grp , aim = rbnAim , u = rbnUp , wut = 'objectrotation' , wuo = upLeg , wu = (0,0,1) ) )
		self.upLegRbn_parCons = pc.parentConstraint( self.upLeg_jnt , self.upLegRbn.rbnAnim_grp , mo = True )
		self.upLegRbnRootCtrl_pntCons = pc.pointConstraint( self.upLeg_jnt , self.upLegRbn.rbnRoot_ctrl )
		self.upLegRbnEndCtrl_pntCons = pc.pointConstraint( self.legRbn_ctrl , self.upLegRbn.rbnEnd_ctrl )
		
		# Ribbon upper leg - twist distributetion
		upLegRbnShp = pc.Dag( self.upLegRbn.rbn_ctrl.shape )
		upLegRbnShp.attr('rootTwistAmp').value = 1 * rbnAmp
		upLegRbnShp.attr('endTwistAmp').value = -1 * rbnAmp
		
		# self.upLegRbnSpc_grp.attr('ry') >> upLegRbnShp.attr('rootTwist')
		# self.lowLegRbnSpc_grp.attr('ry') >> upLegRbnShp.attr('endTwist')

		# Ribbon upper leg - space
		self.upLegRbn.rbnRootTwstZro_grp.snap( upLeg )
		self.upLegRbnRootTwstZroGrp_parCons	= pc.parentConstraint( parent ,
												self.upLegRbn.rbnRootTwstZro_grp ,
												mo = True
												)
		self.upLegRbnRbnRootTwstGrp_parCons	= pc.parentConstraint( self.upLeg_jnt ,
												self.upLegRbn.rbnRootTwst_grp
												)

		self.upLegRbn.rbnEndTwstZro_grp.snap( lowLeg )
		self.upLegRbnEndTwstZroGrp_parCons	= pc.parentConstraint( self.upLeg_jnt ,
												self.upLegRbn.rbnEndTwstZro_grp,
												mo = True
												)
		self.upLegRbnEndTwstGrp_parCons		= pc.parentConstraint( self.lowLeg_jnt ,
												self.upLegRbn.rbnEndTwst_grp
												)

		self.upLegRbn.rbnRootTwst_grp.rotateOrder = 'yzx'
		self.upLegRbn.rbnEndTwst_grp.rotateOrder = 'yzx'
		self.upLegRbn.rbnRootTwst_grp.attr('ry') 	>> self.upLegRbn.rbnRootTwstAmp_mul.attr('i1')
		self.upLegRbn.rbnEndTwst_grp.attr('ry') 	>> self.upLegRbn.rbnEndTwstAmp_mul.attr('i1')
		
		# Ribbon low leg
		if ribbon :
			self.lowLegRbn = pr.RibbonIkHi( size = self.lowLegLen , ax = rbnAx )
		else :
			self.lowLegRbn = pr.RibbonIkLow( size = self.lowLegLen , ax = rbnAx )
		
		self.lowLegRbn.rbnAnim_grp.snapPoint( lowLeg )
		mc.delete( pc.aimConstraint( ankle , self.lowLegRbn.rbnAnim_grp , aim = rbnAim , u = rbnUp , wut = 'objectrotation' , wuo = lowLeg , wu = (0,0,1) ) )
		self.lowLegRbn_parCons = pc.parentConstraint( self.lowLeg_jnt , self.lowLegRbn.rbnAnim_grp , mo = True )
		self.lowLegRbnRootCtrl_pntCons = pc.pointConstraint( self.legRbn_ctrl , self.lowLegRbn.rbnRoot_ctrl )
		self.lowLegRbnEndCtrl_pntCons = pc.pointConstraint( self.ankle_jnt , self.lowLegRbn.rbnEnd_ctrl )
		
		# Ribbon upper leg - twist distributetion
		lowLegRbnShp = pc.Dag( self.lowLegRbn.rbn_ctrl.shape )
		lowLegRbnShp.attr('rootTwistAmp').value = 1 * rbnAmp
		lowLegRbnShp.attr('endTwistAmp').value = -1 * rbnAmp
		
		# Ribbon lower leg - space
		self.lowLegRbn.rbnRootTwstZro_grp.snap( lowLeg )
		# self.lowLegRbnRootTwstZroGrp_parCons	= pc.parentConstraint( self.upArm_jnt ,
		# 										self.lowLegRbn.rbnRootTwstZro_grp
		# 										)
		# self.lowLegRbnRootTwstGrp_parCons		= pc.parentConstraint( self.forearm_jnt ,
		# 										self.lowLegRbn.rbnRootTwst_grp
		# 										)
		
		self.lowLegRbn.rbnEndTwstZro_grp.snap( ankle )
		self.lowLegRbnEndTwstZroGrp_parCons	= pc.parentConstraint( self.lowLeg_jnt ,
												self.lowLegRbn.rbnEndTwstZro_grp ,
												mo = True
												)
		self.lowLegRbnEndTwstGrp_parCons		= pc.parentConstraint( self.ankle_jnt ,
												self.lowLegRbn.rbnEndTwst_grp ,
												mo = True
												)
		self.lowLegRbn.rbnRootTwst_grp.attr('ry') 	>> self.lowLegRbn.rbnRootTwstAmp_mul.attr('i1')
		self.lowLegRbn.rbnEndTwst_grp.attr('ry') 	>> self.lowLegRbn.rbnEndTwstAmp_mul.attr('i1')
		self.lowLegRbn.rbnRootTwst_grp.rotateOrder = 'yzx'
		self.lowLegRbn.rbnEndTwst_grp.rotateOrder = 'yzx'
		
		# Ribbon - group
		self.legRbnCtrlZro_grp.parent( self.legRbnAnim_grp )
		self.upLegRbn.rbnAnim_grp.parent( self.legRbnAnim_grp )
		self.upLegRbn.rbnSkin_grp.parent( skinGrp )
		self.lowLegRbn.rbnAnim_grp.parent( self.legRbnAnim_grp )
		self.lowLegRbn.rbnSkin_grp.parent( skinGrp )
		self.legRbnAnim_grp.parent( self.legRig_grp )
		
		if ribbon :
			self.upLegRbn.rbnJnt_grp.parent( self.legJnt_grp )
			self.lowLegRbn.rbnJnt_grp.parent( self.legJnt_grp )
			self.upLegRbn.rbnStill_grp.parent( stillGrp )
			self.lowLegRbn.rbnStill_grp.parent( stillGrp )

		# # Ribbon - add bend
		# self.legRbn_ctrl.add( ln='bend' , dv=0 , k=True )
		# self.upperLegRbnBend_mul = rigTools.attrAmper(
		# 													self.legRbn_ctrl.attr('bend') ,
		# 													self.upLegRbn.rbnMidJntOfst_grp.attr('tz') ,
		# 													dv = 0.1
		# 												)
		# self.lowerLegRbnBend_mul = rigTools.attrAmper(
		# 													self.legRbn_ctrl.attr('bend') ,
		# 													self.lowLegRbn.rbnMidJntOfst_grp.attr('tz') ,
		# 													dv = 0.1
		# 												)

		# Ribbon - cleanup
		self.legRbn_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.upLegRbn.rbnRoot_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.upLegRbn.rbnEnd_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.lowLegRbn.rbnRoot_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		self.lowLegRbn.rbnEnd_ctrl.lockHideAttrs( 'tx' , 'ty' , 'tz' )
		
		self.upLegRbn.rbnRoot_ctrl.hide()
		self.upLegRbn.rbnEnd_ctrl.hide()
		self.lowLegRbn.rbnRoot_ctrl.hide()
		self.lowLegRbn.rbnEnd_ctrl.hide()
		
		# Rig cleanup
		self.leg_ctrl.attr('fkIk').value = 1
		self.legIk_ctrl.attr('localWorld').value = 1
		self.upLegFk_ctrl.attr('localWorld').value = 1
		
		# self.upLegIk_jnt.attr('v').value = 0
		# self.upLegFk_jnt.attr('v').value = 0
		# self.legIk_ikh.attr('v').value = 0
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
		self.lowLegFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.toeFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.upLegFk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.kneeIkCtrl_crv.lockHideKeyableAttrs()