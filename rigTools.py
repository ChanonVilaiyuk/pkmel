import maya.cmds as mc
import maya.mel as mm

import os
import shutil
import sys
import re

import pkmel.core as pc
reload( pc )

def quickOrient( aimVec=[0,1,0] , upVec=[-1,0,0] ) :
	
	sels = mc.ls( sl=True )
	targ = sels[0]
	src = sels[1]
	
	chldrn = mc.listRelatives( src , s=False , c=True , p=False )

	if chldrn :
		for chld in chldrn :
			mc.parent( chld , w=True )
	
	mc.select( src , r=True )
	tmpUp = mc.duplicate( src , rr=True )[0]
	tmpUpChldrn = mc.listRelatives( tmpUp , f=True )
	
	if tmpUpChldrn :
		mc.delete( tmpUpChldrn )
	
	aim = aimVec
	wu = upVec
	u = upVec
	wuo = tmpUp
	wut = 'objectrotation'
	
	aimCon = mc.aimConstraint( targ , src , aim=aim , wu=wu , wuo=wuo , wut=wut , u=u )
	mc.delete( aimCon )
	mc.delete( tmpUp )
	mc.makeIdentity( src , a=True , r=True , t=True , s=True , jo=False )
	
	if chldrn :
		for chld in chldrn :
			mc.parent( chld , src )
	
	mc.select( src , r=True )

def createBeforeBlendShape() :

	# Create blend shape node with 'before' option.
	# Basically, this is used for connectting animated geo to rendered geo.
	# Select source geo and target geo then run the procedure.

	sels = mc.ls( sl=True )

	localName = sels[-1].split( ':' )[-1]
	tmpNameList = localName.split( '_' )

	if len( tmpNameList ) > 1 :
		tmpNameList[-1] = 'bsn'
	else :
		tmpNameList.append( 'bsn' )

	bsn = '_'.join( tmpNameList )
	mc.blendShape( before=True , origin='world' , n=bsn )
	mc.setAttr( '%s.w[0]' % bsn , 1 )

def selectFacialController() :
	
	ctrls = [
				'jawBsh_ctrl' ,
				'mouthBsh_ctrl' ,
				'mouthBshLFT_ctrl' ,
				'mouthBshRGT_ctrl' ,
				'noseBsh_ctrl' ,
				'eyelidBshLFT_ctrl' ,
				'eyelidBshRGT_ctrl' ,
				'eyebrowBshLFT_ctrl' ,
				'eyebrowBshRGT_ctrl' ,
				'facialBsh_ctrl' ,
				'jaw1LWR_ctrl' ,
				'jaw2LWR_ctrl' ,
				'lowerTeeth_ctrl' ,
				'upperTeeth_ctrl' ,
				'tongue1Fk_ctrl' ,
				'tongue2Fk_ctrl' ,
				'tongue3Fk_ctrl' ,
				'tongue4Fk_ctrl' ,
				'tongue5Fk_ctrl'
			]
	
	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		currNs = sel.replace( sel.split( ':' )[-1] , '' )
		
		for ctrl in ctrls :
			
			currCtrl = '%s%s' % ( currNs , ctrl )
			gmbl = '%s%s' % ( currNs , addElementToName( ctrl , 'Gmbl' ) )
			con = '%s%s' % ( currNs , addElementToName( ctrl , 'Con' ) )
			
			for each in ( currCtrl , gmbl , con ) :
				
				if mc.objExists( each ) :

					mc.select( each , add=True )

def toLambert() :

	sels = mc.ls( sl=True )

	for sel in sels :

		lambert = mc.shadingNode( 'lambert' , asShader=True )
		sg = mc.listConnections( '%s.outColor' % sel )[0]
		fileNode = ''

		if mc.objExists( '%s.color' % sel ) :
			
			fileNodes = mc.listConnections( '%s.color' % sel )
			
			if fileNodes :
				
				fileNode = fileNodes[0]
		
		if fileNode :
			
			mc.connectAttr(
								'%s.outColor' % fileNode ,
								'%s.color' % lambert ,
								f=True
							)

		mc.connectAttr(
								'%s.outColor' % lambert ,
								'%s.surfaceShader' % sg ,
								f=True
							)

		mc.delete( sel )
		mc.rename( lambert , sel )

def getReferencedPathFromMa( scenePath ) :

	maFile = open( os.path.normpath( scenePath ) , 'r' )

	assetPathList = []
	
	for line in maFile :
		
		if line.startswith( 'requires' ) :

			break
		
		if line.startswith( r'//' ) :
			
			continue
		
		result = re.search( r'[a-z|A-Z|/|\\]\S+\.m[a|b]' , line )
		
		if result :
			
			# assetPath = os.path.normpath( line.split( ' ' )[-1].replace( ';' , '' ).replace( '"' , '' ) )
			assetPath = os.path.normpath( result.group( 0 ) )
			if not assetPath in assetPathList :
				assetPathList.append( assetPath )
	
	return assetPathList

def getTextureFromMa( scenePath ) :

	texturePaths = []

	sceneFile = open( os.path.normpath( scenePath ) , 'r' )

	for line in sceneFile :

		if 'setAttr ".ftn" ' in line :

			texturePath = os.path.normpath( line.split( '"string" ' )[-1].split( ';' )[0].replace( '"' , '' ) )

			if not texturePath in texturePaths :
				texturePaths.append( texturePath )

	return texturePaths

def copyToReplacedPath( filePath , searchFor , replaceWith ) :

	folderPath , fileName = os.path.split( os.path.normpath( filePath ) )
	targetFolder = folderPath.replace( searchFor , replaceWith )

	if not os.path.exists( targetFolder ) :
		os.makedirs( targetFolder )

	print 'Copying %s to %s' % ( filePath , targetFolder )
	if os.path.exists( filePath ) :
		shutil.copy2( os.path.normpath( filePath ) , targetFolder )
	else :
		'%s does not exist.' % filePath

def scenePuller( scenePath , searchFor , replaceWith ) :

	assetPaths = getReferencedPathFromMa( scenePath )
	
	texturePaths = []

	for assetPath in assetPaths :
		
		for texturePath in getTextureFromMa( assetPath ) :
			
			if not texturePath in texturePaths :

				texturePaths.append( texturePath )
	
	sceneFolder , sceneName = os.path.split( os.path.normpath( scenePath ) )
	targetSceneFolder = sceneFolder.replace( searchFor , replaceWith )
	
	if not os.path.exists( targetSceneFolder ) :
		os.makedirs( targetSceneFolder )

	print 'Copying %s to %s' % ( scenePath , targetSceneFolder )
	shutil.copy2( os.path.normpath( scenePath ) , targetSceneFolder )
	
	for assetPath in assetPaths :

		copyToReplacedPath( assetPath , searchFor , replaceWith )

	for texturePath in texturePaths :

		copyToReplacedPath( texturePath , searchFor , replaceWith )

def pullSceneBack( scenePath , dropboxRoot , projectRoot ) :

	assetPaths = getReferencedPathFromMa( scenePath )

	texturePaths = []

	for assetPath in assetPaths :
		
		for texturePath in getTextureFromMa( assetPath ) :
			
			if not texturePath in texturePaths :

				texturePaths.append( texturePath )

	sceneFolder , sceneName = os.path.split( os.path.normpath( scenePath ) )
	projectSceneFolder = sceneFolder.replace( dropboxRoot , projectRoot )

	print 'Copying %s to %s' % ( scenePath , projectSceneFolder )
	shutil.copy2( os.path.normpath( scenePath ) , projectSceneFolder )
	
	for assetPath in assetPaths :
		dropboxAssetPath = assetPath.replace( projectRoot , dropboxRoot )
		copyToReplacedPath( dropboxAssetPath , dropboxRoot , projectRoot )
	
	for texturePath in texturePaths :
		dropboxTexturePath = texturePath.replace( projectRoot , dropboxRoot )
		copyToReplacedPath( dropboxTexturePath , dropboxRoot , projectRoot )

