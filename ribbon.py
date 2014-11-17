import maya.cmds as mc
import pkmel.rigTools as rigTools
reload( rigTools )
import pkmel.core as pc
reload( pc )

class RibbonIk( object ) :
	# Ribbon IK object
	def __init__( self ,
					size = 1 ,
					ax = 'y+'
				) :
		# Ribbon information
		rbnInfo 			= self.rbnInfo( ax )
		
		self.rotate 		= rbnInfo[ 'rotate' ]
		self.aimVec 		= rbnInfo[ 'aimVec' ]
		self.invAimVec 		= rbnInfo[ 'invAimVec' ]
		self.upVec 			= rbnInfo[ 'upVec' ]
		self.twstAx 		= rbnInfo[ 'twstAx' ]
		self.sqshAx 		= rbnInfo[ 'sqshAx' ]
		self.ro 			= rbnInfo[ 'ro' ]
				
		# Main group
		self.rbnAnim_grp 	= pc.Null()
		self.rbnJnt_grp 	= pc.Null()
		self.rbnSkin_grp 	= pc.Null()

		self.rbnSkinGrp_parCons = pc.parentConstraint( self.rbnAnim_grp ,
														self.rbnSkin_grp
														)
		self.rbnSkinGrp_scaCons = pc.scaleConstraint( self.rbnAnim_grp ,
														self.rbnSkin_grp
														)
		
		# - Ribbon joint -
		self.rbnCtrl_grp = pc.Null()
		
		# -- Root joint --
		self.rbnRoot_jnt 	= pc.Joint()
		self.rbnRoot_ctrl 	= pc.Control( 'plus' )
		self.rbnRootCtrlZro_grp = pc.group( self.rbnRoot_ctrl  )
		self.rbnRootCtrlAim_grp = pc.Null()
		
		self.rbnRootJnt_parCons = pc.parentConstraint( self.rbnRootCtrlAim_grp ,
														self.rbnRoot_jnt
														)
		self.rbnRoot_jnt.parent( self.rbnJnt_grp )
		
		self.rbnRootCtrlAim_grp.parent( self.rbnRoot_ctrl )
		self.rbnRoot_ctrl.scaleShape( size * 0.1 )
		self.rbnRoot_ctrl.color = 'yellow'
		self.rbnRoot_jnt.attr('v').value = 0
		# -- End Root joint --
		
		# -- End joint --
		self.rbnEnd_jnt = pc.Joint()
		self.rbnEnd_ctrl = pc.Control( 'plus' )
		self.rbnEndCtrlZro_grp = pc.group( self.rbnEnd_ctrl  )
		self.rbnEndCtrlAim_grp = pc.Null()
		
		self.rbnEndJnt_parCons = pc.parentConstraint( self.rbnEndCtrlAim_grp ,
								self.rbnEnd_jnt )
		self.rbnEnd_jnt.parent( self.rbnJnt_grp )
		
		self.rbnEndCtrlAim_grp.parent( self.rbnEnd_ctrl )
		self.rbnEnd_ctrl.scaleShape( size * 0.1 )
		self.rbnEnd_ctrl.color = 'yellow'
		
		endPos = ( self.aimVec[0] * size , self.aimVec[1] * size , self.aimVec[2] * size )
		self.rbnEndCtrlZro_grp.attr('t').value = endPos
		self.rbnEnd_jnt.attr('v').value = 0
		# -- End End joint --
		
		# -- Middle joint --
		self.rbnMid_jnt = pc.Joint()
		self.rbnMidJntOfst_grp = pc.Null()
		self.rbnMidJntZro_grp = pc.group( self.rbnMidJntOfst_grp )
		self.rbn_ctrl = rigTools.jointControl( 'square' )
		self.rbnCtrlAim_grp = pc.group( self.rbn_ctrl )
		self.rbnCtrlZro_grp = pc.group( self.rbnCtrlAim_grp )

		self.rbn_ctrl.attr( 'ro' ).value = self.ro
		
		self.rbnMidJnt_parCons = pc.parentConstraint( self.rbnMidJntOfst_grp ,
														self.rbnMid_jnt
													)
		self.rbnMid_jnt.parent( self.rbnJnt_grp )
		
		self.rbnMidJntZro_grp.parent( self.rbn_ctrl )
		self.rbn_ctrl.rotateShape( self.rotate )
		self.rbn_ctrl.scaleShape( size * 0.25 )
		self.rbn_ctrl.color = 'yellow'
		
		self.rbn_ctrl.add( ln = 'autoTwist' , at = 'float' ,
							k = True , min = 0 , max = 1 )

		rbnCtrlShp = pc.Dag( self.rbn_ctrl.shape )
		rbnCtrlShp.add( ln = 'upVector' , sn = 'u' , at = 'double3' , k = False )
		rbnCtrlShp.add( p = 'upVector' , ln = 'upVectorX' , sn = 'ux' ,
						at = 'double' , k = False )
		rbnCtrlShp.add( p = 'upVector' , ln = 'upVectorY' , sn = 'uy' ,
						at = 'double' , k = False )
		rbnCtrlShp.add( p = 'upVector' , ln = 'upVectorZ' , sn = 'uz' ,
						at = 'double' , k = False )
		
		rbnCtrlShp.attr('u').value = self.upVec
		self.rbnMid_jnt.attr('v').value = 0
		# -- End Middle joint --
		# - End Ribbon joint -
		
		# - Ribbon rig -
		self.rbnRootCtrlAimGrp_aimCons 	= pc.aimConstraint( self.rbnEnd_ctrl ,
															self.rbnRootCtrlAim_grp ,
															aim = self.aimVec , u = self.upVec ,
															wut = 'objectrotation' ,
															wuo = '%s' % self.rbnRoot_ctrl ,
															wu = self.upVec
															)
		self.rbnEndCtrlAimGrp_aimCons 	= pc.aimConstraint( self.rbnRoot_ctrl ,
															self.rbnEndCtrlAim_grp ,
															aim = self.invAimVec , u = self.upVec ,
															wut = 'objectrotation' ,
															wuo = '%s' % self.rbnEnd_ctrl ,
															wu = self.upVec
															)
		self.rbnCtrlZeroGrp_pntCons 	= pc.pointConstraint( self.rbnRoot_ctrl ,
																self.rbnEnd_ctrl ,
																self.rbnCtrlZro_grp
															)
		self.rbnCtrlAimGrp_aimCons 		= pc.aimConstraint( self.rbnEnd_ctrl ,
															self.rbnCtrlAim_grp ,
															aim = self.aimVec , u = self.upVec ,
															wut = 'objectrotation' ,
															wuo = '%s' % self.rbnCtrlZro_grp ,
															wu = self.upVec
															)
		
		mc.parent( self.rbnRootCtrlZro_grp , self.rbnEndCtrlZro_grp ,
					self.rbnCtrlZro_grp , self.rbnCtrl_grp
					)
		self.rbnCtrl_grp.parent( self.rbnAnim_grp )
		
		rbnCtrlShp.attr('u') >> self.rbnRootCtrlAimGrp_aimCons.attr('u')
		rbnCtrlShp.attr('u') >> self.rbnRootCtrlAimGrp_aimCons.attr('wu')
		rbnCtrlShp.attr('u') >> self.rbnEndCtrlAimGrp_aimCons.attr('u')
		rbnCtrlShp.attr('u') >> self.rbnEndCtrlAimGrp_aimCons.attr('wu')
		rbnCtrlShp.attr('u') >> self.rbnCtrlAimGrp_aimCons.attr('u')
		rbnCtrlShp.attr('u') >> self.rbnCtrlAimGrp_aimCons.attr('wu')
		# - End Ribbon rig -
		
		# - Space node -
		self.rbnRootTwst_grp	= pc.Null()
		self.rbnRootTwstZro_grp	= pc.group( self.rbnRootTwst_grp )
		self.rbnEndTwst_grp		= pc.Null()
		self.rbnEndTwstZro_grp	= pc.group( self.rbnEndTwst_grp )

		self.rbnEndTwstZro_grp.attr('t').value 		= endPos
		self.rbnRootTwst_grp.attr( 'ro' ).value 	= self.ro
		self.rbnEndTwst_grp.attr( 'ro' ).value 		= self.ro

		self.rbnRootTwstZro_grp.parent( self.rbnAnim_grp )
		self.rbnEndTwstZro_grp.parent( self.rbnAnim_grp )

		# - Twist distribution -
		self.rbnRootTwst_add 	= pc.AddDoubleLinear()
		self.rbnEndTwst_add 	= pc.AddDoubleLinear()
		
		rbnCtrlShp = pc.Dag( self.rbn_ctrl.shape )
		
		rbnCtrlShp.add( ln = 'rootTwistAmp' , dv = 1 )
		rbnCtrlShp.add( ln = 'endTwistAmp' , dv = 1 )
		
		self.rbnRootTwstAmp_mul 	= pc.MultDoubleLinear()
		self.rbnEndTwstAmp_mul 		= pc.MultDoubleLinear()
		self.rbnRootAutoTwst_mul 	= pc.MultDoubleLinear()
		self.rbnEndAutoTwst_mul 	= pc.MultDoubleLinear()

		
		self.rbnRootTwst_grp.attr(self.twstAx) 	>> self.rbnRootTwstAmp_mul.attr('i1')
		self.rbnEndTwst_grp.attr(self.twstAx) 	>> self.rbnEndTwstAmp_mul.attr('i1')
		rbnCtrlShp.attr('rootTwistAmp') 	>> self.rbnRootTwstAmp_mul.attr('i2')
		rbnCtrlShp.attr('endTwistAmp') 		>> self.rbnEndTwstAmp_mul.attr('i2')
		
		self.rbn_ctrl.attr('autoTwist') 	>> self.rbnRootAutoTwst_mul.attr('i1')
		self.rbn_ctrl.attr('autoTwist') 	>> self.rbnEndAutoTwst_mul.attr('i1')
		self.rbnRootTwstAmp_mul.attr('o') 	>> self.rbnRootAutoTwst_mul.attr('i2')
		self.rbnEndTwstAmp_mul.attr('o') 	>> self.rbnEndAutoTwst_mul.attr('i2')
		
		self.rbnRootAutoTwst_mul.attr('o') 	>> self.rbnRootTwst_add.attr('i1')
		self.rbnEndAutoTwst_mul.attr('o') 	>> self.rbnEndTwst_add.attr('i1')

		# - Cleanup -
		# rigTools.lockUnusedAttrs( self )
		
		for attr in ('tx','ty','tz','rx','ry','rz') :
			self.rbnAnim_grp.attr( attr ).l = False
		
		for attr in ('rx','ry','rz','sx','sy','sz','v'):
			self.rbnRoot_ctrl.attr( attr ).lockHide()
			self.rbnEnd_ctrl.attr( attr ).lockHide()
		
		for attr in ('sx','sy','sz','v') :
			self.rbn_ctrl.attr( attr ).lockHide()
		# - End Cleanup -

	def rbnInfo( self , ax = 'y+' ) :
		# Input 	: ribbon axis
		# Output 	: ribbon information
		# Valid axes are : 'x+', 'x-', 'y+', 'y-', 'z+' and 'z-'
		twstAx 		=  'rx'
		sqshAx 		= ( 'sy' , 'sz' )
		aimVec 		= ( 1 , 0 , 0 )
		invAimVec 	= ( -1 , 0 , 0 )
		upVec 		= ( 0 , 0 , 1 )
		rotate 		= ( 0 , 0 , -90 )
		ro			= 0
		if ax == 'x+' :
			twstAx 		=  'rx'
			sqshAx 		= ( 'sy' , 'sz' )
			aimVec 		= ( 1 , 0 , 0 )
			invAimVec 	= ( -1 , 0 , 0 )
			upVec 		= ( 0 , 0 , 1 )
			rotate 		= ( 0 , 0 , -90 )
			ro			= 0
		
		elif ax == 'x-' :
			twstAx 		=  'rx'
			sqshAx 		= ( 'sy' , 'sz' )
			aimVec 		= ( -1 , 0 , 0 )
			invAimVec 	= ( 1 , 0 , 0 )
			upVec 		= ( 0 , 0 , 1 )
			rotate 		= ( 0 , 0 , 90 )
			ro			= 0
		
		elif ax == 'y+' :
			twstAx 		=  'ry'
			sqshAx 		= ( 'sx' , 'sz' )
			aimVec 		= ( 0 , 1 , 0 )
			invAimVec 	= ( 0 , -1 , 0 )
			upVec 		= ( 0 , 0 , 1 )
			rotate 		= ( 0 , 0 , 0 )
			ro			= 1
		
		elif ax == 'y-' :
			twstAx 		=  'ry'
			sqshAx 		= ( 'sx' , 'sz' )
			aimVec 		= ( 0 , -1 , 0 )
			invAimVec 	= ( 0 , 1 , 0 )
			upVec 		= ( 0 , 0 , 1 )
			rotate 		= ( 0 , 0 , 180 )
			ro			= 1
		
		elif ax == 'z+' :
			twstAx 		=  'rz'
			sqshAx 		= ( 'sx' , 'sy' )
			aimVec 		= ( 0 , 0 , 1 )
			invAimVec 	= ( 0 , 0 , -1 )
			upVec 		= ( 0 , 1 , 0 )
			rotate 		= ( 90 , 0 , 180 )
			ro			= 2
		
		elif ax == 'z-' :
			twstAx 		=  'rz'
			sqshAx 		= ( 'sx' , 'sy' )
			aimVec 		= ( 0 , 0 , -1 )
			invAimVec 	= ( 0 , 0 , 1 )
			upVec 		= ( 0 , 1 , 0 )
			rotate 		= ( -90 , 0 , 0 )
			ro 			= 2
		
		return { 'twstAx' 	: twstAx ,
				'sqshAx' 	: sqshAx ,
				'upVec' 	: upVec ,
				'rotate' 	: rotate ,
				'aimVec' 	: aimVec ,
				'invAimVec' : invAimVec ,
				'ro'		: ro
				}

