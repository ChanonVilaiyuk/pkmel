# Main group module
import maya.cmds as mc
import pkmel.core as pc
import pkmel.rigTools as rigTools
reload( pc )
reload( rigTools )

class MainGroup( object ) :
	
	def __init__( self ) :
		# Template controls
		if mc.objExists( 'placement_tmpCtrl' ) :
			placement = pc.Dag( 'placement_tmpCtrl' )
			self.charSize = self.findCharHeight( placement ) / 28
		else :
			self.charSize = 1
		
		# Nodes
		self.rig_grp = pc.Null()
		self.still_grp = pc.Null()
		self.jnt_grp = pc.Null()
		self.ikh_grp = pc.Null()
		
		self.master_ctrl = pc.Control( 'square' )
		self.placement_ctrl = pc.Control( 'crossArrow' )
		self.placement_ctrl.add( ln='size' , k=True , dv=1 )
		for attr in ('sx','sy','sz') :
			self.placement_ctrl.attr( 'size' ) >> self.placement_ctrl.attr( attr )
		
		self.offset_ctrl = pc.Control( 'circle' )
		self.anim_grp = pc.Null()
		self.skin_grp = pc.Null()
		
		# Shape adjustment
		self.master_ctrl.color = 'yellow'
		self.placement_ctrl.color = 'yellow'
		self.offset_ctrl.color = 'yellow'
		self.placement_ctrl.scaleShape( self.charSize * 4 )
		
		# Hierarchy setting
		self.offset_ctrl.parent( self.placement_ctrl )
		self.anim_grp.parent( self.offset_ctrl )
		self.jnt_grp.parent( self.offset_ctrl )
		self.ikh_grp.parent( self.offset_ctrl )
		self.skin_grp.parent( self.offset_ctrl )
		self.placement_ctrl.parent( self.master_ctrl )
		self.master_ctrl.parent( self.rig_grp )
		self.still_grp.parent( self.rig_grp )
		
		# Rotate order adjustment
		self.master_ctrl.rotateOrder = 'xzy'
		self.placement_ctrl.rotateOrder = 'xzy'
		self.offset_ctrl.rotateOrder = 'xzy'
		
		# Rig cleanup
		for attr in ('tx','ty','tz','rx','ry','rz','sx','sy','sz') :
			self.rig_grp.attr( attr ).lockHide()
			self.still_grp.attr( attr ).lockHide()
			self.anim_grp.attr( attr ).lockHide()
			self.jnt_grp.attr( attr ).lockHide()
			self.ikh_grp.attr( attr ).lockHide()
			self.skin_grp.attr( attr ).lockHide()
		
		self.jnt_grp.attr( 'v' ).v = 0
		self.ikh_grp.attr( 'v' ).v = 0
		
		for attr in ('sx','sy','sz','v') :
			self.offset_ctrl.attr( attr ).lockHide()
			self.placement_ctrl.attr( attr ).lockHide()
		
		self.master_ctrl.attr( 'v' ).lockHide()

	def findCharHeight( self , placement = '' ) :
		# Finding the height of the character
		chldrn = pc.listAllChildren( placement )
		height = 0
		
		for chld in chldrn :
			curr = pc.Dag( chld )
			if curr.ws and curr.ws[ 1 ] > height :
				height = curr.ws[ 1 ]
		
		return height