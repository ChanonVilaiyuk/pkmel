import maya.cmds as mc
import maya.mel as mm
import os
import shutil
import pickle
import subprocess

import pkmel.core as pc
reload( pc )
import pkmel.rigTools as rigTools
reload( rigTools )

def doChangeTextureExtensionTo( extension='jpg' ) :

	fns = mc.ls( type='file' )

	for fn in fns :

		currTxtPath = os.path.normpath( mc.getAttr( '%s.fileTextureName' % fn ) )
		currTxtFldPath , currTxtNameExt = os.path.split( currTxtPath )
		currTxtName , currTxtExt = os.path.splitext( currTxtNameExt )

		fixedTxtPath = os.path.join(
										currTxtFldPath ,
										'%s.%s' % ( currTxtName , extension )
									)
		print fixedTxtPath
		mc.setAttr( '%s.fileTextureName' % fn , fixedTxtPath , type='string' )

def doConvertExrTextureFromSelectedFileNode() :

	rvio = os.path.normpath( r'O:\systemTool\convertor\Tweak\RV-3.12.20-32\bin\rvio.exe' )

	fns = mc.ls( sl=True , type='file' )

	for fn in fns :

		currTxtPath = os.path.normpath( mc.getAttr( '%s.fileTextureName' % fn ) )
		currTxtFldPath , currTxtNameExt = os.path.split( currTxtPath )
		currTxtName , currTxtExt = os.path.splitext( currTxtNameExt )
		
		if currTxtExt == '.exr' :

			tifPath = os.path.join( currTxtFldPath , '%s.tif' % currTxtName )

			if not os.path.exists( tifPath ) :

				cmd = '%s %s -o %s' % ( rvio , currTxtPath , tifPath )
				subprocess.call( cmd )
				mc.setAttr( '%s.fileTextureName' % fn , tifPath , type='string' )
			else :

				mc.setAttr( '%s.fileTextureName' % fn , tifPath , type='string' )

		else :

			exrTxtPath = os.path.join( currTxtFldPath , '%s.exr' % currTxtName )
			mc.setAttr( '%s.fileTextureName' % fn , exrTxtPath , type='string' )

def createMov(
					tmpFilePath='' ,
					fps=24 ,
					outFilePath=''
				) :
	
	ffmpeg = os.path.normpath( r'O:/systemTool/toolPack/O/systemTool/python/playBlastPlus/convertor/ffmpeg_codec/bin/ffmpeg.exe' )

	cmd = '%s -y -i "%s" -r %s' % ( ffmpeg , os.path.normpath( tmpFilePath ) , fps )
	cmd += ' -vcodec libx264 -vprofile baseline -crf 22 -bf 0 -pix_fmt yuv420p'
	cmd += ' -f mov %s' % os.path.normpath( outFilePath )
	
	subprocess.call( cmd )
	
	return outFilePath

def pfAssetRelinkTexture() :
	prefix = r'P:\Lego_Template\asset\3D\friendHotelSetFromPf\source'

	for each in mc.ls( type='file' ) :
		
		mc.setAttr( '%s.fileTextureName' % each , l=False )
		currTexturePath = mc.getAttr( '%s.fileTextureName' % each )
		
		tifPath = os.path.join( prefix , currTexturePath ).replace( '.exr' , '.tif' )
		
		mc.setAttr(  '%s.fileTextureName' % each , tifPath , type='string' )

def pfAssetImportMatFile() :

	scenePath = os.path.normpath( mc.file( q=True , sn=True ) )
	sceneFolderPath , sceneNameExt = os.path.split( scenePath )

	matFilePath = os.path.join( sceneFolderPath , 'mat.ma' )

	mc.file( matFilePath , i=True )

def pfAssetReAssignShader() :

	scenePath = os.path.normpath( mc.file( q=True , sn=True ) )
	sceneFolderPath , sceneNameExt = os.path.split( scenePath )
	
	shdFls = [ f for f in os.listdir( sceneFolderPath ) if f.endswith( '.shd' ) ]

	currShdFl = os.path.join( sceneFolderPath , shdFls[0] )

	geoToShader = pickle.load( open( currShdFl , 'rb' ) )

	print geoToShader

	for geo in geoToShader.keys() :

		assignShader( geoToShader[ geo ] , geo )

		print geoToShader[ geo ]