class RibbonIkHi( RibbonIk ) :
	# Hi-res version of ribbon IK.
	def __init__(
					self ,
					size = 1 ,
					ax = 'y+'
				) :

		super( RibbonIkHi , self ).__init__( size , ax )

		# Main group
		self.rbnStill_grp = pc.Null()

		# Ribbon geo
		self.rbn_nrb = rigTools.ribbonSurface()
		self.rbn_nrb.parent( self.rbnStill_grp )
		
		# Ribbon surface shape adjustment
		self.rbn_nrb.scaleShape( size )
		self.rbn_nrb.rotateShape( self.rotate )
		
		# - Point on surface -
		self.rbnPos_grp = pc.Null()
		self.rbnDtlCtrl_grp = pc.Null()

		rbnCtrlShp = pc.Dag( self.rbn_ctrl.shape )
		rbnCtrlShp.add( ln = 'detail' , at = 'double' ,
						k = True , min = 0 , max = 1 )
		rbnCtrlShp.attr('detail') >> self.rbnDtlCtrl_grp.attr('v')
		self.rbnPos_grp.parent( self.rbnStill_grp )
		self.rbnDtlCtrl_grp.parent( self.rbnAnim_grp )
		self.rbnSkin_grp.parent( self.rbnAnim_grp )
		
		poss = []
		posis = []
		aimcons = []
		
		for ix in range( 5 ) :
			pos = pc.Null()
			posi = pc.PointOnSurfaceInfo()
			
			self.rbn_nrb.attr('worldSpace[0]') >> posi.attr('is')
			posi.attr('position') >> pos.attr('t')
			posi.attr('parameterU').value = 0.5
			posi.attr('turnOnPercentage').value = 1
			
			aimcon = pc.AimConstraint()
			aimcon.attr('a').value = self.aimVec
			aimcon.attr('u').value = self.upVec
			
			posi.attr('n') >> aimcon.attr('wu')
			posi.attr('tv') >> aimcon.attr('tg[0].tt')
			aimcon.attr('cr') >> pos.attr('r')
			
			aimcon.parent( pos )
			pos.parent( self.rbnPos_grp )
			
			poss.append( pos )
			posis.append( posi )
			aimcons.append( aimcon )
		
		posis[0].attr('parameterV').value = 0.1
		posis[1].attr('parameterV').value = 0.3
		posis[2].attr('parameterV').value = 0.5
		posis[3].attr('parameterV').value = 0.7
		posis[4].attr('parameterV').value = 0.9
		
		( self.rbnPos1_grp ,
		self.rbnPos2_grp ,
		self.rbnPos3_grp ,
		self.rbnPos4_grp ,
		self.rbnPos5_grp
		) = poss
		( self.rbn1_posi ,
		self.rbn2_posi ,
		self.rbn3_posi ,
		self.rbn4_posi ,
		self.rbn5_posi
		) = posis
		( self.rbnPos1_aimCons ,
		self.rbnPos2_aimCons ,
		self.rbnPos3_aimCons ,
		self.rbnPos4_aimCons ,
		self.rbnPos5_aimCons
		) = aimcons
		# - end Point on surface -

		# - Detail controller and skin joint -
		dtlCtrls = []
		dtlJnts = []
		dtlTwsts = []
		dtlZros = []
		sqshPmas = []
		
		dtlJntParconss 	= []
		dtlCtrlParconss = []
		
		for ix in range( 5 ) :
			
			dtlCtrl = pc.Control('circle')
			dtlJnt = pc.Joint()
			dtlTwst = pc.Null()
			dtlZro = pc.Null()
			sqshPma = pc.PlusMinusAverage()
			
			dtlCtrls.append( dtlCtrl )
			dtlJnts.append( dtlJnt )
			dtlTwsts.append( dtlTwst )
			dtlZros.append( dtlZro )
			sqshPmas.append( sqshPma )

			# Shape adjustment
			dtlCtrl.rotateShape( self.rotate )
			dtlCtrl.scaleShape( size * 0.25 )
			dtlCtrl.color = 'softBlue'

			# Hierarchy setup
			dtlCtrl.parent( dtlTwst )
			dtlTwst.parent( dtlZro )
			
			dtlZro.parent( self.rbnDtlCtrl_grp )
			dtlJnt.parent( self.rbnSkin_grp )

			# Squash setup
			dtlCtrl.add( ln = 'squash' , k = True )
			sqshPma.add( ln = 'default' , min = 1 , max = 1 , dv = 1 , k = True )
			sqshPma.attr('default') >> sqshPma.last1D()
			dtlCtrl.attr('squash') >> sqshPma.last1D()
			sqshPma.attr('output1D') >> dtlJnt.attr( self.sqshAx[0] )
			sqshPma.attr('output1D') >> dtlJnt.attr( self.sqshAx[1] )
			dtlCtrl.lockHideAttrs( 'sx' , 'sy' , 'sz' , 'v' )

			dtlCtrlParconss.append( pc.parentConstraint( poss[ix] , dtlZro ) )
			dtlJntParconss.append( pc.parentConstraint( dtlCtrl , dtlJnt ) )
		
		( self.rbnDtl1_ctrl ,
		self.rbnDtl2_ctrl ,
		self.rbnDtl3_ctrl ,
		self.rbnDtl4_ctrl ,
		self.rbnDtl5_ctrl
		) = dtlCtrls
		( self.rbnDtl1_jnt ,
		self.rbnDtl2_jnt ,
		self.rbnDtl3_jnt ,
		self.rbnDtl4_jnt ,
		self.rbnDtl5_jnt
		) = dtlJnts
		( self.rbnDtl1Twst_grp ,
		self.rbnDtl2Twst_grp ,
		self.rbnDtl3Twst_grp ,
		self.rbnDtl4Twst_grp ,
		self.rbnDtl5Twst_grp
		) = dtlTwsts
		( self.rbnDtl1Zro_grp ,
		self.rbnDtl2Zro_grp ,
		self.rbnDtl3Zro_grp ,
		self.rbnDtl4Zro_grp ,
		self.rbnDtl5Zro_grp
		) = dtlZros
		( self.rbnDtl1Sqsh_pma ,
		self.rbnDtl2Sqsh_pma ,
		self.rbnDtl3Sqsh_pma ,
		self.rbnDtl4Sqsh_pma ,
		self.rbnDtl5Sqsh_pma
		) = sqshPmas
		
		( self.rbnDtl1Ctrl_parCons ,
		self.rbnDtl2Ctrl_parCons ,
		self.rbnDtl3Ctrl_parCons ,
		self.rbnDtl4Ctrl_parCons ,
		self.rbnDtl5Ctrl_parCons
		) = dtlCtrlParconss
		( self.rbnDtl1Jnt_parCons ,
		self.rbnDtl2Jnt_parCons ,
		self.rbnDtl3Jnt_parCons ,
		self.rbnDtl4Jnt_parCons ,
		self.rbnDtl5Jnt_parCons
		) = dtlJntParconss
		# - End Detail controller and skin joint -

		# - Twist distribution -
		self.rbn_ctrl.add( ln = 'rootTwist' , at = 'float' , k = True )
		self.rbn_ctrl.add( ln = 'endTwist' , at = 'float' , k = True )

		self.rbn_ctrl.attr('rootTwist') 	>> self.rbnRootTwst_add.attr('i2')
		self.rbn_ctrl.attr('endTwist') 		>> self.rbnEndTwst_add.attr('i2')

		# -- Twist on skin joint 1 --
		self.rbnRootTwst_add.attr('o') >> dtlTwsts[0].attr( self.twstAx )

		# -- Twsit on skin joint 2-4 --
		twstMdvs = []
		twstPmas = []
		for ix in range( 3 ) :
			
			endVal = 0.25 * ( ix + 1 )
			startVal = 0.25 * ( 4 - ( ix + 1 ) )
			
			twstMdv = pc.MultiplyDivide()
			twstPma = pc.PlusMinusAverage()
			twstMdvs.append( twstMdv )
			twstPmas.append( twstPma )
			
			twstMdv.attr('i1x').value = endVal
			twstMdv.attr('i1y').value = startVal
			self.rbnEndTwst_add.attr('o') >> twstMdv.attr('i2x')
			self.rbnRootTwst_add.attr('o') >> twstMdv.attr('i2y')
			twstMdv.attr('ox') >> twstPma.last1D()
			twstMdv.attr('oy') >> twstPma.last1D()
			twstPma.attr('output1D') >> dtlTwsts[ix+1].attr( self.twstAx )

		# -- Twist on skin joint 5 --
		self.rbnEndTwst_add.attr('o') >> self.rbnDtl5Twst_grp.attr( self.twstAx )

		self.rbnDtl2Twst_mdv , self.rbnDtl3Twst_mdv , self.rbnDtl4Twst_mdv = twstMdvs
		self.rbnDtl2Twst_pma , self.rbnDtl3Twst_pma , self.rbnDtl4Twst_pma = twstPmas
		# - End Twist distribution -

		# - Binding skin -
		self.rbn_skc = pc.SkinCluster( self.rbnRoot_jnt , self.rbnMid_jnt ,
						self.rbnEnd_jnt , self.rbn_nrb ,
						dr = 7 , mi = 2 )

		# -- Adjust skin weight --
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][7]' % self.rbn_nrb , tv = [ self.rbnEnd_jnt , 1 ] )
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][6]' % self.rbn_nrb , tv = [ self.rbnMid_jnt , 0.2 ] )
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][5]' % self.rbn_nrb , tv = [ self.rbnMid_jnt , 0.5 ] )
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][4]' % self.rbn_nrb , tv = [ self.rbnEnd_jnt , 0.1 ] )
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][3]' % self.rbn_nrb , tv = [ self.rbnRoot_jnt , 0.1 ] )
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][2]' % self.rbn_nrb , tv = [ self.rbnRoot_jnt , 0.5 ] )
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][1]' % self.rbn_nrb , tv = [ self.rbnRoot_jnt , 0.8 ] )
		mc.skinPercent( self.rbn_skc , '%s.cv[0:3][0]' % self.rbn_nrb , tv = [ self.rbnRoot_jnt , 1 ] )
		# - End binding skin -

		# - Squash setup -
		self.rbn_ctrl.add( ln = 'squash' , at = 'float' , k = True )

		# - Squash setup - Squash attribute amplitude
		self.rbnSquashAmp_mul = pc.MultDoubleLinear()
		self.rbnSquashAmp_mul.attr('i2').v = 0.1
		self.rbn_ctrl.attr('squash') >> self.rbnSquashAmp_mul.attr('i1')

		for ix in range( 5 ) :
			self.rbnSquashAmp_mul.attr('o') >> sqshPmas[ix].last1D()
		
		# - Cleanup -
		self.rbn_nrb.attr('v').v = 0

