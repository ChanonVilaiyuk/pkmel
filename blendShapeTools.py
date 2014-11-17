# System module.
import re

# Maya module.
import maya.cmds as mc
import maya.mel as mm

# Custom module.
import pkmel.core as pc
reload( pc )
import pkmel.rigTools as rigTools
reload( rigTools )

SIDE = [
		'LFT' ,
		'RGT'
		]

BLEND_BUFFER = 'facialBuffer_bsh'

EYEBROW_SIDE	= [
					'eyebrowUp_bsh' ,
					'eyebrowDn_bsh' ,
					'eyebrowIn_bsh' ,
					'eyebrowOut_bsh' ,
					'eyebrowInnerUp_bsh' ,
					'eyebrowInnerDn_bsh' ,
					'eyebrowMidUp_bsh' ,
					'eyebrowMidDn_bsh' ,
					'eyebrowOuterUp_bsh' ,
					'eyebrowOuterDn_bsh' ,
					'eyebrowTurnF_bsh' ,
					'eyebrowTurnC_bsh'
					]

LID_SIDE 		= [
					'upLidUp_bsh' ,
					'upLidDn_bsh' ,
					'loLidUp_bsh' ,
					'loLidDn_bsh' ,
					'upLidTwistF_bsh' ,
					'upLidTwistC_bsh' ,
					'loLidTwistF_bsh' ,
					'loLidTwistC_bsh' ,
					'upLidDnInbA_bsh' ,
					'upLidDnInbB_bsh' ,
					'upLidDnInbC_bsh' ,
					'loLidUpInbA_bsh' ,
					'loLidUpInbB_bsh' ,
					'loLidUpInbC_bsh' ,
					]

MOUTH_SIDE 		= [
					'upLipUp_bsh' ,
					'upLipDn_bsh' ,
					'loLipUp_bsh' ,
					'loLipDn_bsh' ,
					'cnrLipUp_bsh' ,
					'cnrLipDn_bsh' ,
					'cnrLipIn_bsh' ,
					'cnrLipOut_bsh' ,
					'cnrLipPartIn_bsh' ,
					'cnrLipPartOut_bsh' ,
					'cnrLipPuffIn_bsh' ,
					'cnrLipPuffOut_bsh' ,
					'snear_bsh' ,
					'cheek_bsh' ,
					'puff_bsh'
					]

MOUTH 			= [
					'mouthUp_bsh' ,
					'mouthDn_bsh' ,
					'mouthTurnL_bsh' ,
					'mouthTurnR_bsh' ,
					'mouthTurnF_bsh' ,
					'mouthTurnC_bsh' ,
					'mouthClench_bsh' ,
					'mouthPull_bsh' ,
					'mouthUWQ_bsh' ,
					'upLipUpMid_bsh' ,
					'upLipDnMid_bsh' ,
					'loLipUpMid_bsh' ,
					'loLipDnMid_bsh' ,
					'upLipUp_bsh' ,
					'upLipDn_bsh' ,
					'loLipUp_bsh' ,
					'loLipDn_bsh' ,
					'upLipCurlIn_bsh' ,
					'upLipCurlOut_bsh' ,
					'loLipCurlIn_bsh' ,
					'loLipCurlOut_bsh' ,
					]

NOSE_SIDE 		= [
					'noseUp_bsh' ,
					'noseDn_bsh' ,
					'noseTurnF_bsh' ,
					'noseTurnC_bsh'
					]

FACE 			= [
					'faceSquash_bsh' ,
					'faceStretch_bsh' ,
					'faceEyebrowPull_bsh'
					]

NOSE 			= [
					'noseSquash_bsh' ,
					'noseStretch_bsh'
					]

WITH_SIDE = [
				EYEBROW_SIDE ,
				LID_SIDE ,
				MOUTH_SIDE ,
				NOSE_SIDE
			]

WITHOUT_SIDE = [
					MOUTH ,
					FACE ,
					NOSE
				]

