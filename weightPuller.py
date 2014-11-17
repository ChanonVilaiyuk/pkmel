# Weight puller
import maya.cmds as mc
import maya.mel as mm
from functools import partial

def run() :
	# WeightPuller call back
	ui = WeightPuller()
	ui.show()

class WeightPuller( object ) :
	
	def __init__( self ) :
		print 'Script for searching and replacing skin weight value.\nCreated by peckpeckpeckpeckpeck@gmail.com'
		self.ui = 'pkWeightPuller'
		self.win = '%sWin' % self.ui
	
	def show( self ) :
		
		oSrch = 'LFT'
		oRep = 'RGT'
		oMul = 0
		
		if mc.window( self.win , exists=True ) :
			oSrch = mc.textField( '%sSrchTF'%self.ui , q=True , tx=True )
			oRep = mc.textField( '%sRepTF'%self.ui , q=True , tx=True )
			oMul = mc.floatField( '%sMultFF'%self.ui , q=True , v=True )
			mc.deleteUI( self.win )
		
		mc.window( self.win , t='pkWeightPuller' , rtf=True )
		
		mc.columnLayout( '%sMainCL'%self.ui , adj=True )
		
		mc.text( l='Search for' , align='center' )
		mc.textField( '%sSrchTF'%self.ui , tx=oSrch )
		mc.text( l='Replace with' , align='center' )
		mc.textField( '%sRepTF'%self.ui , tx=oRep )
		mc.button( '%sSwapBUT'%self.ui , l='Swap' , c=partial( self.swap ) )
		mc.floatField( '%sMultFF'%self.ui , minValue=0 , maxValue=1 , v=oMul )
		mc.button( '%sBUT'%self.ui , l='Pull' , c=partial( self.pull ) )
		
		mc.showWindow( self.win )
		mc.window( self.win , e=True , w=180 )
		mc.window( self.win , e=True , h=180 )
		
	def swap( self , arg=None ) :
		# Swap search and replace text field's value
		srch = mc.textField( '%sSrchTF'%self.ui , q=True , tx=True )
		rep = mc.textField( '%sRepTF'%self.ui , q=True , tx=True )
		
		mc.textField( '%sSrchTF'%self.ui , edit=True , tx=rep )
		mc.textField( '%sRepTF'%self.ui , edit=True , tx=srch )
	
	def pull( self , arg=None ) :
		
		# Info
		srch = mc.textField( '%sSrchTF'%self.ui , q=True , tx=True )
		rep = mc.textField( '%sRepTF'%self.ui , q=True , tx=True )
		mult = mc.floatField( '%sMultFF'%self.ui , q=True , v=True )
		
		sels = mc.ls( sl=True , fl=True )
		
		# Collect all skin cluster nodes as a dict
		skns = []
		sknDct = {}
		
		for sel in sels :
			skn = mm.eval( 'findRelatedSkinCluster %s' % sel.split( '.' )[0] )
			sknDct[ sel ] = skn
			
			if not skn in skns :
				skns.append( skn )
		
		# Disable normalize weight for all skin cluster nodes
		for skn in skns :
			if mc.getAttr( '%s.normalizeWeights' % skn ) :
				mc.setAttr( '%s.normalizeWeights' % skn , 0 )
		
		# Iterate through selected points
		for sel in sels :
			
			skn = sknDct[sel]
			infs = mc.skinCluster( skn , q=True , inf=True )
			wghtVals = mc.skinPercent( skn , sel , q=True , v=True )
			
			# Iterate through all influence nodes
			for ix in range( len( infs ) ) :
				
				# If keyword is found in the current influence node
				if srch in infs[ix] :
					
					pullVal = wghtVals[ix] * mult
					srcVal = wghtVals[ix] - pullVal
					repInf = infs[ix].replace( srch , rep )
					
					# If replaced influence is member of object's influences
					if repInf in infs :
						mc.skinPercent( skn , sel , transformValue=[ ( infs[ix] , srcVal ) ,
							( repInf , pullVal ) ] )
					else :
						print '%s has no %s as its influence' % ( skn , repInf )
		
		# Enable normalize weights
		for skn in skns :
			if not mc.getAttr( '%s.normalizeWeights' % skn ) :
				mc.setAttr( '%s.normalizeWeights' % skn , 1 )

