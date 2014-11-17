# fngr rig module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class FingerRig( object ) :
	
	def __init__( self ,
				fngr = 'index' ,
				parent = 'handLFT_jnt' , 
				armCtrl = 'armLFT_ctrl' ,
				side = 'LFT' ,
				animGrp = 'anim_grp' ,
				skinGrp = 'skin_grp' ,
				stillGrp = 'still_grp' ,
				charSize = 1 ,
				tmpJnt = ( 'index1LFT_tmpJnt' , 'index2LFT_tmpJnt' , 'index3LFT_tmpJnt' , 'index4LFT_tmpJnt' , 'index5LFT_tmpJnt' ) ) :
		
		# Checking parent
		wristJnt = pc.Dag( parent )
		if not wristJnt.exists :
			wristJnt = pc.Null()
			wristJnt.parent( skinGrp )
			
		# Template objects
		arm = pc.Dag( armCtrl )
		
		fngr1 = pc.Dag( tmpJnt[0] )
		fngr2 = pc.Dag( tmpJnt[1] )
		fngr3 = pc.Dag( tmpJnt[2] )
		fngr4 = pc.Dag( tmpJnt[3] )
		fngr5 = pc.Dag( tmpJnt[4] )
		
		# Skin joints
		self.fngr1_jnt = rigTools.jointAt( fngr1 )
		self.fngr2_jnt = rigTools.jointAt( fngr2 )
		self.fngr3_jnt = rigTools.jointAt( fngr3 )
		self.fngr4_jnt = rigTools.jointAt( fngr4 )
		self.fngr5_jnt = rigTools.jointAt( fngr5 )
		
		# Skin joint - parenting
		self.fngr1_jnt.parent( wristJnt )
		self.fngr2_jnt.parent( self.fngr1_jnt )
		self.fngr3_jnt.parent( self.fngr2_jnt )
		self.fngr4_jnt.parent( self.fngr3_jnt )
		self.fngr5_jnt.parent( self.fngr4_jnt )
		
		self.fngr1_jnt.attr('segmentScaleCompensate').v = 0
		
		mc.parentConstraint( self.fngr1_jnt , fngr1 )
		mc.parentConstraint( self.fngr2_jnt , fngr2 )
		mc.parentConstraint( self.fngr3_jnt , fngr3 )
		mc.parentConstraint( self.fngr4_jnt , fngr4 )
		mc.parentConstraint( self.fngr5_jnt , fngr5 )
		
		# Main group
		self.fngrRig_grp = pc.Null()
		self.fngrGrp_parCons = pc.parentConstraint( wristJnt , self.fngrRig_grp )
		self.fngrGrp_scaCons = pc.scaleConstraint( wristJnt , self.fngrRig_grp )
		
		# fngr control
		self.fngr_ctrl = pc.Control( 'stick' )
		self.fngrCtrlZro_grp = pc.group( self.fngr_ctrl )
		self.fngrCtrlZro_grp.snap( fngr1 )
		self.fngrCtrlZro_grp.parent( self.fngrRig_grp )
		
		# fngr control - shape adjustment
		self.fngr_ctrl.color = 'blue'
		self.fngr_ctrl.scaleShape( charSize )
		
		# Aim
		self.fngrAim_grp = pc.Null()
		#self.fngrAim_grp.snap( fngr2 )
		
		#self.fngrTarget_ctrl = pc.Control( 'plus' )
		#self.fngrTargetCtrlZro_grp = pc.group( self.fngrTarget_ctrl )
		#self.fngrTargetCtrlZro_grp.snapPoint( fngr5 )
		
		# Aim control - shape adjustment
		#self.fngrTarget_ctrl.color = 'blue'
		#self.fngrTarget_ctrl.scaleShape( charSize )
		
		# Aim - curve guide
		#self.fngrTarget_crv , self.fngrTarget1_clstr , self.fngrTarget2_clstr = rigTools.crvGuide( ctrl = self.fngrAim_grp , target = self.fngrTarget_ctrl )
		
		#self.fngrTarget_crv.parent( self.fngrRig_grp )
		#self.fngrTarget_crv.attr('inheritsTransform').value = 0
		#self.fngrTarget_crv.attr('t').value = (0,0,0)
		#self.fngrTarget_crv.attr('r').value = (0,0,0)
		
		#self.fngrTarget_crv.attr('overrideEnabled').value = 1
		#self.fngrTarget_crv.attr('overrideDisplayType').value = 2
		
		# ----- FK -----
		# FK main group
		self.fngrFk_grp = pc.Null()
		self.fngrFk_grp.snap( fngr1 )
		self.fngrFk_grp.parent( self.fngr_ctrl )
		
		# FK controls
		self.fngr1Fk_ctrl = rigTools.jointControl( 'circle' )
		self.fngr1FkCtrlTwst_grp = pc.group( self.fngr1Fk_ctrl )
		self.fngr1FkCtrlSdk_grp = pc.group( self.fngr1FkCtrlTwst_grp )
		self.fngr1FkCtrlZro_grp = pc.group( self.fngr1FkCtrlSdk_grp )
		
		self.fngr2Fk_ctrl = rigTools.jointControl( 'circle' )
		self.fngr2FkCtrlTwst_grp = pc.group( self.fngr2Fk_ctrl )
		self.fngr2FkCtrlSdk_grp = pc.group( self.fngr2FkCtrlTwst_grp )
		self.fngr2FkCtrlZro_grp = pc.group( self.fngr2FkCtrlSdk_grp )
		
		self.fngr3Fk_ctrl = rigTools.jointControl( 'circle' )
		self.fngr3FkCtrlTwst_grp = pc.group( self.fngr3Fk_ctrl )
		self.fngr3FkCtrlSdk_grp = pc.group( self.fngr3FkCtrlTwst_grp )
		self.fngr3FkCtrlZro_grp = pc.group( self.fngr3FkCtrlSdk_grp )
		
		self.fngr4Fk_ctrl = rigTools.jointControl( 'circle' )
		self.fngr4FkCtrlTwst_grp = pc.group( self.fngr4Fk_ctrl )
		self.fngr4FkCtrlSdk_grp = pc.group( self.fngr4FkCtrlTwst_grp )
		self.fngr4FkCtrlZro_grp = pc.group( self.fngr4FkCtrlSdk_grp )
		
		# FK control - parenting and positioning
		self.fngr1FkCtrlZro_grp.snap( fngr1 )
		self.fngr2FkCtrlZro_grp.snap( fngr2 )
		self.fngr3FkCtrlZro_grp.snap( fngr3 )
		self.fngr4FkCtrlZro_grp.snap( fngr4 )
		
		self.fngr1FkCtrlZro_grp.parent( self.fngrFk_grp )
		self.fngrAim_grp.parent( self.fngr1Fk_ctrl )
		#self.fngrTargetCtrlZro_grp.parent( self.fngr1Fk_ctrl )
		self.fngr2FkCtrlZro_grp.parent( self.fngrAim_grp )
		self.fngr3FkCtrlZro_grp.parent( self.fngr2Fk_ctrl )
		self.fngr4FkCtrlZro_grp.parent( self.fngr3Fk_ctrl )
		
		# fngr aim - target local/world orientation
		#self.fngrTargetCtrlLoc_grp,self.fngrTargetCtrlWor_grp,self.fngrTargetCtrlWorGrp_parCons , self.fngrTargetCtrlZroGrp_parCons , self.fngrTargetCtrlZroGrpParCons_rev = rigTools.parentLocalWorldCtrl( self.fngrTarget_ctrl , self.fngr1Fk_ctrl , animGrp , self.fngrTargetCtrlZro_grp )
		
		# FK control - shape adjustment
		self.fngr1Fk_ctrl.color = 'red'
		self.fngr2Fk_ctrl.color = 'red'
		self.fngr3Fk_ctrl.color = 'red'
		self.fngr4Fk_ctrl.color = 'red'
		self.fngr1Fk_ctrl.scaleShape( 0.5 * charSize )
		self.fngr2Fk_ctrl.scaleShape( 0.5 * charSize )
		self.fngr3Fk_ctrl.scaleShape( 0.5 * charSize )
		self.fngr4Fk_ctrl.scaleShape( 0.5 * charSize )
		
		# FK control - rotate order adjustment
		self.fngr1Fk_ctrl.rotateOrder = 'xzy'
		self.fngr2Fk_ctrl.rotateOrder = 'xzy'
		self.fngr3Fk_ctrl.rotateOrder = 'xzy'
		self.fngr4Fk_ctrl.rotateOrder = 'xzy'
		
		# fngr aim - aim constraint
		#if side == 'LFT' :
			#self.fngrAimGrp_aimCons = pc.aimConstraint(self.fngrTarget_ctrl,self.fngrAim_grp,aimVector=(0,1,0),upVector=(0,0,1),worldUpType="objectrotation",worldUpVector=(0,0,1),worldUpObject=self.fngr1Fk_ctrl,mo=True)
		#else :
			#self.fngrAimGrp_aimCons = pc.aimConstraint(self.fngrTarget_ctrl,self.fngrAim_grp,aimVector=(0,-1,0),upVector=(0,0,1),worldUpType="objectrotation",worldUpVector=(0,0,1),worldUpObject=self.fngr1Fk_ctrl,mo=True)
		
		# FK control - stretch control
		self.fngr2FkStretch_add , self.fngr2FkStretch_mul = rigTools.fkStretch( ctrl = self.fngr2Fk_ctrl , target = self.fngr3FkCtrlZro_grp )
		self.fngr3FkStretch_add , self.fngr3FkStretch_mul = rigTools.fkStretch( ctrl = self.fngr3Fk_ctrl , target = self.fngr4FkCtrlZro_grp )
		self.fngr4FkStretch_add , self.fngr4FkStretch_mul = rigTools.fkStretch( ctrl = self.fngr4Fk_ctrl , target = self.fngr5_jnt )
		
		# FK control - stretch control - stretch collector
		self.fngr2FkCtrlStretch_pma = pc.PlusMinusAverage()
		self.fngr3FkCtrlStretch_pma = pc.PlusMinusAverage()
		self.fngr4FkCtrlStretch_pma = pc.PlusMinusAverage()
		
		self.fngr2FkCtrlStretch_pma.attr('o1') >> self.fngr3FkCtrlZro_grp.attr('ty')
		self.fngr3FkCtrlStretch_pma.attr('o1') >> self.fngr4FkCtrlZro_grp.attr('ty')
		self.fngr4FkCtrlStretch_pma.attr('o1') >> self.fngr5_jnt.attr('ty')
		
		self.fngr2FkStretch_add.attr('o') >> self.fngr2FkCtrlStretch_pma.last1D()
		self.fngr3FkStretch_add.attr('o') >> self.fngr3FkCtrlStretch_pma.last1D()
		self.fngr4FkStretch_add.attr('o') >> self.fngr4FkCtrlStretch_pma.last1D()
		
		# Fk control - adjusting stretch amplitude
		self.fngr2FkStretchAmp_mul = rigTools.attrAmper( self.fngr2Fk_ctrl.attr('stretch') , self.fngr2FkStretch_mul.attr('i2') , dv = 0.1 )
		self.fngr3FkStretchAmp_mul = rigTools.attrAmper( self.fngr3Fk_ctrl.attr('stretch') , self.fngr3FkStretch_mul.attr('i2') , dv = 0.1 )
		self.fngr4FkStretchAmp_mul = rigTools.attrAmper( self.fngr4Fk_ctrl.attr('stretch') , self.fngr4FkStretch_mul.attr('i2') , dv = 0.1 )
		
		# FK control - connect to joint
		self.fngr1Jnt_parCons = pc.parentConstraint( self.fngr1Fk_ctrl , self.fngr1_jnt )
		self.fngr2Jnt_parCons = pc.parentConstraint( self.fngr2Fk_ctrl , self.fngr2_jnt )
		self.fngr3Jnt_parCons = pc.parentConstraint( self.fngr3Fk_ctrl , self.fngr3_jnt )
		self.fngr4Jnt_parCons = pc.parentConstraint( self.fngr4Fk_ctrl , self.fngr4_jnt )
		
		# Attribute control - plusMinusAverage - rotation collector
		self.fngr1FkCtrlSdkRx_pma = pc.PlusMinusAverage()
		self.fngr2FkCtrlSdkRx_pma = pc.PlusMinusAverage()
		self.fngr3FkCtrlSdkRx_pma = pc.PlusMinusAverage()
		self.fngr4FkCtrlSdkRx_pma = pc.PlusMinusAverage()
		
		self.fngr1FkCtrlSdkRy_pma = pc.PlusMinusAverage()
		self.fngr2FkCtrlSdkRy_pma = pc.PlusMinusAverage()
		self.fngr3FkCtrlSdkRy_pma = pc.PlusMinusAverage()
		self.fngr4FkCtrlSdkRy_pma = pc.PlusMinusAverage()
		
		self.fngr1FkCtrlSdkRz_pma = pc.PlusMinusAverage()
		self.fngr2FkCtrlSdkRz_pma = pc.PlusMinusAverage()
		self.fngr3FkCtrlSdkRz_pma = pc.PlusMinusAverage()
		self.fngr4FkCtrlSdkRz_pma = pc.PlusMinusAverage()
		
		self.fngr1FkCtrlSdkRx_pma.attr('o1') >> self.fngr1FkCtrlSdk_grp.attr('rx')
		self.fngr2FkCtrlSdkRx_pma.attr('o1') >> self.fngr2FkCtrlSdk_grp.attr('rx')
		self.fngr3FkCtrlSdkRx_pma.attr('o1') >> self.fngr3FkCtrlSdk_grp.attr('rx')
		self.fngr4FkCtrlSdkRx_pma.attr('o1') >> self.fngr4FkCtrlSdk_grp.attr('rx')
		
		self.fngr1FkCtrlSdkRy_pma.attr('o1') >> self.fngr1FkCtrlTwst_grp.attr('ry')
		self.fngr2FkCtrlSdkRy_pma.attr('o1') >> self.fngr2FkCtrlTwst_grp.attr('ry')
		self.fngr3FkCtrlSdkRy_pma.attr('o1') >> self.fngr3FkCtrlTwst_grp.attr('ry')
		self.fngr4FkCtrlSdkRy_pma.attr('o1') >> self.fngr4FkCtrlTwst_grp.attr('ry')
		
		self.fngr1FkCtrlSdkRz_pma.attr('o1') >> self.fngr1FkCtrlSdk_grp.attr('rz')
		self.fngr2FkCtrlSdkRz_pma.attr('o1') >> self.fngr2FkCtrlSdk_grp.attr('rz')
		self.fngr3FkCtrlSdkRz_pma.attr('o1') >> self.fngr3FkCtrlSdk_grp.attr('rz')
		self.fngr4FkCtrlSdkRz_pma.attr('o1') >> self.fngr4FkCtrlSdk_grp.attr('rz')
		
		# Hand attribute control
		armShape = pc.Dag( arm.shape )
		# '__hand__' , 'fist' , 'cup' , 'spread' and 'baseSpread'
		if not arm.attr( '__hand__' ).exists :
			arm.add( ln = '__hand__' , k = True )
			arm.attr( '__hand__' ).set( l = True )
		
		# Hand attribute control - fist
		if not arm.attr( 'fist' ).exists :
			arm.add( ln = 'fist' , k = True )
		
		self.fngr1FistRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.fngr1FkCtrlSdkRx_pma.last1D(),dv=0,ampAttr='%s1FistRx'%fngr)
		self.fngr1FistRzAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.fngr1FkCtrlSdkRz_pma.last1D(),dv=0,ampAttr='%s1FistRz'%fngr)
		
		self.fngr2FistRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.fngr2FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='%s2FistRx'%fngr)
		self.fngr2FistRyAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.fngr2FkCtrlSdkRy_pma.last1D(),dv=0,ampAttr='%s2FistRy'%fngr)
		self.fngr2FistRzAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.fngr2FkCtrlSdkRz_pma.last1D(),dv=0,ampAttr='%s2FistRz'%fngr)
		
		self.fngr3FistRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.fngr3FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='%s3FistRx'%fngr)
		
		self.fngr4FistRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('fist'),targetAttr=self.fngr4FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='%s4FistRx'%fngr)
		
		# Hand attribute control - cup
		if not arm.attr( 'cup' ).exists :
			arm.add( ln = 'cup' , k = True )
		
		self.fngr1CupRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('cup'),targetAttr=self.fngr1FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='%s1CupRx'%fngr)
		self.fngr2CupRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('cup'),targetAttr=self.fngr2FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='%s2CupRx'%fngr)
		self.fngr3CupRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('cup'),targetAttr=self.fngr3FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='%s3CupRx'%fngr)
		self.fngr4CupRxAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('cup'),targetAttr=self.fngr4FkCtrlSdkRx_pma.last1D(),dv=-0,ampAttr='%s4CupRx'%fngr)
		
		# Hand attribute control - spread
		if not arm.attr( 'spread' ).exists :
			arm.add( ln = 'spread' , k = True )

		self.fngrSpreadAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('spread'),targetAttr=self.fngr2FkCtrlSdkRz_pma.last1D(),dv=-0,ampAttr='%s2Spread'%fngr)
		
		# Hand attribute control - break
		if not arm.attr( 'break' ).exists :
			arm.add( ln = 'break' , k = True )
		
		self.fngr2BreakAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('break'),targetAttr=self.fngr2FkCtrlSdkRz_pma.last1D(),dv=-9,ampAttr='%sBreak'%fngr)
		
		# Hand attribute control - flex
		if not arm.attr( 'flex' ).exists :
			arm.add( ln = 'flex' , k = True )
		
		self.fngr2FlexAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('flex'),targetAttr=self.fngr2FkCtrlSdkRx_pma.last1D(),dv=-9,ampAttr='%sFlex'%fngr)
		
		# Hand attribute control - baseSpread
		if not arm.attr( 'baseSpread' ).exists :
			arm.add( ln = 'baseSpread' , k = True )
		
		self.fngr1BaseSpreadAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('baseSpread'),targetAttr=self.fngr1FkCtrlSdkRz_pma.last1D(),dv=-0,ampAttr='%sBaseSpread'%fngr)
		
		# Hand attribute control - baseBreak
		if not arm.attr( 'baseBreak' ).exists :
			arm.add( ln = 'baseBreak' , k = True )
		
		self.fngr2BaseBreakAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('baseBreak'),targetAttr=self.fngr1FkCtrlSdkRz_pma.last1D(),dv=-9,ampAttr='%sBaseBreak'%fngr)
		
		# Hand attribute control - baseFlex
		if not arm.attr( 'baseFlex' ).exists :
			arm.add( ln = 'baseFlex' , k = True )
		
		self.fngr2BaseFlexAmp_mul = rigTools.attrAmper(ctrlAttr=arm.attr('baseFlex'),targetAttr=self.fngr1FkCtrlSdkRx_pma.last1D(),dv=-9,ampAttr='%sBaseFlex'%fngr)
		
		# fngr attribute control
		# attrs = ( '__%s__' % fngr , 'fold' , 'stretch' , '__fngr1__' , 'fngr1Fold' , 'fngr1Spread' , '__fngr2__' , 'fngr2Fold' , 'fngr2Spread' , '__fngr3__' , 'fngr3Fold' , 'fngr3Spread' , '__fngr4__' , 'fngr4Fold' , 'fngr4Spread' )
		self.fngr_ctrl.add( ln = '__%s__' % fngr , k = True )
		self.fngr_ctrl.attr( '__%s__' % fngr ).set( l = True )
		
		# fngr attribute control - fold
		self.fngr_ctrl.add( ln = 'fold' , k = True )
		
		self.fngr2FngrFoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fold'),targetAttr=self.fngr2FkCtrlSdkRx_pma.last1D(),dv=-9)
		self.fngr3FngrFoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fold'),targetAttr=self.fngr3FkCtrlSdkRx_pma.last1D(),dv=-9)
		self.fngr4FngrFoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fold'),targetAttr=self.fngr4FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# fngr attribute control - stretch
		self.fngr_ctrl.add( ln = 'stretch' , k = True )
		
		self.fngrStretchFngr2_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('stretch'),targetAttr=self.fngr2FkCtrlStretch_pma.last1D(),dv=self.fngr2FkStretch_mul.attr('i1').value)
		self.fngrStretchFngr3_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('stretch'),targetAttr=self.fngr3FkCtrlStretch_pma.last1D(),dv=self.fngr3FkStretch_mul.attr('i1').value)
		self.fngrStretchFngr4_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('stretch'),targetAttr=self.fngr4FkCtrlStretch_pma.last1D(),dv=self.fngr4FkStretch_mul.attr('i1').value)
		
		# fngr attribute control - adjusting stretch amplitude
		self.fngrStretchFngr2Amp_mul = rigTools.attrAmper( self.fngr_ctrl.attr('stretch') , self.fngrStretchFngr2_mul.attr('i2') , dv = 0.1 )
		self.fngrStretchFngr3Amp_mul = rigTools.attrAmper( self.fngr_ctrl.attr('stretch') , self.fngrStretchFngr3_mul.attr('i2') , dv = 0.1 )
		self.fngrStretchFngr4Amp_mul = rigTools.attrAmper( self.fngr_ctrl.attr('stretch') , self.fngrStretchFngr4_mul.attr('i2') , dv = 0.1 )
		
		# fngr attribute control - __fngr1__
		self.fngr_ctrl.add( ln = '__fngr1__' , k = True )
		self.fngr_ctrl.attr( '__fngr1__' ).set( l = True )
		
		# fngr attribute control - __fngr1__ - fngr1Fold
		self.fngr_ctrl.add( ln = 'fngr1Fold' , k = True )
		self.fngr1FoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr1Fold'),targetAttr=self.fngr1FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr1__ - fngr1Spread
		self.fngr_ctrl.add( ln = 'fngr1Spread' , k = True )
		self.fngr1SpreadAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr1Spread'),targetAttr=self.fngr1FkCtrlSdkRz_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr1__ - fngr1Twist
		self.fngr_ctrl.add( ln = 'fngr1Twist' , k = True )
		self.fngr1TwistAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr1Twist'),targetAttr=self.fngr1FkCtrlSdkRy_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr2__
		self.fngr_ctrl.add( ln = '__fngr2__' , k = True )
		self.fngr_ctrl.attr( '__fngr2__' ).set( l = True )
		
		# fngr attribute control - __fngr2__ - fngr2Fold
		self.fngr_ctrl.add( ln = 'fngr2Fold' , k = True )
		self.fngr2FoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr2Fold'),targetAttr=self.fngr2FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr2__ - fngr2Spread
		self.fngr_ctrl.add( ln = 'fngr2Spread' , k = True )
		self.fngr2SpreadAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr2Spread'),targetAttr=self.fngr2FkCtrlSdkRz_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr2__ - fngr2Twist
		self.fngr_ctrl.add( ln = 'fngr2Twist' , k = True )
		self.fngr2TwistAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr2Twist'),targetAttr=self.fngr2FkCtrlSdkRy_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr3__
		self.fngr_ctrl.add( ln = '__fngr3__' , k = True )
		self.fngr_ctrl.attr( '__fngr3__' ).set( l = True )
		
		# fngr attribute control - __fngr3__ - fngr3Fold
		self.fngr_ctrl.add( ln = 'fngr3Fold' , k = True )
		self.fngr3FoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr3Fold'),targetAttr=self.fngr3FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr3__ - fngr3Spread
		self.fngr_ctrl.add( ln = 'fngr3Spread' , k = True )
		self.fngr3SpreadAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr3Spread'),targetAttr=self.fngr3FkCtrlSdkRz_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr3__ - fngr3Twist
		self.fngr_ctrl.add( ln = 'fngr3Twist' , k = True )
		self.fngr3TwistAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr3Twist'),targetAttr=self.fngr3FkCtrlSdkRy_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr4__
		self.fngr_ctrl.add( ln = '__fngr4__' , k = True )
		self.fngr_ctrl.attr( '__fngr4__' ).set( l = True )
		
		# fngr attribute control - __fngr4__ - fngr4Fold
		self.fngr_ctrl.add( ln = 'fngr4Fold' , k = True )
		self.fngr4FoldAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr4Fold'),targetAttr=self.fngr4FkCtrlSdkRx_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr4__ - fngr4Spread
		self.fngr_ctrl.add( ln = 'fngr4Spread' , k = True )
		self.fngr4SpreadAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr4Spread'),targetAttr=self.fngr4FkCtrlSdkRz_pma.last1D(),dv=-9)
		
		# fngr attribute control - __fngr4__ - fngr4Twist
		self.fngr_ctrl.add( ln = 'fngr4Twist' , k = True )
		self.fngr4TwistAmp_mul = rigTools.attrAmper(ctrlAttr=self.fngr_ctrl.attr('fngr4Twist'),targetAttr=self.fngr4FkCtrlSdkRy_pma.last1D(),dv=-9)
		
		# Group
		self.fngrRig_grp.parent( animGrp )
		
		# Rig cleanup		
		rigTools.lockUnusedAttrs( self )
		self.fngr1Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.fngr2Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.fngr3Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		self.fngr4Fk_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
		#self.fngrTarget_ctrl.lockHideAttrs( 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )
		self.fngr_ctrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )
