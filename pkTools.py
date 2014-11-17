import maya.cmds as mc
import maya.mel as mm
import pkmel.core as pc
import pkmel.rigTools as rigTools
import os
import shutil

import maya.cmds as mc

import sys
sys.path.append( 'P:\\BKK\\systemTool\\python' )

# import sg
# from sg import utils as sgUtils
# reload( sgUtils )

def cityConnectSelectedToLayeredTexture() :
	lyrTxt = 'face_layeredTexture'
	sels = mc.ls( sl=True )
	for sel in sels :
		idx = sels.index( sel )
		mc.connectAttr( '%s.outColor' % sel ,
							'%s.inputs[%d].color' % ( lyrTxt ,
														idx
													) ,
							f=True
						)
		mc.connectAttr( '%s.outAlpha' % sel ,
							'%s.inputs[%d].alpha' % ( lyrTxt ,
														idx
													) ,
							f=True
						)

def cityP2dConnect() :
	cmd = 'connectAttr -force mouthFile_placement2DTexture.outUV mouth17_file.uvCoord; connectAttr -force mouthFile_placement2DTexture.outUvFilterSize mouth17_file.uvFilterSize; connectAttr -force mouthFile_placement2DTexture.coverage mouth17_file.coverage; connectAttr -force mouthFile_placement2DTexture.translateFrame mouth17_file.translateFrame; connectAttr -force mouthFile_placement2DTexture.rotateFrame mouth17_file.rotateFrame; connectAttr -force mouthFile_placement2DTexture.mirrorU mouth17_file.mirrorU; connectAttr -force mouthFile_placement2DTexture.mirrorV mouth17_file.mirrorV; connectAttr -force mouthFile_placement2DTexture.stagger mouth17_file.stagger; connectAttr -force mouthFile_placement2DTexture.wrapU mouth17_file.wrapU; connectAttr -force mouthFile_placement2DTexture.wrapV mouth17_file.wrapV; connectAttr -force mouthFile_placement2DTexture.repeatUV mouth17_file.repeatUV; connectAttr -force mouthFile_placement2DTexture.vertexUvOne mouth17_file.vertexUvOne; connectAttr -force mouthFile_placement2DTexture.vertexUvTwo mouth17_file.vertexUvTwo; connectAttr -force mouthFile_placement2DTexture.vertexUvThree mouth17_file.vertexUvThree; connectAttr -force mouthFile_placement2DTexture.vertexCameraOne mouth17_file.vertexCameraOne; connectAttr -force mouthFile_placement2DTexture.noiseUV mouth17_file.noiseUV; connectAttr -force mouthFile_placement2DTexture.offset mouth17_file.offset; connectAttr -force mouthFile_placement2DTexture.rotateUV mouth17_file.rotateUV;'

	for sel in mc.ls( sl=True ) :
		currCmd = cmd.replace( 'mouth17_file' , sel )
		mm.eval( currCmd )

def cityAddConditionToLayeredTexture( ctrlAttr='' , fileNodes=[] ) :

	# ctrlAttr = 'R_eye_ctrl.eye_blink'
	# fileNodes = [ 'eye0RGT_file' ,
	# 				'eye1RGT_file'
	# 			]

	sides = ( 'LFT' , 'RGT' )

	for fileNode in fileNodes :
		startNo = 1
		idx = fileNodes.index( fileNode )
		currSide = '_'

		for side in sides :
			if side in fileNode :
				currSide = '%s_' % side

		currName , currType = fileNode.split( currSide )

		cnd = mc.createNode( 'condition' ,
						n='%s%s%scnd' % ( currName ,
											'%s%s' % ( currType[0].capitalize() ,
														currType[1:]
														) ,
											currSide
										)
							)
		mc.connectAttr( ctrlAttr , '%s.firstTerm' % cnd )
		mc.setAttr( '%s.secondTerm' % cnd , idx )
		mc.setAttr( '%s.colorIfTrueR' % cnd , 1 )
		mc.setAttr( '%s.colorIfFalseR' % cnd , 0 )

		targetConnection = mc.listConnections( '%s.outColor' % fileNode , p=True , d=True , s=False )[0]
		lyrTxtNode , inputIdx , color = targetConnection.split( '.' )
		print lyrTxtNode , inputIdx , color
		mc.connectAttr( '%s.outColorR' % cnd , 
						'%s.%s.isVisible' % ( lyrTxtNode , inputIdx )
						) 


def afPieceRig() :

	anim = 'anim_grp'
	sels = mc.ls( sl=True )
	splitter = 'Hires'

	for sel in sels :
		lowres = sel.replace( splitter , 'Lores' )
		sides = ( 'LFT' , 'RGT' )
		currName = sel.split( splitter )[0]
		currSide = ''

		for side in sides :
			if side in sel :
				currSide = side

		ctrl = pc.Control( 'stick' )
		ctrl.name = '%s%s_ctrl' % ( currName , currSide )
		ctrl.lockHideAttrs( 'v' )
		ctrl.color = 'green'

		oriGrp = pc.group( ctrl )
		oriGrp.name = '%sCtrlOri%s_grp' % ( currName , currSide )

		zroGrp = pc.group( oriGrp )
		zroGrp.name = '%sCtrlZro%s_grp' % ( currName , currSide )

		zroGrp.snapPoint( sel )
		try :
			mc.parentConstraint( ctrl , sel , mo=True )
		except :
			pass

		try :
			mc.parentConstraint( ctrl , lowres , mo=True )
		except :
			pass

		try :
			mc.scaleConstraint( ctrl , sel , mo=True )
		except :
			pass

		try :
			mc.scaleConstraint( ctrl , lowres , mo=True )
		except :
			pass

		ctrl.add( ln='geoVis' , min=0 , max=1 , dv=1 , k=True )

		hiresZgrp = mc.listRelatives( sel , p=True )[0]
		lowresZgrp = mc.listRelatives( lowres , p=True )[0]

		mc.connectAttr( '%s.geoVis' % ctrl , '%s.v' % hiresZgrp )
		mc.connectAttr( '%s.geoVis' % ctrl , '%s.v' % lowresZgrp )

		mc.select( ctrl , r=True )
		mc.select( zroGrp , add=True )
		mc.select( anim , add=True )
		mc.select( oriGrp , add=True )
		rigTools.doAddParentLocWor()

def citySetMainAttr() :

	root = 'P:/BKK'

	sn = mc.file( q=True , sn=True ).replace( root , '' )
	elms = sn.split( '/' )

	proj = elms[1]
	asset = elms[2]
	assetType = elms[3]
	assetClass = elms[4]
	assetSubClass = elms[5]
	assetName = elms[6]

	rigGrp = 'Rig_Grp'

	mc.setAttr( '%s.assetType' % rigGrp , assetClass , type='string' )
	mc.setAttr( '%s.assetSubType' % rigGrp , assetSubClass , type='string' )
	mc.setAttr( '%s.assetName' % rigGrp , assetName , type='string' )

def lotrConnectTexture() :

	ctrl , img = mc.ls( sl=True )

	mc.addAttr( ctrl , ln='facialTexture' ,
				at='enum' ,
				en='default:happy:angry' ,
				k =True
			)

	if not mc.getAttr( '%s.useFrameExtension' % img ) :
	    mc.setAttr( '%s.useFrameExtension' % img , 1 )

	mc.connectAttr( '%s.facialTexture' % ctrl ,
					'%s.frameExtension' % img ,
					f=True
					)

