import maya.cmds as mc
import maya.mel as mm
from functools import partial

def run() :
	# WeightScaler call back
	ui = WeightScaler()
	ui.show()

class WeightScaler( object ) :
	
	def __init__( self ) :
		print 'Script for scaling minimum skin weight value.\nCreated by peckpeckpeckpeckpeck@gmail.com'
		self.ui = 'WeightScaler'
		self.win = '%sWin' % self.ui

	def show( self ) :
		
		if mc.window( self.win , exists=True ) :
			mc.deleteUI( self.win )
		
		mc.window( self.win , t='WeightScaler' , rtf=True )
		
		mc.columnLayout( '%sMainCL'%self.ui , adj=True , columnAttach=('both', 1) )
		
		mc.floatField( '%sScaleValFF'%self.ui )
		
		mc.separator()
		
		mc.button( l='Scale' ,
				h=50 ,
				c=partial( self.scaleMin ) )
		
		mc.showWindow( self.win )
		mc.window( self.win , e=True , w=126 , h=126 )
	
	def getScaleVal( self ) :
		
		return mc.floatField( '%sScaleValFF'%self.ui , q=True , v=True )
		
	def scaleMin( self , arg=None ) :
		
		val = self.getScaleVal()
		
		vtcs = mc.ls( sl=True , fl=True )
		
		for vtc in vtcs :
			
			geo = vtc.split( '.' )[0]
			skn = mm.eval( 'findRelatedSkinCluster( "%s" )' % geo )
			
			mc.setAttr( '%s.normalizeWeights' % skn , False )
			
			infs = mc.skinCluster( skn , q=True , inf=True )
			skinVals = mc.skinPercent( skn , vtc , q = True , v = True )
			
			maxVal = sorted( skinVals )[-1]
			
			minVal = 1
			for skinVal in skinVals :
				if skinVal and skinVal < minVal :
					minVal = skinVal
			
			minId = skinVals.index( minVal )
			maxId = skinVals.index( maxVal )
			
			newMin = minVal * val
			newMax = maxVal + ( minVal - newMin )
			
			mc.skinPercent( skn , vtc , tv = ( infs[minId] , newMin ) )
			mc.skinPercent( skn , vtc , tv = ( infs[maxId] , newMax ) )
			
			mc.setAttr( '%s.normalizeWeights' % skn , True )

