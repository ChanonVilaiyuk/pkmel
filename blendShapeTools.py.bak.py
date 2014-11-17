import maya.cmds as mc
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
					'loLidUpInbC_bsh'
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
						'lowerTwist' ,
						# 'upperInner' ,
						# 'upperMiddle' ,
						# 'upperOuter' ,
						# 'lowerInner' ,
						# 'lowerMiddle' ,
						# 'lowerOuter'
					]

def createBlendShapeName() :

	# Populate blend shape name regarding WITH_SIDE and WITHOUT_SIDE global name.
	blendShapeNames = []

	for bshSide in WITH_SIDE :
		for bshName in bshSide :
			for side in SIDE :
				if not 'inb' in bshSide :
					blendShapeNames.append( bshName.replace( '_' , '%s_' % side ) )
	
	for bsh in WITHOUT_SIDE :
		for bshName in bsh :
			if not 'inb' in bsh :
				blendShapeNames.append( bshName )
	
	return blendShapeNames

def connectBlendShape() :
	
	# Connect blended shape objects to blend buffer object.
	
	mc.blendShape( createBlendShapeName() , BLEND_BUFFER )

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

def getAttrMax( attr = 'node.attr' ) :
	# Return max value of given attribute
	node = pc.Dag( attr.split('.')[0] )
	attr = attr.split('.')[1]
	
	trnsAttrs = ( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'rx' , 'ry ' , 'rz' )
	
	if attr in trnsAttrs :
		return node.attr('x%sl'%attr).v
	else :
		return mc.attributeQuery( attr , node=node , max=True)[0]