class RibbonIkLow( RibbonIk ) :
	# Low-res version of ribbon IK.
	def __init__(
					self ,
					size = 1 ,
					ax = 'y+'
				) :

		super( RibbonIkLow , self ).__init__( size , ax )

		# - Skin joint -
		self.rbn_jnt = pc.Joint()
		self.rbnJntOfst_grp = pc.group( self.rbn_jnt )
		self.rbnJntZro_grp = pc.group( self.rbnJntOfst_grp )

		self.rbnJntZroGrp_parCons = pc.parentConstraint(
															self.rbn_ctrl ,
															self.rbnJntZro_grp
														)
		self.rbnJntZro_grp.parent( self.rbnSkin_grp )

		# - Squash setup -
		self.rbn_ctrl.add( ln = 'squash' , at = 'float' , k = True )

		# - Squash setup - Squash attribute amplitude
		self.rbnSquashAmp_mul = pc.MultDoubleLinear()
		self.rbnSquashAmp_mul.attr('i2').v = 0.1
		self.rbn_ctrl.attr('squash') >> self.rbnSquashAmp_mul.attr('i1')

		self.rbnSquash_add = pc.AddDoubleLinear()
		self.rbnSquash_add.add( ln='default' , min=1 , max=1 , dv=1 , k=True )

		self.rbnSquash_add.attr( 'default' ) >> self.rbnSquash_add.attr( 'i1' )
		self.rbnSquashAmp_mul.attr( 'o' ) >> self.rbnSquash_add.attr( 'i2' )
		self.rbnSquash_add.attr( 'o' ) >> self.rbn_jnt.attr( self.sqshAx[0] )
		self.rbnSquash_add.attr( 'o' ) >> self.rbn_jnt.attr( self.sqshAx[1] )

		# - Twist distribution -
		self.rbnTwst_mdv = pc.MultiplyDivide()
		self.rbnTwst_pma = pc.PlusMinusAverage()
		
		self.rbnTwst_mdv.attr('i1x').value = 0.5
		self.rbnTwst_mdv.attr('i1y').value = 0.5
		
		self.rbnRootTwst_add.attr('o') 		>> self.rbnTwst_mdv.attr('i2y')
		self.rbnEndTwst_add.attr('o') 		>> self.rbnTwst_mdv.attr('i2x')
		self.rbnTwst_mdv.attr('ox') 		>> self.rbnTwst_pma.last1D()
		self.rbnTwst_mdv.attr('oy') 		>> self.rbnTwst_pma.last1D()
		self.rbnTwst_pma.attr('output1D') 	>> self.rbnJntOfst_grp.attr(self.twstAx)