def getRelatedShader( node='' ) :

	# Get shader assigned to given node.

	shader = None
	
	mc.select( node , r=True )
	shapes = mc.ls( dag=True , o=True , s=True , sl=True , ni=True )
	
	sgs = mc.listConnections( shapes , type='shadingEngine' )
	if sgs :
		shader = mc.listConnections( '%s.surfaceShader' % sgs[0] , s=True , d=False )[0]

	return shader

def assignShader( shader='' , geo='' ) :
	
	for each in mc.ls( geo , l=True ) :

		cmd = 'assignSG %s %s' % ( shader , each )

		try :
			mm.eval( cmd )
		except :
			print 'Cannot assign %s to %s' % ( shader , geo )
	
	return True


def writeSelectedShadingData() :

	scenePath = os.path.normpath( mc.file( q=True , sn=True ) )
	sceneFolderPath , sceneNameExt = os.path.split( scenePath )
	sceneName , sceneExt = os.path.splitext( sceneNameExt )

	shadingDataName = '%sShadingData.shd' % sceneName

	shadingDataPath = os.path.join(
										sceneFolderPath ,
										shadingDataName
									)

	relatedShaderDict = {}

	for sel in mc.ls( sl=True , l=True ) :
		
		shader = getRelatedShader( sel )
		if shader :
			relatedShaderDict[ sel ] = shader

	pickle.dump( relatedShaderDict , open( shadingDataPath , 'wb' ) )
	
	print 'Shading data has been written to %s' % shadingDataPath
	return shadingDataPath

def batchRenameFiles( folderPath='' , search='' , replace='' ) :
	
	cleanedPath = os.path.normpath( folderPath )
	files = [ f for f in os.listdir( cleanedPath ) if os.path.isfile( os.path.join( cleanedPath , f ) ) ]
	
	for _file in files :
		
		currFileName = _file.replace( search , replace )
		oldFilePath = os.path.join( cleanedPath , _file )
		currFilePath = os.path.join( cleanedPath , currFileName )
		shutil.move( oldFilePath , currFilePath )