def twoWaysConnect( attrOut = 'ctrl.tx' ,
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
			
			attrIn = ( '%s.%s%s_bsh' % ( bshNode , charName , targetAttr[0] ) ,
						'%s.%s%s_bsh' % ( bshNode , charName , targetAttr[1] )
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
			attrIn = '%s.%s%s_bsh' % ( bshNode , charName , targetAttr )
			mul = rigTools.attrAmper( ctrlAttr = attrOut ,
								targetAttr = attrIn ,
								dv = outAmper ,
								ampAttr = ''
								)
			mul.name = '%s%s%sAmp%s_mul' % ( charName ,
												ctrlName ,
												'%s%s'% ( sourceAttr[0].capitalize() ,
															sourceAttr[1:]
														) ,
												currSide
											)

def connectControl() :
	
	charName = ''
	
	#- Jaw joint -
	bshCtrl = 'jawBsh_ctrl'
	bshNode = 'jawJawOpen_jnt'

	infoDct = {
				0 : { 'tx' : 'ry' } ,
				1 : { 'ty' : 'rx' } ,
				2 : { 'bend' : 'rz' } ,
				3 : { 'slideUD' : 'ty' } ,
				4 : { 'slideIO' : 'tz' } ,
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
		bshNode = 'lidBsh%s_jnt' % side
		
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
	
	#- Mouth -
	bshCtrl = 'mouthBsh_ctrl'
	bshNode = 'facialBuffer_bsn'
	
	infoDct = {
				0 : { 'tx' : ( 'mouthTurnL' , 'mouthTurnR' ) } ,
				1 : { 'ty' : ( 'mouthUp' , 'mouthDn' ) } ,
				2 : { 'turn' : ( 'mouthTurnF' , 'mouthTurnC' ) } ,
				3 : { 'upperUD' : ( 'upLipUp' , 'upLipDn' ) } ,
				4 : { 'lowerUD' : ( 'loLipUp' , 'loLipDn' ) } ,
				5 : { 'upperMidUD' : ( 'upLipUpMid' , 'upLipDnMid' ) } ,
				6 : { 'lowerMidUD' : ( 'loLipUpMid' , 'loLipDnMid' ) } ,
				7 : { 'upperCurl' : ( 'upLipCurlOut' , 'upLipCurlIn' ) } ,
				8 : { 'lowerCurl' : ( 'loLipCurlOut' , 'loLipCurlIn' ) } ,
				9 : { 'clench' : 'mouthClench' } ,
				10 : { 'pull' : 'mouthPull' } ,
				11 : { 'u' : 'mouthUWQ' }
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
					0 : { 'ty' : ( 'noseSquash' , 'noseStretch' ) } ,
					1 : { 'leftUp' : ( 'noseUpLFT' , 'noseDnLFT' ) } ,
					2 : { 'leftTurn' : ( 'noseTurnFLFT' , 'noseTurnCLFT' ) } ,
					3 : { 'rightUp' : ( 'noseUpRGT' , 'noseDnRGT' ) } ,
					4 : { 'rightTurn' : ( 'noseTurnFRGT' , 'noseTurnCRGT' ) } ,
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
					0 : { 'tx' : ( 'cnrLipOut%s'%side , 'cnrLipIn%s'%side ) } ,
					1 : { 'ty' : ( 'cnrLipUp%s'%side , 'cnrLipDn%s'%side ) } ,
					2 : { 'upperUD' : ( 'upLipUp%s'%side , 'upLipDn%s'%side ) } ,
					3 : { 'lowerUD' : ( 'loLipUp%s'%side , 'loLipDn%s'%side ) } ,
					4 : { 'partIO' : ( 'cnrLipPartOut%s'%side , 'cnrLipPartIn%s'%side ) } ,
					5 : { 'snear' : 'snear%s'%side } ,
					5 : { 'cheek' : 'cheek%s'%side } ,
					6 : { 'puff' : 'puff%s'%side } ,
					7 : { 'pull' : ( 'cnrLipPuffOut%s'%side , 'cnrLipPuffIn%s'%side ) }
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
					0 : { 'tx' : ( 'eyebrowOut%s'%side , 'eyebrowIn%s'%side ) } ,
					1 : { 'ty' : ( 'eyebrowUp%s'%side , 'eyebrowDn%s'%side ) } ,
					2 : { 'turn' : ( 'eyebrowTurnF%s'%side , 'eyebrowTurnC%s'%side ) } ,
					3 : { 'innerUD' : ( 'eyebrowInnerUp%s'%side , 'eyebrowInnerDn%s'%side ) } ,
					4 : { 'middleUD' : ( 'eyebrowMidUp%s'%side , 'eyebrowMidDn%s'%side ) } ,
					5 : { 'outerUD' : ( 'eyebrowOuterUp%s'%side , 'eyebrowOuterDn%s'%side ) }
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
					0 : { 'upperUD' : ( 'upLidUp%s'%side , 'upLidDn%s'%side ) } ,
					1 : { 'lowerUD' : ( 'loLidUp%s'%side , 'loLidDn%s'%side ) } ,
					2 : { 'upperTwist' : ( 'upLidTwistF%s'%side , 'upLidTwistC%s'%side ) } ,
					3 : { 'lowerTwist' : ( 'loLidTwistF%s'%side , 'loLidTwistC%s'%side ) } ,
					}
		
		ctrlToBsh(
					charName = charName ,
					bshCtrl = bshCtrl ,
					bshNode = bshNode ,
					infoDct = infoDct
				)

	#- Add automation -
	# 1. mouth left/right tx to puff
	# 2. mouth left/right ty to cheek
	# 3. jaw ty to puff

	# mouthBshTyLFT_mul

	# Adding collector
	bshNode = 'facialBuffer_bsn'
	puffLftColl	= addCollector( '%s.puffLFT_bsh' % bshNode )
	puffRgtColl	= addCollector( '%s.puffRGT_bsh' % bshNode )
	cheekLftColl	= addCollector( '%s.cheekLFT_bsh' % bshNode )
	cheekRgtColl	= addCollector( '%s.cheekRGT_bsh' % bshNode )

	rigTools.doAttrAmp( 'mouthBshLFT_ctrl.tx' ,
						puffLftColl.last1D()
						)
	rigTools.doAttrAmp( 'mouthBshRGT_ctrl.tx' ,
						puffRgtColl.last1D()
						)
	rigTools.doAttrAmp( 'mouthBshLFT_ctrl.ty' ,
						cheekLftColl.last1D()
						)
	rigTools.doAttrAmp( 'mouthBshRGT_ctrl.ty' ,
						cheekRgtColl.last1D()
						)