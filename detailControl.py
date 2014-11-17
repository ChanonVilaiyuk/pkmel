import maya.cmds as mc
import pkmel.core as pc

def pointOnEdge( obj = '' , edge = '' ) :
	# Create transform node that will be sticked on given edge
	prxy = pc.Dag( obj )
	edgeId = ''.join( [ x for x in edge.split('.')[1] if x.isdigit() ] )
	msh = pc.Dag( edge.split('.')[0] )

	rvt = pc.Null()
	
	# Casting edge to two vertices
	vtxs = [ x for x in mc.polyInfo( edge , ev = True )[0].split( ':' )[1].split( ' ' ) if x.isdigit() ]
	
	# Curve from mesh edge
	cfme = pc.CurveFromMeshEdge()
	msh.attr('w') >> cfme.attr('im')
	cfme.attr('ei[0]').value = int( edgeId )
	
	# Point on curve info
	poci = pc.PointOnCurveInfo()
	cfme.attr('outputCurve') >> poci.attr('ic')
	poci.attr('position') >> rvt.attr('t')
	poci.attr('turnOnPercentage').value = 1
	
	# Finding world position
	vtxAPos = mc.xform( '%s.vtx[%s]' % ( msh , vtxs[0] ) , q = True , t = True , ws = True )
	vtxBPos = mc.xform( '%s.vtx[%s]' % ( msh , vtxs[1] ) , q = True , t = True , ws = True )
	prxyPos = prxy.ws
	
	# Finding length and length ratio
	edgeLen = pc.mag( ( vtxBPos[0] - vtxAPos[0] , vtxBPos[1] - vtxAPos[1] , vtxBPos[2] - vtxAPos[2] ) )
	prxyLen = pc.mag( ( prxyPos[0] - vtxAPos[0] , prxyPos[1] - vtxAPos[1] , prxyPos[2] - vtxAPos[2] ) )
	lenRatio = prxyLen / edgeLen
	
	poci.attr('parameter').value = lenRatio
	
	return rvt , cfme , poci

def jointOnTransform( obj = '' ) :
	# Create joint at given transform node
	obj = pc.Dag( obj )
	jnt = pc.Joint()
	grp = pc.group( jnt )
	grp.snapPoint( obj )
	
	return jnt , grp

def controlOnSelectedEdge() :
	# Create control that will be sticked on selected mesh edge
	# Select transform node, edge then run script
	sels = pc.lssl()
	
	ctrlPos = sels[0]
	edge = sels[1]
	
	jnt , jntGrp = jointOnTransform( ctrlPos )
	
	# Creating control
	ctrl , ctrlGrp = jointOnTransform( ctrlPos )
	ctrl.attr( 'radius' ).v = 0
	ctrl.lockHideAttrs( 'v' , 'radius' )
	mc.setAttr( ctrl.attr( 'radius' ) , k=False , channelBox=False )
	ctrlInvGrp = pc.group( ctrl )
	ctrlInvMdv = pc.MultiplyDivide()
	
	# Creating rivet
	rvt , cfme , poci = pointOnEdge( ctrlPos , edge )
	pntCon = pc.pointConstraint( rvt , ctrlGrp , mo = True )
	
	# Countering control's transformation
	ctrlInvMdv.attr('i2x').value = -1
	ctrlInvMdv.attr('i2y').value = -1
	ctrlInvMdv.attr('i2z').value = -1
	ctrl.attr('t') >> ctrlInvMdv.attr('i1')
	ctrlInvMdv.attr('o') >> ctrlInvGrp.attr('t')
	
	# Connecting control to joint
	ctrl.rotateOrder = jnt.rotateOrder
	ctrl.attr('t') >> jnt.attr('t')
	ctrl.attr('r') >> jnt.attr('r')
	ctrl.attr('s') >> jnt.attr('s')
	
	# Control's shape adjustment
	ctrl.createCurve( 'cube' )
	ctrl.color = 'red'

def autoName( charName = '' , elem = '' , side = '' ) :
	# Renaming facial control
	# Select control then run script
	if charName and ( not '_' in charName ) :
		charName += '_'
	
	ctrl = pc.lssl()[ 0 ]
	ctrlInvGrp = mc.listRelatives( ctrl , p = True )[0]
	ctrlZroGrp = mc.listRelatives( ctrlInvGrp , p = True )[0]
	
	ctrlZroGrpPntCon = mc.listConnections( ctrlZroGrp , d = True , s = False)[0]
	
	sknJnt = mc.listConnections( '%s.r' % ctrl , d = True , s = False )[0]
	sknJntZroGrp = mc.listRelatives( sknJnt , p = True )[0]
	ctrlInvMdv = mc.listConnections( '%s.t' % ctrlInvGrp , d = False , s = True )[0]
	
	rvt = mc.listConnections( '%s.target[0].targetTranslate' % ctrlZroGrpPntCon , d = False , s = True )[0]
	poci = mc.listConnections( '%s.translate' % rvt , d = False , s = True )[0]
	cfme = mc.listConnections( '%s.ic' % poci , d = False , s = True )[0]
	
	# Renaming
	mc.rename( ctrl , '%s%sDtl%s_ctrl' % ( charName , elem , side ) )
	mc.rename( ctrlInvGrp , '%s%sDtlCtrlInv%s_grp' % ( charName , elem , side ) )
	mc.rename( ctrlZroGrp , '%s%sDtlCtrlZro%s_grp' % ( charName , elem , side ) )
	mc.rename( ctrlZroGrpPntCon , '%s%sDtlCtrlZroGrp%s_pntCons' % ( charName , elem , side ) )
	mc.rename( sknJnt , '%s%sDtl%s_jnt' % ( charName , elem , side ) )
	mc.rename( sknJntZroGrp , '%s%sDtlJntZro%s_grp' % ( charName , elem , side ) )
	mc.rename( ctrlInvMdv , '%s%sDtlCtrlInv%s_mdv' % ( charName , elem , side ) )
	mc.rename( rvt , '%s%sDtlRvt%s_grp' % ( charName , elem , side ) )
	mc.rename( poci , '%s%sDtl%s_poci' % ( charName , elem , side ) )
	mc.rename( cfme , '%s%sDtl%s_cfme' % ( charName , elem , side ) )

def autoNameList( charname='' , elem='' , side='' ) :
	
	sels = mc.ls( sl=True )
	
	for ix in range( 0 , len( sels ) ) :
		
		currElem = '%s%s' % ( elem , str( ix+1 ) )
		mc.select( sels[ ix ] , r=True )
		autoname( charName = '' , elem = currElem , side = side )

