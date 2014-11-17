# Neck rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
import pkmel.ribbon as pr
reload( pc )
reload( rigTools )
reload( pr )

class NeckRig( object ) :
	
	def __init__(
						self ,
						parent 		= 'spine3_jnt' ,
						animGrp 	= 'anim_grp' ,
						jntGrp 		= 'jnt_grp' ,
						skinGrp 	= 'skin_grp' ,
						stillGrp 	= 'still_grp' ,
						ribbon 		= False ,
						ax 			= 'y' ,
						charSize 	= 1 ,
						tmpJnt 		= (
										'neck1_tmpJnt' ,
										'head1_tmpJnt'
										)
					) :
		
		# Checking parent
		spine3Jnt = pc.Dag( parent )
		if not spine3Jnt.exists :
			spine3Jnt = pc.Null()
			spine3Jnt.parent( skinGrp )
		
		# Template object
		neck1 = pc.Dag( tmpJnt[0] )
		neck2 = pc.Dag( tmpJnt[1] )
		
		# Skin joints
		self.neck1_jnt = rigTools.jointAt( neck1 )
		self.neck2_jnt = rigTools.jointAt( neck2 )
		
		self.neck2_jnt.parent( self.neck1_jnt )
		self.neck1_jnt.parent( spine3Jnt )
		
		mc.parentConstraint( self.neck1_jnt , neck1 )
		# mc.parentConstraint( self.neck2_jnt , neck2 )
		
		# Main group
		self.neckRig_grp = pc.Null()
		self.neckRigGrp_parCons = pc.parentConstraint( spine3Jnt , self.neckRig_grp )
		
		self.neckJnt_grp = pc.Null()
		self.neckJntGrp_parCons = pc.parentConstraint( spine3Jnt , self.neckJnt_grp )
		
		# Length
		self.neckLen = pc.distance( neck1 , neck2 )
		
		# ----- FK -----
		# FK main group
		self.neckFkCtrl_grp = pc.Null()
		self.neckFkCtrl_grp.snap( neck1 )
		self.neckFkCtrl_grp.parent( self.neckRig_grp )
		
		self.neckFkJnt_grp = pc.Null()
		self.neckFkJnt_grp.snap( neck1 )
		self.neckFkJnt_grp.parent( self.neckJnt_grp )
		
		# FK joints
		self.neck1Fk_jnt = rigTools.jointAt( neck1 )
		self.neck2Fk_jnt = rigTools.jointAt( neck2 )
		
		self.neck2Fk_jnt.parent( self.neck1Fk_jnt )
		self.neck1Fk_jnt.parent( self.neckFkJnt_grp )
		
		# FK controls
		self.neck1Fk_ctrl = rigTools.jointControl( 'circle' )
		self.neck1FkGmbl_ctrl = pc.addGimbal( self.neck1Fk_ctrl )
		self.neck1FkCtrlZro_grp = rigTools.zeroGroup( self.neck1Fk_ctrl )
		
		# FK control - parenting and positioning
		self.neck1FkCtrlZro_grp.snapPoint( neck1 )
		self.neck1Fk_ctrl.snapOrient( neck1 )
		self.neck1Fk_ctrl.freeze( r=True )
		self.neck1FkCtrlZro_grp.parent( self.neckFkCtrl_grp )
		
		# FK control - shape adjustment
		self.neck1Fk_ctrl.color = 'red'
		self.neck1Fk_ctrl.scaleShape( 3 * charSize )
		
		# FK control - rotate order adjustment
		self.neck1Fk_ctrl.rotateOrder = 'xzy'
		self.neck1FkGmbl_ctrl.rotateOrder = 'xzy'
		
		# FK control - stretch
		( self.neck1FkStretch_add ,
		self.neck1FkStretch_mul ) = rigTools.fkStretch( ctrl = self.neck1Fk_ctrl ,
									target = self.neck2Fk_jnt ,
									ax = ax )
		
		# FK control - adjusting stretch amplitude
		self.neck1FkStretchAmp_mul = rigTools.attrAmper( self.neck1Fk_ctrl.attr('stretch') ,
														self.neck1FkStretch_mul.attr('i2') ,
														dv = 0.1
														)
		
		# FK control - local/world setup
		( self.neck1FkCtrlLoc_grp ,
		self.neck1FkCtrlWor_grp ,
		self.neck1FkCtrlWorGrp_oriCons ,
		self.neck1FkCtrlZroGrp_oriCons ,
		self.neck1FkCtrlZroGrpOriCons_rev ) = rigTools.orientLocalWorldCtrl( self.neck1Fk_ctrl ,
																			self.neckFkCtrl_grp ,
																			animGrp ,
																			self.neck1FkCtrlZro_grp
																		)
		
		# self.neck1FkCtrlLoc_grp.parent( self.neckFkCtrl_grp )
		# self.neck1FkCtrlWor_grp.parent( self.neckFkCtrl_grp )
		
		# Connect to joint
		self.neck1FkJnt_oriCons = pc.parentConstraint( self.neck1FkGmbl_ctrl , self.neck1Fk_jnt )
		
		# Connect to joint
		self.neck1Jnt_parCons = pc.parentConstraint( self.neck1Fk_jnt , self.neck1_jnt )
		self.neck2Jnt_parCons = pc.parentConstraint( self.neck2Fk_jnt , self.neck2_jnt )
		
		# Group
		self.neckRig_grp.parent( animGrp )
		self.neckJnt_grp.parent( jntGrp )
		
		# Ribbon - ribbon
		if ribbon :
			self.neckRbn = pr.RibbonIkHi( size = self.neckLen , ax = '%s+' % ax )
		else :
			self.neckRbn = pr.RibbonIkLow( size = self.neckLen , ax = '%s+' % ax )
		
		self.neckRbn.rbnAnim_grp.snap( neck1 )
		mc.delete( pc.aimConstraint( neck2 ,
										self.neckRbn.rbnAnim_grp ,
										aim = (0,1,0) , u = (1,0,0) ,
										wut = 'vector' , wu = (1,0,0)
									)
				)
		self.neckRbn_parCons = pc.parentConstraint( self.neck1_jnt , self.neckRbn.rbnAnim_grp , mo = True )
		
		# Ribbon - twist
		# self.neckRbn.rbnRootTwstZro_grp.snap( neck1 )
		# self.neckRbnRootTwstZroGrp_parCons	= pc.parentConstraint( spine3Jnt ,
		# 										self.neckRbn.rbnRootTwstZro_grp
		# 										)
		# self.neckRbnRootTwstGrp_parCons		= pc.parentConstraint( self.neck1_jnt ,
		# 										self.neckRbn.rbnRootTwst_grp
		# 										)

		self.neckRbn.rbnEndTwstZro_grp.snap( neck2 )
		self.neckRbnEndTwstZroGrp_parCons	= pc.parentConstraint( self.neck1_jnt ,
												self.neckRbn.rbnEndTwstZro_grp ,
												mo = True
												)
		self.neckRbn.rbnEndTwst_grp.snap( neck2 )
		# self.neckRbnEndTwstGrp_parCons		= pc.parentConstraint( self.wrist_jnt ,
		# 										self.neckRbn.rbnEndTwst_grp ,
		# 										mo = True
		# 										)
		
		self.neckRbn.rbnRootTwst_grp.attr(ax) 	>> self.neckRbn.rbnRootTwstAmp_mul.attr('i1')
		self.neckRbn.rbnEndTwst_grp.attr(ax) 	>> self.neckRbn.rbnEndTwstAmp_mul.attr('i1')
		
		# Ribbon - group
		self.neckRbn.rbnAnim_grp.parent( self.neckRig_grp )
		self.neckRbn.rbnSkin_grp.parent( skinGrp )
		self.neckRbn.rbnJnt_grp.parent( jntGrp )
		if ribbon :
			self.neckRbn.rbnStill_grp.parent( stillGrp )
		
		# Ribbon - cleanup
		for attr in ('tx','ty','tz') :
			self.neckRbn.rbnRoot_ctrl.attr( attr ).lockHide()
			self.neckRbn.rbnEnd_ctrl.attr( attr ).lockHide()
		
		self.neckRbn.rbnRoot_ctrl.hide()
		self.neckRbn.rbnEnd_ctrl.hide()
		
		# Rig cleanup
		self.neck1Fk_ctrl.attr('localWorld').value = 1
				
		rigTools.lockUnusedAttrs( self )
		# self.neck1Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		for attr in ('sx','sy','sz','v') :
			self.neck1Fk_ctrl.attr( attr ).lockHide()