# FK/IK match module
import maya.cmds as mc
import pkmel.core as pc

def callback() :
	
	sels = pc.lssl()
	sel = pc.Dag( sels[0] )
	
	side = ''
	elem = ''
	
	if 'LFT' in sel.name :
		side = 'LFT'
	elif 'RGT' in sel.name :
		side = 'RGT'

	nodeType = sel.name.split( '_' )[-1]

	nodeName = sel.name.replace( '%s_%s' % ( side , nodeType ) , '' )

	if sel.attr('localWorld').exists :
		for each in sels :
			localWorld( each )
		mc.select( sels )
	
	elif 'arm' in sel.name :
		
		prefix = sel.name.split('arm')[0]
		
		if sel.attr('fkIk').value :
			
			armIkToFk( prefix = prefix , elem = elem , side = side )
		else :
			armFkToIk( prefix = prefix , elem = elem , side = side )
		mc.select( sel )
		
	elif 'leg' in sel.name :
		
		tmp = nodeName.split('leg')
		print tmp
		prefix = tmp[0]
		elem = tmp[1]

		if sel.attr('fkIk').value :
			
			legIkToFk( prefix = prefix , elem = elem , side = side )
		else :
			legFkToIk( prefix = prefix , elem = elem , side = side )
		mc.select( sel )
		
	elif 'spine' in sel.name :
		
		prefix = sel.name.split('spine')[0]
		
		if sel.attr('fkIk').value :
			
			spineIkToFk( prefix = prefix , elem = '' )
		else :
			spineFkToIk( prefix = prefix , elem = '' )
		
		mc.select( sel )

def localWorld( ctrl = '' ) :
	
	# Control
	ctrl = pc.Dag( ctrl )
	grp = pc.Dag( ctrl.getParent() )
	
	# Template control
	prxy = pc.Joint()
	tmp = pc.Joint()
	tmpGrp = pc.group( tmp )
	
	# Rotate order adjustment
	prxy.attr('rotateOrder').value = ctrl.attr('rotateOrder').value
	tmp.attr('rotateOrder').value = ctrl.attr('rotateOrder').value
	
	# Joint orient adjustment
	if ctrl.type == 'joint' :
		prxy.attr('jointOrient').value = ctrl.attr('jointOrient').value
		tmp.attr('jointOrient').value = ctrl.attr('jointOrient').value
	
	# Snaping controls
	prxy.snap( ctrl )
	tmpGrp.snap( ctrl )
	
	tmpCons = pc.parentConstraint( prxy , tmp )
	
	if ctrl.attr('localWorld').value :
		ctrl.attr('localWorld').value = 0
	else :
		ctrl.attr('localWorld').value = 1

	tmpGrp.snap( grp )
	
	attrs = ('tx','ty','tz','rx','ry','rz')
	
	for attr in attrs :
		if not ctrl.attr( attr ).lock :
			ctrl.attr( attr ).value = tmp.attr( attr ).value
	
	# Cleanup
	mc.delete( tmpGrp )
	mc.delete( prxy )

