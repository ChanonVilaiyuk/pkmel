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
	fn = '%s/ctrlAttr.txt' % dataFld
	writeCtrlAttr( ctrls , fn )
	
	print 'Exporting all control attribute is done.'

def readAllCtrl( search = '' , replace = '' ) :
	
	dataFld = pc.getDataFld()
	
	if not os.path.isdir( dataFld ) :
   		 os.mkdir( dataFld )
	
	ctrls = mc.ls( "*trl" )
	fn = '%s/ctrlAttr.txt' % dataFld
	readCtrlAttr( fn , search = search , replace = replace )
	
	print 'Importing all control attribute is done.'

def writeCtrlAttr( ctrls = [] , fn = '' ) :
	
	fid = open( fn , 'w' )
	
	ctrlDct = {}
	
	for ctrl in ctrls :
		
		currCtrl = pc.Dag( ctrl )
		currShape = pc.Dag( currCtrl.shape )
		
		for each in ( currCtrl , currShape ) :
			
			if mc.objExists( each ) :
				attrs = mc.listAttr( each , ud=True )
				keyableAttrs = mc.listAttr( each , k=True )
				lockAttrs = mc.listAttr( each , l=True )
				
				if attrs :
					for attr in attrs :
						currCtrlAttr = '%s.%s' % ( each , attr )
						ctrlDct[ currCtrlAttr ] = [ False , False ]
						
						if lockAttrs and ( attr in lockAttrs ) :
							ctrlDct[ currCtrlAttr ][0] = True
						if keyableAttrs and ( attr in keyableAttrs ) :
							ctrlDct[ currCtrlAttr ][1] = True
	
	pickle.dump( ctrlDct , fid )
	fid.close()

def readCtrlAttr( fn = '' , search = '' , replace = '' ) :
	
	fid = open( fn , 'r' )
	ctrlDct = pickle.load( fid )
	fid.close()
	
	for key in ctrlDct.keys() :
		
		if search :
			currCtrlAttr = key.replace( search , replace )
		else :
			currCtrlAttr = key
		
		if mc.objExists( currCtrlAttr ) :
			
			keyable = ctrlDct[ currCtrlAttr ][1]
			lock = ctrlDct[ currCtrlAttr ][0]
			
			mc.setAttr( currCtrlAttr , k=keyable )
			mc.setAttr( currCtrlAttr , l=lock )





















