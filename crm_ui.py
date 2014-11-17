import maya.cmds as mc
import pkmel.core as pc
reload( pc )
import pkmel.rigTools as rigTools
reload( rigTools )
import pkmel.mainGroup as pmain
reload( pmain )
import pkmel.rootRig as proot
reload( proot )
import pkmel.pelvisRig as ppelv
reload( ppelv )
import pkmel.spineRig as pspi
reload( pspi )
import pkmel.neckRig as pneck
reload( pneck )
import pkmel.headRig as phead
reload( phead )
import pkmel.clavicleRig as pclav
reload( pclav )
import pkmel.armRig as parm
reload( parm )
import pkmel.legRig as pleg
reload( pleg )
import pkmel.fingerRig as pfngr
reload( pfngr )
import pkmel.thumbRig as pthmb
reload( pthmb )
import pkmel.ribbon as prbn
reload( prbn )
import pkmel.humanSpineRig as phspi
reload( phspi )
import pkmel.backLegRig as pbleg
reload( pbleg )
import pkmel.fkRig as pfk
reload(pfk)



# from nuTools.manager import chaRig as cr
from nuTools import misc
import pymel.core as pm
import maya.OpenMaya as OpenMaya
import sys

class BaseUi(object):
	def __init__(self, parent):
		self.uiparent = parent
		self.rigCol = None
		self._REQUIRE = {}

		#rig objs
		self.rigParent = None 
		self.animGrp = None
		self.jntGrp = None
		self.ikhGrp = None
		self.skinGrp = None
		self.stillGrp = None

	
	def create(self):
		with pm.columnLayout(adj=True, parent=self.uiparent, rs=2) as self.masterCol:
			with pm.rowColumnLayout(nc=2, co=[(1, 'left', 77), (2, 'left', 5)]):
				pm.text(l='Rig Scale: ')
				self.rigSizeFloatSliderGrp = pm.floatSliderGrp(f=True, v=1, max=5, min=0.01, fs=0.01, cw=([1,33], [2,110]), pre=2)
			with pm.rowColumnLayout(nc=4, co=[(1, 'left', 105), (2, 'left', 5), (3, 'left', 12), (4, 'left', 5)]):
				pm.text(l='elem')
				self.elemTxtFld = pm.textField(w=65, ed=True)
				pm.text(l='side')
				with pm.optionMenu(w=40) as self.sideMenu:
					pm.menuItem(l='')
					pm.menuItem(l='LFT')
					pm.menuItem(l='RGT')
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 95), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='parent')
				self.rigParentTxtFld = pm.textField(w=142, ed=False)
				self.loadParentButt = pm.button(l='<<', c=pm.Callback(self.loadRigParent))

			with pm.columnLayout(adj=True) as self.mainCol:
				#waiting for extensions from different rig modules
				pass
			with pm.frameLayout(label='Rig Groups', borderStyle='out', mh=5, mw=5, cll=True, cl=True, w=375):
				with pm.rowColumnLayout(nc=3, co=[(1, 'left', 80), (2, 'left', 5), (3, 'left', 5)]):
					pm.text(l='animGrp')
					self.animGrpTxtFld = pm.textField(ed=False)
					self.loadAnimGrpButt = pm.button(l='<<', c=pm.Callback(self.loadAnimGrp))
					pm.text(l='jntGrp')
					self.jntGrpTxtFld = pm.textField(ed=False)
					self.loadJntGrpButt = pm.button(l='<<', c=pm.Callback(self.loadJntGrp))
					pm.text(l='ikhGrp')
					self.ikhGrpTxtFld = pm.textField(ed=False)
					self.loadIkhGrpButt = pm.button(l='<<', c=pm.Callback(self.loadIkhGrp))
					pm.text(l='skinGrp')
					self.skinGrpTxtFld = pm.textField(ed=False)
					self.loadSkinGrpButt = pm.button(l='<<', c=pm.Callback(self.loadSkinGrp))
					pm.text(l='stillGrp')
					self.stillGrpTxtFld = pm.textField(ed=False)
					self.loadStillGrpButt = pm.button(l='<<', c=pm.Callback(self.loadStillGrp))


	def checkRequires(self):
		missingObjs = []

		for varName, obj in self._REQUIRE.iteritems():
			if not obj:
				missingObjs.append(varName)

		if missingObjs:
			OpenMaya.MGlobal.displayError('%s  are missing!' %missingObjs),
			return False
		return True
		

	def clearUi(self):
		pm.deleteUI(self.mainCol)

	def getSide(self):
		return self.sideMenu.getValue()

	def getElem(self):
		txt = self.elemTxtFld.getText()
		if not txt:
			txt = ''
		return txt

	def getRigScale(self):
		return self.rigSizeFloatSliderGrp.getValue()

	def loadRigParent(self, sel=None):
		if not sel:
			sel = misc.getSel()
		if not sel:
			self.rigParent = None
			self.rigParentTxtFld.setText('')
			return
		self.rigParent = sel
		self.rigParentTxtFld.setText(sel.nodeName())

	def loadAnimGrp(self, sel=None):
		if not sel:
			sel = misc.getSel()
		if not sel:
			self.animGrp = None
			self.animGrpTxtFld.setText('')
			return
		self.animGrp = sel
		self.animGrpTxtFld.setText(self.animGrp.nodeName())
	
	def loadJntGrp(self, sel=None):
		if not sel:
			sel = misc.getSel()
		if not sel:
			self.jntGrp = None
			self.jntGrpTxtFld.setText('')
			return
		self.jntGrp = sel
		self.jntGrpTxtFld.setText(sel.nodeName())

	def loadIkhGrp(self, sel=None):
		if not sel:
			sel = misc.getSel()
		if not sel:
			self.ikhGrp = None
			self.ikhGrpTxtFld.setText('')
			return
		self.ikhGrp = sel
		self.ikhGrpTxtFld.setText(sel.nodeName())

	def loadSkinGrp(self, sel=None):
		if not sel:
			sel = misc.getSel()
		if not sel:
			self.skinGrp = None
			self.skinGrpTxtFld.setText('')
			return
		self.skinGrp = sel
		self.skinGrpTxtFld.setText(sel.nodeName())

	def loadStillGrp(self, sel=None):
		if not sel:
			sel = misc.getSel()
		if not sel:
			self.stillGrp = None
			self.stillGrpTxtFld.setText('')
			return
		self.stillGrp = sel
		self.stillGrpTxtFld.setText(sel.nodeName())

	def loadObjsToTxtFld(self, objs, txtFld):
		objNames = []
		if not objs:
			txtFld.setText('')
			return
		for obj in objs:
			objNames.append(obj.nodeName())
		txtFld.setText(str(objNames))

	def loadObjToTxtFld(self, obj, txtFld):
		txtFld.setText(obj.nodeName())

	def clearElemSideTxtFld(self):
		self.elemTxtFld.setText('')
		self.sideMenu.setValue('')