def frdAddEyeSpec() :

	lftSpecCtrl = 'eyeSpecLFT_ctrl'
	lftSpecCtrlShp = 'eyeSpecLFT_ctrlShape'
	lftSpecGrp = 'eyeSpecLFT_grp'
	lftSpecJnt = 'eyeSpecLFT_jnt'
	lftSpecAdd = 'eyeSpacLFT_add'

	rgtSpecCtrl = 'eyeSpecRGT_ctrl'
	rgtSpecCtrlShp = 'eyeSpecRGT_ctrlShape'
	rgtSpecGrp = 'eyeSpecRGT_grp'
	rgtSpecJnt = 'eyeSpecRGT_jnt'
	rgtSpecAdd = 'eyeSpacRGT_add'

	lftRp = mc.xform( lftSpecCtrl , q=True , rp=True , ws=True )
	lftSp = mc.xform( lftSpecCtrl , q=True , sp=True , ws=True )

	rgtRp = mc.xform( rgtSpecCtrl , q=True , rp=True , ws=True )
	rgtSp = mc.xform( rgtSpecCtrl , q=True , sp=True , ws=True )

	print lftRp , lftSp , rgtRp , rgtSp

	ctrls = ( lftSpecCtrl , rgtSpecCtrl )
	attrs = ( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )

	for ctrl in ctrls :
		for attr in attrs :
			mc.setAttr( '%s.%s' % ( ctrl , attr ) , l=True )

	lftSubSpecCtrl = pc.Control( 'circle' )
	lftSubSpecCtrl.name = 'eyeSpecSubLFT_ctrl'
	lftSubSpecCtrl.color = 'white'
	lftSubSpecCtrl.rotateShape( ( 90 , 0 , 0 ) )
	lftSubSpecCtrl.scaleShape( 0.05 )
	lftSubSpecCtrl.attr( 'v' ).lockHide()

	lftSubSpecCtrlGrp = pc.group( lftSubSpecCtrl )
	lftSubSpecCtrlGrp.name = 'eyeSpecSubCtrlZroLFT_grp'

	lftSubSpecCtrlGrp.snap( lftSpecGrp )

	mc.addAttr( lftSpecCtrlShp , ln='subCtrlVis' , at='float' , min=0 , max=1 , k=True )
	mc.connectAttr( '%s.subCtrlVis' % lftSpecCtrlShp ,  lftSubSpecCtrlGrp.attr( 'v' ) )

	# mc.xform( lftSubSpecCtrl , rp=lftRp )
	mc.move( lftRp[0] , lftRp[1] , lftRp[2] , '%s.rotatePivot' % lftSubSpecCtrl , a=True )

	mc.parent( lftSubSpecCtrlGrp , lftSpecCtrl )
	mc.parent( lftSpecGrp , lftSubSpecCtrl )

	try :
		mc.setAttr( '%s.default' % lftSpecAdd , 0 )
	except :
		pass

	rgtSubSpecCtrl = pc.Control( 'circle' )
	rgtSubSpecCtrl.name = 'eyeSpecSubRGT_ctrl'
	rgtSubSpecCtrl.color = 'white'
	rgtSubSpecCtrl.rotateShape( ( 90 , 0 , 0 ) )
	rgtSubSpecCtrl.scaleShape( 0.05 )
	rgtSubSpecCtrl.attr( 'v' ).lockHide()

	rgtSubSpecCtrlGrp = pc.group( rgtSubSpecCtrl )
	rgtSubSpecCtrlGrp.name = 'eyeSpecSubCtrlZroRGT_grp'

	rgtSubSpecCtrlGrp.snap( rgtSpecGrp )

	mc.addAttr( rgtSpecCtrlShp , ln='subCtrlVis' , at='float' , min=0 , max=1 , k=True )
	mc.connectAttr( '%s.subCtrlVis' % rgtSpecCtrlShp ,  rgtSubSpecCtrlGrp.attr( 'v' ) )

	# mc.xform( rgtSubSpecCtrl , rp=rgtRp )
	mc.move( rgtRp[0] , rgtRp[1] , rgtRp[2] , '%s.rotatePivot' % rgtSubSpecCtrl , a=True )

	mc.parent( rgtSubSpecCtrlGrp , rgtSpecCtrl )
	mc.parent( rgtSpecGrp , rgtSubSpecCtrl )

	try :
		mc.setAttr( '%s.default' % rgtSpecAdd , 0 )
	except :
		pass

def city2DDoCreateNewRenderLayer() :
	
	result = mc.promptDialog(
								title='Render Layer Name',
								message='Enter Name:' ,
								button=[ 'OK' , 'Cancel' ] ,
								defaultButton='OK',
								cancelButton='Cancel',
								dismissString='Cancel'
							)
	
	if result == 'OK' :
		newLayerName = mc.promptDialog( query=True , text=True )
		city2DCreateNewRenderLayer( newLayerName )

def city2DCreateNewRenderLayer( newLayerName='' ) :

	sels = mc.ls( sl=True )
	currLayer = mc.editRenderLayerGlobals( query=True, currentRenderLayer=True )

	if not newLayerName in mc.ls( type='renderLayer' ) :
		mc.createRenderLayer( n=newLayerName )

	for sel in sels :
		
		if not currLayer == 'defaultRenderLayer' :
			mc.editRenderLayerMembers( currLayer , sel , r=True )

		mc.editRenderLayerMembers( newLayerName , sel )

	mc.editRenderLayerGlobals( currentRenderLayer=newLayerName )

def city2DImportFaceGeo() :

	facialFile = r'Y:/USERS/Peck/proj/testCity2D/assets/miniFigEye/hero/rig.mb'

	mc.file( facialFile , i=True )

def city2DParentFaceGeo() :

	faceGeo = 'eyeGuideGeo_grp'
	geoGrp = 'headGeo_grp'
	mc.parent( faceGeo , geoGrp )
	mc.parentConstraint( 'head2Skin_jnt' , faceGeo , mo=True )

