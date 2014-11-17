# Head rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class HeadRig( object ) :
	
	def __init__( self ,
				parent = 'neck2_jnt' ,
				animGrp = 'anim_grp' ,
				skinGrp = 'skin_grp' ,
				charSize = 1 ,
				tmpJnt = (
								'head1_tmpJnt' ,
								'head2_tmpJnt' ,
								'eyeLFT_tmpJnt' ,
								'eyeRGT_tmpJnt' ,
								'jaw1LWR_tmpJnt' ,
								'jaw2LWR_tmpJnt' ,
								'jaw3LWR_tmpJnt' ,
								'jaw1UPR_tmpJnt' ,
								'jaw2UPR_tmpJnt' ,
								'eye_tmpJnt' ,
								'eyeTrgtLFT_tmpJnt' ,
								'eyeTrgtRGT_tmpJnt'
							)
				) :
		
		# Checking parent
		neck2Jnt = pc.Dag( parent )
		if not neck2Jnt.exists :
			neck2Jnt = pc.Null()
			neck2Jnt.parent( skinGrp )
		
		# Template objects
		head1 = pc.Dag( tmpJnt[0] )
		head2 = pc.Dag( tmpJnt[1] )
		eyeLft = pc.Dag( tmpJnt[2] )
		eyeRgt = pc.Dag( tmpJnt[3] )
		jaw1Lwr = pc.Dag( tmpJnt[4] )
		jaw2Lwr = pc.Dag( tmpJnt[5] )
		jaw3Lwr = pc.Dag( tmpJnt[6] )
		jaw1Upr = pc.Dag( tmpJnt[7] )
		jaw2Upr = pc.Dag( tmpJnt[8] )
		
		eyeCtrl = pc.Dag( tmpJnt[9] )
		eyeTrgtLft = pc.Dag( tmpJnt[10] )
		eyeTrgtRgt = pc.Dag( tmpJnt[11] )
		eyeLftCtrl = pc.Dag( tmpJnt[2] )
		eyeRgtCtrl = pc.Dag( tmpJnt[3] )
		
		# Skin joints
		# self.head1_jnt = rigTools.jointAt( head1 )
		# self.head2_jnt = rigTools.jointAt( head2 )
		# self.eyeLFT_jnt = rigTools.jointAt( eyeLft )
		# self.eyeRGT_jnt = rigTools.jointAt( eyeRgt )
		# self.jaw1LWR_jnt = rigTools.jointAt( jaw1Lwr )
		# self.jaw2LWR_jnt = rigTools.jointAt( jaw2Lwr )
		# self.jaw3LWR_jnt = rigTools.jointAt( jaw3Lwr )
		# self.jaw1UPR_jnt = rigTools.jointAt( jaw1Upr )
		# self.jaw2UPR_jnt = rigTools.jointAt( jaw2Upr )
		
		# Skin joint - parenting
		# self.head2_jnt.parent( self.head1_jnt )
		# self.eyeLFT_jnt.parent( self.head1_jnt )
		# self.eyeRGT_jnt.parent( self.head1_jnt )
		# self.jaw1LWR_jnt.parent( self.head1_jnt )
		# self.jaw2LWR_jnt.parent( self.jaw1LWR_jnt )
		# self.jaw3LWR_jnt.parent( self.jaw2LWR_jnt )
		# self.jaw1UPR_jnt.parent( self.head1_jnt )
		# self.jaw2UPR_jnt.parent( self.jaw1UPR_jnt )
		# self.head1_jnt.parent( neck2Jnt )
		
		# Skin joint - disable scale compensate
		# self.head2_jnt.attr('ssc').value = 0
		# self.eyeLFT_jnt.attr('ssc').value = 0
		# self.eyeRGT_jnt.attr('ssc').value = 0
		# self.jaw1LWR_jnt.attr('ssc').value = 0
		# self.jaw2LWR_jnt.attr('ssc').value = 0
		# self.jaw3LWR_jnt.attr('ssc').value = 0
		# self.jaw1UPR_jnt.attr('ssc').value = 0
		# self.jaw2UPR_jnt.attr('ssc').value = 0
		
		# Main group
		self.headRig_grp = pc.Null()
		self.headRigGrp_parCons = pc.parentConstraint( neck2Jnt , self.headRig_grp )
		
		#---------------------------------------------------------
		# Head
		# Head - skin joints
		self.head1_jnt = rigTools.jointAt( head1 )
		self.head2_jnt = rigTools.jointAt( head2 )
		
		mc.parentConstraint( self.head1_jnt , head1 )
		mc.parentConstraint( self.head2_jnt , head2 )
		
		self.head2_jnt.attr('ssc').value = 0
		
		self.head2_jnt.parent( self.head1_jnt )
		self.head1_jnt.parent( neck2Jnt )
		
		# Head control
		self.head_ctrl = rigTools.jointControl( 'cube' )
		self.headCtrlZro_grp = rigTools.zeroGroup( self.head_ctrl )
		
		# Head control - parenting and positioning
		self.headCtrlZro_grp.snapPoint( self.head1_jnt )
		self.head_ctrl.snapOrient( self.head1_jnt )
		self.head_ctrl.freeze( t = False , r = True , s = False )
		self.headCtrlZro_grp.parent( self.headRig_grp )
		
		self.headGmbl_ctrl = pc.addGimbal( self.head_ctrl )
		
		# Head control - shape adjustment
		self.head_ctrl.color = 'blue'
		self.head_ctrl.scaleShape( 3 * charSize )

		# Head control - rotate order adjustment
		self.head_ctrl.rotateOrder = 'xzy'
		self.headGmbl_ctrl.rotateOrder = 'xzy'
		
		# Head control - local/world setup
		# parentLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , oriGrp = '' )
		# return locGrp , worGrp , worGrpParCons , parGrpParCons , parGrpParConsRev
		self.headCtrlLoc_grp,self.headCtrlWor_grp,self.headCtrlWorGrp_oriCons,self.headCtrlZroGrp_oriCons,self.headCtrlZroGrpOriCons_rev = rigTools.orientLocalWorldCtrl( self.head_ctrl , self.headRig_grp , animGrp , self.headCtrlZro_grp )
		
		# Head control - connect to joint
		self.headJnt_parCons = pc.parentConstraint( self.headGmbl_ctrl , self.head1_jnt )
		self.headJnt_scCons = pc.scaleConstraint( self.headGmbl_ctrl , self.head1_jnt )
		
		# Head cleanup
		self.head_ctrl.attr('localWorld').value = 1
		self.head_ctrl.attr( 'v' ).lockHide()
		
		#---------------------------------------------------------
		
		# Lower Jaw
		if jaw1Lwr.exists and jaw2Lwr.exists :
			
			# Lower Jaw skin joints
			self.jaw1LWR_jnt = rigTools.jointAt( jaw1Lwr )
			self.jaw2LWR_jnt = rigTools.jointAt( jaw2Lwr )
			self.jaw3LWR_jnt = rigTools.jointAt( jaw3Lwr )
			
			mc.parentConstraint( self.jaw1LWR_jnt , jaw1Lwr )
			mc.parentConstraint( self.jaw2LWR_jnt , jaw2Lwr )
			mc.parentConstraint( self.jaw3LWR_jnt , jaw3Lwr )
			
			self.jaw3LWR_jnt.parent( self.jaw2LWR_jnt )
			self.jaw2LWR_jnt.parent( self.jaw1LWR_jnt )
			self.jaw1LWR_jnt.parent( self.head1_jnt )
			self.jaw1LWR_jnt.attr('segmentScaleCompensate').v = 0
			
			# Jaw 1 lower control
			# self.jaw1LWR_ctrl , self.jaw1CtrlLWR_jnt , self.jaw1GmblLWR_ctrl = rigTools.twoJointsControl( 'square' )
			self.jaw1LWR_ctrl = rigTools.jointControl( 'square' )
			self.jaw1GmblLWR_ctrl = pc.addGimbal( self.jaw1LWR_ctrl )
			self.jaw1CtrlZroLWR_grp = rigTools.zeroGroup( self.jaw1LWR_ctrl )
			
			# Jaw 1 lower control - parenting and positioning
			self.jaw1CtrlZroLWR_grp.snap( self.jaw1LWR_jnt )
			self.jaw1CtrlZroLWR_grp.parent( self.headGmbl_ctrl )
			
			# Jaw 1 lower control - shape adjustment
			self.jaw1LWR_ctrl.color = 'red'
			self.jaw1LWR_ctrl.scaleShape( 3 * charSize )
			
			# Jaw 1 lower control - rotate order adjustment
			self.jaw1LWR_ctrl.rotateOrder = 'zyx'
			self.jaw1GmblLWR_ctrl.rotateOrder = 'zyx'
			
			# Jaw 1 lower control - connect to joint
			self.jaw1JntLWR_parCons = pc.parentConstraint( self.jaw1GmblLWR_ctrl , self.jaw1LWR_jnt )
			self.jaw1JntLWR_scaCons = pc.scaleConstraint( self.jaw1GmblLWR_ctrl , self.jaw1LWR_jnt )
			
			#---------------------------------------------------------
			
			# Jaw 2 lower control
			self.jaw2LWR_ctrl = rigTools.jointControl( 'square' )
			self.jaw2GmblLWR_ctrl = pc.addGimbal( self.jaw2LWR_ctrl)
			self.jaw2CtrlZroLWR_grp = rigTools.zeroGroup( self.jaw2LWR_ctrl )
			
			# Jaw 2 lower control - parenting and positioning
			self.jaw2CtrlZroLWR_grp.snap( self.jaw2LWR_jnt )
			self.jaw2CtrlZroLWR_grp.parent( self.jaw1GmblLWR_ctrl )
			
			# Jaw 2 lower control - shape adjustment
			self.jaw2LWR_ctrl.color = 'red'
			self.jaw2LWR_ctrl.scaleShape( 3 * charSize )
			
			# Jaw 2 lower control - rotate order adjustment
			self.jaw2LWR_ctrl.rotateOrder = 'zyx'
			self.jaw2GmblLWR_ctrl.rotateOrder = 'zyx'
			
			# Jaw 2 lower control - connect to joint
			self.jaw2JntLWR_parCons = pc.parentConstraint( self.jaw2GmblLWR_ctrl , self.jaw2LWR_jnt )
			self.jaw2JntLWR_scaCons = pc.scaleConstraint( self.jaw2GmblLWR_ctrl , self.jaw2LWR_jnt )
			
			# Lower Jaw Clean up
			self.jaw1LWR_ctrl.attr( 'v' ).lockHide()
			self.jaw2LWR_ctrl.attr( 'v' ).lockHide()
		
		#---------------------------------------------------------
		
		# Upper Jaw
		if jaw1Upr.exists and jaw2Upr.exists :
			
			# Skin joints
			self.jaw1UPR_jnt = rigTools.jointAt( jaw1Upr )
			self.jaw2UPR_jnt = rigTools.jointAt( jaw2Upr )
			
			mc.parentConstraint( self.jaw1UPR_jnt , jaw1Upr )
			mc.parentConstraint( self.jaw2UPR_jnt , jaw2Upr )
			
			self.jaw1UPR_jnt.parent( self.head1_jnt )
			self.jaw2UPR_jnt.parent( self.jaw1UPR_jnt )
			
			self.jaw1UPR_jnt.attr('ssc').value = 0
			self.jaw2UPR_jnt.attr('ssc').value = 0
			
			# Jaw 1 upper control
			self.jaw1UPR_ctrl = rigTools.jointControl( 'square' )
			self.jaw1GmblUPR_ctrl = pc.addGimbal( self.jaw1UPR_ctrl )
			self.jaw1CtrlZroUPR_grp = rigTools.zeroGroup( self.jaw1UPR_ctrl )
			self.jaw1UPR_ctrl.attr('ssc').value = 0
			
			# Jaw 1 upper control - parenting and positioning
			self.jaw1CtrlZroUPR_grp.snap( self.jaw1UPR_jnt )
			self.jaw1CtrlZroUPR_grp.parent( self.headGmbl_ctrl )
					
			# Jaw 1 upper control - shape adjustment
			self.jaw1UPR_ctrl.color = 'blue'
			self.jaw1UPR_ctrl.scaleShape( 3 * charSize )
			
			# Jaw 1 upper control - rotate order adjustment
			self.jaw1UPR_ctrl.rotateOrder = 'zyx'
			self.jaw1GmblUPR_ctrl.rotateOrder = 'zyx'
			
			# Jaw 1 upper control - connect to joint
			self.jaw1JntUPR_parCons = pc.parentConstraint( self.jaw1GmblUPR_ctrl , self.jaw1UPR_jnt )
			self.jaw1JntUPR_scaCons = pc.scaleConstraint( self.jaw1GmblUPR_ctrl , self.jaw1UPR_jnt )
			
			# Upper Jaw cleanup
			self.jaw1UPR_ctrl.attr( 'v' ).lockHide()
		
		#---------------------------------------------------------
		
		# Eye
		if eyeLft.exists or eyeRgt.exists :
			# Eye control
			self.eye_ctrl = pc.Control( 'capsule' )
			self.eyeOfst_ctrl = pc.group( self.eye_ctrl )
			self.eyeCtrlZro_grp = pc.group( self.eyeOfst_ctrl )
			
			# Eye control - positioning and parenting
			self.eyeCtrlZro_grp.snap( eyeCtrl )
			self.eyeCtrlZro_grp.parent( self.headGmbl_ctrl )
			
			# Eye control - shape adjustment
			self.eye_ctrl.color = 'yellow'
			self.eye_ctrl.scaleShape( 3 * charSize )
			
			# Eye control - local/world setup
			self.eyeCtrlLoc_grp,self.eyeCtrlWor_grp,self.eyeCtrlWorGrp_oriCons,self.eyeCtrlZroGrp_oriCons,self.eyeCtrlZroGrpOriCons_rev = rigTools.parentLocalWorldCtrl( self.eye_ctrl , self.headGmbl_ctrl , animGrp , self.eyeCtrlZro_grp )
			
			# Cleanup
			for attr in ('sx','sy','sz','v') :
				self.eyeOfst_ctrl.attr( attr ).lockHide()
				self.eye_ctrl.attr( attr ).lockHide()
		
		# Left Eye
		if eyeLft.exists :
			
			# Left Eye skin joint
			self.eyeLFT_jnt = rigTools.jointAt( eyeLft )
			self.lidLFT_jnt = rigTools.jointAt( eyeLft )
			
			mc.parentConstraint( self.eyeLFT_jnt , eyeLft )
			
			self.lidLFT_jnt.parent( self.eyeLFT_jnt )
			self.eyeLFT_jnt.parent( self.head1_jnt )
			self.lidLFT_jnt.attr('ssc').value = 0
			self.eyeLFT_jnt.attr('ssc').value = 0

			# Left Eye control
			self.eyeLFT_ctrl = rigTools.jointControl( 'sphere' )
			self.eyeGmblLFT_ctrl = pc.addGimbal( self.eyeLFT_ctrl )
			self.eyeCtrlAimLFT_grp = rigTools.zeroGroup( self.eyeLFT_ctrl )
			self.eyeCtrlZroLFT_grp = rigTools.zeroGroup( self.eyeCtrlAimLFT_grp )
			
			# Left Eye control - positioning and parenting
			self.eyeCtrlZroLFT_grp.snap( self.eyeLFT_jnt )
			self.eyeCtrlZroLFT_grp.parent( self.headGmbl_ctrl )
			
			# Left Eye control - shape adjustment
			self.eyeLFT_ctrl.color = 'softBlue'
			self.eyeLFT_ctrl.scaleShape( 3 * charSize )
			
			# Left Eye control - rotate order adjustment
			self.eyeLFT_ctrl.rotateOrder = 'zxy'
			self.eyeGmblLFT_ctrl.rotateOrder = 'zxy'
			
			# Left Eye control - connect to joint
			self.eyeJntLFT_parCons = pc.parentConstraint( self.eyeGmblLFT_ctrl , self.eyeLFT_jnt )
			self.eyeJntLFT_sclCons = pc.scaleConstraint( self.eyeGmblLFT_ctrl , self.eyeLFT_jnt )
			
			# Left Eye target control
			self.eyeTrgtLFT_ctrl = pc.Control( 'plus' )
			self.eyeTrgtZroLFT_grp = pc.group( self.eyeTrgtLFT_ctrl )
			
			# Left Eye target control - positioning and parenting
			mc.delete( pc.pointConstraint( self.eyeLFT_jnt , self.eyeTrgtZroLFT_grp ) )
			mc.delete( pc.pointConstraint( self.eye_ctrl , self.eyeTrgtZroLFT_grp , skip = ( 'x' , 'y' ) ) )
			self.eyeTrgtZroLFT_grp.parent( self.eye_ctrl )
			
			# Left Eye target control - shape adjustment
			self.eyeTrgtLFT_ctrl.color = 'softBlue'
			self.eyeTrgtLFT_ctrl.scaleShape( 3 * charSize )
			
			self.eyeCtrlAimGrpLFT_aimCons = pc.aimConstraint(self.eyeTrgtLFT_ctrl,self.eyeCtrlAimLFT_grp,aimVector=(0,0,1),upVector=(0,1,0),worldUpType="objectrotation",worldUpVector=(0,1,0),worldUpObject=self.head2_jnt)
			
			# Left eye lid control
			self.eyeLFT_ctrl.add( ln='lidFollow' , min=0 , max=1 , k=True )
			self.lidJntLFT_oriCons = pc.orientConstraint( self.head1_jnt , self.eyeLFT_jnt , self.lidLFT_jnt , mo=True )
			
			self.lidFollowLFT_rev = pc.Reverse()
			self.eyeLFT_ctrl.attr( 'lidFollow' ) >> self.lidJntLFT_oriCons.attr( 'w1' )
			self.eyeLFT_ctrl.attr( 'lidFollow' ) >> self.lidFollowLFT_rev.attr( 'ix' )
			self.lidFollowLFT_rev.attr( 'ox' ) >> self.lidJntLFT_oriCons.attr( 'w0' )
			
			# Left eye guide curve
			self.eyeCtrlLFT_crv , self.eyeCtrl1LFT_clstr , self.eyeCtrl2LFT_clstr = rigTools.crvGuide( ctrl = self.eyeLFT_ctrl , target = self.eyeTrgtLFT_ctrl )
			
			self.eyeCtrlLFT_crv.attr('inheritsTransform').value = 0
			self.eyeCtrlLFT_crv.attr('overrideEnabled').value = 1
			self.eyeCtrlLFT_crv.attr('overrideDisplayType').value = 2
			
			self.eyeCtrlLFT_crv.parent( self.headRig_grp )
			self.eyeCtrlLFT_crv.attr('t').value = (0,0,0)
			self.eyeCtrlLFT_crv.attr('r').value = (0,0,0)
			
			# Cleanup
			self.eyeLFT_ctrl.attr( 'v' ).lockHide()
			for attr in ('rx','ry','rz','sx','sy','sz','v') :
				self.eyeTrgtLFT_ctrl.attr( attr ).lockHide()
		
		# Right Eye
		if eyeRgt.exists :
			
			# Right Eye skin joint
			self.eyeRGT_jnt = rigTools.jointAt( eyeRgt )
			self.lidRGT_jnt = rigTools.jointAt( eyeRgt )
			
			mc.parentConstraint( self.eyeRGT_jnt , eyeRgt )
			
			self.lidRGT_jnt.parent( self.eyeRGT_jnt )
			self.eyeRGT_jnt.parent( self.head1_jnt )
			self.lidRGT_jnt.attr('ssc').value = 0
			self.eyeRGT_jnt.attr('ssc').value = 0
			
			# Right Eye control
			self.eyeRGT_ctrl = rigTools.jointControl( 'sphere' )
			self.eyeGmblRGT_ctrl = pc.addGimbal( self.eyeRGT_ctrl )
			self.eyeCtrlAimRGT_grp = rigTools.zeroGroup( self.eyeRGT_ctrl )
			self.eyeCtrlZroRGT_grp = rigTools.zeroGroup( self.eyeCtrlAimRGT_grp )
			
			# Right Eye control - positioning and parenting
			self.eyeCtrlZroRGT_grp.snap( self.eyeRGT_jnt )
			self.eyeCtrlZroRGT_grp.parent( self.headGmbl_ctrl )
			
			# Right Eye control - shape adjustment
			self.eyeRGT_ctrl.color = 'softBlue'
			self.eyeRGT_ctrl.scaleShape( 3 * charSize )
			
			# Right Eye control - rotate order adjustment
			self.eyeRGT_ctrl.rotateOrder = 'zxy'
			self.eyeGmblRGT_ctrl.rotateOrder = 'zxy'
			
			# Right Eye control - connect to joint
			self.eyeJntRGT_parCons = pc.parentConstraint( self.eyeGmblRGT_ctrl , self.eyeRGT_jnt )
			self.eyeJntRGT_sclCons = pc.scaleConstraint( self.eyeGmblRGT_ctrl , self.eyeRGT_jnt )
			
			# Right Eye target control
			self.eyeTrgtRGT_ctrl = pc.Control( 'plus' )
			self.eyeTrgtZroRGT_grp = pc.group( self.eyeTrgtRGT_ctrl )
			
			# Right Eye target control - positioning and parenting
			mc.delete( pc.pointConstraint( self.eyeRGT_jnt , self.eyeTrgtZroRGT_grp ) )
			mc.delete( pc.pointConstraint( self.eye_ctrl , self.eyeTrgtZroRGT_grp , skip = ( 'x' , 'y' ) ) )
			self.eyeTrgtZroRGT_grp.parent( self.eye_ctrl )
			
			# Right Eye target control - shape adjustment
			self.eyeTrgtRGT_ctrl.color = 'softBlue'
			self.eyeTrgtRGT_ctrl.scaleShape( 3 * charSize )
			
			self.eyeCtrlAimGrpRGT_aimCons = pc.aimConstraint(self.eyeTrgtRGT_ctrl,self.eyeCtrlAimRGT_grp,aimVector=(0,0,1),upVector=(0,1,0),worldUpType="objectrotation",worldUpVector=(0,1,0),worldUpObject=self.head2_jnt)
			
			# Right eye lid control
			self.eyeRGT_ctrl.add( ln='lidFollow' , min=0 , max=1 , k=True )
			self.lidJntRGT_oriCons = pc.orientConstraint( self.head1_jnt , self.eyeRGT_jnt , self.lidRGT_jnt , mo=True )
			
			self.lidFollowRGT_rev = pc.Reverse()
			self.eyeRGT_ctrl.attr( 'lidFollow' ) >> self.lidJntRGT_oriCons.attr( 'w1' )
			self.eyeRGT_ctrl.attr( 'lidFollow' ) >> self.lidFollowRGT_rev.attr( 'ix' )
			self.lidFollowRGT_rev.attr( 'ox' ) >> self.lidJntRGT_oriCons.attr( 'w0' )
			
			# Right eye guide curve
			self.eyeCtrlRGT_crv , self.eyeCtrl1RGT_clstr , self.eyeCtrl2RGT_clstr = rigTools.crvGuide( ctrl = self.eyeRGT_ctrl , target = self.eyeTrgtRGT_ctrl )
			
			self.eyeCtrlRGT_crv.attr('inheritsTransform').value = 0
			self.eyeCtrlRGT_crv.attr('overrideEnabled').value = 1
			self.eyeCtrlRGT_crv.attr('overrideDisplayType').value = 2
			
			self.eyeCtrlRGT_crv.parent( self.headRig_grp )
			self.eyeCtrlRGT_crv.attr('t').value = (0,0,0)
			self.eyeCtrlRGT_crv.attr('r').value = (0,0,0)
			
			# Cleanup
			self.eyeRGT_ctrl.attr( 'v' ).lockHide()
			for attr in ('rx','ry','rz','sx','sy','sz','v') :
				self.eyeTrgtRGT_ctrl.attr( attr ).lockHide()
		
		#---------------------------------------------------------
		
		# Group
		self.headRig_grp.parent( animGrp )
		
		# Rig cleanup		
		rigTools.lockUnusedAttrs( self )