class mainGroup(BaseUi):
	_DESCRIPTION = """Create necessary groups.
	METHOD: None
	REQUIRES: None"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			pm.text(l='Click the button below to create.')

		self.baseUi.clearElemSideTxtFld()


	def call(self):
		mainGroup = pmain.MainGroup()
		rigTools.nodeNaming( mainGroup , charName = '' , elem = self.baseUi.getElem() , side = '' )

		#auto load groups
		self.baseUi.loadAnimGrp(sel=pm.PyNode(mainGroup.anim_grp))
		self.baseUi.loadJntGrp(sel=pm.PyNode(mainGroup.jnt_grp))
		self.baseUi.loadIkhGrp(sel=pm.PyNode(mainGroup.ikh_grp))
		self.baseUi.loadSkinGrp(sel=pm.PyNode(mainGroup.skin_grp))
		self.baseUi.loadStillGrp(sel=pm.PyNode(mainGroup.still_grp))



class rootRig(BaseUi):
	_DESCRIPTION = """Single joint rig. Ideal for the root joint.
	METHOD: Constraint
	PARENT: None
	REQUIRES: 1 joints

	[ root ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sel = misc.getSel(selType='joint', num=1)
		if not sel:
			self.tmpJnts = None
			self.tmpJntsTxtFld.setText('')
			return
		self.tmpJnts = sel
		self.loadObjToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Anim Grp':self.baseUi.animGrp, 
						'Skin Grp':self.baseUi.skinGrp }
		if not self.checkRequires():
			return

		rootRig = proot.RootRig( animGrp = self.baseUi.animGrp.longName() ,
								skinGrp = self.baseUi.skinGrp.longName() ,
								charSize = self.baseUi.getRigScale(),
								tmpJnt = self.tmpJnts.longName() )

		rigTools.nodeNaming( rootRig ,
							charName = '' ,
							elem = self.baseUi.getElem() ,
							side = self.baseUi.getSide() )