def spineFkToIk( prefix = '' , elem = '' ) :
	# Spine control
	spi = pc.Dag( mc.ls( '%s*spine%s_ctrl' % ( prefix , elem ) )[0] )
	
	# FK controls
	spi1FkCtrl = pc.Dag( mc.ls( '%s*spine1Fk%s_ctrl' % ( prefix , elem ) )[0] )
	spi2FkCtrl = pc.Dag( mc.ls( '%s*spine2Fk%s_ctrl' % ( prefix , elem ) )[0] )
	
	# IK controls
	spiIkRootCtrl = pc.Dag( mc.ls( '%s*spineIkRoot%s_ctrl' % ( prefix , elem ) )[0] )
	spiIkCtrl = pc.Dag( mc.ls( '%s*spineIk%s_ctrl' % ( prefix , elem ) )[0] )
	
	# Fk joints
	spi1Fk = pc.Dag( mc.ls( '%s*spine1Fk%s_jnt' % ( prefix , elem ) )[0] )
	spi2Fk = pc.Dag( mc.ls( '%s*spine2Fk%s_jnt' % ( prefix , elem ) )[0] )
	spi3Fk = pc.Dag( mc.ls( '%s*spine3Fk%s_jnt' % ( prefix , elem ) )[0] )
	
	# Ik joints
	spi1Ik = pc.Dag( mc.ls( '%s*spine1Ik%s_jnt' % ( prefix , elem ) )[0] )
	spi2Ik = pc.Dag( mc.ls( '%s*spine2Ik%s_jnt' % ( prefix , elem ) )[0] )
	spi3Ik = pc.Dag( mc.ls( '%s*spine3Ik%s_jnt' % ( prefix , elem ) )[0] )
	
	# Template objects
	spi1 = pc.Joint()
	spi1Grp = pc.group( spi1 )
	spi2 = pc.Joint()
	spi2Grp = pc.group( spi2 )
	
	# Rotate order adjustment
	spi1.attr('rotateOrder').value = spiIkRootCtrl.attr('rotateOrder').value
	spi2.attr('rotateOrder').value = spiIkCtrl.attr('rotateOrder').value
	
	# Joint orient adjustment
	spi1.attr('jointOrient').value = spiIkRootCtrl.attr('jointOrient').value
	spi2.attr('jointOrient').value = spiIkCtrl.attr('jointOrient').value
	
	# Snaping controls
	spi1Grp.snap( spiIkRootCtrl.getParent() )
	spi1.snap( spi1Fk )
	spiIkRootCtrl.attr('t').value = spi1.attr('t').value
	
	spi2Grp.snap( spiIkCtrl.getParent() )
	spi2.snap( spi2Fk )
	spiIkCtrl.attr('t').value = spi2.attr('t').value
	spiIkCtrl.attr('r').value = spi2.attr('r').value
	
	# Adjusting stretch
	spiIkCtrl.attr('autoStretch').value = 0
	spiIkCtrl.attr('lowerStretch').value = spi1FkCtrl.attr('stretch').value
	spiIkCtrl.attr('upperStretch').value = spi2FkCtrl.attr('stretch').value
	
	spi.attr('fkIk').value = 1
	
	# Cleanup
	mc.delete( spi1Grp )
	mc.delete( spi2Grp )

def spineIkToFk( prefix = '' , elem = '' ) :
	# Spine control
	spi = pc.Dag( mc.ls( '%s*spine%s_ctrl' % ( prefix , elem ) )[0] )
	
	# FK controls
	spi1FkCtrl = pc.Dag( mc.ls( '%s*spine1Fk%s_ctrl' % ( prefix , elem ) )[0] )
	spi2FkCtrl = pc.Dag( mc.ls( '%s*spine2Fk%s_ctrl' % ( prefix , elem ) )[0] )
	
	# IK controls
	spiIkRootCtrl = pc.Dag( mc.ls( '%s*spineIkRoot%s_ctrl' % ( prefix , elem ) )[0] )
	spiIkCtrl = pc.Dag( mc.ls( '%s*spineIk%s_ctrl' % ( prefix , elem ) )[0] )
	
	# Fk joints
	spi1Fk = pc.Dag( mc.ls( '%s*spine1Fk%s_jnt' % ( prefix , elem ) )[0] )
	spi2Fk = pc.Dag( mc.ls( '%s*spine2Fk%s_jnt' % ( prefix , elem ) )[0] )
	spi3Fk = pc.Dag( mc.ls( '%s*spine3Fk%s_jnt' % ( prefix , elem ) )[0] )
	
	# Ik joints
	spi1Ik = pc.Dag( mc.ls( '%s*spine1Ik%s_jnt' % ( prefix , elem ) )[0] )
	spi2Ik = pc.Dag( mc.ls( '%s*spine2Ik%s_jnt' % ( prefix , elem ) )[0] )
	spi3Ik = pc.Dag( mc.ls( '%s*spine3Ik%s_jnt' % ( prefix , elem ) )[0] )
	
	# Template objects
	spi1 = pc.Joint()
	spi1Grp = pc.group( spi1 )
	spi2 = pc.Joint()
	spi2Grp = pc.group( spi2 )
	
	# Rotate order adjustment
	spi1.attr('rotateOrder').value = spi1FkCtrl.attr('rotateOrder').value
	spi2.attr('rotateOrder').value = spi2FkCtrl.attr('rotateOrder').value
	
	# Joint orient adjustment
	spi1.attr('jointOrient').value = spi1FkCtrl.attr('jointOrient').value
	spi2.attr('jointOrient').value = spi2FkCtrl.attr('jointOrient').value
	
	# Snaping controls
	spi1Grp.snap( spi1FkCtrl.getParent() )
	spi1.snap( spi1Ik )
	spi1FkCtrl.attr('t').value = spi1.attr('t').value
	spi1FkCtrl.attr('r').value = spi1.attr('r').value
	
	spi1FkCtrl.attr('stretch').value = 0
	spi1FkCtrl.attr('stretch').value = ( ( spi2Ik.attr('ty').value/spi2Fk.attr('ty').value ) - 1 ) * 10
	
	spi2Grp.snap( spi2FkCtrl.getParent() )
	spi2.snap( spi2Ik )
	#spi2FkCtrl.attr('t').value = spi2.attr('t').value
	spi2FkCtrl.attr('r').value = spi2.attr('r').value
	
	spi2FkCtrl.attr('stretch').value = spiIkCtrl.attr('upperStretch').value
	
	spi.attr('fkIk').value = 0
	
	# Cleanup
	mc.delete( spi1Grp )
	mc.delete( spi2Grp )