def removeNonRelatedTexture( textureFolderPath='' ) :

	cleanedPath = os.path.normpath( textureFolderPath )
	
	txtFiles = []
	for txtFile in os.listdir( cleanedPath ) :

		txtFilePath = os.path.join(
										cleanedPath ,
										txtFile
									)

		if os.path.isfile( txtFilePath ) :
			txtFiles.append( txtFilePath )

	sceneTxts = []
	for fileNode in mc.ls( type='file' ) :
		sceneTxts.append( os.path.normpath( mc.getAttr( '%s.fileTextureName' % fileNode ) ) )

	for txtFile in txtFiles :

		if not txtFile in sceneTxts :

			print 'Removing %s' % txtFile
			os.remove( txtFile )

	return True

def removeShadingNode() :

	types = (
				'file' ,
				'place2dTexture' ,
				'gammaCorrect' ,
				'sampleInfo' ,
				'renderLayer' ,
				'VRayLightMtl' ,
				'ramp' ,
				'VRayPlaceEnvTex' ,
				'VRayMtl' ,
				'VRayBlendMtl'
			)
	
	for type_ in types :
		
		nodes = mc.ls( type=type_ )
		
		if nodes :
			
			for node in nodes :
				try :
					mc.delete( node )
				except :
					pass

def createCleanedCamera() :

	# Select camera then run the script.
	# Script will duplicate selected camera.

	cleanedCam = 'cleanedNuke_cam'

	if mc.objExists( cleanedCam ) :
		mc.delete( cleanedCam )

	selectedCam = ''
	selectedCamShp = ''

	selected = mc.ls( sl=True , l=True )[0]
	
	if mc.nodeType( selected ) == 'camera' :
		selectedCamShp = selected
		selectedCam = mc.listRelatives( selected , p=True , f=True )[0]
	else :
		selectedCam = selected
		selectedCamShp = mc.listRelatives( selected , type='shape' , f=True )[0]

	mc.select( selectedCam )
	mc.duplicate( selectedCam , rr=True , n=cleanedCam )
	mc.parent( w=True )

	duppedCamShp = mc.listRelatives( cleanedCam , type='shape' , f=True )[0]

	for attr in ( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' ) :
		mc.setAttr( '%s.%s' % ( cleanedCam , attr ) , l=False )

	minTime = mc.playbackOptions( q=True , min=True )
	maxTime = mc.playbackOptions( q=True , max=True )

	animCurves = mc.listConnections( selectedCamShp , s=True , type='animCurve' )
	attrs = []
	if animCurves :
		for animCurve in animCurves :
			
			attr = mc.listConnections( animCurve , d=True , p=True )[0].split( '.' )[1]
			
			mc.copyKey( selectedCamShp , attribute=attr )
			mc.pasteKey( duppedCamShp , attribute=attr )
	
	parCons = mc.parentConstraint( selectedCam , cleanedCam )
	mc.bakeResults( cleanedCam , simulation=True , t=( minTime , maxTime ) )
	mc.delete( parCons )

def renameSelectedFileNode() :
	
	sels = mc.ls( sl=True )[0]
	name = ''
	type_ = ''

	nameResult = mc.promptDialog(
									title='File Node Name',
									message='Enter Name:',
									button=['OK', 'Cancel'],
									defaultButton='OK',
									cancelButton='Cancel',
									dismissString='Cancel'
								)
	
	if nameResult == 'OK':
		name = mc.promptDialog( query=True , text=True )

	typeResult = mc.promptDialog(
									title='File Node Type',
									message='Enter Type:',
									button=['OK', 'Cancel'],
									defaultButton='OK',
									cancelButton='Cancel',
									dismissString='Cancel'
								)
	
	if typeResult == 'OK':
		type_ = mc.promptDialog( query=True , text=True )
	
	if name and type_ :
		renameFileAndTextureNode( sels , name , type_ )

	p2ds = mc.listConnections( '%s.uvCoord' % mc.ls( sl=True )[0] , s=True , d=False )
	
	if p2ds :

		mc.select( p2ds , r=True )
		renameSelectedPlace2dTexture()

def isKeywordInLine( kws=() , line='' ) :
	
	result = False
	for kw in kws :
		if kw in line :
			result = True
	
	return result

def removeUnusedNodeFromMaFile( filePath='' ) :
	
	kws = (
				'uiConfigurationScriptNode' ,
				'delight' ,
				'mentalray' ,
				'miDefaultOptions' ,
				'defaultRenderLayer' ,
				'renderLayerManager' ,
				'modelPanel4ViewSelectedSet' ,
				'lockNode'
			)
	
	filePath = os.path.normpath( filePath )
	folderPath , fileNameExt = os.path.split( filePath )
	
	tmpFilePath = '%s.tmp' % filePath
	
	print 'Fixing %s' % filePath
	
	fid = open( filePath , 'r' )
	
	tmpid = open( tmpFilePath , 'w' )
	foundKw = False
	write = True
	
	for line in fid :
		
		if isKeywordInLine( kws , line ) :
			foundKw = True
			write = False
		
		if foundKw and line.startswith( '	' ) :
			write = False
		
		if foundKw and not line.startswith( '	' ) and not isKeywordInLine( kws , line ) :
			foundKw = False
			write = True
		
		if write :
			tmpid.write( line )
	
	fid.close()
	tmpid.close()
	
	bakFilePath = '%s.bak' % filePath
	
	shutil.copy2( filePath , bakFilePath )
	shutil.copy2( tmpFilePath , filePath )
	os.remove( tmpFilePath )
	os.remove( bakFilePath )
	
	print 'Fixing %s done.' % filePath

def renameSelectedPlace2dTexture() :

	for each in mc.ls( sl=True ) :

		targets = mc.listConnections( each , d=True , s=False )

		if targets :

			nodeName , nodeSide , nodeType = getElementName( targets[0] )

			mc.rename( each , '%s%s%s_place2dTexture' % ( nodeName , capitalizeFirst( nodeType ) , nodeSide ) )

def renameMatInfo() :

	exceptions = [ 'initialMaterialInfo' ]

	for each in mc.ls( type='materialInfo' ) :

		sg = mc.listConnections( '%s.shadingGroup' % each )
		if sg :
			if not each in exceptions :
				mc.rename( each , '%s_materialInfo' % sg[0] )

def changeTexturePath( textureFolder='' ) :

	cleanedPath = os.path.normpath( textureFolder )
	
	for each in mc.ls( type='file' ) :
		
		oldFolderPath , oldFileName = os.path.split( mc.getAttr( '%s.fileTextureName' % each ) )
		localTexturePath = os.path.join(
											cleanedPath ,
											oldFileName
										)
		
		mc.setAttr( '%s.fileTextureName' % each , localTexturePath , type='string' )

def doAddOriGrp() :

	sels = mc.ls( sl=True )

	for sel in sels :
		
		parent = mc.listRelatives( sel , p=True )[0]
		nodeName , nodeSide , nodeType = getElementName( sel )
		
		grp = pc.Null()
		grp.name = '%s%sOri%s_grp' % ( nodeName , capitalizeFirst( nodeType ) , nodeSide )
		grp.snap( parent )
		grp.parent( parent )
		mc.parent( sel , grp )

def doAddElem( elm='' ) :

	for each in sorted( mc.ls( sl=True , l=True ) , reverse=True ) :
		name = each.split( '|' )[-1]
		mc.rename( each , addElementToName( name , elm ) )

def groupOnCurve( crv='' ) :

	crvObj = pc.Dag( crv )
	crvShpObj = pc.Dag( crvObj.shape )

	grp = pc.Null()
	poci = pc.PointOnCurveInfo()

	grp.add( ln='parameter' , k=True , min=0 , max=1 )
	crvShpObj.attr('worldSpace[0]') >> poci.attr('ic')
	poci.attr( 'turnOnPercentage' ).v = True
	poci.attr('position') >> grp.attr('t')
	grp.attr( 'parameter' ) >> poci.attr( 'parameter' )
	grp.lockHideAttrs( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' , 'v' )

	return grp , poci

def connectProxySkinJoint() :

	# Connect proxy skin joint to skin joint.

	proxyJnts = mc.ls( '*:*ProxySkin*_jnt' )

	for proxyJnt in proxyJnts :

		proxyNs , proxyName = proxyJnt.split( ':' )
		skinJntName = proxyName.replace( 'ProxySkin' , '' )
		
		skinJnts = mc.ls( '*:%s' % skinJntName )

		if skinJnts :

			skinJnt = skinJnts[0]
			try :
				mc.parentConstraint( skinJnt , proxyJnt , mo=True )
				mc.scaleConstraint( skinJnt , proxyJnt , mo=True )
			except :
				print proxyJnt
		else :
			print 'Cannot find skin joint for %s' % proxyJnt

def selectSkinJoint() :

	unbindedJoints = [u'rootProxySkin_jnt', u'pelvisProxySkin_jnt', u'upLegProxySkinLFT_jnt', u'lowLegProxySkinLFT_jnt', u'upLegProxySkinRGT_jnt', u'lowLegProxySkinRGT_jnt', u'spine1ProxySkin_jnt', u'spine2ProxySkin_jnt', u'spine3ProxySkin_jnt', u'spine4ProxySkin_jnt', u'spine5ProxySkin_jnt', u'neck1ProxySkin_jnt', u'neck2ProxySkin_jnt', u'clav1ProxySkinLFT_jnt', u'upArmProxySkinLFT_jnt', u'forearmProxySkinLFT_jnt', u'wristProxySkinLFT_jnt', u'clav1ProxySkinRGT_jnt', u'clav2ProxySkinRGT_jnt', u'upArmProxySkinRGT_jnt', u'clav2ProxySkinLFT_jnt', u'forearmProxySkinRGT_jnt', u'wristProxySkinRGT_jnt']
	mc.select( clear=True )
	for jnt in mc.ls( type='joint' ) :
		if not jnt in unbindedJoints :
			mc.select( jnt , add=True )

def removeAllShader() :

	exceptions = ( 'initialShadingGroup' , 'initialParticleSE' )

	for each in mc.ls( type='shadingEngine' ) :
		if not each in exceptions :

			shaders = mc.listConnections( '%s.surfaceShader' % each )
			if shaders :
				try :
					mc.delete( shaders[0] )
					print '%s has been deleted.' % shaders[0]
				except :
					print '%s cannot be deleted.' % shaders[0]
			try :
				mc.delete( each )
				print '%s has been deleted.' % each
			except :
				print '%s cannot be deleted.' % each

def uvOffsetor() :

	sels = mc.ls( sl=True )

	for ix in range( len( sels ) ) :

		obj = sels[ix]
		

		vtxNo = mc.polyEvaluate( obj , v=True )

		mc.select( '%s.vtx[0:%d]' % ( obj , vtxNo ) , r=True )

		cmd = 'PolySelectConvert 4;'
		mm.eval( cmd )

		mc.polyEditUV( u=ix )

	mc.select( sels )

def importProxySkinJoint() :
	
	modulePath , moduleFile = os.path.split( pc.__file__ )
	proxySkinJointPath = os.path.join(
											modulePath ,
											'proxySkinJoint_1.ma'
										)
	mc.file( proxySkinJointPath , i=True )

def attachSelectedProxySkinJointToSkinJoint( namespace='' ) :
	'''
	Select proxy skin joints then run script.
	'''
	for each in mc.ls( sl=True ) :
		mc.delete(
					mc.parentConstraint(
											'%s:%s' % (
															namespace ,
															each.replace( 'ProxySkin' , '' )
														) ,
											each
										)
				)
		mc.makeIdentity( each , a=True , r=True , t=True , s=True )

def detachSelectedEdge() :

	objs = []

	for sel in mc.ls( sl=True , fl=True ) :

		obj = sel.split( '.' )[0]

		if not obj in objs :
			objs.append( obj )
	
	mm.eval( 'DetachComponent' )
	mc.select( objs , r=True )
	mm.eval( 'SeparatePolygon' )
	mc.delete( ch=True )

def selectBakeController() :
	sels = mc.ls( sl=True )
	nss = []
	ctrls = []

	for sel in sels :
		currNs = ''
		try :
			currNs = sel.replace( sel.split( ':' )[-1] , '' )
		except :
			pass

		if not currNs in nss :
			nss.append( currNs )

	for ns in nss :
		
		ctrlFilter = '%s*_ctrl' % ns
		currCtrls = mc.ls( ctrlFilter )

		for ctrl in currCtrls :
			
			ctrls.append( ctrl )

	mc.select( ctrls , r=True )


def selectNoPlacement() :

	selectAllController( [ 'master_ctrl' , 'placement_ctrl' , 'offset_ctrl' ] )

def selectAllController( exceptions=[] ) :

	sels = mc.ls( sl=True )
	nss = []
	ctrls = []

	for sel in sels :
		currNs = ''
		try :
			currNs = sel.replace( sel.split( ':' )[-1] , '' )
		except :
			pass

		if not currNs in nss :
			nss.append( currNs )

	for ns in nss :
		
		ctrlFilter = '%s*_ctrl' % ns
		currCtrls = mc.ls( ctrlFilter )

		for ctrl in currCtrls :

			canAppend = True

			connections = mc.listConnections( ctrl , s=True , d=False )
			if connections :
				for connection in connections :
					if 'Constraint' in mc.nodeType( connection ) :
						canAppend = False

			if exceptions :
				for exception in exceptions :
					if exception in ctrl :
						canAppend = False

			if canAppend :
				ctrls.append( ctrl )

	mc.select( ctrls , r=True )

def importRigElement() :
	# Import all rig element.
	# Find children of 'addRig_grp' node
	# and parent to the constraint source.
	
	# Import all referenced files
	importAllReferences()
	
	addRig = 'delete_grp'
	
	if mc.objExists( addRig ) :
		
		for each in mc.listRelatives( addRig , type='transform' ) :
			
			parent = findConstraintSource( each )
			print each , parent
			try :
				mc.parent( each , parent )
			except :
				pass
		
		mc.delete( addRig )

def findConstraintSource( node='' ) :

	# Find the constraint source of given node.

	constrs = []

	# parConstrs = mc.listConnections( node , s=True , type='parentConstraint' )
	# scaConstrs = mc.listConnections( node , s=True , type='scaleConstraint' )
	
	parConstrs = mc.listConnections( '%s.tx' % node , s=True , type='parentConstraint' )
	scaConstrs = mc.listConnections( '%s.sx' % node , s=True , type='scaleConstraint' )
	
	if parConstrs :
		for each in parConstrs :
			constrs.append( each )
	
	if scaConstrs :
		for each in scaConstrs :
			constrs.append( each )
	
	if constrs :
		parent = mc.listConnections( '%s.target[0].targetTranslate' % constrs[0] , s=True )[0]
		mc.delete( constrs )
		return parent
	else :
		return None

def importAllReferences() :
	
	# Import all reference.
	
	rfns = mc.ls( type='reference' )

	if rfns :
		
		for rfn in rfns :
			
			if not rfn == 'sharedReferenceNode' :
				
				try :
					fn = mc.referenceQuery( rfn , filename=True )
					
					mc.file( fn , importReference=True )
					
					print '%s has been imported.' % rfn
				
				except RuntimeError :
					
					print '%s is not connected to reference file.' % rfn

def renameSelectedShadingGroup() :

	for each in mc.ls( sl=True ) :
		
		mat = mc.listConnections( '%s.surfaceShader' % each ,
									s=True ,
									d=False
								)[0]

		currName , currSide , currType = getElementName( mat )
		sgName = '%s%s%s%s_sg' % ( currName ,
										currType[0].capitalize() ,
										currType[1:] ,
										currSide
									)
	
	mc.rename( each , sgName )

def addElementToName( objName='' , element='' ) :

	nodeName , nodeSide , nodeType = getElementName( objName )

	return '%s%s%s_%s' % ( nodeName , capitalizeFirst( element ) , nodeSide , nodeType )

def getElementName( objName='' ) :

	nodeName = ''
	nodeSide = ''
	nodeType = ''

	sides = ( 'LFT' , 'RGT' )
	for side in sides :
		if side in objName :
			nodeSide = side
	try :
		nodeName , nodeType = objName.split( '%s_' % nodeSide )
	except ValueError :
		nodeName = objName
		nodeType = ''

	return nodeName , nodeSide , nodeType

def capitalizeFirst( inputName='' ) :
	
	kwDict = { 'LFT_' : 'Left' ,
				'RGT_' : 'Right'
				}
	
	for key in kwDict.keys() :
		if key in inputName :
			inputName = inputName.replace( key , kwDict[key] )
	
	return '%s%s' % ( inputName[0].capitalize() , inputName[1:] )

def doAttrOffsetValue( sourceObjAttr='' , targetObjAttr='' , offsetValue=1 ) :
	
	targetObj , targetAttr = targetObjAttr.split( '.' )
	targetName , targetSide , targetType = getElementName( targetObj )
	
	add = attrOffsetValue( sourceObjAttr , targetObjAttr , offsetValue )
	
	add.name = '%s%s%sOffset%s_add' % (
										targetName ,
										capitalizeFirst( targetType ) ,
										capitalizeFirst( targetAttr ) ,
										targetSide
									)
	
	return add

def doAttrAmp( sourceObjAttr='' , targetObjAttr='' , ampAttr='' ) :
	
	# sourceObj , sourceAttr = sourceObjAttr.split( '.' )
	# sourceName , sourceSide , sourceType = getElementName( sourceObj )

	targetObj , targetAttr = targetObjAttr.split( '.' )
	targetName , targetSide , targetType = getElementName( targetObj )
	
	mul = attrAmper(
						ctrlAttr = sourceObjAttr ,
						targetAttr = targetObjAttr ,
						dv = 1 ,
						ampAttr = ampAttr
					)
	
	mul.name = '%s%s%sAmp%s_mul' % (
										targetName ,
										capitalizeFirst( targetType ) ,
										capitalizeFirst( targetAttr ) ,
										targetSide
									)
	
	return mul

def doAddParentLocWor() :
	
	ctrl , loc , wor , zro = mc.ls(sl=True)
	( locGrp ,
		worGrp ,
		worParcon ,
		zroParcon ,
		rev ) = parentLocalWorldCtrl( ctrl , loc , wor , zro )
	
	currName = ''
	currSide = '_'
	
	for side in ( 'LFT' , 'RGT' ) :
		if side in ctrl :
			currSide = '%s_' % side
	
	currName = ctrl.split( currSide )[0]
	locGrp.name = '%sCtrlLoc%sgrp' % ( currName , currSide )
	worGrp.name = '%sCtrlWor%sgrp' % ( currName , currSide )
	worParcon.name = '%s_parentConstraint1' % worGrp
	rev.name = '%sCtrlLocWor%srev' % ( currName , currSide )

def doAddOrientLocWor() :
	
	ctrl , loc , wor , zro = mc.ls(sl=True)
	( locGrp ,
		worGrp ,
		worParcon ,
		zroParcon ,
		rev ) = orientLocalWorldCtrl( ctrl , loc , wor , zro )
	
	currName = ''
	currSide = '_'
	
	for side in ( 'LFT' , 'RGT' ) :
		if side in ctrl :
			currSide = '%s_' % side
	
	currName = ctrl.split( currSide )[0]
	locGrp.name = '%sCtrlLoc%sgrp' % ( currName , currSide )
	worGrp.name = '%sCtrlWor%sgrp' % ( currName , currSide )
	worParcon.name = '%s_orientConstraint1' % worGrp
	rev.name = '%sCtrlLocWor%srev' % ( currName , currSide )

def doAddCtrl( shape='circle' ) :
	
	jnts = mc.ls( sl=True , l=True )
	ctrls = []
	gmbls = []
	zgrps = []
	
	for jnt in jnts :
		jntName = ''
		if ':' in jnt :
			jntName = jnt.split( ':' )[-1].split( '|' )[-1]
		else :
			jntName = jnt.split( '|' )[-1]
		
		currName = ''
		currSide = '_'
		
		sides = ( 'LFT' , 'RGT' )
		for side in sides :
			if side in jntName :
				currSide = '%s_' % side
		
		currName = jntName.split( currSide )[0]
		
		ctrl = pc.Control( shape )
		ctrl.lockHideAttrs( 'v' )
		ctrl.color = 'blue'
		ctrl.name = '%s%sctrl' % ( currName , currSide )
		
		mc.select( ctrl , r=True )
		zgrp = doZeroGroup()[0]
		
		mc.select( ctrl , r=True )
		gmbl = doAddGimbal()[0]

		conCtrl = pc.addConCtrl( ctrl )
		conCtrl.name = '%sCon%sctrl' % ( currName , currSide )
		
		zgrp.snap( jnt )
		mc.parentConstraint( gmbl , jnt )
		mc.scaleConstraint( gmbl , jnt )

		ctrls.append( ctrl )
		gmbls.append( gmbl )
		zgrps.append( zgrp )

	return ctrls , gmbls , zgrps

def doAddGimbal() :
	ctrls = mc.ls( sl=True )
	gmbls = []
	
	for ctrl in ctrls :
		
		gmbl = pc.addGimbal( ctrl )
		
		currName = ''
		currSide = '_'
		
		sides = ( 'LFT' , 'RGT' )
		for side in sides :
			if side in ctrl :
				currSide = '%s_' % side
		
		currName = ctrl.split( currSide )[0]
		
		gmbl.name = '%sGmbl%sctrl' % ( currName , currSide )
		gmbls.append( gmbl )
		
	return gmbls

def hideControl() :
	# Scale selected controller to zero and remove all keyable attributes.
	sels = mc.ls( sl=True )
	for each in sels :
		
		ctrl = pc.Dag( each )
		ctrl.scaleShape( 0 )
		
		for attr in mc.listAttr( ctrl , k=True ) :
			
			ctrl.attr( attr ).lockHide()
		
		shp = pc.Dag( ctrl.shape )
		
		if mc.objExists( shp.attr( 'gimbalControl' ) ) :
			
			gmbl = pc.Dag( mc.listConnections( shp.attr( 'gimbalControl' ) , d=True , s=False )[0] )
			gmbl.scaleShape( 0 )
			for attr in mc.listAttr( gmbl , k=True ) :
				print gmbl , attr
				gmbl.attr( attr ).lockHide()
	
	mc.select( sels , r=True )

def skinLattice() :
	
	# Bind selected lattice to the selected joints
	# Select a lattice then joints
	
	sels = mc.ls( sl=True )
	lat = sels[-1]
	jnts = sels[:-1]
	
	# Bind lattice to joints
	skc = mc.skinCluster( jnts , lat , dr = 7 , mi = 2 , tsb=True )[0]
	jntNo = len( jnts )
	
	for ix in range( 0 , jntNo ) :
		# Edit the skin values
		currId = jntNo - ix - 1
		
		vtcsA = '%s.pt[0:1][%s][0]' % ( lat , currId )
		vtcsB = '%s.pt[0:1][%s][1]' % ( lat , currId )
		
		mc.skinPercent( skc , vtcsA , tv = [ jnts[ix] , 1 ] )
		mc.skinPercent( skc , vtcsB , tv = [ jnts[ix] , 1 ] )

def renameLattice( name='' ) :
	
	# Rename the lattice, lattice base, ffd and ffd set
	# Select lattice node the run the script
	
	lat = mc.ls( sl=True )[0]
	latShp = mc.listRelatives( lat , s=True )[0]
	ffd = mc.listConnections( '%s.worldMatrix[0]' % latShp , d=True , s=False )[0]
	ffdSet = mc.listConnections( '%s.message' % ffd , d=True , s=True )[0]
	latBase = mc.listConnections( '%s.baseLatticeMatrix' % ffd , d=False , s=True )[0]
	latBaseShp = mc.listRelatives( latBase , s=True )[0]
	
	mc.rename( lat , '%s_ffdLattice' % name )
	print 'Rename %s to %s' % ( lat , '%s_ffdLattice' % name )
	
	mc.rename( latBase , '%s_ffdBase' % name )
	print 'Rename %s to %s' % ( latBase , '%s_ffdBase' % name )
	
	mc.rename( ffd , '%s_ffd' % name )
	print 'Rename %s to %s' % ( ffd , '%s_ffd' % name )
	
	mc.rename( ffdSet , '%s_ffdSet' % name )
	print 'Rename %s to %s' % ( ffdSet , '%s_ffdSet' % name )

def resetJointOrient() :
	
	# Reset the orientation of selected joints to zero
	# Select joints the run the script
	
	for each in mc.ls( sl=True ) :
		
		prnts = mc.listRelatives( each , p=True )
		chldrn = mc.listRelatives( each , c=True )
		
		if prnts :
			mc.parent( each , w=True )
		
		if chldrn :
			mc.parent( chldrn[0] , w=True )
		
		mc.setAttr( '%s.jointOrient' % each , 0 , 0 , 0 )
		
		if prnts :
			mc.parent( each , prnts[0] )
		
		if chldrn :
			mc.parent( chldrn[0] , each )

def disableOpposite() :
	
	# Turn opposite attribute of selected geometries to off
	# Select transform node the run the script
	
	for sel in mc.ls( sl=True , l=True ) :
		
		shp = mc.listRelatives( sel , s=True , f=True )[0]
		
		mc.setAttr( '%s.opposite' % shp , 0 )

def displayBorder() :

	for sel in mc.ls( sl=True , l=True ) :
		
		shp = mc.listRelatives( sel , s=True , f=True )[0]
		
		mc.setAttr( '%s.displayBorders' % shp , 1 )

def addOffsetGroup() :
	# Create offset group for selected controller
	sel = mc.ls( sl=True )[0]
	
	currSide = ''
	sides = ( 'LFT' , 'RGT' )
	
	for side in sides :
		
		if side in sel :
			
			currSide = side
	
	currName , currType = sel.split( '%s_' % currSide )
	
	offGrpName = '%s%s%sOfst%s_grp' % ( currName , currType[0].upper() , currType[1:] , currSide )
	
	prnt = mc.listRelatives( sel , p=True )[0]
	offGrp = mc.group( em=True , n=offGrpName )
	mc.delete( mc.parentConstraint( prnt , offGrp ) )
	mc.parent( offGrp , prnt , r=False )
	mc.parent( sel , offGrp )
	
	attrs = ( 'v' )
	# attrs = ( 'v' )
	
	for attr in attrs :
		mc.setAttr( '%s.%s' % ( offGrp , attr ) , k=False , l=True )
	
	return offGrpName

def renameClusterHandleShape() :
	
	clsHndls = mc.ls( 'clusterHandleShape*' )
	
	for clsHndl in clsHndls :
		
		clstr = mc.listConnections(  '%s.clusterTransforms[0]' % clsHndl , d=True , s=False )[0]
		mc.rename( clsHndl , '%sShape' % clstr )

def locatorOnMidPos() :
	
	sels = mc.ls( sl = True , fl = True , l = True )
	no = len( sels )
	posSum = [0,0,0]
	loc = pc.Locator()
	
	for sel in sels :
		
		currPos = mc.xform( sel , q = True , t = True , ws = True )
		posSum[0] += currPos[0]
		posSum[1] += currPos[1]
		posSum[2] += currPos[2]
	
	loc.attr('tx').v = posSum[0]/no
	loc.attr('ty').v = posSum[1]/no
	loc.attr('tz').v = posSum[2]/no
	
	return loc

def renameSelectedSkinSet() :
	
	for sel in mc.ls( sl=True ) :
		
		try :
			
			renameDeformerSet( sel , 'skinCluster' )
			renameDeformerSet( sel , 'tweak' )
			
		except TypeError :
			
			print '%s has no related skinCluster node' % sel

def renameDeformerSet( obj='' , defType='' ) :
	
	shape = mc.listRelatives( obj , s=True )[0]
	# shape = obj
	dfNode = mc.listConnections( shape , s=True , d=False , type=defType )[0]
	dfSet = mc.listConnections( dfNode , s=False , d=True , type='objectSet' )[0]
	
	suffix = '%s%s' % ( defType[0].upper() , defType[1:] )
	mc.rename( dfNode , '%s%s' % ( obj , suffix ) )
	mc.rename( dfSet , '%s%sSet' % ( obj , suffix ) )

def renameClusterHandleShape() :
	
	for each in mc.ls( '*clusterHandleShape*' , l=True ) :
		
		clstr = mc.listConnections( '%s.clusterTransforms[0]' % each , d=True )[0]
		mc.rename( each , '%sShape' % clstr )

def alignJawCtrl() :
	# Align jaw control to jaw joint.
	# Select jaw control curve then jaw joint.
	sels = mc.ls( sl = True )
	
	ctrl = sels[0]
	jnt = sels[1]
	
	shp = mc.listRelatives( ctrl , shapes=True )[0]
	mc.select( shp , r=True )
	
	fstCv = 14
	scdCv = 2
	
	fstPos = mc.xform( '%s.cv[%s]' % (shp,fstCv) , q=True , ws=True , t=True )
	scdPos = mc.xform( '%s.cv[%s]' % (shp,scdCv) , q=True , ws=True , t=True )
	midPos = [ (fstPos[0]+scdPos[0])/2 , (fstPos[1]+scdPos[1])/2 , (fstPos[2]+scdPos[2])/2 ]
	
	clstr = mc.cluster()[1]
	mc.select( clstr , r=True )
	mc.move( midPos[0] , midPos[1] , midPos[2] , '%s.rotatePivot' % clstr )
	mc.move( midPos[0] , midPos[1] , midPos[2] , '%s.scalePivot' % clstr )
	
	mc.delete( mc.pointConstraint( jnt , clstr ) )
	
	tipJnt = mc.listRelatives( jnt , type = 'joint' )[0]
	
	if tipJnt :
		
		mc.delete( mc.aimConstraint(tipJnt,clstr,aim=(0,0,1),u=(1,0,0),wut='vector',wu=(1,0,0)))

def scaleGimbalControl( size=0.8 ) :
	
	gmblCtrls = mc.ls( '*Gmbl*_ctrl' )
	
	for each in gmblCtrls :
		
		ctrl = pc.Dag( each.replace( 'Gmbl' , '' ) )
		gmbl = pc.Dag( each )
		copyCurveShape( ctrl , gmbl )
		gmbl.scaleShape( size )

def scaleConControl( size=1.2 ) :
	
	gmblCtrls = mc.ls( '*Con*_ctrl' )
	
	for each in gmblCtrls :
		ctrl = pc.Dag( each.replace( 'Con' , '' ) )
		gmbl = pc.Dag( each )
		copyCurveShape( ctrl , gmbl )
		gmbl.scaleShape( size )

def cleanUpCtrlShapeName() :
	
	ctrls = mc.ls( '*_ply' )
	
	for ctrl in ctrls :
		
		shapes = mc.listRelatives( ctrl , s=True )
		
		if shapes :
			
			mc.rename( shapes[0] , '%sShape' % ctrl )

def mirrorCurveShape( obj = '' , search = '' , replace = '' ) :
	# Mirror NURBs curve shape
	crv = pc.Dag( obj )
	crvShape = pc.Dag( crv.shape )
	cv = crvShape.attr('spans').value + crvShape.attr('degree').value
	
	origCrv = pc.Dag( crv.name.replace( search , replace ) )
	origCrvShape = pc.Dag( origCrv.shape )
	
	for ix in range( 0 , cv ) :
		
		pos = mc.xform( '%s.cv[%s]' % ( origCrvShape , str(ix) ) , q = True , t = True , ws = True )
		mc.xform( '%s.cv[%s]' % ( crv.name , str(ix) ) , t = ( -pos[0] , pos[1] , pos[2] ) , ws = True )

def copyCurveShape( src = '' , target = '' ) :
	# Copy NURBs curve shape
	crv = pc.Dag( target )
	if len( crv.shape ) > 1 :
		crvShape = pc.Dag( crv.shape[0] )
	else :
		crvShape = pc.Dag( crv.shape )
	
	cv = crvShape.attr('spans').value + crvShape.attr('degree').value
	
	origCrv = pc.Dag( src )
	origCrvShape = pc.Dag( origCrv.shape )
	
	for ix in range( 0 , cv ) :
		
		pos = mc.xform( '%s.cv[%s]' % ( origCrvShape , str(ix) ) , q = True , t = True , ws = True )
		mc.xform( '%s.cv[%s]' % ( crv.name , str(ix) ) , t = ( pos[0] , pos[1] , pos[2] ) , ws = True )

def jointControl( crvType = '' ) :
	# Creating joint node with curve shape.
	jnt = pc.Joint()
	jnt.createCurve( crvType )
	jnt.attr('radius').v = 0
	jnt.attr('radius').lock = 1
	jnt.attr('radius').hide = 1
	
	return jnt

def jointAt( obj ) :
	# Create joint at postion of given object
	# Returns : joint object
	target = pc.Dag( obj )
	
	jnt = pc.Joint()
	
	jnt.snap( target )
	jnt.freeze( r = True , s = True )
	jnt.rotateOrder = target.rotateOrder
	if target.attr( 'radius' ).exists :
		jnt.attr( 'radius' ).v = target.attr( 'radius' ).v
	mc.select( cl = True )
	
	return jnt

def blend2Vectors( attr = '' , objA = '' , objB = '' , target = '' ) :
	# Blending 2 vector attributes
	blend = pc.BlendColors()
	mc.connectAttr( '%s.%s' % ( objA , attr ) , blend.attr( 'color1' ) )
	mc.connectAttr( '%s.%s' % ( objB , attr ) , blend.attr( 'color2' ) )
	
	if target :
		blend.attr( 'output' ) >> target.attr( attr )
	
	mc.select( cl = True )
	
	return blend

def crvGuide( ctrl = '' , target = '' ) :
	# Create NURBs curve between control and target
	# Returns : curve and two clusters
	crv = pc.Dag( mc.curve( d = 1 , p = [ ( 0 , 0 , 0 ) , ( 0 , 0 , 0 ) ] ) )
	clstr1 = pc.Dag( mc.cluster( '%s.cv[0]' % crv , wn = ( ctrl , ctrl ) )[ 0 ] )
	clstr2 = pc.Dag( mc.cluster( '%s.cv[1]' % crv , wn = ( target , target ) )[ 0 ] )
	mc.select( cl = True )
	
	return crv , clstr1 , clstr2

def visCtrlr( ctrl = '' , attrName = '' , target = '' ) :
	# Add visibility control
	mc.addAttr( ctrl , ln = attrName , at = 'bool' , k = True )
	mc.setAttr( '%s.%s' % ( ctrl , attrName ) , cb = True )
	mc.connectAttr( '%s.%s' % ( ctrl , attrName ) , '%s.v' % target )
	mc.select( cl = True )

def attrOffsetValue( ctrlAttr = '' , targetAttr = '' , offsetValue = 1 ) :

	add = pc.AddDoubleLinear()

	add.add( ln='offsetValue' , k=True , dv=offsetValue )

	mc.connectAttr( ctrlAttr , '%s.i1' % add , f=True )
	mc.connectAttr( '%s.offsetValue' % add , '%s.i2' % add , f=True )
	mc.connectAttr( '%s.o' % add , targetAttr , f=True )

	return add

def attrAmper( ctrlAttr = '' , targetAttr = '' , dv = 1 , ampAttr = '' ) :
	# Create attribute amplifier
	# Returns : multiDoubleLinear
	shape = pc.Dag( '' )
	try :
		shape = pc.Dag( mc.listRelatives( str( ctrlAttr ).split('.')[0] )[0] )
	except :
		pass
	mul = pc.MultDoubleLinear()
	
	mul.add( ln = 'amp' , k = True , dv = dv )
	
	if shape.exists and ampAttr :
		if shape.attr( ampAttr ).exists :
			shape.attr(ampAttr) >> mul.attr('amp')
		else :
			shape.add( ln = ampAttr , k = True , dv = dv )
			shape.attr(ampAttr) >> mul.attr('amp')
	
	mul.attr('amp') >> mul.attr('i1')
	mc.connectAttr( ctrlAttr , '%s.i2' % mul.name )
	mc.connectAttr( '%s.o' % mul.name , targetAttr , f = True )
	mc.select( cl = True )
	
	return mul

def fkStretch( ctrl = '' , attr = '' , target = '' , ax = 'y' ) :
	# Create stretchy FK by using translation of its child
	# Returns : addDoubleLinear and multiDoulbleLinear
	if attr :
		if not mc.objExists( '%s.%s' % ( ctrl , attr ) ) :
			mc.addAttr( ctrl , ln = attr , at = 'float' , k = True )		
	else :
		if mc.objExists( '%s.stretch' % ctrl ) :
			attr = 'stretch'
		else :
			mc.addAttr( ctrl , ln = 'stretch' , at = 'float' , k = True )
			attr = 'stretch'
	
	add = pc.AddDoubleLinear()
	
	div = mc.getAttr( '%s.t%s' % ( target , ax ) )
	mul = attrAmper( '%s.%s' % ( ctrl , attr ) , '%s.i2' % add , dv = div )
	add.add( ln = 'default' , k = True , dv = div )
	add.attr('default') >> add.attr('i1')
	add.attr('o') >> '%s.t%s' % ( target , ax )
	
	mc.select( cl = True )
	
	return add , mul

def orientLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , oriGrp = '' ) :
	# Blending orientation between local and world object.
	# Returns : locGrp , worGrp , worGrpOriCons , oriGrpOriCons and oriGrpOriConsRev
	locGrp = pc.Null()
	worGrp = pc.Null()
	locGrp.snap( oriGrp )
	worGrp.snap( oriGrp )
	
	oLoc = str( locGrp.name )
	oWor = str( worGrp.name )
	
	locGrp.name = 'local'
	worGrp.name = 'world'
	
	worGrpOriCons = pc.orientConstraint( worldObj , worGrp , mo = True )
	oriGrpOriCons = pc.orientConstraint( locGrp , worGrp , oriGrp )
	oriGrpOriConsRev = pc.Reverse()
	
	locGrp.name = oLoc
	worGrp.name = oWor
	
	con = pc.Dag( ctrl )
	
	attr = 'localWorld'
	con.add( ln = attr , k = True, min = 0 , max = 1 )
	con.attr( attr ) >> oriGrpOriCons.attr( 'w1' )
	con.attr( attr ) >> oriGrpOriConsRev.attr( 'ix' )
	oriGrpOriConsRev.attr( 'ox' ) >> oriGrpOriCons.attr( 'w0' )
	
	locGrp.parent( localObj )
	worGrp.parent( localObj )
	pc.clsl()
	
	return locGrp , worGrp , worGrpOriCons , oriGrpOriCons , oriGrpOriConsRev

def parentLocalWorldCtrl( ctrl = '' , localObj = '' , worldObj = '' , parGrp = '' ) :
	# Blending parent between local and world object.
	# Returns : locGrp , worGrp , worGrpParCons , parGrpParCons and parGrpParConsRev
	locGrp = pc.Null()
	worGrp = pc.Null()
	
	locGrp.snap( parGrp )
	worGrp.snap( parGrp )
	
	worGrpParCons = pc.parentConstraint( worldObj , worGrp , mo = True )
	parGrpParCons = pc.parentConstraint( locGrp , worGrp , parGrp )
	parGrpParConsRev = pc.Reverse()
	
	con = pc.Dag( ctrl )
	
	attr = 'localWorld'
	con.add( ln = attr , k = True, min = 0 , max = 1 )
	con.attr( attr ) >> parGrpParCons.attr( 'w1' )
	con.attr( attr ) >> parGrpParConsRev.attr( 'ix' )
	parGrpParConsRev.attr( 'ox' ) >> parGrpParCons.attr( 'w0' )
	
	locGrp.parent( localObj )
	worGrp.parent( localObj )
	pc.clsl()
	
	return locGrp , worGrp , worGrpParCons , parGrpParCons , parGrpParConsRev

def copyCurveShape( source = '' , target = '' ) :
	
	src = pc.Dag( source )
	srcShape = pc.Dag( src.shape )
	trgt = pc.Dag( target )
	trgtShape = pc.Dag( trgt.shape )
	
	cv = srcShape.attr('spans').value + srcShape.attr('degree').value
	
	for ix in range( 0 , cv ) :
		pos = mc.xform( '%s.cv[%s]' % ( srcShape , str(ix) ) , q = True , ws = True , t = True )
		mc.xform( '%s.cv[%s]' % ( trgtShape , str(ix) ) , t = pos , ws = True )

def zeroGroup( obj = '' ) :
	# Create zero group
	chld = pc.Dag( obj )
	grp = pc.Null()
	grp.snap( chld )
	chld.parent( grp )
	
	return grp

def doZeroGroup() :
	# Create zero group with naming
	sels = mc.ls( sl=True )
	sides = ( 'LFT' , 'RGT' , 'UPR' , 'LWR' )
	zroGrps = []
	
	for sel in sels :
		
		curr = pc.Dag( sel )
		prnt = curr.getParent()
		zGrp = zeroGroup( sel )
		
		nameLst = curr.name.split( '_' )
		currType = nameLst[-1]
		charName = ''
		midName = ''
		currSide = ''
		
		if len( nameLst ) == 3 :
			charName = '%s_' % nameLst[0]
			midName = nameLst[1]
		else :
			midName = nameLst[0]
		
		for side in sides :
			if side in midName :
				currSide = side
				midName = midName.replace( side , '' )
		
		zGrp.name = '%s%s%s%sZro%s_grp' % ( charName ,
											midName ,
											currType[0].upper() ,
											currType[1:] ,
											currSide
											)
		
		if prnt :
			zGrp.parent( prnt )
			print 'aaaa'
		
		zroGrps.append( zGrp )
	
	return zroGrps

def wireIkCurve() :
	# Ribbon curve for ribbon IK
	return pc.curve( d = 3 , p = [
									( 0 , 0 , 0 ) ,
									( 0 , 0.0666667 , 0 ) ,
									( 0 , 0.2 , 0 ) ,
									( 0 , 0.4 , 0 ) ,
									( 0 , 0.6 , 0 ) ,
									( 0 , 0.8 , 0 ) ,
									( 0 , 0.933333 , 0 ) ,
									( 0 , 1 , 0 )
								]
					)

def ribbonCurve() :
	# Ribbon curve for ribbon IK
	return pc.curve( d = 1 , p = [ ( 0 , 0 , 0 ) , ( 0 , 1 , 0 ) ] )

def ribbonSurface() :
	# Ribbon geometry for ribbon IK
	nrb = pc.nurbsPlane( p = (0,0,0) ,
							ax = (0,0,1) ,
							w = True ,
							lr = 5 ,
							d = 3 , u = 1 ,
							v = 5 , ch = 0
						)
	nrb.attr('t').value = (0,2.5,0)
	nrb.freeze()
	nrb.attr('rp').value = (0,0,0)
	nrb.attr('sp').value = (0,0,0)
	nrb.scaleShape( 0.2 )
	
	return nrb

def constrainAttributeNaming( cnstrs ) :
	
	for cnstr in cnstrs :
		
		cnstrType = mc.nodeType( cnstr )

		dummyAttr = 'targetTranslate'

		if cnstrType == 'parentConstraint' :

			dummyAttr = 'target[000].targetTranslate'

		elif cnstrType == 'pointConstraint' :

			dummyAttr = 'target[000].targetTranslate'

		elif cnstrType == 'orientConstraint' :

			dummyAttr = 'target[000].targetRotate'

		elif cnstrType == 'scaleConstraint' :

			dummyAttr = 'target[000].targetScale'

		elif cnstrType == 'aimConstraint' :

			dummyAttr = 'target[000].targetTranslate'

		elif cnstrType == 'poleVectorConstraint' :

			dummyAttr = 'constraintRotatePivot'

		if mc.listAttr( cnstr , ud=True ) :

			udAttrs = sorted( mc.listAttr( cnstr , ud=True ) )

			for ix in range( len( udAttrs ) ) :

				currNodeAttrName = '%s.%s' % ( cnstr , udAttrs[ix] )

				outAttr = dummyAttr.replace( '000' , str( ix ) )
				target = mc.listConnections( '%s.%s' % ( cnstr , outAttr ) , s=True )[0]

				newAttrName = '%sW%s' % ( target , str( ix ) )
				print '%s -- %s' % ( udAttrs[ix] , newAttrName )

				lock = False

				if mc.getAttr( currNodeAttrName , l=True ) :
					lock = True
					mc.setAttr( currNodeAttrName , l=False )

				if not udAttrs[ix] == newAttrName :
					mc.renameAttr( currNodeAttrName , newAttrName )

				if lock :
					mc.setAttr( '%s.%s' % ( cnstr , newAttrName ) , l=True )

def nodeNaming( obj , charName = '' , elem = '' , side = '' ) :
	'''
	Auto-naming all attributes within the given object.
	'''
	if charName and ( not '_' in charName ) :
		charName = '%s_' % charName
	
	allAttrs = dir( obj )
	cnstrs = []
	
	for attr in allAttrs :

		if ( not '__' in attr ) and ( '_' in attr ) :
			
			nodeName , nodeType = attr.split( '_' )
			newName = '%s%s%s%s_%s' % ( charName , nodeName , elem , side , nodeType )
			cmd = 'obj.%s.name = "%s"' % ( attr , newName )
			exec( cmd )

			if 'Constraint' in mc.nodeType( newName ) :
				cnstrs.append( newName )

	constrainAttributeNaming( cnstrs )

def dummyNaming( obj , attr = '' , dummy = '' , charName = '' , elem = '' , side = '' ) :
	'''
	Auto-naming all attributes within the given object.
	Script will replace the "attr" with the "dummy".
	'''
	if charName and ( not '_' in charName ) :
		charName = '%s_' % charName
	
	allAttrs = dir( obj )
	cnstrs = []
	
	for eachAttr in allAttrs :
		if ( not '__' in eachAttr ) and ( '_' in eachAttr ) :
			
			nodeName , nodeType = eachAttr.split( '_' )
			nodeName = nodeName.replace( attr , dummy )
			newName = '%s%s%s%s_%s' % ( charName , nodeName , elem , side , nodeType )
			cmd = 'obj.%s.name = "%s"' % ( eachAttr , newName )
			exec( cmd )

			if 'Constraint' in mc.nodeType( newName ) :
					cnstrs.append( newName )

	constrainAttributeNaming( cnstrs )

def lockUnusedAttrs( obj ) :
	# Lock unused attributes
	lckLst = [
				'grp' ,
				'parCons' ,
				'pntCons' ,
				'oriCons' ,
				'aimCons' ,
				'polCons' ,
				'scaCons'
			]
	
	nodes = dir( obj )
	
	for node in nodes :
		for lck in lckLst :
			attrLen = len( node )
			lckLen = len( lck )
			
			if attrLen > lckLen and node[ -lckLen : ] == lck :
				nodeName = eval( 'obj.%s' % node )
				kAttrs = mc.listAttr( nodeName , k=True )
				
				for kAttr in kAttrs :
					if not mc.attributeQuery( kAttr.split( '.' )[0] , n=nodeName , multi=True ) :
						mc.setAttr( '%s.%s' % ( nodeName , kAttr ) , l=True )

def cleanupAllModel() :

	# Clean all gemotry in the scene.
	removeAllNamespace()
	# Get poly shape node and NURBs shape node.
	shps = mc.ls( type='mesh' , l=True ) + mc.ls( type='nurbsSurface' , l=True )

	for shp in shps :

		if mc.objExists( shp ) :

			cleanupShape( shp )

	# Delete unused shading nodes.
	mm.eval( 'MLdeleteUnused' )

def cleanupSelectedModel() :

	# Clean slected model.

	sels = mc.ls( sl=True )

	for sel in sels :

		shps = mc.listRelatives( sel , s=True )

		try :

			for shp in shps :
				cleanupShape( shp )

		except :

			print '%s has no related shape.' % sel

def cleanupShape( shp='' ) :
	
	# Process to cleanup model before start rigging.
	# 1. Soft edge.
	# 2. Freeze transformations.
	# 3. Assign default material.
	# 4. Enable all render attribute.
	# 5. Turn opposite attribute off.
	# 6. Delete construction history.
	
	# Input		: None
	# Output	: Cleaned geometry
	
	# Soft edge.
	mc.select( shp , r=True )
	cmd = 'polyNormalPerVertex -ufn true;'
	mm.eval( cmd )
	cmd = 'polySoftEdge -a 180 -ch 1;'
	mm.eval( cmd )
	
	# Freeze transformation
	tf = mc.listRelatives( shp , p=True , type='transform' , f=True )[0]
	mc.select( tf , r=True )
	mc.makeIdentity( a=True , t=True , r=True , s=True )
	
	# Assign lambert1 to current shape
	mc.select( shp , r=True )
	mc.hyperShade( assign='lambert1' )
	
	# Enable all render attribute.
	attrs = (
				'castsShadows' ,
				'receiveShadows' ,
				'motionBlur' ,
				'primaryVisibility' ,
				'smoothShading' ,
				'visibleInReflections' ,
				'visibleInRefractions' ,
				'doubleSided'
			)
	for attr in attrs :
		nodeAttr = '%s.%s' % ( shp , attr ) 
		if not mc.getAttr( nodeAttr ) :
			mc.setAttr( nodeAttr , 1 )
	
	# Turn opposite attribute off.
	opposite = '%s.opposite' % shp
	if mc.getAttr( opposite ) :
		mc.setAttr( opposite , 0 )
	
	# Delete construction history.
	mc.delete( shp , ch=True )

def importAllReference() :
	
	# Import all reference.
	# Input		: None
	# Output	: Name of imported reference node.
	
	rfns = mc.ls( type='reference' )
	impRfns = []
	
	for rfn in rfns :
		
		if not rfn == 'sharedReferenceNode' :
			
			try :
				
				fn = mc.referenceQuery( rfn , filename=True )
				mc.file( fn , importReference=True )
				print '%s has been imported.' % rfn
				impRfns.append( rfn )
				
			except RuntimeError :
				
				print '%s is not connected to reference file.' % rfn
				mc.lockNode( rfn , l=0 )
				mc.delete( rfn )
			
	return impRfns

def removeAllNodeInNamespace( ns='' ) :

	# Remove every nodes that belong to the given namespace.
	# Input		: Namespace
	# Output	: Empty namespace
	
	nodes = mc.ls( '%s:*' % ns , l=True )
	mc.namespace( set=':' )

	if nodes :
		# If current namespace contains nodes,
		# delete them.
		for node in nodes :

			if mc.objExists( node ) :

				lockState = mc.lockNode( node , q=True )[0]

				if lockState :
					mc.lockNode( node , l=False )
				newName = ''
				try :
					newName = mc.rename( node , node.split( ':' )[-1] )
					# print '%s has been renamed to %s' % ( node , newName )
				except :
					pass
				mc.lockNode( newName , l=lockState )

def removeLeafNamespace( parentNs=':' ) :

	# Recursively find leaf namespace of the given namespace,
	# then remove it.
	# Input		: Namespace
	# Output	: None
	
	nss = mc.namespaceInfo( lon=True )
	
	# If current namespace is root,
	# remove system namespaces from current namespaces.
	if parentNs == ':' :
		nss.remove( 'UI' )
		nss.remove( 'shared' )

	if nss :
		# If current namespace contains some namespaces,
		for ns in nss :
			# iterate through every child namespaces.
			
			mc.namespace( set=':' )
			mc.namespace( set=ns )
			# mc.namespace( set=currentNs )
			childNss = mc.namespaceInfo( lon=True )

			if childNss :
				# If current child namespace contains namespaces,
				# send itself to removeLeafNamespace.
				removeLeafNamespace( ns.split( ':' )[-1] )

			else :
				# If current namespace does not contain any namespace,
				# rename all node belong to the current namespace then
				# remove current namespace.
				removeAllNodeInNamespace( ns )
				try :
					mc.namespace( rm=ns )
				except :
					pass
				# print '%s has been removed.' % ns

def removeAllNamespace() :

	# Recursively remove all namespace in current scene.
	# Input		: None
	# Output	: Removed namespace.

	mc.namespace( set=':' )
	sysNss = [ 'UI' , 'shared' ]
	nss = mc.namespaceInfo( lon=True )

	if nss == sysNss :
		# If there are only 'UI' nad 'shared' namespaces exist in the scene,
		# process is done.
		print 'All namespaces have been removed.'

	else :
		# If there are some namespaces in the scene,
		# remove leaf namespace then call 'removeAllNamespace' again.
		removeLeafNamespace( ':' )
		removeAllNamespace()
	
	return [ ns for ns in nss if not ns in sysNss ]

def shaderAssigner() :
	# Assigning temporary shader to selected objects
	sels = mc.ls( sl=True )
	name = ''
	side = ''

	nameResult = mc.promptDialog(
									title='Shading Name',
									message='Enter Name:',
									button=['OK', 'Cancel'],
									defaultButton='OK',
									cancelButton='Cancel',
									dismissString='Cancel'
								)
	
	if nameResult == 'OK':
		name = mc.promptDialog(query=True, text=True)
	
	if name :
		
		shadingName = '%sTmp_mat' % name
		
		if not mc.objExists( shadingName ) :
			
			mc.shadingNode( 'lambert' , asShader=True , n=shadingName )
		
		mc.select( sels , r=True )
		cmd = 'hyperShade -assign %s;' % shadingName
		mm.eval( cmd )
		
		mc.select( shadingName , r=True )

def fileNodeRenamer() :
	
	nameResult = mc.promptDialog(
										title='File node renamer',
										message='Enter Name:',
										button=['OK', 'Cancel'],
										defaultButton='OK',
										cancelButton='Cancel',
										dismissString='Cancel'
									)
	
	if nameResult == 'OK':
		name = mc.promptDialog( query=True , text=True )
	
	if name :
		
		sel = mc.ls( sl=True )[0]
		fileNodeName = '%s_file' % name
		mc.rename( sel , fileNodeName )

		p2d = mc.listConnections( fileNodeName , s=True , d=False )
		if p2d :
			mc.rename( p2d[0] , '%sFile_place2dTexture' % name )

def dupShade() :
	# Duplicating material from referenced mesh to meshes
	sels = mc.ls( sl=True , l=True )
	
	mc.hyperShade( smn=True )
	
	refMat = mc.ls( sl=True )[0]
	
	if ':' in refMat :
		matName = refMat.split( ':' )[-1]
	else :
		matName = refMat
	
	if not mc.objExists( matName ) :
		mc.duplicate( upstreamNodes=True )
	
	for sel in sels :
		if not sel == sels[0] :
			mc.select( sel , r=True )
			mc.hyperShade( assign=matName )
	
	mc.select( sels , r=True )

def transferShade() :
	
	sels = mc.ls( sl=True , l=True )
	
	mc.hyperShade( smn=True )
	
	refMat = mc.ls( sl=True )[0]

	for sel in sels :
		if not sel == sels[0] :
			mc.select( sel , r=True )
			mc.hyperShade( assign=refMat )
	
	mc.select( sels , r=True )

def removeSelectedReference() :
	# Removing selected reference from the scene
	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		if mc.objExists( sel ) and mc.referenceQuery( sel , isNodeReferenced=True ) :
			
			refNode = mc.referenceQuery( sel , referenceNode=True )
			fileName = mc.referenceQuery( refNode , filename=True )
			mc.file( fileName , rr=True )

def importSelectedReference() :
	# Removing selected reference from the scene
	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		if mc.objExists( sel ) and mc.referenceQuery( sel , isNodeReferenced=True ) :
			
			refNode = mc.referenceQuery( sel , referenceNode=True , topReference=True )
			fileName = mc.referenceQuery( refNode , filename=True )
			mc.file( fileName , i=True )

def reloadSelectedReference() :
	# Removing selected reference from the scene
	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		if mc.objExists( sel ) and mc.referenceQuery( sel , isNodeReferenced=True ) :
			
			refNode = mc.referenceQuery( sel , referenceNode=True , topReference=True )
			fileName = mc.referenceQuery( refNode , filename=True )
			mc.file( fileName , lr=True )