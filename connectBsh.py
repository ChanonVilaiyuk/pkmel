import maya.cmds as mc
import pkmel.core as pc
reload( pc )
import pkmel.rigTools as pa
reload( pa )

SIDE = [
		'LFT' ,
		'RGT'
		]

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
					'upLidInUp_bsh' ,
					'upLidMidUp_bsh' ,
					'upLidOutUp_bsh' ,
					'loLidInUp_bsh' ,
					'loLidMidUp_bsh' ,
					'loLidOutUp_bsh'
					]

MOUTH_SIDE 			= [
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
					'cheekUp_bsh' ,
					'cheekLo_bsh'
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

def dupObjectForBlendShape() :

	bshList = {
				'face' : FACE ,
				'mouth' : MOUTH ,
				'nose' : NOSE
				}
	bshSideList = {
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
	for bshName in bshSideList.keys() :

		# Iterate through each sides.
		for side in SIDE :

			xVal += xOffset

			currBshNode = '%s%s_bsh' % ( bshName , side )
			bshGrp = '%sBsh%s_grp' % ( bshName , side )
			mc.group( em=True , n=bshGrp )

			yVal = 0

			# Iterate through each blend shapes.
			for bsh in bshSideList[ bshName ] :

				currBsh = bsh.replace( '_' , '%s_' % side )

				mc.select( sel , r=True )
				duppedNode = mc.duplicate( sel , rr=True )[0]
				mc.rename( duppedNode , currBsh )
				mc.parent( currBsh , bshGrp )
				mc.move( 0 , yVal , 0 , currBsh , r=True )
				
				yVal += yOffset

			mc.move( xVal , 0 , 0 , bshGrp , r=True )

	# Iterate through each blend shape nodes.
	for bshName in bshList :
		
		xVal += xOffset
		
		currBshNode = '%s_bsh' % bshName
		bshGrp = '%sBsh_grp' % bshName
		mc.group( em=True , n=bshGrp )
		
		yVal = 0
		
		# Iterate through each blend shapes.
		for bsh in bshList[ bshName ] :
			
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
		
		amp = pa.attrAmper( ctrlAttr = ctrl.attr(ctrlAttr) ,
							targetAttr = clmp.attr('inputR') ,
							dv = outAmper
							)
		amp.attr('o') >> clmp.attr('inputG')
		
		return clmp , mul , amp
	else :
		ctrl.attr(ctrlAttr) >> clmp.attr('inputR')
		ctrl.attr(ctrlAttr) >> clmp.attr('inputG')
		
		return clmp , mul

def ctrlToOfstCtrl( charName = '' ,
					ctrl = '' ,
					ofstCtrl = '' ,
					infoDct = {}
					) :
	
	# Connecting blend shape controller to offset controller
	
	sides = ( 'LFT' , 'RGT' )
	currSide = ''
	
	for side in sides :
		if side in bshCtrl :
			currSide = side
	
	ctrlName = ctrl.replace( '_ctrl' , '' ).replace( charName , '' )
	
	for each in infoDct.keys() :
		
		attrOut = '%s.%s' % ( ctrl , each )
		attrIn = '%s.%s' % ( ofstCtrl , infoDct[each] )
		mul = pa.attrAmper( ctrlAttr = attrOut ,
							targetAttr = attrIn ,
							dv = 1 ,
							ampAttr = '%sAmp'%each
							)
		
		mul.name = '%s%s%sAmp%s_mul' % ( charName ,
											ctrlName ,
											'%s%s'% ( each[0].capitalize() , each[1:] ) ,
											currSide
										)

def ctrlToBsh( charName = '' ,
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
	
	for each in infoDct.keys() :

		# Iterate to every key, control attribute, in infoDct.
		
		attrOut = '%s.%s' % ( bshCtrl , each )
		outAmper = 1.00/getAttrMax( attrOut )
		
		if type( infoDct[each] ) is type(()) :
			
			attrIn = ( '%s.%s%s_bsh' % ( bshNode , charName , infoDct[each][0] ) ,
						'%s.%s%s_bsh' % ( bshNode , charName , infoDct[each][1] )
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
													'%s%s'% ( each[0].capitalize() , each[1:] ) ,
													currSide
												)
			
			clmp.name = '%s%s%s%s_clmp' % ( charName ,
											ctrlName ,
											'%s%s'% ( each[0].capitalize() ,
														each[1:]
													) ,
											currSide
											)
			mul.name = '%s%s%s%s_mul' % ( charName ,
											ctrlName ,
											'%s%s'% ( each[0].capitalize() ,
														each[1:]
													) ,
											currSide
											)
			
		else :
			attrIn = '%s.%s%s_bsh' % ( bshNode , charName , infoDct[each] )
			mul = pa.attrAmper( ctrlAttr = attrOut ,
								targetAttr = attrIn ,
								dv = outAmper ,
								ampAttr = ''
								)
			mul.name = '%s%s%sAmp%s_mul' % ( charName ,
												ctrlName ,
												'%s%s'% ( each[0].capitalize() ,
															each[1:]
														) ,
												currSide
											)

# charName = ''

# #- Mouth -
# bshCtrl = '%smouthBsh_ctrl' % charName
# bshNode = '%slips_bsh' % charName

# infoDct = { 'tx' : ( 'mouthL' , 'mouthR' ) ,\
# 	'ty' : ( 'mouthUp' , 'mouthDn' ) ,\
# 	'rz' : ( 'mouthTurnC' , 'mouthTurnF' ) ,\
# 	'upperUD' : ( 'upLipsUp' , 'upLipsDn' ) ,\
# 	'lowerUD' : ( 'loLipsUp' , 'loLipsDn' ) ,\
# 	'upperCurl' : ( 'upLipsCurlOut' , 'upLipsCurlIn' ) ,\
# 	'lowerCurl' : ( 'loLipsCurlOut' , 'loLipsCurlIn' ) ,\
# 	'clench' : 'mouthClench' ,\
# 	'pull' : 'mouthPull' ,\
# 	'' : 'mouthU'
# 	}

# ctrlToBsh( charName = charName , bshCtrl = bshCtrl , bshNode = bshNode , infoDct = infoDct )

# #- Mouth L/R -
# for ix in ( 'LFT' , 'RGT' ) :
	
# 	bshCtrl = '%smouthBsh%s_ctrl' % ( charName , ix )
# 	bshNode = '%slips%s_bsh' % ( charName , ix )
	
# 	infoDct = { 'tx' : ( 'crnrMouthOut%s'%ix , 'crnrMouthIn%s'%ix ) ,\
# 	'ty' : ( 'crnrMouthUp%s'%ix , 'crnrMouthDn%s'%ix ) ,\
# 	'upperUD' : ( 'upLipsUp%s'%ix , 'upLipsDn%s'%ix ) ,\
# 	'lowerUD' : ( 'loLipsUp%s'%ix , 'loLipsDn%s'%ix ) ,\
# 	'partIO' : ( 'lipsPartOut%s'%ix , 'lipsPartIn%s'%ix ) ,\
# 	'snear' : 'cheekUpr%s'%ix ,\
# 	'puff' : 'cheekLwr%s'%ix ,\
# 	'pull' : ( 'crnrMouthPuffOut%s'%ix , 'crnrMouthPuffIn%s'%ix )
# 	}
	
# 	ctrlToBsh( charName = charName , bshCtrl = bshCtrl , bshNode = bshNode , infoDct = infoDct )

# #- Eyebrows LFT,RGT,CNTR -
# for ix in ('LFT','RGT', 'CNTR' ) :
	
# 	no = str( ix )
# 	bshCtrl = '%sebBsh%s_ctrl' % ( charName , no )
# 	bshNode = '%seb%s_bsh' % ( charName , no )
	
# 	infoDct = { 'tx' : ( 'ebOut%s'%no , 'ebIn%s'%no ) ,\
# 		'ty' : ( 'ebUp%s'%no , 'ebDn%s'%no ) ,\
# 		'innerUD' : ( 'ebInnerUp%s'%no , 'ebInnerDn%s'%no ) ,\
# 		'middleUD' : ( 'ebMidUp%s'%no , 'ebMidDn%s'%no ) ,\
# 		'outerUD' : ( 'ebOuterUp%s'%no , 'ebOuterDn%s'%no )
# 		}
	
# 	ctrlToBsh( charName = charName , bshCtrl = bshCtrl , bshNode = bshNode , infoDct = infoDct )

# #- Eyes LFT,RGT,CNTR -
# for ix in ('LFT','RGT', 'CNTR' ) :
	
# 	no = str( ix )
# 	bshCtrl = '%seyeBsh%s_ctrl' % ( charName , no )
# 	bshNode = '%slid%s_bsh' % ( charName , no )
	
# 	infoDct = { 'upLidUD' : ( 'upLidUp%s'%no , 'upLidDn%s'%no ) ,\
# 		'loLidUD' : ( 'loLidUp%s'%no , 'loLidDn%s'%no ) ,\
# 		'upLidTW' : ( 'upLidTWF%s'%no , 'upLidTWC%s'%no ) ,\
# 		'loLidTW' : ( 'loLidTWF%s'%no , 'loLidTWC%s'%no )
# 		}
	
# 	ctrlToBsh( charName = charName , bshCtrl = bshCtrl , bshNode = bshNode , infoDct = infoDct )

# for ix in ('LFT','RGT', 'CNTR' ) :
	
# 	no = str( ix )
# 	ctrl = '%seyeBsh%s_ctrl' % ( charName , no )
# 	ofstCtrl = '%seyeOff%s_grp' % ( charName , no )
	
# 	infoDct = { 'tx' : 'ry' ,\
# 		'ty' : 'rx'
# 		}
	
# 	ctrlToOfstCtrl( charName = charName , ctrl = ctrl , ofstCtrl = ofstCtrl , infoDct = infoDct )

# #- Jaw -
# ctrl = '%sjawBsh_ctrl' % charName
# ofstCtrl = '%sjaw1OffLWR_grp' % charName

# infoDct = { 'tx' : 'ry' ,\
# 	'ty' : 'rx' ,\
# 	'rz' : 'rz' ,\
# 	'slideUD' : 'tz' ,\
# 	'slideLR' : 'tx' ,\
# 	'slideIO' : 'ty'
# 	}

# ctrlToOfstCtrl( charName = charName , ctrl = ctrl , ofstCtrl = ofstCtrl , infoDct = infoDct )

# #- Face L/R -
# #for ix in ( 'LFT' , 'RGT' ) :
	
# 	#bshCtrl = '%sface%s_ctrl' % ( charName , ix )
# 	#bshNode = '%slips%s_bsh' % ( charName , ix )
	
# 	#infoDct = { 'snear' : 'cheekUpr%s'%ix ,\
# 	#'cheek' : 'cheekLwr%s'%ix ,\
# 	#'puff' : ( 'crnrMouthPuffOut%s'%ix , 'crnrMouthPuffIn%s'%ix )
# 	#}
	
# 	#ctrlToBsh( charName = charName , bshCtrl = bshCtrl , bshNode = bshNode , infoDct = infoDct )

# #- Tongue -
# ctrl = '%stongueBsh_ctrl' % charName
# ofstCtrl = '%stongue2CtrlOff_grp' % charName

# infoDct = { 'tx' : 'rz' ,\
# 	'ty' : 'rx' ,\
# 	'rz' : 'ry' ,\
# 	'slideUD' : 'tz' ,\
# 	'slideLR' : 'tx' ,\
# 	'slideIO' : 'ty'
# 	}

# ctrlToOfstCtrl( charName = charName , ctrl = ctrl , ofstCtrl = ofstCtrl , infoDct = infoDct )

# for ix in range(3,7) :
	
# 	no = str( ix )
# 	ctrl = '%stongueBsh_ctrl' % charName
# 	ofstCtrl = '%stongue%sCtrlOff_grp' % ( charName , no )
	
# 	infoDct = { 'curlUD' : 'rx' ,\
# 		'curlLR' : 'rz' ,\
# 		'stretch' : 'ty'
# 		}
	
# 	for each in infoDct.keys() :
		
# 		attrOut = '%s.%s' % (ctrl,each)
# 		attrIn = '%s.%s' % (ofstCtrl,infoDct[each])
		
# 		mul = pa.attrAmper( ctrlAttr = attrOut , targetAttr = attrIn , dv = 1 , ampAttr = '%s%s'%(each,str(ix)) )
		
# 		mul.name = '%s%s%s%sAmp_mul' % ( charName , 'tongue' , '%s%s'% ( each[0].capitalize() , each[1:] ) , no )