def chimaPullThemDown() :

	num = -6975.209
	nodes = mc.ls( sl=True )
	tys = []

	for node in nodes :
		
		src = mc.listConnections( '%s.ty' % node , p=True , s=True , d=False )[0]
		srcType = mc.nodeType( src )
		ty = ''

		if srcType == 'character' :
			ty = mc.listConnections( src , s=True , d=False )[0]
		elif srcType == 'animCurveTL' :
			ty = src.split( '.' )[0]
		else :
			print '%s has been constrained to object' % node
			ty = None
		if ty :
			tys.append( ty )
	
	mc.keyframe( tys ,
					e=True ,
					includeUpperBound=False ,
					animation='objects' ,
					time=(0,100000) ,
					r=True ,
					o='move' ,
					timeChange=0 ,
					valueChange=num
				)

def cityCleanupRig() :

	# 1. Remove 'props_GRP'

	# 2
	mc.rename( 'Ctrl_GRP|L_PoleVector_Ctrl_GRP|L_PoleVector_Ctrl' , 'L_ArmPoleVector_Ctrl' )
	mc.rename( 'Ctrl_GRP|L_PoleVector_Ctrl_GRP' , 'L_ArmPoleVector_Ctrl_GRP' )

	mc.delete( 'Ctrl_GRP|R_PoleVector_Ctrl_GRP|R_PoleVector_Ctrl|R_PoleVector_Ctrl' )
	mc.rename( 'Ctrl_GRP|R_PoleVector_Ctrl_GRP|R_PoleVector_Ctrl' , 'R_ArmPoleVector_Ctrl' )
	mc.rename( 'Ctrl_GRP|R_PoleVector_Ctrl_GRP' , 'R_ArmPoleVector_Ctrl_GRP' )

	# 4.
	mc.rename( 'R_fingerCtrl_GRP|group1_parentConstraint1' , 'R_fingerCtrl_GRP_parentConstraint1' )
	mc.rename( 'L_fingerCtrl_GRP|group1_parentConstraint1' , 'L_fingerCtrl_GRP_parentConstraint1' )

	# 5.
	mc.rename( 'R_Knee_Ctrl_GRP|R_Knee_Ctrl|R_Knee_Ctrl' , 'R_Knee_CtrlShape' )

	# 6. export/import weight and cleanup models.

def importLavalSword() :

	swordPath = 'C:/Users/animator/Desktop/lavalSword.ma'

	ctrlGrp = 'Ctrl_Grp'
	geoGrp = 'Render_Grp'
	superRoot = 'SuperRoot_Ctrl'

	parentJnt = 'Spine4BND'

	swordRigGrp = 'prop_Rig_g'
	swordGeoGrp = 'prop_Mesh_g'

	swordOffset = ( -1.7 , 3.7 , -0.75 )
	swordOrient = ( 0 , 0 , -135 )

	mc.file( swordPath , i=True )

	mc.setAttr( '%s.t' % swordRigGrp , swordOffset[0] ,
	            swordOffset[1] , swordOffset[2] )
	mc.setAttr( '%s.r' % swordRigGrp , swordOrient[0] ,
	            swordOrient[1] , swordOrient[2] )

	mc.parentConstraint( parentJnt , swordRigGrp , mo=True )

	mc.addAttr( superRoot , ln='swordVis' , min=0 ,
	            max=1 , dv=0 , k=True )

	mc.connectAttr( '%s.swordVis' % superRoot ,
	                '%s.v' % swordRigGrp )
	mc.connectAttr( '%s.swordVis' % superRoot ,
	                '%s.v' % swordGeoGrp )

	mc.parent( swordRigGrp , ctrlGrp )
	mc.parent( swordGeoGrp , geoGrp )

def removeAllNodeInNamespace( ns='' ) :

	# Remove every nodes that belong to the given namespace.
	# Input : namespace
	# Output : Nonde
	
	nodes = mc.ls( '%s:*' % ns )
	mc.namespace( set=':' )

	if nodes :
		# If current namespace contains nodes,
		# delete them.
		for node in nodes :

			if mc.objExists( node ) :

				lockState = mc.lockNode( node , q=True )[0]

				if lockState :
					mc.lockNode( node , l=False )
				
				try :
					newName = mc.rename( node , node.split( ':' )[-1] )
					print '%s has been renamed to %s' % ( node , newName )
				except :
					pass
					
				mc.lockNode( newName , l=lockState )

def removeLeafNamespace( parentNs=':' ) :

	# Recursively remove leaf namespace of the given namespace.
	# Input : namespace
	# Output : None
	
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
				# rename every nodes belong to the current namespace then
				# remove current namespace.
				removeAllNodeInNamespace( ns )
				mc.namespace( rm=ns )
				print '%s has been removed.' % ns

def removeAllNamespace() :

	# Recursively remove all namespace in the scene.
	# Input : None
	# Output : None

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

def pipeAddMainGrpAttr() :

	rigGrp = mc.ls( '*:rig_grp' )[0]

	attrs = ( 'assetType' , 'assetSubType' ,
				'assetName' , 'project' ,
				'assetPath' , 'exportType'
			)

	for attr in attrs :
		mc.addAttr( rigGrp , ln=attr , dt='string' )