MOUTH_ATTR = [
					'mouthTurn' ,
					'upperLip' ,
					'lowerLip' ,
					'upperCurl' ,
					'lowerCurl' ,
					'clench' ,
					'pull' ,
					'u'
				]

MOUTH_SIDE_ATTR = [
						'upper' ,
						'lower' ,
						'part' ,
						'snear' ,
						'cheek' ,
						'puff'
					]

EYEBROW_SIDE_ATTR = [
						'inner' ,
						'middle' ,
						'outer' ,
						'turn'
					]

EYELID_SIDE_ATTR = [
						'upper' ,
						'lower' ,
						'upperTwist' ,
						'lowerTwist'
					]

def createBlendShapeName( skipInb=True) :
	
	# Populate blend shape name regarding WITH_SIDE and WITHOUT_SIDE global name.
	
	blendShapeNames = []
	
	for bshSide in WITH_SIDE :
		for bshName in bshSide :
			for side in SIDE :
				if not 'Inb' in bshName :
					blendShapeNames.append( bshName.replace( '_' , '%s_' % side ) )
	
	for bsh in WITHOUT_SIDE :
		for bshName in bsh :
			if not 'Inb' in bshName :
				blendShapeNames.append( bshName )
	
	return blendShapeNames

def connectInbetween(
						blendShapeObject = '' ,
						blendShapeNode = '' ,
						inbetweenBlendShape = '' ,
						targetBlendShapeName = '' ,
						weightValue = ''
					) :
	
	# Add inbetween blend shape.

	aliasAttrList = mc.aliasAttr( blendShapeNode , q=True )

	for each in aliasAttrList :

		if each == targetBlendShapeName :

			idx = aliasAttrList.index( each )
			wStr = str( aliasAttrList[ idx+1 ] )
			wIdx = re.findall( r'\d+' , wStr )[0]

			cmd = 'blendShape -e  -ib -t %s %s %s %s %s;' % (
																blendShapeObject ,
																wIdx ,
																inbetweenBlendShape ,
																weightValue ,
																blendShapeNode
															)
			
			mm.eval( cmd )

def getAttrMax( attr = 'node.attr' ) :
	# Return max value of given attribute
	node = pc.Dag( attr.split('.')[0] )
	attr = attr.split('.')[1]
	
	trnsAttrs = ( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'rx' , 'ry ' , 'rz' )
	
	if attr in trnsAttrs :
		return node.attr('x%sl'%attr).v
	else :
		return mc.attributeQuery( attr , node=node , max=True)[0]

def twoWaysConnect(
						attrOut = 'ctrl.tx' ,
						attrIn = ( 'bsh.outBsh' , 'bsh.inBsh' ) ,
						outAmper = 1
					) :
	# Connecting driver attribute to driven blend shapes with two cases
	# attrIn[1] for direct connection
	# attrIn[2] for inverse connection
	
	# Getting informations
	ctrl = pc.Dag( attrOut.split('.')[0] )
	ctrlAttr = attrOut.split('.')[1]
	bsh = pc.Dag( attrIn[0].split('.')[0] )
	bshAttrA = attrIn[0].split('.')[1]
	bshAttrB = attrIn[1].split('.')[1]
	
	clmp = pc.Clamp()
	mul = pc.MultDoubleLinear()
	
	clmp.attr('maxR').v = 1
	clmp.attr('minG').v = -1
	
	clmp.attr('outputG') >> mul.attr('i1')
	mul.attr('i2').v = -1
	mul.attr('o') >> bsh.attr(bshAttrB)
	clmp.attr('outputR') >> bsh.attr(bshAttrA)
	
	if not outAmper == 1 :
		
		amp = rigTools.attrAmper( ctrlAttr = ctrl.attr(ctrlAttr) ,
							targetAttr = clmp.attr('inputR') ,
							dv = outAmper
							)
		amp.attr('o') >> clmp.attr('inputG')
		
		return clmp , mul , amp
	else :
		ctrl.attr(ctrlAttr) >> clmp.attr('inputR')
		ctrl.attr(ctrlAttr) >> clmp.attr('inputG')
		
		return clmp , mul

