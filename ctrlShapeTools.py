import maya.cmds as mc
import os
import pickle
import pkmel.core as pc
reload( pc )

def writeAllCtrl() :
	
	dataFld = pc.getDataFld()
	
	if not os.path.isdir( dataFld ) :
   		 os.mkdir( dataFld )
	
	ctrls = mc.ls( "*trl" )
	fn = '%s/ctrlShape.txt' % dataFld
	writeCtrlShape( ctrls , fn )
	
	print 'Exporting all control shape is done.'

def readAllCtrl( search = '' , replace = '' ) :
	
	dataFld = pc.getDataFld()
	
	if not os.path.isdir( dataFld ) :
   		 os.mkdir( dataFld )
	
	ctrls = mc.ls( "*trl" )
	fn = '%s/ctrlShape.txt' % dataFld
	print fn
	readCtrlShape( ctrls , fn , search = search , replace = replace )
	
	print 'Importing all control shape is done.'

def writeCtrlShape( ctrls = [] , fn = '' ) :
	
	fid = open( fn , 'w' )
	
	ctrlDct = {}
	
	for ctrl in ctrls :
		
		shapes = mc.listRelatives( ctrl , s = True )
		
		if type( shapes ) == type( [] ) and mc.nodeType( shapes[0] ) == 'nurbsCurve' :
			
			cv = mc.getAttr( '%s.spans' % shapes[0] ) + mc.getAttr( '%s.degree' % shapes[0] )
		
			for ix in range( 0 , cv ) :
				
				cvName = '%s.cv[%s]' % ( shapes[0] , str( ix ) )
				ctrlDct[ cvName ] = mc.xform( cvName , q = True , os = True , t = True )
			
	pickle.dump( ctrlDct , fid )
	fid.close()

def readCtrlShape( ctrls = [] , fn = '' , search = '' , replace = '' ) :
	
	fid = open( fn , 'r' )
	ctrlDct = pickle.load( fid )
	fid.close()
	
	for key in ctrlDct.keys() :
		# print key
		if search :
			currVtx = key.replace( search , replace )
		else :
			currVtx = key
		
		obj = currVtx.split('.')[0]
		
		if mc.objExists( obj ) :
			mc.xform( currVtx , os = True , t = ctrlDct[ currVtx ] )