def city2DGroupCharacterParts() :

	geoGrp = 'geo_grp'

	bodyGrp = mc.group( n='bodyGeo_grp' , em=True )
	headGrp = mc.group( n='headGeo_grp' , em=True )
	lHandGrp = mc.group( n='handGeoLFT_grp' , em=True )
	rHandGrp = mc.group( n='handGeoRGT_grp' , em=True )
	# lArmGrp = mc.group( n='armGeoLFT_grp' , em=True )
	# rArmGrp = mc.group( n='armGeoRGT_grp' , em=True )
	lLegGrp = mc.group( n='legGeoLFT_grp' , em=True )
	rLegGrp = mc.group( n='legGeoRGT_grp' , em=True )

	legGeoGrp = 'legGeo_grp'
	lArmGeoGrp = 'armGeoLFT_grp'
	rArmGeoGrp = 'armGeoRGT_grp'
	lLegGeo = 'legLFT_ply'
	rLegGeo = 'legRGT_ply'
	lHandGeoGrp = 'handPlyZroLFT_grp'
	rHandGeoGrp = 'handPlyZroRGT_grp'
	head = 'head_ply'
	body = 'body_ply'
	pelvis = 'pelvis_ply'
	hip = 'hip_ply'

	mc.parent( head , headGrp )
	mc.parent( lLegGeo , headGrp )
	mc.parent( lLegGeo , lLegGrp )
	mc.parent( rLegGeo , rLegGrp )
	mc.parent( lHandGeoGrp , lHandGrp )
	mc.parent( rHandGeoGrp , rHandGrp )
	mc.parent( body , hip , pelvis , bodyGrp )

	mc.parent( headGrp , geoGrp )
	mc.parent( lHandGrp , geoGrp )
	mc.parent( rHandGrp , geoGrp )
	mc.parent( lLegGrp , legGeoGrp )
	mc.parent( rLegGrp , legGeoGrp )
	mc.parent( bodyGrp , geoGrp )

def city2DTransferColorToIncan() :

	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		mc.hyperShade( objects=sel )

		objs = mc.ls( sl=True )

		colSources = mc.listConnections( '%s.color' % sel , source=True , p=True )
		transSources = mc.listConnections( '%s.transparency' % sel , source=True , p=True )
		
		surfaceShd = mc.shadingNode( 'surfaceShader' , asShader=True )
		
		if colSources :
			mc.connectAttr( colSources[0] , '%s.outColor' % surfaceShd )
		else :
			colVals = mc.getAttr( '%s.color' % sel )
			mc.setAttr(
						'%s.outColor' % surfaceShd ,
						colVals[0][0] ,
						colVals[0][1] ,
						colVals[0][2]
						)

		if transSources :
			mc.connectAttr(
								transSources[0] ,
								'%s.outTransparency' % surfaceShd
							)

		if objs and surfaceShd :
			mc.select( objs , r=True )
			mc.hyperShade( assign=surfaceShd )

		if mc.objExists( sel ) :
			mc.delete( sel )

def city2DPublish( pubType='Render' ) :

	# Auto fill asset data
	from rigTool import genScript
	reload(genScript)

	genScript.autoAssign()

	mc.file( s=True )

	scenePath = os.path.normpath( mc.file( q=True , sn=True ) )
	sceneFolderPath , sceneNameExt = os.path.split( scenePath )
	sceneFolderPathElem = sceneFolderPath.split( os.sep )

	refFolderPath = os.path.join(
									sceneFolderPathElem[0] ,
									os.sep ,
									sceneFolderPathElem[1] ,
									sceneFolderPathElem[2] ,
									sceneFolderPathElem[3] ,
									sceneFolderPathElem[4] ,
									sceneFolderPathElem[5] ,
									sceneFolderPathElem[6] ,
									'ref'
								)
	pubFileName = '%s_%s.mb' % ( sceneFolderPathElem[6] , pubType )

	pubFilePath = os.path.join( refFolderPath , pubFileName )

	mc.file( rn=pubFilePath )
	mc.file( type='mayaBinary', s=True )

	print '\nScene has been published to %s\n' % pubFilePath