def addCollector( nodeAttr='' ) :

	# Adding plusMinusAverage node for collecting every input.

	inputNodeName , inputNodeAttr = nodeAttr.split( '.' )
	nodeObj = pc.Dag( inputNodeName )
	nodeElemName , nodeSide , nodeType = rigTools.getElementName( inputNodeName )

	collector = pc.PlusMinusAverage()
	collector.name = '%s%s%s%s_pma' % ( nodeElemName ,
										rigTools.capitalizeFirst( nodeType ) ,
										rigTools.capitalizeFirst( inputNodeAttr ) ,
										nodeSide
										)

	# If current node.attribute already has driver attribute.
	driverNodeAttr = mc.listConnections( nodeAttr , p=True , s=True , d=False )
	if driverNodeAttr :
		driverName , driverAttr = driverNodeAttr[0].split( '.' )
		driverObj = pc.Dag( driverName )

		mc.connectAttr( driverObj.attr( driverAttr ) , collector.last1D() )

	collector.attr( 'output1D' ) >> nodeObj.attr( inputNodeAttr )

	return collector

def ctrlToBsh(
				charName = '' ,
				bshCtrl = '' ,
				bshNode = '' ,
				infoDct = {}
				) :
	
	# Connecting blend shape controller to blend shapes

	# Get side from blend shape controller.
	sides = ( 'LFT' , 'RGT' )
	currSide = ''
	
	for side in sides :
		if side in bshCtrl :
			currSide = side
	
	# Generate name from given controller.
	ctrlName = bshCtrl.replace( '_ctrl' , '' ).replace( charName , '' ).replace( currSide , '' )
	
	for idx in sorted( infoDct.keys() ) :

		# Iterate to every key, control attribute, in infoDct.

		sourceAttr , targetAttr = infoDct[ idx ].popitem()
		
		attrOut = '%s.%s' % ( bshCtrl , sourceAttr )
		if not mc.objExists( attrOut ) :
			mc.addAttr( bshCtrl , ln=sourceAttr , min=-10 , max=10 , dv=0 , k=True )

		outAmper = 1.00/getAttrMax( attrOut )

		if type( targetAttr ) is type(()) :
			
			attrIn = ( '%s.%s' % ( bshNode , targetAttr[0] ) ,
						'%s.%s' % ( bshNode , targetAttr[1] )
						)

			if outAmper == 1 :
				clmp , mul = twoWaysConnect( attrOut = attrOut ,
												attrIn = attrIn ,
												outAmper = outAmper
											)
				
			else :
				clmp , mul , amp = twoWaysConnect( attrOut = attrOut ,
													attrIn = attrIn ,
													outAmper = outAmper
												)
				
				amp.name = '%s%s%sAmp%s_mul' % ( charName ,
													ctrlName ,
													'%s%s'% ( sourceAttr[0].capitalize() ,
																sourceAttr[1:]
															) ,
													currSide
												)
			
			clmp.name = '%s%s%s%s_clmp' % ( charName ,
											ctrlName ,
											'%s%s'% ( sourceAttr[0].capitalize() ,
														sourceAttr[1:]
													) ,
											currSide
											)
			mul.name = '%s%s%s%s_mul' % ( charName ,
											ctrlName ,
											'%s%s'% ( sourceAttr[0].capitalize() ,
														sourceAttr[1:]
													) ,
											currSide
											)
		
		else :
			attrIn = '%s.%s' % ( bshNode , targetAttr )
			mul = rigTools.attrAmper(
										ctrlAttr = attrOut ,
										targetAttr = attrIn ,
										dv = outAmper ,
										ampAttr = ''
									)
			mul.name = '%s%s%sAmp%s_mul' % (
												charName ,
												ctrlName ,
												'%s%s'% ( sourceAttr[0].capitalize() ,
															sourceAttr[1:]
														) ,
												currSide
											)