class pelvisRig(BaseUi):
	_DESCRIPTION = """Single joint rig. Ideal for the pelvis.
	METHOD: Constraint
	PARENT: root(root_jnt)
	REQUIRES: 1 joints

	[ pelvis ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sel = misc.getSel(selType='joint', num=1)
		if not sel:
			self.tmpJnts = None
			self.tmpJntsTxtFld.setText('')
			return

		self.tmpJnts = sel
		self.loadObjToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt': self.tmpJnts,
						'Parent': self.baseUi.rigParent,  
						'Anim Grp': self.baseUi.animGrp, 
						'Skin Grp': self.baseUi.skinGrp}
		if not self.checkRequires():
			return

		pelvisRig = ppelv.PelvisRig( parent = self.baseUi.rigParent.longName()  ,
									animGrp = self.baseUi.animGrp.longName() ,
									skinGrp = self.baseUi.skinGrp.longName() ,
									charSize = self.baseUi.getRigScale() ,
									tmpJnt = self.tmpJnts.longName() )

		rigTools.nodeNaming( pelvisRig ,
							charName = '' ,
							elem = self.baseUi.getElem() ,
							side = self.baseUi.getSide() )



class humanSpineRig(BaseUi):
	_DESCRIPTION = """Perfect for biped back.
	METHOD: FK
	PARENT: root(root_jnt)
	REQUIRES: 5 joints

	[ spine1, spine2, spine3, spine4, neck ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []
		self.defaultAxis = 'y'

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=2, co=[(1, 'left', 135), (2, 'left', 5)]):
				pm.text(l='axis')
				with pm.optionMenu(w=60) as self.axisMenu:
					pm.menuItem(l='x')
					pm.menuItem(l='y')
					pm.menuItem(l='z')
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.axisMenu.setValue(self.defaultAxis)
		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=5)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 5:
			OpenMaya.MGlobal.displayWarning('This module reqires 5 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Jnt Grp':self.baseUi.jntGrp, 
						'Ikh Grp':self.baseUi.ikhGrp, 
						'Skin Grp':self.baseUi.skinGrp, 
						'Still Grp':self.baseUi.stillGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		spineRig = phspi.HumanSpineRig( parent = self.baseUi.rigParent.longName() ,
						animGrp = self.baseUi.animGrp.longName() ,
						jntGrp = self.baseUi.jntGrp.longName() ,
						ikhGrp = self.baseUi.ikhGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						stillGrp = self.baseUi.stillGrp.longName() ,
						ax = self.axisMenu.getValue() ,
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( spineRig ,
					charName = '' ,
					elem = self.baseUi.getElem() ,
					side =  self.baseUi.getSide() )


class neckRig(BaseUi):
	_DESCRIPTION = """2 joint rig with optional 3 or 5 ribbon inbetween.
	METHOD: FK, Ribbon
	PARENT: Tip of spine(spine5)
	REQUIRES: 2 joints

	[ neck1, head1 ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []
		self.defaultAxis = 'y'

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=2, co=[(1, 'left', 155), (2, 'left', 5)]):
				pm.text(l='axis')
				with pm.optionMenu(w=60) as self.axisMenu:
					pm.menuItem(l='x')
					pm.menuItem(l='y')
					pm.menuItem(l='z')
			with pm.columnLayout(adj=True, rs=2, co=['left', 165]):	
				self.ribbonChkBox = pm.checkBox(l='Ribbon Lo/Hi', v=False)
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

			

		self.axisMenu.setValue(self.defaultAxis)
		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=2)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 2:
			OpenMaya.MGlobal.displayWarning('This module reqires 2 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Jnt Grp':self.baseUi.jntGrp, 
						'Ikh Grp':self.baseUi.ikhGrp, 
						'Skin Grp':self.baseUi.skinGrp, 
						'Still Grp':self.baseUi.stillGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		neckRig = pneck.NeckRig( parent = self.baseUi.rigParent.longName() ,
						animGrp = self.baseUi.animGrp.longName() ,
						jntGrp = self.baseUi.jntGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						stillGrp = self.baseUi.stillGrp.longName() ,
						ribbon = self.ribbonChkBox.getValue(),
						ax = self.axisMenu.getValue() ,
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( neckRig ,
					charName = '' ,
					elem = self.baseUi.getElem() ,
					side =  self.baseUi.getSide() )

		rigTools.dummyNaming( obj = neckRig.neckRbn ,
			attr = 'rbn' ,
			dummy = 'neckRbn' ,
			charName = '' ,
			elem = self.baseUi.getElem() ,
			side = self.baseUi.getSide() )


class headRig(BaseUi):
	_DESCRIPTION = """Creature head with optional eyeball and jaw rig.
	METHOD: FK, Aim
	PARENT: Tip of neck(neck2)
	REQUIRES: 2-12 joints

	[ head1, head2 ]
	[eyeLFT, eyeRHT]
	[eyeTrgt, eyeTrgtLFT, eyeTrgtRHT]
	[jaw01UP, jaw02UP]
	[jaw01LO, jaw02LO, jaw03LO]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = [None] * 12 #list with 12 empty spaces
		self.defaultAxis = 'y'
		self.spaceGrp = None

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.columnLayout(adj=True, rs=2, co=['left', 165]):	
				self.eyeRigChkBox = pm.checkBox(l='Eyes Rig', v=True)
				self.jawRigChkBox = pm.checkBox(l='Jaw Rig', v=True)
			pm.text(l='Load tmpJnts')
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 20), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='head(2)')
				self.headJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadHeadJntButt = pm.button(l='<<', c=pm.Callback(self.loadHeadTmpJnts, 'head'))

				pm.text(l='eyeballs(2)')
				self.eyeBallJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadEyeBallJntButt = pm.button(l='<<', c=pm.Callback(self.loadHeadTmpJnts, 'eyeballs'))

				pm.text(l='eyeTrgts(3)')
				self.eyeTrgtJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadEyeTrgtJntButt = pm.button(l='<<', c=pm.Callback(self.loadHeadTmpJnts, 'eyeTrgts'))

				pm.text(l='jawUP(2)')
				self.jawUpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadJawUpJntButt = pm.button(l='<<', c=pm.Callback(self.loadHeadTmpJnts, 'jawUP'))

				pm.text(l='jawLO(3)')
				self.jawLoJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadJawLoJntButt = pm.button(l='<<', c=pm.Callback(self.loadHeadTmpJnts, 'jawLO'))
			
			pm.text(l='load space grp.(optional)')
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='spaceGrp')
				self.spaceGrpTxtFld = pm.textField(w=230, ed=False)
				self.loadSpaceGrpButt = pm.button(l='<<', c=pm.Callback(self.loadSpaceGrp))

		self.baseUi.clearElemSideTxtFld()

	def loadHeadTmpJnts(self, part):
		sels = misc.getSel(selType='joint', num='inf')

		if part == 'head':
			try:
				self.loadObjsToTxtFld(sels, self.headJntsTxtFld)
				self.tmpJnts[0] = sels[0]
				self.tmpJnts[1] = sels[1]
				if len(sels) != 2:
					OpenMaya.MGlobal.displayWarning('Need 2 joints for head. [head1, head2]')
			except: self.tmpJnts[0], self.tmpJnts[1] = None, None

		elif part == 'eyeballs':
			try:
				self.loadObjsToTxtFld(sels, self.eyeBallJntsTxtFld)
				self.tmpJnts[2] = sels[0]
				self.tmpJnts[3] = sels[1]
				if len(sels) != 2:
					OpenMaya.MGlobal.displayWarning('Need 2 joints for eyeBalls. [LFT, RHT]')
			except: self.tmpJnts[2], self.tmpJnts[3] = None, None
			
		elif part == 'eyeTrgts':
			try:
				self.loadObjsToTxtFld(sels, self.eyeTrgtJntsTxtFld)
				self.tmpJnts[9] = sels[0]
				self.tmpJnts[10] = sels[1]
				self.tmpJnts[11] = sels[2]
				if len(sels) != 3:
					OpenMaya.MGlobal.displayWarning('Need 3 joints for eyeTrgts. [MID, LFT, RHT]')
			except: self.tmpJnts[9], self.tmpJnts[10], self.tmpJnts[11] = None, None, None
			
		elif part == 'jawUP':
			try:
				self.loadObjsToTxtFld(sels, self.jawUpJntsTxtFld)
				self.tmpJnts[7] = sels[0]
				self.tmpJnts[8] = sels[1]
				if len(sels) != 2:
					OpenMaya.MGlobal.displayWarning('Need 2 joints for jawUP. [jaw1, jaw2]')
			except: self.tmpJnts[7], self.tmpJnts[8] = None, None
			
		elif part == 'jawLO':
			try:
				self.loadObjsToTxtFld(sels, self.jawLoJntsTxtFld)
				self.tmpJnts[4] = sels[0]
				self.tmpJnts[5] = sels[1]
				self.tmpJnts[6] = sels[2]
				if len(sels) != 3:
					OpenMaya.MGlobal.displayWarning('Need 3 joints for jawLO. [jaw1, jaw2, jaw3]')
			except: self.tmpJnts[4], self.tmpJnts[5], self.tmpJnts[6] = None, None, None
			

	def loadSpaceGrp(self):
		sel = misc.getSel()
		self.loadObjToTxtFld(sel, self.spaceGrpTxtFld)
		self.spaceGrp = sel

	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent.longName(), 
						'Anim Grp':self.baseUi.animGrp,  
						'Skin Grp':self.baseUi.skinGrp}

		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			if j:
				tmpJntsLongNames.append(j.longName())

		headRig = phead.HeadRig( parent = self.baseUi.rigParent.longName() ,
						animGrp = self.baseUi.animGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						spaceGrp = self.spaceGrp.longName(),
						eyeRig = self.eyeRigChkBox.getValue(),
						jawRig = self.jawRigChkBox.getValue(),
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( headRig ,
					charName = '' ,
					elem = self.baseUi.getElem() ,
					side =  self.baseUi.getSide() )

class clavicleRig(BaseUi):
	_DESCRIPTION = """2 joint rig. Ideal for clavicle.
	METHOD: FK
	PARENT: spine joint(spine4)
	REQUIRES: 2 joints

	[ clav, upArm ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=2)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 2:
			OpenMaya.MGlobal.displayWarning('This module requires 2 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Skin Grp':self.baseUi.skinGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		clavRig = pclav.ClavicleRig( parent = self.baseUi.rigParent.longName() ,
						side = self.baseUi.getSide(),
						animGrp = self.baseUi.animGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( clavRig ,
					charName = '' ,
					elem = self.baseUi.getElem(),
					side = self.baseUi.getSide() )


class armRig(BaseUi):
	_DESCRIPTION = """Human arm rig with optional 3 or 5 ribbon inbetween.
	METHOD: IK/FK, Ribbon
	PARENT: clavicle(clav2)
	REQUIRES: 5 joints

	[ upArm, elbow, wrist, hand, elbowPv ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))
			with pm.columnLayout(adj=True, rs=2, co=['left', 155]):	
				self.ribbonChkBox = pm.checkBox(l='Ribbon Lo/Hi', v=True)

		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=5)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 5:
			OpenMaya.MGlobal.displayWarning('This module requires 5 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Jnt Grp':self.baseUi.jntGrp, 
						'Ikh Grp':self.baseUi.ikhGrp, 
						'Skin Grp':self.baseUi.skinGrp, 
						'Still Grp':self.baseUi.stillGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		elem = self.baseUi.getElem()
		side = self.baseUi.getSide()

		armRig = parm.ArmRig( parent = self.baseUi.rigParent.longName() ,
						side = side ,
						animGrp = self.baseUi.animGrp.longName() ,
						jntGrp = self.baseUi.jntGrp.longName() ,
						ikhGrp = self.baseUi.ikhGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						stillGrp = self.baseUi.stillGrp.longName() ,
						ribbon = self.ribbonChkBox.getValue(),
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( armRig ,
					charName = '' ,
					elem = elem ,
					side =  side )

		rigTools.dummyNaming( obj = armRig.upArmRbn ,
					attr = 'rbn' ,
					dummy = 'upArmRbn' ,
					charName = '' ,
					elem =  elem ,
					side =  side )

		rigTools.dummyNaming( obj = armRig.forearmRbn ,
					attr = 'rbn' ,
					dummy = 'forearmRbn' ,
					charName = '' ,
					elem = elem ,
					side =  side )


class legRig(BaseUi):
	_DESCRIPTION = """Human leg rig with optional 3 or 5 ribbon inbetween.
	METHOD: IK/FK, Ribbon
	PARENT: pelvis(pelvis)
	REQUIRES: 9 joints

	[ upLeg, knee, ankle, 
	ball, toe, heel, 
	footIn, footOut, 
	kneePv ]
	"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.columnLayout(adj=True, rs=2, co=['left', 165]):	
				self.ribbonChkBox = pm.checkBox(l='Ribbon Lo/Hi', v=True)
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=9)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 9:
			OpenMaya.MGlobal.displayWarning('This module requires 9 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Jnt Grp':self.baseUi.jntGrp, 
						'Ikh Grp':self.baseUi.ikhGrp, 
						'Skin Grp':self.baseUi.skinGrp, 
						'Still Grp':self.baseUi.stillGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		elem = self.baseUi.getElem()
		side = self.baseUi.getSide()

		legRig = pleg.LegRig( parent = self.baseUi.rigParent.longName() ,
						side = side ,
						animGrp = self.baseUi.animGrp.longName() ,
						jntGrp = self.baseUi.jntGrp.longName() ,
						ikhGrp = self.baseUi.ikhGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						stillGrp = self.baseUi.stillGrp.longName() ,
						ribbon = self.ribbonChkBox.getValue(),
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( legRig ,
					charName = '' ,
					elem = elem ,
					side =  side )

		rigTools.dummyNaming( obj = legRig.upLegRbn ,
					attr = 'rbn' ,
					dummy = 'upLegRbn' ,
					charName = '' ,
					elem =  elem ,
					side =  side )

		rigTools.dummyNaming( obj = legRig.lowLegRbn ,
					attr = 'rbn' ,
					dummy = 'lowLegRbn' ,
					charName = '' ,
					elem = elem ,
					side =  side )


class fingerRig(BaseUi):
	_DESCRIPTION = """5 joint rig with handy attribute on sepcified ctrl. Ideal for fingers.
	METHOD: FK, preset attributes
	PARENT: hand(hand)
	REQUIRES: 5 joints

	[ finger1, finger2, finger3 finger4, finger5 ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []
		self.attrCtrl = None

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=2, co=[(1, 'left', 130), (2, 'left', 5)]):
				pm.text(l='Finger Name')
				with pm.optionMenu(w=60) as self.fingerNameMenu:
					pm.menuItem(l='index')
					pm.menuItem(l='middle')
					pm.menuItem(l='ring')
					pm.menuItem(l='pinky')
					pm.menuItem(l='thumb')
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='attrCtrl')
				self.attrCtrlTxtFld = pm.textField(w=230, ed=False)
				self.loadAttrCtrlButt = pm.button(l='<<', c=pm.Callback(self.loadAttrCtrl))
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.baseUi.clearElemSideTxtFld()


	def loadAttrCtrl(self):
		sel = misc.getSel()
		if not sel.getShape():
			return
		self.loadObjToTxtFld(sel, self.attrCtrlTxtFld)
		self.attrCtrl = sel

	def getFingerName(self):
		fingerName = self.fingerNameMenu.getValue()
		if not fingerName:
			fingerName = 'finger'
		return fingerName

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=5)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 5:
			OpenMaya.MGlobal.displayWarning('This module requires 5 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)

	def setFingerAttr(self, fingerName, ctrlShp):
		if fingerName == 'index':
			ctrlShp.attr('%s2FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s3FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s4FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s2CupRx' % fingerName ).value = -1
			ctrlShp.attr('%s3CupRx' % fingerName ).value = -1
			ctrlShp.attr('%s4CupRx' % fingerName ).value = -1
			ctrlShp.attr('%s2Spread' % fingerName ).value = -9
			ctrlShp.attr('%sBaseSpread' % fingerName ).value = -9

		elif fingerName == 'middle':
			ctrlShp.attr('%s2FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s3FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s4FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s2CupRx' % fingerName ).value = -2.5
			ctrlShp.attr('%s3CupRx' % fingerName ).value = -2.5
			ctrlShp.attr('%s4CupRx' % fingerName ).value = -2.5

		elif fingerName == 'ring':
			ctrlShp.attr('%s2FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s3FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s4FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s2CupRx' % fingerName ).value = -3.5
			ctrlShp.attr('%s3CupRx' % fingerName ).value = -3.5
			ctrlShp.attr('%s4CupRx' % fingerName ).value = -3.5
			ctrlShp.attr('%s2Spread' % fingerName ).value = 4.5
			ctrlShp.attr('%sBaseSpread' % fingerName ).value = 4.5

		elif fingerName == 'pinky':
			ctrlShp.attr('%s2FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s3FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s4FistRx' % fingerName ).value = -9
			ctrlShp.attr('%s2CupRx' % fingerName ).value = -4.5
			ctrlShp.attr('%s3CupRx' % fingerName ).value = -4.5
			ctrlShp.attr('%s4CupRx' % fingerName ).value = -4.5
			ctrlShp.attr('%s2Spread' % fingerName ).value = 9
			ctrlShp.attr('%sBaseSpread' % fingerName ).value = 9

		elif fingerName == 'thumb':
			ctrlShp.attr('%s2FistRx' % fingerName ).value = -4.5
			ctrlShp.attr('%s3FistRx' % fingerName ).value = -9

	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts,
						'Attribute Ctrl': self.attrCtrl,
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Skin Grp':self.baseUi.skinGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		attrCtrl = self.attrCtrl.longName()
		attrCtrlShp = self.attrCtrl.getShape()
		fingerName = self.getFingerName()

		elem = self.baseUi.getElem()
		side = self.baseUi.getSide()

		fingerRig = pfngr.FingerRig( fngr = fingerName ,
				parent = self.baseUi.rigParent.longName() ,
				armCtrl = attrCtrl,
				side = side , 
				animGrp = self.baseUi.animGrp.longName() ,
				skinGrp = self.baseUi.skinGrp.longName() ,
				stillGrp = self.baseUi.stillGrp.longName() ,
				charSize = self.baseUi.getRigScale(),
				tmpJnt = tmpJntsLongNames)

		rigTools.dummyNaming( obj = fingerRig ,
					attr = 'fngr' ,
					dummy = fingerName ,
					charName = '' ,
					elem = elem ,
					side = side )

		attrCtrlShp = pc.Dag(attrCtrlShp)
		self.setFingerAttr(fingerName, attrCtrlShp)


class thumbRig(BaseUi):
	_DESCRIPTION = """4 joint rig with handy attribute on sepcified ctrl. Ideal for thumbs.
	METHOD: FK, preset attributes
	PARENT: wrist(wrist)
	REQUIRES: 4 joints

	[ finger1, finger2, finger3 finger4 ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []
		self.attrCtrl = None

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=2, co=[(1, 'left', 130), (2, 'left', 5)]):
				pm.text(l='Finger Name')
				self.fingerNameTxtFld = pm.textField(tx='thumb', w=60, ed=True)
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='attrCtrl')
				self.attrCtrlTxtFld = pm.textField(w=230, ed=False)
				self.loadAttrCtrlButt = pm.button(l='<<', c=pm.Callback(self.loadAttrCtrl))
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.baseUi.clearElemSideTxtFld()


	def loadAttrCtrl(self):
		sel = misc.getSel()
		if not sel.getShape():
			return
		self.loadObjToTxtFld(sel, self.attrCtrlTxtFld)
		self.attrCtrl = sel

	def getFingerName(self):
		fingerName = self.fingerNameTxtFld.getText()
		if not fingerName:
			fingerName = 'thumb'
		return fingerName

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=4)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 4:
			OpenMaya.MGlobal.displayWarning('This module requires 4 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)

	def setFingerAttr(self, ctrlShp):
		ctrlShp.attr('thumb2FistRx').value = -4.5
		ctrlShp.attr('thumb3FistRx').value = -9

	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts,
						'Attribute Ctrl': self.attrCtrl,
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Skin Grp':self.baseUi.skinGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		attrCtrl = self.attrCtrl.longName()
		attrCtrlShp = self.attrCtrl.getShape()
		fingerName = self.getFingerName()

		elem = self.baseUi.getElem()
		side = self.baseUi.getSide()

		thumbRig = pthmb.ThumbRig(parent = self.baseUi.rigParent.longName() ,
				armCtrl = attrCtrl,
				side = side , 
				animGrp = self.baseUi.animGrp.longName() ,
				skinGrp = self.baseUi.skinGrp.longName() ,
				stillGrp = self.baseUi.stillGrp.longName() ,
				charSize = self.baseUi.getRigScale(),
				tmpJnt = tmpJntsLongNames)
		
		rigTools.dummyNaming( obj = thumbRig ,
					attr = 'thumb' ,
					dummy = fingerName ,
					charName = '' ,
					elem = elem ,
					side = side )

		self.setFingerAttr(attrCtrlShp)

class spineRig(BaseUi):
	_DESCRIPTION = """Perfect for quardruped back.
	METHOD: IK/FK, Ribbon(3 - 5 joints)
	PARENT: root(root_jnt)
	REQUIRES: 3 joints

	[ spine1, spine2, neck ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []
		self.defaultAxis = 'z'

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=2, co=[(1, 'left', 153), (2, 'left', 5)]):
				pm.text(l='axis')
				with pm.optionMenu(w=60) as self.axisMenu:
					pm.menuItem(l='x')
					pm.menuItem(l='y')
					pm.menuItem(l='z')
			with pm.columnLayout(adj=True, rs=2, co=['left', 160]):	
				self.ribbonChkBox = pm.checkBox(l='Ribbon Lo/Hi', v=True)
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.axisMenu.setValue(self.defaultAxis)
		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=3)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels) != 3:
			OpenMaya.MGlobal.displayWarning('This module requires 3 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Jnt Grp':self.baseUi.jntGrp, 
						'Ikh Grp':self.baseUi.ikhGrp, 
						'Skin Grp':self.baseUi.skinGrp, 
						'Still Grp':self.baseUi.stillGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		elem = self.baseUi.getElem()
		side = self.baseUi.getSide()

		spineRig = pspi.SpineRig( parent = self.baseUi.rigParent.longName() ,
						animGrp = self.baseUi.animGrp.longName() ,
						jntGrp = self.baseUi.jntGrp.longName() ,
						ikhGrp = self.baseUi.ikhGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						stillGrp = self.baseUi.stillGrp.longName() ,
						ribbon = self.ribbonChkBox.getValue(),
						ax = self.axisMenu.getValue() ,
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( spineRig ,
					charName = '' ,
					elem = elem ,
					side =  side )


		rigTools.dummyNaming( obj = spineRig.lowSpineRbn ,
					attr = 'rbn' ,
					dummy = 'lowSpineRbn' ,
					charName = '' ,
					elem = elem ,
					side = side )

		rigTools.dummyNaming( obj = spineRig.upSpineRbn ,
					attr = 'rbn' ,
					dummy = 'upSpineRbn' ,
					charName = '' ,
					elem = elem ,
					side = side )


class backLegRig(BaseUi):
	_DESCRIPTION = """Animal hind leg rig with optional ribbon. Ideal for quardruped leg. 
	METHOD: IK/FK, Ribbon
	PARENT: clav or pelvis
	REQUIRES: 10 joints

	[ upLeg, midLeg, lowLeg, 
	ankle, ball, toe, 
	heel, footIn, footOut, 
	kneePv ]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))
			with pm.columnLayout(adj=True, rs=2, co=['left', 155]):	
				self.ribbonChkBox = pm.checkBox(l='Ribbon Lo/Hi', v=True)

		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num=10)
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return

		if len(sels) != 10:
			OpenMaya.MGlobal.displayWarning('This module reqires 10 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts, 
						'Parent':self.baseUi.rigParent, 
						'Anim Grp':self.baseUi.animGrp, 
						'Jnt Grp':self.baseUi.jntGrp, 
						'Ikh Grp':self.baseUi.ikhGrp, 
						'Skin Grp':self.baseUi.skinGrp, 
						'Still Grp':self.baseUi.stillGrp}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		elem = self.baseUi.getElem()
		side = self.baseUi.getSide()

		bLegRig = pbleg.BackLegRig( parent = self.baseUi.rigParent.longName() ,
						side = side ,
						animGrp = self.baseUi.animGrp.longName() ,
						jntGrp = self.baseUi.jntGrp.longName() ,
						ikhGrp = self.baseUi.ikhGrp.longName() ,
						skinGrp = self.baseUi.skinGrp.longName() ,
						stillGrp = self.baseUi.stillGrp.longName() ,
						ribbon = self.ribbonChkBox.getValue(),
						charSize = self.baseUi.getRigScale(),
						tmpJnt = tmpJntsLongNames)

		rigTools.nodeNaming( bLegRig ,
					charName = '' ,
					elem = elem ,
					side = side )

		rigTools.dummyNaming( obj = bLegRig.upLegRbn ,
					attr = 'rbn' ,
					dummy = 'upLegBackRbn' ,
					charName = '' ,
					elem = elem ,
					side = side )

		rigTools.dummyNaming( obj = bLegRig.midLegRbn ,
					attr = 'rbn' ,
					dummy = 'midLegBackRbn' ,
					charName = '' ,
					elem = elem ,
					side = side )

		rigTools.dummyNaming( obj = bLegRig.lowLegRbn ,
					attr = 'rbn' ,
					dummy = 'lowLegBackRbn' ,
					charName = '' ,
					elem = elem ,
					side = side )


class fkRig(BaseUi):
	_DESCRIPTION = """Basic FK rig with squash and stretch.
	METHOD: FK
	PARENT: None
	REQUIRES: <more than 1 joint>

	[ joint1, joint2, ... jointX]"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []
		self.defaultAxis = 'y'
		self.defaultShape = 'circle'

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=2, rs=[(1,3), (2,3)], co=[(1, 'left', 95), (2, 'left', 5)]):
				pm.text(l='axis')
				with pm.optionMenu(w=30) as self.axisMenu:
					pm.menuItem(l='x')
					pm.menuItem(l='y')
					pm.menuItem(l='z')
				pm.text(l='shape')
				with pm.optionMenu(w=60) as self.shapeMenu:
					pm.menuItem(l='circle')
					pm.menuItem(l='square')
					pm.menuItem(l='cube')
					pm.menuItem(l='sphere')
					pm.menuItem(l='stick')
					pm.menuItem(l='plus')
					pm.menuItem(l='crossArrow')
					pm.menuItem(l='capsule')
					pm.menuItem(l='doubleStick')
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 30), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tmpJnts')
				self.tmpJntsTxtFld = pm.textField(w=230, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTmpJnts))

		self.axisMenu.setValue(self.defaultAxis)
		self.shapeMenu.setValue(self.defaultShape)
		self.baseUi.clearElemSideTxtFld()

	def loadTmpJnts(self):
		sels = misc.getSel(selType='joint', num='inf')
		if not sels:
			self.tmpJnts = []
			self.tmpJntsTxtFld.setText('')
			return
		if len(sels)  < 2:
			OpenMaya.MGlobal.displayWarning('This module reqires at least 2 joints')
		self.tmpJnts = sels
		self.loadObjsToTxtFld(self.tmpJnts, self.tmpJntsTxtFld)


	def call(self):
		self._REQUIRE = {'Template Jnt':self.tmpJnts}
		if not self.checkRequires():
			return

		tmpJntsLongNames = []
		for j in self.tmpJnts:
			tmpJntsLongNames.append(j.longName())

		elem = self.baseUi.getElem()
		side = self.baseUi.getSide()

		fkRig = pfk.FkRig(jnts = tmpJntsLongNames ,
						ax = self.axisMenu.getValue() ,
						shape = self.shapeMenu.getValue() ,
						scale = self.baseUi.getRigScale() ,
						elem = elem , 
						side = side )