def legFkToIk( prefix = '' , elem = '' , side = '' ) :
	
	# Arm control
	leg = pc.Dag( mc.ls( '%s*leg%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# FK controls
	upLegFkCtrl = pc.Dag( mc.ls( '%s*upLegFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	lowLegFkCtrl = pc.Dag( mc.ls( '%s*lowLegFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	ankleFkCtrl = pc.Dag( mc.ls( '%s*ankleFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	toeFkCtrl = pc.Dag( mc.ls( '%s*toeFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# IK controls
	legIkRootCtrl = pc.Dag( mc.ls( '%s*legIkRoot%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	legIkCtrl = pc.Dag( mc.ls( '%s*legIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	kneeIkCtrl = pc.Dag( mc.ls( '%s*kneeIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# Fk joints
	upLegFk = pc.Dag( mc.ls( '%s*upLegFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	lowLegFk = pc.Dag( mc.ls( '%s*lowLegFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ankleFk = pc.Dag( mc.ls( '%s*ankleFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ballFk = pc.Dag( mc.ls( '%s*ballFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	toeFk = pc.Dag( mc.ls( '%s*toeFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Ik joints
	upLegIk = pc.Dag( mc.ls( '%s*upLegIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	lowLegIk = pc.Dag( mc.ls( '%s*lowLegIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ankleIk = pc.Dag( mc.ls( '%s*ankleIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ballIk = pc.Dag( mc.ls( '%s*ballIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	toeIk = pc.Dag( mc.ls( '%s*toeIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Template objects
	upLeg = pc.Joint()
	upLegGrp = pc.group( upLeg )
	lowLeg = pc.Joint()
	lowLegGrp = pc.group( lowLeg )
	ankle = pc.Joint()
	ankleGrp = pc.group( ankle )
	
	# Rotate order adjustment
	upLeg.attr('rotateOrder').value = legIkRootCtrl.attr('rotateOrder').value
	#lowLeg.attr('rotateOrder').value = kneeIkCtrl.attr('rotateOrder').value
	ankle.attr('rotateOrder').value = legIkCtrl.attr('rotateOrder').value
	
	# Joint orient adjustment
	upLeg.attr('jointOrient').value = legIkRootCtrl.attr('jointOrient').value
	#lowLeg.attr('jointOrient').value = kneeIkCtrl.attr('jointOrient').value
	ankle.attr('jointOrient').value = legIkCtrl.attr('jointOrient').value
	#mc.select( lowLegGrp )
	#pc.deletrl.attr('jointOrient').value
	
	# Snaping controls
	upLegGrp.snap( legIkRootCtrl.getParent() )
	upLeg.snap( upLegFk )
	legIkRootCtrl.attr('t').value = upLeg.attr('t').value
	#legIkRootCtrl.attr('r').value = upLeg.attr('r').value
	
	ankleGrp.snap( legIkCtrl.getParent() )
	ankle.snap( ankleFk )
	legIkCtrl.attr('t').value = ankle.attr('t').value
	legIkCtrl.attr('r').value = ankle.attr('r').value
	
	lowLegGrp.snap( kneeIkCtrl.getParent() )
	lowLeg.snap( lowLegFk )
	kneeIkCtrl.attr('t').value = lowLeg.attr('t').value
	#kneeIkCtrl.attr('r').value = lowLeg.attr('r').value
	
	# Adjusting stretch
	legIkCtrl.attr('autoStretch').value = 0
	legIkCtrl.attr('upLegStretch').value = upLegFkCtrl.attr('stretch').value
	legIkCtrl.attr('lowLegStretch').value = lowLegFkCtrl.attr('stretch').value
	legIkCtrl.attr('toeStretch').value = toeFkCtrl.attr('stretch').value
	
	leg.attr('fkIk').value = 1
	
	# Cleanup
	mc.delete( upLegGrp )
	mc.delete( lowLegGrp )
	mc.delete( ankleGrp )

def legIkToFk( prefix = '' , elem = '' , side = '' ) :
	
	# Arm control
	leg = pc.Dag( mc.ls( '%s*leg%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# FK controls
	upLegFkCtrl = pc.Dag( mc.ls( '%s*upLegFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	lowLegFkCtrl = pc.Dag( mc.ls( '%s*lowLegFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	ankleFkCtrl = pc.Dag( mc.ls( '%s*ankleFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	toeFkCtrl = pc.Dag( mc.ls( '%s*toeFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# IK controls
	legIkRootCtrl = pc.Dag( mc.ls( '%s*legIkRoot%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	legIkCtrl = pc.Dag( mc.ls( '%s*legIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	kneeIkCtrl = pc.Dag( mc.ls( '%s*kneeIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# Fk joints
	upLegFk = pc.Dag( mc.ls( '%s*upLegFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	lowLegFk = pc.Dag( mc.ls( '%s*lowLegFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ankleFk = pc.Dag( mc.ls( '%s*ankleFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ballFk = pc.Dag( mc.ls( '%s*ballFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	toeFk = pc.Dag( mc.ls( '%s*toeFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Ik joints
	upLegIk = pc.Dag( mc.ls( '%s*upLegIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	lowLegIk = pc.Dag( mc.ls( '%s*lowLegIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ankleIk = pc.Dag( mc.ls( '%s*ankleIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	ballIk = pc.Dag( mc.ls( '%s*ballIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	toeIk = pc.Dag( mc.ls( '%s*toeIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Template objects
	upLeg = pc.Joint()
	upLegGrp = pc.group( upLeg )
	lowLeg = pc.Joint()
	lowLegGrp = pc.group( lowLeg )
	ankle = pc.Joint()
	ankleGrp = pc.group( ankle )
	
	# Rotate order adjustment
	upLeg.attr('rotateOrder').value = upLegFkCtrl.attr('rotateOrder').value
	lowLeg.attr('rotateOrder').value = lowLegFkCtrl.attr('rotateOrder').value
	ankle.attr('rotateOrder').value = ankleFkCtrl.attr('rotateOrder').value
	
	# Joint orient adjustment
	upLeg.attr('jointOrient').value = upLegFkCtrl.attr('jointOrient').value
	lowLeg.attr('jointOrient').value = lowLegFkCtrl.attr('jointOrient').value
	ankle.attr('jointOrient').value = ankleFkCtrl.attr('jointOrient').value
	
	# Snaping controls
	upLegGrp.snap( upLegFkCtrl.getParent() )
	upLeg.snap( upLegIk )
	upLegFkCtrl.attr('t').value = upLeg.attr('t').value
	upLegFkCtrl.attr('r').value = upLeg.attr('r').value
	
	upLegFkCtrl.attr('stretch').value = 0
	upLegFkCtrl.attr('stretch').value = ( ( lowLegIk.attr('ty').value/lowLegFk.attr('ty').value ) - 1 ) * 10
	
	lowLegGrp.snap( lowLegFkCtrl.getParent() )
	lowLeg.snap( lowLegIk )
	lowLegFkCtrl.attr('r').value = lowLeg.attr('r').value
	
	lowLegFkCtrl.attr('stretch').value = 0
	lowLegFkCtrl.attr('stretch').value = ( ( ankleIk.attr('ty').value/ankleFk.attr('ty').value ) - 1 ) * 10
	
	ankleGrp.snap( ankleFkCtrl.getParent() )
	ankle.snap( ankleIk )
	ankleFkCtrl.attr('r').value = ankle.attr('r').value
	
	toeFkCtrl.attr('r').value = (0,0,0)
	toeFkCtrl.attr('rx').value = -legIkCtrl.attr('toeBend').value
	toeFkCtrl.attr('stretch').value = legIkCtrl.attr('toeStretch').value
	
	leg.attr('fkIk').value = 0
	
	# Cleanup
	mc.delete( upLegGrp )
	mc.delete( lowLegGrp )
	mc.delete( ankleGrp )

def armIkToFk( prefix = '' , elem = '' , side = '' ) :
	
	# Arm control
	arm = pc.Dag( mc.ls( '%s*arm%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# FK controls
	upArmFkCtrl = pc.Dag( mc.ls( '%s*upArmFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	forearmFkCtrl = pc.Dag( mc.ls( '%s*forearmFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	wristFkCtrl = pc.Dag( mc.ls( '%s*wristFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# IK controls
	armIkRootCtrl = pc.Dag( mc.ls( '%s*armIkRoot%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	armIkCtrl = pc.Dag( mc.ls( '%s*armIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	elbowIkCtrl = pc.Dag( mc.ls( '%s*elbowIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# Fk joints
	upArmFk = pc.Dag( mc.ls( '%s*upArmFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	forearmFk = pc.Dag( mc.ls( '%s*forearmFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	wristFk = pc.Dag( mc.ls( '%s*wristFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	handFk = pc.Dag( mc.ls( '%s*handFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Ik joints
	upArmIk = pc.Dag( mc.ls( '%s*upArmIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	forearmIk = pc.Dag( mc.ls( '%s*forearmIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	wristIk = pc.Dag( mc.ls( '%s*wristIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	handIk = pc.Dag( mc.ls( '%s*handIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Template objects
	upArm = pc.Joint()
	upArmGrp = pc.group( upArm )
	forearm = pc.Joint()
	forearmGrp = pc.group( forearm )
	wrist = pc.Joint()
	wristGrp = pc.group( wrist )
	
	# Rotate order adjustment
	upArm.attr('rotateOrder').value = upArmFkCtrl.attr('rotateOrder').value
	forearm.attr('rotateOrder').value = forearmFkCtrl.attr('rotateOrder').value
	wrist.attr('rotateOrder').value = wristFkCtrl.attr('rotateOrder').value
	
	# Joint orient adjustment
	upArm.attr('jointOrient').value = upArmFkCtrl.attr('jointOrient').value
	forearm.attr('jointOrient').value = forearmFkCtrl.attr('jointOrient').value
	wrist.attr('jointOrient').value = wristFkCtrl.attr('jointOrient').value
	
	# Snaping controls
	upArmGrp.snap( upArmFkCtrl.getParent() )
	upArm.snap( upArmIk )
	upArmFkCtrl.attr('r').value = upArm.attr('r').value
	upArmFkCtrl.attr('t').value = upArm.attr('t').value
	
	upArmFkCtrl.attr('stretch').value = 0
	upArmFkCtrl.attr('stretch').value = ( ( forearmIk.attr('ty').value/forearmFk.attr('ty').value ) - 1 ) * 10
	
	forearmGrp.snap( forearmFkCtrl.getParent() )
	forearm.snap( forearmIk )
	forearmFkCtrl.attr('r').value = forearm.attr('r').value
	
	forearmFkCtrl.attr('stretch').value = 0
	forearmFkCtrl.attr('stretch').value = ( ( wristIk.attr('ty').value/wristFk.attr('ty').value ) - 1 ) * 10
	
	wristGrp.snap( wristFkCtrl.getParent() )
	wrist.snap( wristIk )
	wristFkCtrl.attr('r').value = wrist.attr('r').value
	
	#wristFkCtrl.attr('stretch').value = armIkCtrl.attr('handStretch').value
	#wristFkCtrl.attr('handRoll').value = handIk.attr('rz').value
	
	arm.attr('fkIk').value = 0
	
	# Cleanup
	mc.delete( upArmGrp )
	mc.delete( forearmGrp )
	mc.delete( wristGrp )

def armFkToIk( prefix = '' , elem = '' , side = '' ) :
	
	# Arm control
	arm = pc.Dag( mc.ls( '%s*arm%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# FK controls
	upArmFkCtrl = pc.Dag( mc.ls( '%s*upArmFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	forearmFkCtrl = pc.Dag( mc.ls( '%s*forearmFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	wristFkCtrl = pc.Dag( mc.ls( '%s*wristFk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# IK controls
	armIkRootCtrl = pc.Dag( mc.ls( '%s*armIkRoot%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	armIkCtrl = pc.Dag( mc.ls( '%s*armIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	elbowIkCtrl = pc.Dag( mc.ls( '%s*elbowIk%s%s_ctrl' % ( prefix , elem , side ) )[0] )
	
	# Fk joints
	upArmFk = pc.Dag( mc.ls( '%s*upArmFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	forearmFk = pc.Dag( mc.ls( '%s*forearmFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	wristFk = pc.Dag( mc.ls( '%s*wristFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	handFk = pc.Dag( mc.ls( '%s*handFk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Ik joints
	upArmIk = pc.Dag( mc.ls( '%s*upArmIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	forearmIk = pc.Dag( mc.ls( '%s*forearmIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	wristIk = pc.Dag( mc.ls( '%s*wristIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	handIk = pc.Dag( mc.ls( '%s*handIk%s%s_jnt' % ( prefix , elem , side ) )[0] )
	
	# Template objects
	upArm = pc.Joint()
	upArmGrp = pc.group( upArm )
	forearm = pc.Joint()
	forearmGrp = pc.group( forearm )
	wrist = pc.Joint()
	wristGrp = pc.group( wrist )
	
	# Rotate order adjustment
	upArm.attr('rotateOrder').value = armIkRootCtrl.attr('rotateOrder').value
	wrist.attr('rotateOrder').value = armIkCtrl.attr('rotateOrder').value
	forearm.attr('rotateOrder').value = elbowIkCtrl.attr('rotateOrder').value
	
	# Joint orient adjustment
	upArm.attr('jointOrient').value = armIkRootCtrl.attr('jointOrient').value
	wrist.attr('jointOrient').value = armIkCtrl.attr('jointOrient').value
	
	# Snaping controls
	upArmGrp.snap( armIkRootCtrl.getParent() )
	upArm.snap( upArmFk )
	armIkRootCtrl.attr('t').value = upArm.attr('t').value
	#armIkRootCtrl.attr('r').value = upArm.attr('r').value
	
	wristGrp.snap( armIkCtrl.getParent() )
	mc.delete( mc.scaleConstraint( armIkCtrl.getParent() , wristGrp ) )
	wrist.snap( wristFk )
	armIkCtrl.attr('t').value = wrist.attr('t').value
	armIkCtrl.attr('r').value = wrist.attr('r').value
	
	forearmGrp.snap( elbowIkCtrl.getParent() )
	mc.delete( mc.scaleConstraint( elbowIkCtrl.getParent() , forearmGrp ) )
	forearm.snap( forearmFk )
	elbowIkCtrl.attr('t').value = forearm.attr('t').value
	#elbowIkCtrl.attr('r').value = forearm.attr('r').value
	
	# Adjusting stretch
	armIkCtrl.attr('autoStretch').value = 0
	#armIkCtrl.attr('handRoll').value = 0
	armIkCtrl.attr('upArmStretch').value = upArmFkCtrl.attr('stretch').value
	armIkCtrl.attr('forearmStretch').value = forearmFkCtrl.attr('stretch').value
	#armIkCtrl.attr('handStretch').value = wristFkCtrl.attr('stretch').value
	
	arm.attr('fkIk').value = 1
	
	# Cleanup
	mc.delete( upArmGrp )
	mc.delete( forearmGrp )
	mc.delete( wristGrp )