def connectBlendShape() :
	
	# Connect blended shape objects to blend buffer object.

	bufferObj = 'facialBuffer_bsh'
	bufferName = 'facialBuffer_bsn'
	mc.blendShape( createBlendShapeName() , bufferObj , n=bufferName )

	# Upper lid left
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'upLidDnInbALFT_bsh' ,
						targetBlendShapeName = 'upLidDnLFT_bsh' ,
						weightValue = '0.25'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'upLidDnInbBLFT_bsh' ,
						targetBlendShapeName = 'upLidDnLFT_bsh' ,
						weightValue = '0.5'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'upLidDnInbCLFT_bsh' ,
						targetBlendShapeName = 'upLidDnLFT_bsh' ,
						weightValue = '0.75'
					)
	# Upper lid right
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'upLidDnInbARGT_bsh' ,
						targetBlendShapeName = 'upLidDnRGT_bsh' ,
						weightValue = '0.25'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'upLidDnInbBRGT_bsh' ,
						targetBlendShapeName = 'upLidDnRGT_bsh' ,
						weightValue = '0.5'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'upLidDnInbCRGT_bsh' ,
						targetBlendShapeName = 'upLidDnRGT_bsh' ,
						weightValue = '0.75'
					)
	# Lower lid left
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'loLidUpInbALFT_bsh' ,
						targetBlendShapeName = 'loLidUpLFT_bsh' ,
						weightValue = '0.25'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'loLidUpInbBLFT_bsh' ,
						targetBlendShapeName = 'loLidUpLFT_bsh' ,
						weightValue = '0.5'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'loLidUpInbCLFT_bsh' ,
						targetBlendShapeName = 'loLidUpLFT_bsh' ,
						weightValue = '0.75'
					)
	# Lower lid right
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'loLidUpInbARGT_bsh' ,
						targetBlendShapeName = 'loLidUpRGT_bsh' ,
						weightValue = '0.25'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'loLidUpInbBRGT_bsh' ,
						targetBlendShapeName = 'loLidUpRGT_bsh' ,
						weightValue = '0.5'
					)
	connectInbetween(
						blendShapeObject = 'facialBuffer_bsh' ,
						blendShapeNode = 'facialBuffer_bsn' ,
						inbetweenBlendShape = 'loLidUpInbCRGT_bsh' ,
						targetBlendShapeName = 'loLidUpRGT_bsh' ,
						weightValue = '0.75'
					)

	# Add facial skin.
	cmd = 'blendShape -e  -t facialBuffer_bsh 116 facialSkin_bsh 1 facialBuffer_bsn;'
	mm.eval( cmd )

def dupObjectForBlendShape() :
	
	bshNameDict = {
					'face' : FACE ,
					'mouth' : MOUTH ,
					'nose' : NOSE
					}
	bshSideNameDict = {
						'eyebrow' : EYEBROW_SIDE ,
						'lid' : LID_SIDE ,
						'mouth' : MOUTH_SIDE ,
						'nose' : NOSE_SIDE
						}
	
	sel = mc.ls( sl=True )[0]
	
	bb = mc.exactWorldBoundingBox()
	yOffset = float( abs( bb[1] - bb[4] ) * 1.1 )
	xOffset = float( abs( bb[0] - bb[3] ) * 1.2 )
	
	xVal = 0

	# # Facial skin node
	# mc.select( sel , r=True )
	# duppedNode = mc.duplicate( sel , rr=True )[0]
	# mc.rename( duppedNode , 'facialSkin_bsh' )
	
	# Iterate through each blend shape with side nodes.
	for bshName in bshSideNameDict.keys() :
		
		# Iterate through each sides.
		for side in SIDE :
			
			xVal += xOffset
			
			currBshNode = '%s%s_bsh' % ( bshName , side )
			bshGrp = '%sBsh%s_grp' % ( bshName , side )
			mc.group( em=True , n=bshGrp )
			
			yVal = 0
			
			# Iterate through each blend shapes.
			for bsh in bshSideNameDict[ bshName ] :
				
				currBsh = bsh.replace( '_' , '%s_' % side )
				
				mc.select( sel , r=True )
				duppedNode = mc.duplicate( sel , rr=True )[0]
				mc.rename( duppedNode , currBsh )
				mc.parent( currBsh , bshGrp )
				mc.move( 0 , yVal , 0 , currBsh , r=True )
				
				yVal += yOffset
			
			mc.move( xVal , 0 , 0 , bshGrp , r=True )
	
	# Iterate through each blend shape nodes.
	for bshName in bshNameDict :
		
		xVal += xOffset
		
		currBshNode = '%s_bsh' % bshName
		bshGrp = '%sBsh_grp' % bshName
		mc.group( em=True , n=bshGrp )
		
		yVal = 0
		
		# Iterate through each blend shapes.
		for bsh in bshNameDict[ bshName ] :
			
			currBsh = bsh
			
			mc.select( sel , r=True )
			duppedNode = mc.duplicate( sel , rr=True )[0]
			mc.rename( duppedNode , currBsh )
			mc.parent( currBsh , bshGrp )
			mc.move( 0 , yVal , 0 , currBsh , r=True )
			
			yVal += yOffset
		
		mc.move( xVal , 0 , 0 , bshGrp , r=True )