def city2DRef( pubType='Anim' ) :
	
	scenePath = os.path.normpath( mc.file( q=True , sn=True ) )
	sceneFolderPath , sceneNameExt = os.path.split( scenePath )
	sceneFolderPathElem = sceneFolderPath.split( os.sep )

	refFolderPath = os.path.join(
									sceneFolderPathElem[0] ,
									os.sep ,
									sceneFolderPathElem[1] ,
									sceneFolderPathElem[2] ,
									sceneFolderPathElem[3] ,
									sceneFolderPathElem[4] ,
									sceneFolderPathElem[5] ,
									sceneFolderPathElem[6] ,
									'ref'
								)
	pubFileName = '%s_%s' % ( sceneFolderPathElem[6] , pubType )
	pubFileNameExt = '%s.mb' % pubFileName
	
	pubFilePath = os.path.join( refFolderPath , pubFileNameExt )
	
	mc.file( pubFilePath , r=True , ns=pubFileName )

def createThumbnail( width=450 , height=300 ) :

	currentUserPath = os.path.normpath( os.path.expanduser('~') )
	tmpFilePath = os.path.join(
									currentUserPath ,
									'playblastTemp'
								)
	
	oWidth = mc.getAttr( 'defaultResolution.width' )
	oHeight = mc.getAttr( 'defaultResolution.height' )
	
	# width = 450
	# height = 300

	frame = mc.currentTime( q=True )

	args = {
				'format' : 'iff' ,
				'filename' : tmpFilePath ,
				'frame' : frame ,
				'forceOverwrite' : True ,
				'clearCache' : True ,
				'viewer' : 0 ,
				'showOrnaments' : 0 ,
				'fp' : 4 ,
				'percent' : 100 ,
				'quality' : 100 ,
				'width' : width ,
				'height' : height ,
				'offScreen' : True ,
				'indexFromZero' : True
			}

	mc.setAttr( 'defaultResolution.aspectLock' , False )
	mc.setAttr( 'defaultResolution.width' , width )
	mc.setAttr( 'defaultResolution.height' , height )
	
	mc.setAttr( 'defaultRenderGlobals.imageFormat' , 32 )
	mc.playblast( **args )

	# mc.setAttr( 'defaultResolution.width' , oWidth )
	# mc.setAttr( 'defaultResolution.height' , oHeight )
	
	blastFilePath = '%s%splayblastTemp.0000.png' % ( currentUserPath , os.sep )
	return blastFilePath

def city2DSetPlayblastCam( cam='persp' ) :

	camShp = mc.listRelatives( cam , s=True )[0]
	
	mc.setAttr( 'defaultResolution.width' , 450 )
	mc.setAttr( 'defaultResolution.height' , 300 )

	mc.setAttr( '%s.focalLength' % camShp , 60 )
	mc.camera(
				cam ,
				e=True ,
				displayFilmGate=False ,
				displayResolution=True ,
				filmFit='overscan'
			)

def city2DCreateThumbnail() :

	import sg.utils as sgUtil
	reload( sgUtil )

	scenePath = os.path.normpath( mc.file( q=True , sn=True ) )
	sceneData = scenePath.split( os.sep )

	projName = sceneData[1]
	assetName = sceneData[6]
	assetType = sceneData[4]
	assetSubType = sceneData[5]

	mc.camera(
				'persp' ,
				e=True ,
				displayFilmGate=False ,
				displayResolution=True ,
				filmFit='overscan'
			)

	imgPath = os.path.normpath( createThumbnail() )

	iconPath = os.path.join(
								sceneData[0] ,
								os.sep ,
								sceneData[1] ,
								sceneData[2] ,
								sceneData[3] ,
								sceneData[4] ,
								sceneData[5] ,
								sceneData[6] ,
								'images' ,
								'icon' ,
								'%s.png' % sceneData[6]
							)
	
	shutil.copy2( imgPath , iconPath )

	sgUtil.sgUploadAssetIcon(
								projName ,
								assetName ,
								assetType ,
								assetSubType ,
								imgPath
							)