def pipeCleanModel() :
	
	# Get poly shape node and NURBs shape node.
	shps = mc.ls( type='mesh' , l=True ) + mc.ls( type='nurbsSurface' , l=True )
	
	for shp in shps :
		if mc.objExists( shp ) :
			# Smooth normal
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
			attrs = ( 'castsShadows' , 'receiveShadows' ,
						'motionBlur' , 'primaryVisibility' ,
						'smoothShading' , 'visibleInReflections' ,
						'visibleInRefractions' , 'doubleSided'
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
	
	# Delete unused shading nodes.
	mm.eval( 'MLdeleteUnused' )

def friendsSetShotRange() :
	# Select shot node then run script.
	shot = mc.ls( sl=True , type='shot')[0]

	start = mc.getAttr( '%s.startFrame' % shot )
	end = mc.getAttr( '%s.endFrame' % shot )

	mc.playbackOptions( min=start )
	mc.playbackOptions( max=end )

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
		
		shadingName = '%sTmp_lambert' % name
		
		if not mc.objExists( shadingName ) :
			
			mc.shadingNode( 'lambert' , asShader=True , n=shadingName )
		
		mc.select( sels , r=True )
		cmd = 'hyperShade -assign %s;' % shadingName
		mm.eval( cmd )
		
		mc.select( shadingName , r=True )

def friendsAttachManEyelash() :
	
	lashPth = '/playground/USERS/Peck/projs/friends/manLid.ma'
	mc.file( lashPth , i=True )
	
	lashWrapGeo = 'manEyelashWrap_ply'
	
	mc.parent( 'manEyelashGeo_grp' , 'Anim_Geo_Grp' )
	mc.parent( 'manEyelashWrapGeo_grp' , 'still_grp' )
	mc.setAttr( 'manEyelashWrapGeo_grp.v' , 0 )
	
	# deformer -type wrap mesh_eyelash;
	mc.select( lashWrapGeo , r=True )
	mc.select( 'mesh_body' , add=True )
	
	# cmd = 'deformer -type wrap %s;' % lashWrapGeo
	# mm.eval( cmd )

def friendsBeachRig() :
	
	for each in mc.ls( sl=True ) :
    
		currName = each.split( '_' )[0]
		
		ctrl = pc.Control( 'circle' )
		ctrl.name = '%s_ctrl' % currName
		ctrl.color = 'red'
		ctrl.attr( 'v' ).lock = True
		ctrl.attr( 'v' ).hide = True
		ctrl.scaleShape( 7 )
		grp = pc.group( ctrl )
		grp.snap( each )
		grp.name = '%sCtrlZro_grp' % currName
		
		geoZro = mc.listRelatives( each , p=True )[0]
		geoGrp = mc.listRelatives( geoZro , p=True )[0]
		rigGrp = geoGrp.replace( 'Geo_' , 'Rig_' )
		
		if not mc.objExists( rigGrp ) :
			mc.group( em=True , n=rigGrp )
		
		mc.parentConstraint( ctrl , geoZro , mo=True)
		mc.scaleConstraint( ctrl , geoZro , mo=True )
		mc.parent( grp , rigGrp )

def friendsGetAllController() :
	# Select super root then run the script
	
	sels = mc.ls( sl=True , l=True )
	ctrls = []
	
	for sel in sels :
		
		chldrn = mc.listRelatives( sel , ad=True , type='transform' , f=True )
		
		for chld in chldrn :
			
			shps = mc.listRelatives( chld , shapes=True , f=True )
			
			if shps :
				
				currShape = shps[0]
				currType = mc.nodeType( currShape )
				
				if ( currType == 'nurbsCurve' ) and ( ( chld[-5:] == '_ctrl') or ( chld[-5:] == '_Ctrl') ):
					ctrls.append( chld )
	
	print ctrls
	mc.select( ctrls , r=True )
	# mc.select( sels , add=True )

def friendsRearrangeSequencer() :
	
	shots = sorted( mc.ls( type='shot' ) )
	snds = mc.ls( type='audio' )
	sqs = mc.ls( type='sequencer' )
	
	sqMan = 'sequenceManager1'
	sq = 'sequencer1'
	for ix in range( len( shots ) ) :
		if not mc.objExists( sq ) :
		    mc.createNode( 'sequencer' , n=sq )
		print '%s.message' % shots[ix]
		mc.connectAttr( '%s.message' % shots[ix] , '%s.shots[%d]' % ( sq , ix ) , f=True )
	
	mc.connectAttr( '%s.message' % sq , '%s.sequences[0]' % sqMan , f=True )
	
	for ix in range( len( snds ) ) :
		if not ':' in snds[ ix ] :
		    mc.connectAttr( '%s.message' % snds[ix] , '%s.audio[%d]' % ( sq , ix ) , f=True )

def friendsImportManNail() :

	if mc.objExists( 'nailGeo_grp' ) :
		mc.delete( 'nailGeo_grp' )
	
	mc.file( '/playground/USERS/Peck/projs/friends/manNail.ma' , i=True )
	mc.group( em=True , n='nailGeo_grp' )
	mc.parent( 'mesh_manNail' , 'nailGeo_grp' )
	mc.parent( 'mesh_manToenails' , 'nailGeo_grp' )
	mc.parent( 'nailGeo_grp' , 'Anim_Geo_Grp' )

def friendsAttachSkirtFix( name='' ) :
	
	geo = mc.ls( '*:%sFixGeo_grp' % name )[0]
	jnt = mc.ls( '*:%sFixJnt_grp' % name )[0]
	rig = mc.ls( '*:%sFixRig_grp' % name )[0]
	
	rootZro = mc.ls( '*:%sFix*RootCtrlZro_grp' % name )[0]
	
	animGrp = mc.ls( '*:anim_grp' )[0]
	stillGrp = mc.ls( '*:still_grp' )[0]
	pelvis = mc.ls( '*:pelvis_jnt' )[0]
	
	addRig = 'addRig_grp'
	
	if not mc.objExists( addRig ) :
		mc.group( em=True , n=addRig )
	
	mc.parent( geo , addRig )
	mc.parent( jnt , addRig )
	mc.parent( rig , addRig )
	
	mc.parentConstraint( stillGrp , geo , mo=True )
	mc.scaleConstraint( stillGrp , geo , mo=True )
	mc.parentConstraint( stillGrp , jnt , mo=True )
	mc.scaleConstraint( stillGrp , jnt , mo=True )
	mc.parentConstraint( animGrp , rig , mo=True )
	mc.scaleConstraint( animGrp , rig , mo=True )
	
	#skirtC_Rig:skirtCFixRootCtrlZro_grp
	mc.parentConstraint( pelvis , rig , mo=True )
	
	mc.setAttr( '%s.v' % jnt , 0 )
	mc.setAttr( '%s.v' % geo , 0 )

def friendsSkirtRig() :
	# Select skirt joints then run script.
	jnts = mc.ls( sl=True )
	
	for jnt in jnts :
		
		currJnt = pc.Dag( jnt )
		
		sides = ( 'LFT' , 'RGT' )
		currSide = '_'
		
		for side in sides :
			if side in jnt :
				currSide = '%s_' % side
		
		currName = jnt.split( currSide )[0]
		
		ctrl = pc.Control( 'circle' )
		ctrl.name = '%s%sctrl' % ( currName , currSide )
		ctrl.color = 'softBlue'
		
		zGrp = rigTools.zeroGroup( ctrl )
		zGrp.name = '%sCtrlZro%sgrp' % ( currName , currSide )
		zGrp.snap( jnt )
		
		ctrl.lockHideAttrs( 'v' )
		
		attrs = ( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' )
		for attr in attrs :
			ctrl.attr( attr ) >> currJnt.attr( attr )

def chimaAddWingBsh() :
	# Add wing blend shapes to bird character
	cmd = 'file -import -type "mayaAscii" -rpr "geo_1" -options "v=0"  -pr -loadReferenceDepth "all" "Y:/USERS/Peck/projs/chimaWingFold/geo_1.ma";'
	mm.eval( cmd )

	mc.select( 'wingFoldLFT_bsh' , r=True )
	mc.select( 'wingFoldLFT_bsh' , add=True )
	cmd = 'blendShape -e  -t Eggbert_wings_geo 2 wingFoldLFT_bsh 1 -t Eggbert_wings_geo 3 wingFoldRGT_bsh 1 wings_bls;'
	mm.eval( cmd )


	rootCtrl = 'Pelvis_Ctrl'
	mc.addAttr( rootCtrl , ln='L_wingFoldB' , k=True , min=0 , max=10 )
	mc.addAttr( rootCtrl , ln='R_wingFoldB' , k=True , min=0 , max=10 )


	lMdv = mc.createNode( 'multDoubleLinear' , n='wingFoldBBshLFT_mdv' )

	mc.connectAttr( '%s.L_wingFoldB' % rootCtrl , '%s.i1' % lMdv )
	mc.setAttr( '%s.i2' % lMdv , 0.1 )
	mc.connectAttr( '%s.o' % lMdv , 'wings_bls.wingFoldLFT_bsh' )

	rMdv = mc.createNode( 'multDoubleLinear' , n='wingFoldBBshRGT_mdv' )

	mc.connectAttr( '%s.R_wingFoldB' % rootCtrl , '%s.i1' % rMdv )
	mc.setAttr( '%s.i2' % rMdv , 0.1 )
	mc.connectAttr( '%s.o' % rMdv , 'wings_bls.wingFoldRGT_bsh' )

	mc.delete( 'wingFold_bsh' )
	mc.delete( 'wingOrig_bsh' )
	mc.delete( 'wingFoldLFT_bsh' )
	mc.delete( 'wingFoldRGT_bsh' )

def chimaAddAddonAttr() :
	# Select controller and group of add-on geometries then run the script
	ctrl , geoGrp = mc.ls( sl=True )
	
	# addAttr -ln "addOn2"  -at "enum" -en "off:addon01:"  |Rig_Grp|SuperRoot_Grp|SuperRoot_Ctrl;
	# setAttr -e-keyable true |Rig_Grp|SuperRoot_Grp|SuperRoot_Ctrl.addOn2;
	# addAttr -e -enumName "off:addon01:addon02:addon03:" ".addOn";
	
	cnt = 1
	cntStr = '01'
	
	if not mc.objExists( '%s.addOn' % ctrl ) :
		
		mc.addAttr( ctrl , ln='addOn' , at='enum' , en='off:addon01:' , k=True )
	
	else :
		
		enumStr = mc.attributeQuery( 'addOn' , node=ctrl , listEnum=True )[0]
		lastAddOn = enumStr.split( ':' )[-1]
				
		cntStr = lastAddOn.split( 'addon' )[-1]
		cnt = int( cntStr ) + 1
		cntStr = '%02d' % cnt
				
		enumStr = '%s:addon%s:' % ( enumStr , cntStr )
		
		mc.addAttr( '%s.addOn' % ctrl , e=True , enumName=enumStr )
		
	cnd = mc.createNode( 'condition' , n='addon%s' % cntStr )
	mc.connectAttr( '%s.addOn' % ctrl , '%s.firstTerm' % cnd )
	mc.setAttr( '%s.colorIfTrueR' % cnd , 1 )
	mc.setAttr( '%s.colorIfFalseR' % cnd , 0 )
	mc.setAttr( '%s.secondTerm' % cnd , cnt )
	mc.connectAttr( '%s.outColorR' % cnd , '%s.v' % geoGrp )

def friendsAttachRainCoatRig() :

	mesh = 'mesh_rainCoat'
	fixMesh = 'rainCoatRig:rainCoatFix_ply'

	animGrp = 'anim_grp'
	jntGrp = 'skin_grp'
	stillGrp = 'still_grp'
	rootJnt = 'root_jnt'

	fixGeoGrp = 'rainCoatRig:rainCoatFixGeo_grp'
	fixJntGrp = 'rainCoatRig:rainCoatFixJnt_grp'
	fixRigGrp = 'rainCoatRig:rainCoatFixRig_grp'
	fixRootGrp = 'rainCoatRig:rainCoatFixRootCtrlZro_grp'
	addRig = 'addRig_grp'

	ns = 'rainCoatRig'

	if not mc.ls( '%s:*' % ns ) :

		fpth = '/dsPipe/Lego_Friends/asset/3D/character/main/andreaFisher/dev/maya/wip/scenes/rainCoatRig.ma'

		cmd = 'file -r -type "mayaAscii" -gl -loadReferenceDepth "all" -namespace "rainCoatRig" -options "v=0" "%s";' % fpth
		mm.eval( cmd )

	mc.parentConstraint( stillGrp , fixJntGrp )
	mc.scaleConstraint( stillGrp , fixJntGrp )

	mc.parentConstraint( animGrp , fixRigGrp )
	mc.scaleConstraint( animGrp , fixRigGrp )

	mc.parentConstraint( stillGrp , fixGeoGrp )
	mc.scaleConstraint( stillGrp , fixGeoGrp )

	mc.parentConstraint( rootJnt , fixRootGrp , mo=True )

	if not mc.ls( addRig ) :
		mc.group( em=True , n=addRig )

	try :
		mc.parent( fixGeoGrp , addRig )
		mc.parent( fixJntGrp , addRig )
		mc.parent( fixRigGrp , addRig )
	except :
		pass

	cmd = 'blendShape -frontOfChain -n "rainCoatBuffer_bsn";'
	mc.select( fixMesh )
	mc.select( mesh , add=True )

	mm.eval( cmd )

	mc.addAttr( 'SuperRoot_Ctrl' , ln='rainCoatVis' , min=0 , max=1 , dv=0 , k=True )
	mc.connectAttr( 'SuperRoot_Ctrl.rainCoatVis' , '%s.v' % fixRigGrp )

	mc.setAttr( 'rainCoatBuffer_bsn.rainCoatFix_ply' , 1 )

def friendsAttachHairRig() :
	
	# Attach hair rig to the character
	geoGrp = 'Anim_Geo_Grp'
	animGrp = mc.ls( '*:anim_grp' )[0]
	jntGrp = mc.ls( '*:skin_grp' )[0]
	stillGrp = mc.ls( '*:still_grp' )[0]
	head2Jnt = mc.ls( '*:head2_jnt' )[0]
	spine3Jnt = mc.ls( '*:spine3_jnt' )[0]
	
	hairRigGrp = mc.ls( '*:hair*Rig_grp' )[0]
	hairJntGrp = mc.ls( '*:hair*Jnt_grp' )[0]
	hairGeoGrp = mc.ls( '*:hair?Geo_grp' )[0]
	zroGrp = mc.ls( '*:hair?RootCtrlZro_grp' )[0]
	
	# Delete constraint nodes that has been attached to geo_grp
	cnncs = mc.listConnections( hairGeoGrp , type='constraint' )
	cnstrs = []
	
	if cnncs :
		for cnnc in cnncs :
			if not cnnc in cnstrs :
				cnstrs.append( cnnc )
		
		# Delete constraints node
		if cnstrs :
			mc.delete( cnstrs )
	
	# Transfer the offet values from hairGeoGrp to hairRigGrp
	for attr in ( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' , 'sx' , 'sy' , 'sz' ) :
		src = '%s.%s' % ( hairGeoGrp , attr )
		trgt = '%s.%s' % ( hairRigGrp , attr )
		srcVal = mc.getAttr( src )
		trgtVal = mc.getAttr( trgt )
		
		mc.setAttr( trgt , srcVal )
		mc.setAttr( src , trgtVal )
	
	# Create add_rig grp
	addRig = 'addRig_grp'
	if not mc.objExists( addRig ) :
		addRig = mc.group( em=True , n=addRig )
	
	# Parent nodes to the addRig_grp
	mc.parent( hairRigGrp , addRig )
	mc.parent( hairJntGrp , addRig )
	mc.parent( hairGeoGrp , addRig )
	
	# Add constraints to nodes
	mc.parentConstraint( head2Jnt , zroGrp , mo=True )
	mc.scaleConstraint( head2Jnt , zroGrp , mo=True )
	
	mc.parentConstraint( geoGrp , hairGeoGrp , mo=True )
	mc.scaleConstraint( geoGrp , hairGeoGrp , mo=True )
		
	mc.parentConstraint( animGrp , hairRigGrp , mo=True )
	mc.scaleConstraint( animGrp , hairRigGrp , mo=True )
	
	mc.parentConstraint( jntGrp , hairJntGrp , mo=True )
	mc.scaleConstraint( jntGrp , hairJntGrp , mo=True )
	
	if mc.ls( '*:hair*Still_grp' ) :
		
		hairStillGrp = mc.ls( '*:hair*Still_grp' )[0]
		worOriGrp = mc.ls( '*:hair?WorOri_grp' )[0]
		
		mc.parent( hairStillGrp , addRig )
		
		mc.parentConstraint( stillGrp , hairStillGrp , mo=True )
		mc.scaleConstraint( stillGrp , hairStillGrp , mo=True )
		
		mc.parentConstraint( spine3Jnt , worOriGrp , mo=True )
		mc.scaleConstraint( spine3Jnt , worOriGrp , mo=True )
	
def friendsCreateProxyCube() :
	# Create a polygon cube as a proxy of a hair mesh
	# Select joints then run script
	
	sels = mc.ls( sl=True )
	selSize = len( sels )
	
	cube = mc.polyCube( sx=1 , sy=len( sels )-1 , sz = 1 , ch=False )[0]
	
	for ix in range( selSize ) :
		
		# print sels[ len( sels ) - ix - 1 ]
		# select -r pCube1.vtx[0:1] pCube1.vtx[18:19] ;
		# select -r pCube1.vtx[2:3] pCube1.vtx[16:17] ;
		# CreateCluster;
		minA , maxA = 0 + ( ix*2 ) , 1 + ( ix*2 )
		minB , maxB = ( selSize * 4 ) - 2 - ( ix*2 ) , ( selSize * 4 ) - 1 - ( ix*2 )
		
		mc.select( '%s.vtx[%s:%s]' % ( cube , minA , maxA ) , r=True )
		mc.select( '%s.vtx[%s:%s]' % ( cube , minB , maxB ) , add=True )
		
		mm.eval( 'CreateCluster' )
		clstr = mc.ls( sl=True )[0]
		zGrp = rigTools.zeroGroup( clstr )
		mc.parentConstraint( sels[ ix ] , zGrp )
		
def friendsAddSpineOri() :
	
	# Create spine orientation to the selected control
	# Select control and world orientation group then run the script
	ctrl , worGrp = mc.ls( sl=True )
	
	mc.addAttr( ctrl , ln='headSpine' , min=0 , max=1 , k=True )
	
	sides = ( 'LFT' , 'RGT' , 'Back' )
	currSide = '_'
	
	for side in sides :
		
		if side in ctrl :
			currSide = '%s_' % side
	
	name = ctrl.split( currSide )[0]
	
	#worGrp = 'hairAWorOri%sgrp' % currSide
	ctrlOriGrp = '%sCtrlOri%sgrp' % ( name , currSide )
	
	oriGrp = '%sSpineOri%sgrp' % ( name , currSide )
	mc.group( ctrl , n=oriGrp )
	
	rev = mc.createNode( 'reverse' , n='%sSpineOri%s_rev' % ( name , currSide ) )
	
	parCon = mc.parentConstraint( ctrlOriGrp , worGrp , oriGrp , mo=True )[0]
	
	mc.connectAttr( '%s.headSpine' % ctrl , '%s.ix' % rev )
	mc.connectAttr( '%s.headSpine' % ctrl , '%s.w1' % parCon )
	mc.connectAttr( '%s.ox' % rev , '%s.w0' % parCon )

def friendsRigSimpleHair( name='hairA' ) :
	
	# Create a root controller for hair geometries regarding input name.
	# If a transform node was selected, root controller is going to be snapped to the selected node.
	selected = mc.ls( sl=True )
	
	# Main group
	rigGrp = mc.group( em=True , n= '%sRig_grp' % name )
	
	rootCtrl = pc.Control( 'circle' )
	rootCtrl.color = 'brown' 
	rootCtrl.attr( 'v' ).lockHide()
	rootCtrl.name = '%sRoot_ctrl' % name
	
	zGrp = rigTools.zeroGroup( rootCtrl )
	zGrp.name = '%sRootCtrlZro_grp' % name
	
	if selected :
		zGrp.snap( selected[0] )
	
	zGrp.parent( rigGrp )
	
	rootCtrlGmbl = pc.addGimbal( rootCtrl )
	rootCtrlGmbl.name = '%sRootGmbl_ctrl' % name

def friendsAssignBasicMaterials() :
	# Assign basic materials to basic geometries
	shdPth = '/playground/USERS/Peck/projs/friendsBasicMaterials.ma'
	geoToShd = {'mesh_tongue': 'tongueTmp_lambert', 'mesh_upperGum': 'gumTmp_lambert', 'mesh_lowerGum': 'gumTmp_lambert', 'mesh_irisRGT': 'irisTmp_lambert', 'mesh_irisLFT': 'irisTmp_lambert', 'mesh_pupilLFT': 'pupilTmp_lambert', 'mesh_body': 'skinTmp_lambert', 'mesh_pupilRGT': 'pupilTmp_lambert', 'mesh_scleraRGT': 'scleraTmp_lambert', 'mesh_upperTeeth': 'teethTmp_lambert', 'mesh_eyeSpecLFT': 'eyeSpecTmp_lambert', 'mesh_nails': 'lambert1', 'mesh_lowerTeeth': 'teethTmp_lambert', 'mesh_eyeSpecRGT': 'eyeSpecTmp_lambert', 'mesh_scleraLFT': 'scleraTmp_lambert', 'mesh_corneaLFT': 'corneaTmp_lambert', 'mesh_corneaRGT': 'corneaTmp_lambert', 'mesh_nails' : 'nailsTmp_lambert' }
	
	if not mc.ls( 'skinTmp_lambert' ) :
		
		# Import material file
		print 'Importing %s' % shdPth
		mc.file( shdPth , i=True )
	
	for geo in geoToShd.keys() :
		
		geos = mc.ls( '*:%s' % geo )
		
		if geos :
			mc.select( geos , r=True )
			mc.hyperShade( assign=geoToShd[ geo ] )
	
	# Inner mouth
	faces = [u'mesh_body.f[0:49]', u'mesh_body.f[304]', u'mesh_body.f[306:310]', u'mesh_body.f[312:313]', u'mesh_body.f[315:351]', u'mesh_body.f[497]', u'mesh_body.f[554]', u'mesh_body.f[677:680]', u'mesh_body.f[682:683]', u'mesh_body.f[686]', u'mesh_body.f[688:743]', u'mesh_body.f[1000]', u'mesh_body.f[1002:1006]', u'mesh_body.f[1008:1009]', u'mesh_body.f[1011:1050]', u'mesh_body.f[1198]', u'mesh_body.f[1256]', u'mesh_body.f[1366:1371]', u'mesh_body.f[1373:1374]', u'mesh_body.f[1377]', u'mesh_body.f[5672:5732]', u'mesh_body.f[5852:5937]', u'mesh_body.f[5998:6143]', u'mesh_body.f[311]', u'mesh_body.f[314]', u'mesh_body.f[1007]', u'mesh_body.f[1010]']

	for face in faces :
		currFace = '*:%s' % face
		if mc.ls( currFace ) :
			mc.select( currFace , r=True )
			mc.hyperShade( assign='innerMouthTmp_lambert' )
	
	# Eyebrows
	faces = [ 'mesh_body.f[1379:1482]' , 'mesh_body.f[5491:5494]' ,  'mesh_body.f[5520:5523]' ]
	
	for face in faces :
		currFace = '*:%s' % face
		if mc.ls( currFace ) :
			mc.select( currFace , r=True )
			mc.hyperShade( assign='lambert1' )


def friendsEnableShapeAttrs() :
	# Enable all render attributes in the shape node
	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		shps = mc.listRelatives( sel , shapes=True )
		
		for shp in shps :
			
			attrs = ( 'castsShadows' , 'receiveShadows' , 'motionBlur' , 'primaryVisibility' , 'smoothShading' , 'visibleInReflections' , 'visibleInRefractions' , 'doubleSided' )
			
			for attr in attrs :
				
				if not mc.getAttr( '%s.%s' % ( shp , attr ) ) :
					mc.setAttr( '%s.%s' % ( shp , attr ) , 1 )
					print '"%s.%s" has been enebled' % ( shp , attr )
			
			if mc.getAttr( '%s.opposite' % shp ) :
				mc.setAttr( '%s.opposite' % shp , 0 )

def fixChimaWing() :
	
	cmd = 'blendShape -e  -t Eris_wings_geo 2 foldWing9LFT_bsh 1 wings_bls;'
	mm.eval( cmd )

	cmd = 'blendShape -e  -t Eris_wings_geo 3 foldWing9RGT_bsh 1 wings_bls;'
	mm.eval( cmd )

	cmd = 'blendShape -e  -ib -t Eris_wings_geo 2 foldWing5LFT_bsh 0.5 wings_bls;'
	mm.eval( cmd )

	cmd = 'blendShape -e  -ib -t Eris_wings_geo 2 foldWing3LFT_bsh 0.25 wings_bls;'
	mm.eval( cmd )

	cmd = 'blendShape -e  -ib -t Eris_wings_geo 2 foldWing7LFT_bsh 0.75 wings_bls;'
	mm.eval( cmd )

	cmd = 'blendShape -e  -ib -t Eris_wings_geo 3 foldWing5RGT_bsh 0.5 wings_bls;'
	mm.eval( cmd )

	cmd = 'blendShape -e  -ib -t Eris_wings_geo 3 foldWing3RGT_bsh 0.25 wings_bls;'
	mm.eval( cmd )

	cmd = 'blendShape -e  -ib -t Eris_wings_geo 3 foldWing7RGT_bsh 0.75 wings_bls;'
	mm.eval( cmd )

	rootCtrl = '|Rig_Grp|SuperRoot_Grp|SuperRoot_Ctrl|Root_Ctrl_Grp|Root_Ctrl|Ctrl_Grp|Pelvis_Ctrl_Grp|Pelvis_Ctrl'

	cmd = 'addAttr -ln "L_wingFoldB"  -at double  -min 0 -max 10 -dv 0 -k 1 |Rig_Grp|SuperRoot_Grp|SuperRoot_Ctrl|Root_Ctrl_Grp|Root_Ctrl|Ctrl_Grp|Pelvis_Ctrl_Grp|Pelvis_Ctrl;'
	mm.eval( cmd )

	cmd = 'addAttr -ln "R_wingFoldB"  -at double  -min 0 -max 10 -dv 0 -k 1 |Rig_Grp|SuperRoot_Grp|SuperRoot_Ctrl|Root_Ctrl_Grp|Root_Ctrl|Ctrl_Grp|Pelvis_Ctrl_Grp|Pelvis_Ctrl;'
	mm.eval( cmd )

	lMdv = mc.createNode( 'multDoubleLinear' , n='wingFoldBBshLFT_mdv' )

	mc.connectAttr( '%s.L_wingFoldB' % rootCtrl , '%s.i1' % lMdv )
	mc.setAttr( '%s.i2' % lMdv , 0.1 )
	mc.connectAttr( '%s.o' % lMdv , 'wings_bls.foldWing9LFT_bsh' )

	rMdv = mc.createNode( 'multDoubleLinear' , n='wingFoldBBshRGT_mdv' )

	mc.connectAttr( '%s.R_wingFoldB' % rootCtrl , '%s.i1' % rMdv )
	mc.setAttr( '%s.i2' % rMdv , 0.1 )
	mc.connectAttr( '%s.o' % rMdv , 'wings_bls.foldWing9RGT_bsh' )

def removeStud() :
	# Remove studs from lego models
	
	# Get selected objects
	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		# Separate current mesh
		mc.select( sel , r=True )
		meshes = mc.polySeparate( ch=False )
		
		# Contains mesh's volume as a key and object's name as an element
		volDct = {}

		for mesh in meshes :
			
			# Computing the object's bounding box
			mc.select( mesh )
			bbox = mc.exactWorldBoundingBox( mesh )
			vol = ( ( bbox[3]-bbox[0] ) * ( bbox[4] - bbox[1] ) * ( bbox[5] - bbox[3] ) )
			
			# Making value absolute
			if vol < 0 :
				vol = vol*-1
			
			volDct[ vol ] = mesh
		
		# Get the biggest mesh
		last = volDct[ sorted( volDct.keys() )[-1] ]
		for key in sorted( volDct.keys() ) :
			curr = volDct[ key ]
			if not curr == last :
				mc.delete( curr )
	
	mc.select( sels , r=True )

def transferAllShade( ns='' ) :

	for each in mc.ls( sl=True ) :

		src = '%s:%s' % ( ns , each )
		mc.select( src , r=True )
		mc.select( each , add=True )
		dupShade()

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

def replaceTexturePath( path = '' ) :
	# Replacing texture path
	fileNodes = mc.ls( type='file' )
	
	for fileNode in fileNodes :
		fileName = mc.getAttr( '%s.fileTextureName' % fileNode ).split('/')[-1]
		mc.setAttr( '%s.fileTextureName' % fileNode , '%s/%s' % ( path , fileName ) , type='string' )

def weaponRig() :
	# Rigging weapons
	sels = mc.ls( sl=True )
	
	createWeaponLocator()
	
	for sel in sels :
		
		currName = sel.split( '_' )[1]
		
		ctrl = rigTools.jointControl( 'sphere' )
		ctrl.name = '%s_ctrl' % currName
		ctrl.color = 'yellow'
		
		ctrlGrp = pc.group( ctrl )
		ctrlGrp.name = '%sCtrlZero_grp' % currName
		
		# mc.skinCluster( ctrl , sel , tsb=True )
		mc.parentConstraint( ctrl , sel , mo=True )
		
		lftGrp , rgtGrp = parentLeftRight( ctrl , 'L_weapon_loc' , 'R_weapon_loc' , ctrlGrp )
		lftGrp.name = '%sCtrlLeft_grp' % currName
		rgtGrp.name = '%sCtrlRgt_grp' % currName

def createWeaponLocator() :
	# Creating location for mounting weapons at left hand and right hand
	lHandJnt = 'L_Wrist_BND'
	rHandJnt = 'R_Wrist_BND'
	
	lHand = pc.Locator()
	rHand = pc.Locator()
	
	lHand.name = 'L_weapon_loc'
	rHand.name = 'R_weapon_loc'
	
	lHand.attr( 't' ).v = ( 1.92 , 0 , 0.015 )
	lHand.attr( 'rz' ).v = -15
	rHand.attr( 't' ).v = ( -1.92 , 0 , 0.015 )
	rHand.attr( 'rz' ).v = 15
	
	mc.delete( mc.pointConstraint( lHandJnt , lHand , skip=('x','z') ) )
	mc.delete( mc.pointConstraint( rHandJnt , rHand , skip=('x','z') ) )
	
	mc.parentConstraint( lHandJnt , lHand , mo=True )
	mc.parentConstraint( rHandJnt , rHand , mo=True )

def weaponRig2(jnts=['wristLFT_jnt', 'wristRGT_jnt']) :
	# Rigging weapons
	sels = mc.ls( sl=True )
	
	lHandLoc, rHandLoc = createWeaponLocator2(jnts)
	
	for sel in sels :
		
		currName = sel.split( '_' )[1]
		
		ctrl = rigTools.jointControl( 'sphere' )
		ctrl.name = '%s_ctrl' % currName
		ctrl.color = 'yellow'
		
		ctrlGrp = pc.group( ctrl )
		ctrlGrp.name = '%sCtrlZero_grp' % currName
		
		# mc.skinCluster( ctrl , sel , tsb=True )
		mc.parentConstraint( ctrl , sel , mo=True )
		
		lftGrp , rgtGrp = parentLeftRight( ctrl , lHandLoc.name , rHandLoc.name , ctrlGrp )
		lftGrp.name = '%sCtrlLeft_grp' % currName
		rgtGrp.name = '%sCtrlRgt_grp' % currName

def createWeaponLocator2(jnts) :
	# Creating location for mounting weapons at left hand and right hand
	lHandJnt = jnts[0]
	rHandJnt = jnts[1]
	
	lHand = pc.Locator()
	rHand = pc.Locator()
	
	poses = []
	for i in [lHandJnt,rHandJnt]:
		position = ''
		nsSplit = i.split(':')[-1]
		revElement = nsSplit.split('_')[0][::-1]

		for a in range(len(revElement)):
			if revElement[a].isupper():
				position += revElement[a]
			else:
				break
		poses.append(position[::-1])

	lHand.name = 'weapon%s_loc' %poses[0]
	rHand.name = 'weapon%s_loc' %poses[1]
	
	# lHand.attr( 't' ).v = ( 1.92 , 0 , 0.015 )
	# lHand.attr( 'rz' ).v = -15
	# rHand.attr( 't' ).v = ( -1.92 , 0 , 0.015 )
	# rHand.attr( 'rz' ).v = 15
	
	mc.delete( mc.pointConstraint( lHandJnt , lHand  ) )
	mc.delete( mc.pointConstraint( rHandJnt , rHand  ) )
	
	mc.parentConstraint( lHandJnt , lHand , mo=True )
	mc.parentConstraint( rHandJnt , rHand , mo=True )

	return lHand, rHand


def parentLeftRight( ctrl = '' , localObj = '' , worldObj = '' , parGrp = '' ) :
	# Blending parent between left hand and right hand.
	# Returns : locGrp , worGrp , worGrpParCons , parGrpParCons and parGrpParConsRev
	locGrp = pc.Null()
	worGrp = pc.Null()
	
	locGrp.snap( localObj )
	worGrp.snap( worldObj )
	
	worGrpParCons = pc.parentConstraint( worldObj , worGrp )
	locGrpParCons = pc.parentConstraint( localObj , locGrp )
	parGrpParCons = pc.parentConstraint( locGrp , worGrp , parGrp )
	parGrpParConsRev = pc.Reverse()
	
	con = pc.Dag( ctrl )
	
	attr = 'leftRight'
	con.add( ln = attr , k = True, min = 0 , max = 1 )
	con.attr( attr ) >> parGrpParCons.attr( 'w1' )
	con.attr( attr ) >> parGrpParConsRev.attr( 'ix' )
	parGrpParConsRev.attr( 'ox' ) >> parGrpParCons.attr( 'w0' )
	
	pc.clsl()
	
	return locGrp , worGrp

def makeIcon() :
	# Making icon for Chima
	width = 1280
	height = 720
	ratio = 16.0000/9.0000
	
	currWidth = mc.getAttr( 'defaultResolution.width' )
	currHeight = mc.getAttr( 'defaultResolution.height' )
	currRatio = mc.getAttr( 'defaultResolution.deviceAspectRatio' )
	
	mc.setAttr( 'defaultResolution.lockDeviceAspectRatio' , 1 )
	
	if currWidth == width and currHeight == height :
		
		mc.setAttr( 'defaultRenderQuality.shadingSamples' , 1 )
		mc.setAttr( 'defaultRenderGlobals.imageFormat' , 32 )
		
		currPath = mc.file( q=True , sn=True )
		charName = currPath.split( '/' )[ -1 ].split( '_' )[ 0 ]
		
		iconPath = ''
		splitters = ( 'ref' , 'dev' )
		currSplitter = ''
		for splitter in splitters :
			if splitter in currPath :
				currSplitter = splitter
		
		iconPath = '%simages/icon/%s.png' % ( currPath.split( currSplitter )[0] , charName )
		
		mc.render()
		mm.eval( 'renderWindowSaveImageCallback "renderView" "%s" "PNG"' % iconPath )
		print iconPath
	else :
		mc.setAttr( 'defaultResolution.width' , width )
		mc.setAttr( 'defaultResolution.height' , height )
		mc.setAttr( 'defaultResolution.deviceAspectRatio' , ratio )

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
        	
			refNode = mc.referenceQuery( sel , referenceNode=True )
			fileName = mc.referenceQuery( refNode , filename=True )
			mc.file( fileName , i=True )

def reloadSelectedReference() :
	# Removing selected reference from the scene
	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		if mc.objExists( sel ) and mc.referenceQuery( sel , isNodeReferenced=True ) :
        	
			refNode = mc.referenceQuery( sel , referenceNode=True )
			fileName = mc.referenceQuery( refNode , filename=True )
			mc.file( fileName , lr=True )

def fangRig( ground = '' ) :
	# Rig fang objects
	sels = mc.ls( sl=True , l=True )
	
	for currMesh in sels :
		
		mc.xform( currMesh , cp=True )
		
		objPos = mc.xform( currMesh , q=True , rp=True , ws=True )
		
		distDct = {}
		vtxCount = mc.polyEvaluate( ground , v=True )
		
		for ix in range( vtxCount ) :
			
			currVtx = '%s.vtx[%s]' % ( ground , ix )
			currVtxPos = mc.xform( currVtx , q=True , t=True , ws=True )
			
			dist = pow( pow( ( currVtxPos[0] - objPos[0] ) , 2 ) +
				pow( ( currVtxPos[1] - objPos[1] ) , 2 ) +
				pow( ( currVtxPos[2] - objPos[2] ) , 2 ) , 0.5 )
			
			distDct[ dist ] = currVtx
		
		closestVtx = distDct[ sorted( distDct.keys() )[0] ]
		colosestVtxPos = mc.xform( closestVtx , q=True , t=True , ws=True )
		
		mc.xform( currMesh , rp=[ colosestVtxPos[0] , colosestVtxPos[1] , colosestVtxPos[2] ] )
		mc.xform( currMesh , sp=[ colosestVtxPos[0] , colosestVtxPos[1] , colosestVtxPos[2] ] )
		
		ctrl = mc.circle( ch=False , nr=(0,1,0) )
		ctrlGrp = mc.group( ctrl )
		geoGrp = mc.group( em=True )
		mc.parent( geoGrp , ctrl )
		
		mc.delete( mc.parentConstraint( currMesh , ctrlGrp ) )
		mc.parent( currMesh , geoGrp )
		
		currName = currMesh.split( '|' )[-1].split( '_' )[0]
		
		mc.rename( ctrl , '%s_ctrl' % currName )
		mc.rename( ctrlGrp , '%sCtrl_grp' % currName )
		mc.rename( geoGrp , '%sGeo_grp' % currName )
		
		print '%s done' % currMesh

def removeNamespaces() :
	
	mc.namespace( set=':' )
	nss = mc.namespaceInfo( lon=True )
	
	exeptNss = ( 'UI' , 'shared' )
	
	for ns in nss :
		
		if not ns in exeptNss :

			nodes = mc.ls( '%s:*' % ns )
			
			#parentNs = mc.namespaceInfo( ns , p=True )
			
			for node in nodes :
				
				if mc.objExists( node ) :
					mc.rename( node , node.split( ':' )[-1] )
					print '%s has been renamed' % node
			
			mc.namespace( rm=ns )

def capeRig() :
	capeFile = 'Y:/USERS/Peck/projs/cape/scenes/rig_11.ma'
	cmd = 'file -import -type "mayaAscii" -rpr "capeRig" -options "v=0"  -pr -loadReferenceDepth "all" "%s";' % capeFile
	
	mm.eval( cmd )
	
	mc.parent( 'baseJntZro_grp' , 'Chest_Ctrl' )
	mc.parent( 'capeGeo_grp' , 'Geo_Group' )
	mc.parent( 'capeRig_grp' , 'Ctrl_GRP' )
	# mc.parent( 'capeWeapGeo_grp' , 'Utility_Grp' )

	mc.select( 'baseJntZro_grp' , r=True )
		
def retargetAnimation() :
	
	#file -r -type "mayaAscii" -gl -loadReferenceDepth "all" -namespace "urukhaiLow" -options "v=0" "/dsPipe/Lego_LOTR/Asset/Char/Animal/urukhaiA/Dev/Maya/wip/urukhaiLow.ma";

	srcNs = 'urukhaiA'
	trgtNs = 'urukhaiLow'

	ctrls = [u'Pelvis', u'Spine1BND', u'Spine2BND', u'Spine3BND', u'Spine4BND', u'Spine5BND', u'Spine6BND', u'Head1BND', u'Head2BND', u'Head3BND', u'Head4BND', u'Head5BND', u'L_Shoulder_BND', u'L_Elbow_BND', u'L_Wrist_BND', u'R_Shoulder_BND', u'R_Elbow_BND', u'R_Wrist_BND', u'L_Leg_BND', u'L_Knee_BND', u'L_Ankle_BND', u'R_Leg_BND', u'R_Knee_BND', u'R_Ankle_BND', u'sword_ctrl', u'shield_ctrl']

	for ctrl in ctrls :
	    
		src = '%s:%s' % ( srcNs , ctrl )
		trgt = '%s:%s' % ( trgtNs , ctrl )

		attrs = mc.listAttr( trgt , k=True )

		mc.orientConstraint( src , trgt )    
	    
		if 'translateX' in attrs :
			mc.pointConstraint( src , trgt )



def placeCrowd( clipSources = [] ) :
	
	sels = mc.ls( sl=True )
	
	clipSources = [ 'urukRunSwordLeft1Source' ,
			'urukRunSwordRight1Source' ]
	clipNum = len( clipSources ) - 1
	
	for clip in clipSources :
		
		mc.setAttr( '%s.preCycle'%clip , 100 )
		mc.setAttr( '%s.postCycle'%clip , 100 )
		
		mc.setAttr( '%s.scale'%clip , 1.3 )
	
	for ix in range( len( sels ) ) :
		
		currClip = clipSources[ random.randint( 0 , clipNum ) ]
		
		mc.clip( currClip , c=True )
	
		currNs = 'urukA%sCrowd'%ix
		
		mc.file( '/dsPipe/Lego_LOTR/Asset/Char/Animal/urukhaiA/Dev/Maya/wip/urukhaiLow.ma' ,
			r=True , ns=currNs ,
			options='v=0' )
		
		currRoot = '%s:rig_grp'%currNs
		
		mc.delete( mc.parentConstraint( sels[ ix ] , currRoot ) )
		mc.parent( currRoot , sels[ ix ] )
		
		mc.clip( '%s:uruk_character'%currNs ,
			pasteInstance=True ,
			sc=1 ,
			s=random.randint(0,11) ,
			mapMethod='byAttrName' )

def importAllMaInFolder() :
	
	dir = '/dsPipe/Lego_LOTR/Asset/Char/Animal/urukhaiA/Dev/Maya/wip/animClips'
	
	for each in os.listdir( dir ) :
		
    		if each[-3:] == '.ma' :
			print 'Importing %s' % each
			mc.file( '%s/%s' % ( dir , each ) ,
				i=True , type='mayaAscii' )

def getTweakFromSelectedMesh() :
	
	sels = mc.ls( sl=True )
	geoToTweak = {}
	
	for sel in sels :
		
		shape = mc.listRelatives( sel , shape=True )[0]
		for cnnc in mc.listConnections( shape , d=True , s=False ) :
			if 'tweak' in cnnc :
				geoToTweak[ sel ] = cnnc
	
	return geoToTweak

def geoCrowd() :
	# Import referenced characters
	# select geometries then run script
	sels = mc.ls( sl=True )
	ctrls = []

	for sel in sels :
		
		ns = sel.split( ':' )[0]
		
		if not ns in ctrls :
			
			ctrl = mc.circle( nr=(0,1,0) , ch=False )[0]
			grp = mc.group( ctrl )
			root = '%s:Root_Ctrl' % ns
			
			mc.delete( mc.parentConstraint( root , grp ) )
			
			ctrl = mc.rename( ctrl , ns )
			mc.rename( grp , '%s_grp' % ns )
			ctrls.append( ns )
			
		attrs = ('tx','ty','tz','rx','ry','rz','sx','sy','sz')
		for attr in attrs :
			
			if mc.getAttr( '%s.%s' % ( sel , attr ) , l=True ) :
				mc.setAttr( '%s.%s' % ( sel , attr ) , l=False )
		
		mc.select( sel , r=True )
		mc.duplicate( sel , rr=True )
		geo = mc.ls( sl=True , l=True )[0]
		mc.parent( geo , ctrl )

def addMainGroupAttribute() :
	
	# Add system attributes to the main rig group.
	# Input		: None
	# Output	: Added attributes to rig group.
	nodes = mc.ls()
	rigGrp = 'Rig_Grp'
	for node in nodes :
		if node.endswith( 'rig_grp' ) :
			rigGrp = node

	attrs =	( 	'assetName' , 'assetType' , 'assetSubType' ,
				 'project' ,
				'assetPath' , 'exportType' ,
				'lod'
			)

	for attr in attrs :
		if not mc.objExists( '%s.%s' % ( rigGrp , attr ) ) :
			mc.addAttr( rigGrp , ln=attr , dt='string' )