def connectControl() :
	
	charName = ''
	
	# #- Jaw joint -
	# bshCtrl = 'jawBsh_ctrl'
	# bshNode = 'jawFacialSkin_jnt'

	# infoDct = {
	# 			0 : { 'tx' : 'ry' } ,
	# 			1 : { 'ty' : 'rx' } ,
	# 			2 : { 'bend' : 'rz' } ,
	# 			3 : { 'slideUD' : 'ty' } ,
	# 			4 : { 'slideLR' : 'tx' } ,
	# 			5 : { 'slideIO' : 'tz' } ,
	# 			}
	# ctrlToBsh(
	# 			charName = charName ,
	# 			bshCtrl = bshCtrl ,
	# 			bshNode = bshNode ,
	# 			infoDct = infoDct
	# 		)
	# # Adjust amplifier.
	# mc.setAttr( 'jawBshTxAmp_mul.amp' , 30 )
	# mc.setAttr( 'jawBshTyAmp_mul.amp' , -30 )

	# - Face bsh -
	bshCtrl = 'jawBsh_ctrl'
	bshNode = 'facialBuffer_bsn'

	infoDct = {
				0 : { 'ty' : ( 'faceSquash_bsh' , 'faceStretch_bsh' ) } ,
				}
	ctrlToBsh(
				charName = charName ,
				bshCtrl = bshCtrl ,
				bshNode = bshNode ,
				infoDct = infoDct
			)

	#- Eyelid joint L/R -
	for side in ( 'LFT' , 'RGT' ) :
		
		bshCtrl = 'eyelidBsh%s_ctrl' % side
		bshNode = 'lidFacialSkin%s_jnt' % side
		
		rigTools.doAttrAmp( '%s.%s' % ( bshCtrl , 'tx' ) ,
						'%s.%s' % ( bshNode , 'ry' )
						)
		rigTools.doAttrAmp( '%s.%s' % ( bshCtrl , 'ty' ) ,
							'%s.%s' % ( bshNode , 'rx' )
							)

		if not mc.objExists( '%s.twist' % bshCtrl ) :
			mc.addAttr( bshCtrl , ln='twist' , dv=0 , min=-10 , max=10 , k=True )

		rigTools.doAttrAmp( '%s.%s' % ( bshCtrl , 'twist' ) ,
							'%s.%s' % ( bshNode , 'rz' )
							)
	
	# Adjust amplifier.
	mc.setAttr( 'eyelidBshCtrlTxAmpLFT_mul.amp' , 30 )
	mc.setAttr( 'eyelidBshCtrlTyAmpLFT_mul.amp' , -30 )
	mc.setAttr( 'eyelidBshCtrlTxAmpRGT_mul.amp' , 30 )
	mc.setAttr( 'eyelidBshCtrlTyAmpRGT_mul.amp' , -30 )
	
	#- Mouth -
	bshCtrl = 'mouthBsh_ctrl'
	bshNode = 'facialBuffer_bsn'

	infoDct = {
				0 : { 'tx' : ( 'mouthTurnL_bsh' , 'mouthTurnR_bsh' ) } ,
				1 : { 'ty' : ( 'mouthUp_bsh' , 'mouthDn_bsh' ) } ,
				2 : { 'turn' : ( 'mouthTurnF_bsh' , 'mouthTurnC_bsh' ) } ,
				3 : { 'upperUD' : ( 'upLipUp_bsh' , 'upLipDn_bsh' ) } ,
				4 : { 'lowerUD' : ( 'loLipUp_bsh' , 'loLipDn_bsh' ) } ,
				5 : { 'upperMidUD' : ( 'upLipUpMid_bsh' , 'upLipDnMid_bsh' ) } ,
				6 : { 'lowerMidUD' : ( 'loLipUpMid_bsh' , 'loLipDnMid_bsh' ) } ,
				7 : { 'upperCurl' : ( 'upLipCurlOut_bsh' , 'upLipCurlIn_bsh' ) } ,
				8 : { 'lowerCurl' : ( 'loLipCurlOut_bsh' , 'loLipCurlIn_bsh' ) } ,
				9 : { 'clench' : 'mouthClench_bsh' } ,
				10 : { 'pull' : 'mouthPull_bsh' } ,
				11 : { 'u' : 'mouthUWQ_bsh' }
				}
	
	ctrlToBsh(
				charName = charName ,
				bshCtrl = bshCtrl ,
				bshNode = bshNode ,
				infoDct = infoDct
			)

	#- Nose -
	bshCtrl = 'noseBsh_ctrl'
	bshNode = 'facialBuffer_bsn'

	infoDct = {
					0 : { 'ty' : ( 'noseSquash_bsh' , 'noseStretch_bsh' ) } ,
					1 : { 'leftUp' : ( 'noseUpLFT_bsh' , 'noseDnLFT_bsh' ) } ,
					2 : { 'leftTurn' : ( 'noseTurnFLFT_bsh' , 'noseTurnCLFT_bsh' ) } ,
					3 : { 'rightUp' : ( 'noseUpRGT_bsh' , 'noseDnRGT_bsh' ) } ,
					4 : { 'rightTurn' : ( 'noseTurnFRGT_bsh' , 'noseTurnCRGT_bsh' ) } ,
				}

	ctrlToBsh(
				charName = charName ,
				bshCtrl = bshCtrl ,
				bshNode = bshNode ,
				infoDct = infoDct
			)

	#- Mouth L/R -
	for side in ( 'LFT' , 'RGT' ) :
		
		bshCtrl = '%smouthBsh%s_ctrl' % ( charName , side )
		bshNode = 'facialBuffer_bsn'
		
		infoDct = {
					0 : { 'tx' : ( 'cnrLipOut%s_bsh'%side , 'cnrLipIn%s_bsh'%side ) } ,
					1 : { 'ty' : ( 'cnrLipUp%s_bsh'%side , 'cnrLipDn%s_bsh'%side ) } ,
					2 : { 'upperUD' : ( 'upLipUp%s_bsh'%side , 'upLipDn%s_bsh'%side ) } ,
					3 : { 'lowerUD' : ( 'loLipUp%s_bsh'%side , 'loLipDn%s_bsh'%side ) } ,
					4 : { 'partIO' : ( 'cnrLipPartOut%s_bsh'%side , 'cnrLipPartIn%s_bsh'%side ) } ,
					5 : { 'snear' : 'snear%s_bsh'%side } ,
					6 : { 'cheek' : 'cheek%s_bsh'%side } ,
					7 : { 'puff' : 'puff%s_bsh'%side } ,
					8 : { 'pull' : ( 'cnrLipPuffOut%s_bsh'%side , 'cnrLipPuffIn%s_bsh'%side ) }
					}
		
		ctrlToBsh(
					charName = charName ,
					bshCtrl = bshCtrl ,
					bshNode = bshNode ,
					infoDct = infoDct
				)
	
	#- Eyebrows LFT/RGT
	for side in ('LFT','RGT' ) :
		
		bshCtrl = '%seyebrowBsh%s_ctrl' % ( charName , side )
		bshNode = 'facialBuffer_bsn'
		
		infoDct = {
					0 : { 'tx' : ( 'eyebrowOut%s_bsh'%side , 'eyebrowIn%s_bsh'%side ) } ,
					1 : { 'ty' : ( 'eyebrowUp%s_bsh'%side , 'eyebrowDn%s_bsh'%side ) } ,
					2 : { 'turn' : ( 'eyebrowTurnF%s_bsh'%side , 'eyebrowTurnC%s_bsh'%side ) } ,
					3 : { 'innerUD' : ( 'eyebrowInnerUp%s_bsh'%side , 'eyebrowInnerDn%s_bsh'%side ) } ,
					4 : { 'middleUD' : ( 'eyebrowMidUp%s_bsh'%side , 'eyebrowMidDn%s_bsh'%side ) } ,
					5 : { 'outerUD' : ( 'eyebrowOuterUp%s_bsh'%side , 'eyebrowOuterDn%s_bsh'%side ) }
					}
		
		ctrlToBsh(
					charName = charName ,
					bshCtrl = bshCtrl ,
					bshNode = bshNode ,
					infoDct = infoDct
				)
	
	#- Eyelid LFT/RGT -
	for side in ('LFT','RGT' ) :
		
		bshCtrl = '%seyelidBsh%s_ctrl' % ( charName , side )
		bshNode = 'facialBuffer_bsn'
		
		infoDct = {
					0 : { 'upperUD' : ( 'upLidUp%s_bsh'%side , 'upLidDn%s_bsh'%side ) } ,
					1 : { 'lowerUD' : ( 'loLidUp%s_bsh'%side , 'loLidDn%s_bsh'%side ) } ,
					2 : { 'upperTwist' : ( 'upLidTwistF%s_bsh'%side , 'upLidTwistC%s_bsh'%side ) } ,
					3 : { 'lowerTwist' : ( 'loLidTwistF%s_bsh'%side , 'loLidTwistC%s_bsh'%side ) } ,
					}
		
		ctrlToBsh(
					charName = charName ,
					bshCtrl = bshCtrl ,
					bshNode = bshNode ,
					infoDct = infoDct
				)
	
	# Adding collector
	bshNode = 'facialBuffer_bsn'
	puffLftColl	= addCollector( '%s.puffLFT_bsh' % bshNode )
	puffRgtColl	= addCollector( '%s.puffRGT_bsh' % bshNode )
	cheekLftColl = addCollector( '%s.cheekLFT_bsh' % bshNode )
	cheekRgtColl = addCollector( '%s.cheekRGT_bsh' % bshNode )
	
	# Left corner mouth out
	ctrl = pc.Dag( 'mouthBshLFT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'puffAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTxLFT_clmp.outputR' ,
								puffLftColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	
	# Left corner mouth in
	ctrl = pc.Dag( 'mouthBshLFT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'puffInverseAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTxLFT_clmp.outputG' ,
								puffLftColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = 0.1
	
	# Left corner mouth up
	ctrl = pc.Dag( 'mouthBshLFT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'cheekAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTyLFT_clmp.outputR' ,
								cheekLftColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	
	# Left corner mouth down
	ctrl = pc.Dag( 'mouthBshLFT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'cheekInverseAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTyLFT_clmp.outputG' ,
								cheekLftColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = 0.1
	
	# Right corner mouth out
	ctrl = pc.Dag( 'mouthBshRGT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'puffAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTxRGT_clmp.outputR' ,
								puffRgtColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )

	# Right corner mouth in
	ctrl = pc.Dag( 'mouthBshRGT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'puffInverseAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTxRGT_clmp.outputG' ,
								puffRgtColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = 0.1
	
	# Right corner mouth up
	ctrl = pc.Dag( 'mouthBshRGT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'cheekAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTyRGT_clmp.outputR' ,
								cheekRgtColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	
	# Right corner mouth down
	ctrl = pc.Dag( 'mouthBshRGT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )
	ampAttr = 'cheekInverseAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( 'mouthBshTyRGT_clmp.outputG' ,
								cheekRgtColl.last1D() ,
								)
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = 0.1

	connectAutoLid()

def connectAutoLid() :
	
	lEyeRot = 'lidBshRotLFT_grp'
	rEyeRot = 'lidBshRotRGT_grp'
	
	# Adding collector
	bshNode = 'facialBuffer_bsn'
	upLdDnLeftColl	= addCollector( '%s.upLidDnLFT_bsh' % bshNode )
	loLdUpLeftColl	= addCollector( '%s.loLidUpLFT_bsh' % bshNode )
	upLdDnRightColl	= addCollector( '%s.upLidDnRGT_bsh' % bshNode )
	loLdUpRightColl	= addCollector( '%s.loLidUpRGT_bsh' % bshNode )

	# Clamps
	upperLidDownLeft = mc.createNode( 'clamp' , n='upperLidDownLFT_clmp' )
	lowerLidUpLeft = mc.createNode( 'clamp' , n='lowerLidUpLFT_clmp' )
	upperLidDownRight = mc.createNode( 'clamp' , n='upperLidDownRGT_clmp' )
	lowerLidUpRight = mc.createNode( 'clamp' , n='lowerLidUpRGT_clmp' )

	mc.connectAttr( '%s.rx' % lEyeRot , '%s.inputR' % upperLidDownLeft )
	mc.connectAttr( '%s.rx' % lEyeRot , '%s.inputR' % lowerLidUpLeft )
	mc.connectAttr( '%s.rx' % rEyeRot , '%s.inputR' % upperLidDownRight )
	mc.connectAttr( '%s.rx' % rEyeRot , '%s.inputR' % lowerLidUpRight )

	mc.setAttr( '%s.minR' % upperLidDownLeft , 0 )
	mc.setAttr( '%s.maxR' % upperLidDownLeft , 90 )
	mc.setAttr( '%s.minR' % lowerLidUpLeft , -90 )
	mc.setAttr( '%s.maxR' % lowerLidUpLeft , 0 )

	mc.setAttr( '%s.minR' % upperLidDownRight , 0 )
	mc.setAttr( '%s.maxR' % upperLidDownRight , 90 )
	mc.setAttr( '%s.minR' % lowerLidUpRight , -90 )
	mc.setAttr( '%s.maxR' % lowerLidUpRight , 0 )

	# Left eyelid - controller
	ctrl = pc.Dag( 'eyelidBshLFT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )

	# Left eyelid - Upper lid down attribute
	ampAttr = 'upLidDnAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( '%s.outputR' % upperLidDownLeft ,
								upLdDnLeftColl.last1D() ,
								)
	mul.name = 'upLidDnAmpLFT_mul'
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = 0.01

	# Left eyelid - Lower lid up attribute
	ampAttr = 'loLidUpAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( '%s.outputR' % lowerLidUpLeft ,
								loLdUpLeftColl.last1D() ,
								)
	mul.name = 'loLidUpAmpLFT_mul'
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = -0.01

	# Right eyelid - controller
	ctrl = pc.Dag( 'eyelidBshRGT_ctrl' )
	ctrlShape = pc.Dag( ctrl.shape )

	# Right eyelid - Upper lid down attribute
	ampAttr = 'upLidDnAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( '%s.outputR' % upperLidDownRight ,
								upLdDnRightColl.last1D() ,
								)
	mul.name = 'upLidDnAmpRGT_mul'
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = 0.01

	# Right eyelid - Lower lid up attribute
	ampAttr = 'loLidUpAmp'
	ctrlShape.add( ln=ampAttr , dv=1 , k=True )
	mul = rigTools.doAttrAmp( '%s.outputR' % lowerLidUpRight ,
								loLdUpRightColl.last1D() ,
								)
	mul.name = 'loLidUpAmpRGT_mul'
	ctrlShape.attr( ampAttr ) >> mul.attr( 'i1' )
	ctrlShape.attr( ampAttr ).v = -0.01

	