class ribbon(BaseUi):
	_DESCRIPTION = """Ribbon Ik 3-5 joints. Auto place if parent and tip parent are loaded. 
	METHOD: ribbon
	PARENT: Parent(optional), tipParent(optional)
	REQUIRES: None
	"""

	def __init__(self, baseUi, parent):
		BaseUi.__init__(self, parent)
		self.uiparent = parent
		self.baseUi = baseUi
		self.tmpJnts = []
		self.defaultAxis = 'y+'
		self.tipParent = None

		#ui
		try:
			pm.deleteUI(self.rigCol)
		except: pass

		with pm.columnLayout(adj=True, rs=3, parent=self.uiparent) as self.rigCol:
			with pm.rowColumnLayout(nc=3, co=[(1, 'left', 76), (2, 'left', 5), (3, 'left', 5)]):
				pm.text(l='tip parent')
				self.tipParentTxtFld = pm.textField(w=142, ed=False)
				self.loadTmpJntButt = pm.button(l='<<', c=pm.Callback(self.loadTipParent))
			with pm.rowColumnLayout(nc=2, co=[(1, 'left', 140), (2, 'left', 5)]):
				pm.text(l='axis')
				with pm.optionMenu(w=60) as self.axisMenu:
					pm.menuItem(l='x+')
					pm.menuItem(l='y+')
					pm.menuItem(l='z+')
					pm.menuItem(l='x-')
					pm.menuItem(l='y-')
					pm.menuItem(l='z-')
			with pm.columnLayout(adj=True, rs=2, co=['left', 165]):	
				self.ribbonChkBox = pm.checkBox(l='Ribbon Lo/Hi', v=True)


		self.axisMenu.setValue(self.defaultAxis)
		self.baseUi.clearElemSideTxtFld()

	def loadTipParent(self):
		sels = misc.getSel(num=1)
		if not sels:
			self.tipParent = None
			self.tmpJntsTxtFld.setText('')
			return

		self.tipParent = sels
		self.loadObjToTxtFld(self.tipParent, self.tipParentTxtFld)


	def call(self):
		self._REQUIRE = {'Anim Grp':self.baseUi.animGrp, 
						'Jnt Grp':self.baseUi.jntGrp, 
						'Skin Grp':self.baseUi.skinGrp, 
						'Still Grp':self.baseUi.stillGrp}
		if not self.checkRequires():
			return

		elem = self.baseUi.getElem()
		elem = 'rbn%s' %elem.title()
		side = self.baseUi.getSide()

		if self.ribbonChkBox.getValue() == True:
			ribbonRig = prbn.RibbonIkHi(ax = self.axisMenu.getValue() ,
										size = self.baseUi.getRigScale())
		else:
			ribbonRig = prbn.RibbonIkLow(ax = self.axisMenu.getValue() ,
										size = self.baseUi.getRigScale())
		

		rigTools.dummyNaming( obj = ribbonRig ,
							attr = 'rbn' ,
							dummy = elem ,
							charName = '' ,
							elem = '' ,
							side = side )


		#constraint
		if self.baseUi.rigParent and self.tipParent:
			misc.snapTransform('parent', self.baseUi.rigParent, ribbonRig.rbnAnim_grp, False, True)
			misc.snapTransform('point', self.baseUi.rigParent, ribbonRig.rbnRoot_ctrl, False, False)
			misc.snapTransform('point', self.tipParent, ribbonRig.rbnEnd_ctrl, False, False)

		#parent to main grps
		pm.parent(ribbonRig.rbnAnim_grp, self.baseUi.animGrp)
		pm.parent(ribbonRig.rbnStill_grp, self.baseUi.stillGrp)
		try:
			pm.parent(ribbonRig.rbnJnt_grp, self.baseUi.jntGrp)
		except:
			pass
		pm.parent(ribbonRig.rbnSkin_grp, self.baseUi.skinGrp)