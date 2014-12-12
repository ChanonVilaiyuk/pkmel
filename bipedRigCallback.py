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
import pkmel.humanSpineRig as phspi
reload( phspi )
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

import pkmel.fkRig as pfk
reload( pfk )
import pkmel.fkGroupRig as pfkg
reload( pfkg )

placement = pc.Dag( 'placement_tmpCtrl' )
# Naming
charName = ''
elem = ''

# Rig
mainGroup = pmain.MainGroup()
rigTools.nodeNaming( mainGroup , charName = charName , elem = elem , side = '' )

anim = mainGroup.anim_grp
jnt = mainGroup.jnt_grp
skin = mainGroup.skin_grp
ikh = mainGroup.ikh_grp
still = mainGroup.still_grp
size = mainGroup.charSize

# Root
rootRig = proot.RootRig(
							animGrp = anim ,
							skinGrp = skin ,
							charSize = size ,
							tmpJnt = 'root_tmpJnt'
						)

rigTools.nodeNaming(
						rootRig ,
						charName = charName ,
						elem = elem ,
						side = ''
					)

# Pelvis
pelvisRig = ppelv.PelvisRig(
								parent = rootRig.root_jnt.name ,
								animGrp = anim ,
								skinGrp = skin ,
								charSize = size ,
								tmpJnt = 'pelvis_tmpJnt'
							)

rigTools.nodeNaming(
						pelvisRig ,
						charName = charName ,
						elem = elem ,
						side = ''
					)

# Spine 
spineRig = phspi.HumanSpineRig(
									parent = rootRig.root_jnt.name ,
									animGrp = anim ,
									jntGrp = jnt ,
									ikhGrp = ikh ,
									skinGrp = skin ,
									stillGrp = still ,
									ax = 'y' ,
									charSize = size ,
									tmpJnt = (
													'spine1_tmpJnt' ,
													'spine2_tmpJnt' ,
													'spine3_tmpJnt' ,
													'spine4_tmpJnt' ,
													'neck1_tmpJnt'
												)
								)

rigTools.nodeNaming(
						spineRig ,
						charName = charName ,
						elem = elem ,
						side = ''
					)

# Neck
neckRig = pneck.NeckRig(
							parent = spineRig.spine5_jnt ,
							animGrp = anim ,
							jntGrp = jnt ,
							skinGrp = skin ,
							stillGrp = still ,
							ribbon = False ,
							ax = 'y' ,
							charSize = size ,
							tmpJnt = (
											'neck1_tmpJnt' ,
											'head1_tmpJnt'
										)
						)

rigTools.nodeNaming(
						neckRig ,
						charName = charName ,
						elem = elem ,
						side = ''
					)

rigTools.dummyNaming(
						obj = neckRig.neckRbn ,
						attr = 'rbn' ,
						dummy = 'neckRbn' ,
						charName = charName ,
						elem = elem ,
						side = ''
					)

# Head
headRig = phead.HeadRig(
							parent = neckRig.neck2_jnt ,
							animGrp = anim ,
							skinGrp = skin ,
							charSize = size ,
							tmpJnt = (
										'head1_tmpJnt' ,
										'head2_tmpJnt' ,
										'eyeLFT_tmpJnt' ,
										'eyeRGT_tmpJnt' ,
										'jaw1LWR_tmpJnt' ,
										'jaw2LWR_tmpJnt' ,
										'jaw3LWR_tmpJnt' ,
										'jaw1UPR_tmpJnt' ,
										'jaw2UPR_tmpJnt' ,
										'eye_tmpJnt' ,
										'eyeTrgtLFT_tmpJnt' ,
										'eyeTrgtRGT_tmpJnt'
									)
						)

rigTools.nodeNaming(
						headRig ,
						charName = charName ,
						elem = elem ,
						side = ''
					)

attrs = ( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' )
for attr in attrs :
	neckRig.neckRbn.rbnRootTwst_grp.attr( attr ).l = 0

headPosGrp_parCons = pc.parentConstraint( headRig.head1_jnt , neckRig.neckRbn.rbnRootTwst_grp )

# Clavicle left
clavLRig = pclav.ClavicleRig(
								parent = spineRig.spine4_jnt ,
								side = 'LFT' ,
								animGrp = anim ,
								skinGrp = skin ,
								charSize = size ,
								tmpJnt = (
												'clavLFT_tmpJnt' ,
												'upArmLFT_tmpJnt'
											)
							)

rigTools.nodeNaming(
						clavLRig ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

# Clavicle right:
clavRRig = pclav.ClavicleRig(
								parent = spineRig.spine4_jnt ,
								side = 'RGT' ,
								animGrp = anim ,
								skinGrp = skin ,
								charSize = size ,
								tmpJnt = (
												'clavRGT_tmpJnt' ,
												'upArmRGT_tmpJnt'
											)
							)

rigTools.nodeNaming(
						clavRRig ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

# Arm left
armLRig = parm.ArmRig(
							parent = clavLRig.clav2_jnt ,
							side = 'LFT' ,
							animGrp = anim ,
							jntGrp = jnt ,
							ikhGrp = ikh ,
							skinGrp = skin ,
							stillGrp = still ,
							ribbon = True ,
							charSize = size ,
							tmpJnt = (
											'upArmLFT_tmpJnt' ,
											'forearmLFT_tmpJnt' ,
											'wristLFT_tmpJnt' ,
											'handLFT_tmpJnt' ,
											'elbowIkLFT_tmpJnt'
										)
						)

rigTools.nodeNaming(
						armLRig ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

rigTools.dummyNaming(
						obj = armLRig.upArmRbn ,
						attr = 'rbn' ,
						dummy = 'upArmRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

rigTools.dummyNaming(
						obj = armLRig.forearmRbn ,
						attr = 'rbn' ,
						dummy = 'forearmRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

# Arm right
armRRig = parm.ArmRig(
							parent = clavRRig.clav2_jnt ,
							side = 'RGT' ,
							animGrp = anim ,
							jntGrp = jnt ,
							ikhGrp = ikh ,
							skinGrp = skin ,
							stillGrp = still ,
							ribbon = True ,
							charSize = size ,
							tmpJnt = (
											'upArmRGT_tmpJnt' ,
											'forearmRGT_tmpJnt' ,
											'wristRGT_tmpJnt' ,
											'handRGT_tmpJnt' ,
											'elbowIkRGT_tmpJnt'
										)
						)

rigTools.nodeNaming(
						armRRig ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

rigTools.dummyNaming(
						obj = armRRig.upArmRbn ,
						attr = 'rbn' ,
						dummy = 'upArmRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

rigTools.dummyNaming(
						obj = armRRig.forearmRbn ,
						attr = 'rbn' ,
						dummy = 'forearmRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

# Leg left
legLRig = pleg.LegRig(
						parent = pelvisRig.pelvis_jnt ,
						side = 'LFT' ,
						animGrp = anim ,
						jntGrp = jnt ,
						ikhGrp = ikh ,
						skinGrp = skin ,
						stillGrp = still ,
						ribbon = True ,
						charSize = size ,
						tmpJnt = (
										'upLegLFT_tmpJnt' ,
										'lowLegLFT_tmpJnt' ,
										'ankleLFT_tmpJnt' ,
										'ballLFT_tmpJnt' ,
										'toeLFT_tmpJnt' ,
										'heelLFT_tmpJnt' ,
										'footInLFT_tmpJnt' ,
										'footOutLFT_tmpJnt' ,
										'kneeIkLFT_tmpJnt'
									)
					)

rigTools.nodeNaming(
						legLRig ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

rigTools.dummyNaming(
						obj = legLRig.upLegRbn ,
						attr = 'rbn' ,
						dummy = 'upLegRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

rigTools.dummyNaming(
						obj = legLRig.lowLegRbn ,
						attr = 'rbn' ,
						dummy = 'lowLegRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

# Leg right
legRRig = pleg.LegRig(
							parent = pelvisRig.pelvis_jnt ,
							side = 'RGT' ,
							animGrp = anim ,
							jntGrp = jnt ,
							ikhGrp = ikh ,
							skinGrp = skin ,
							stillGrp = still ,
							ribbon = True ,
							charSize = size ,
							tmpJnt = (
											'upLegRGT_tmpJnt' ,
											'lowLegRGT_tmpJnt' ,
											'ankleRGT_tmpJnt' ,
											'ballRGT_tmpJnt' ,
											'toeRGT_tmpJnt' ,
											'heelRGT_tmpJnt' ,
											'footInRGT_tmpJnt' ,
											'footOutRGT_tmpJnt' ,
											'kneeIkRGT_tmpJnt'
										)
						)

rigTools.nodeNaming(
						legRRig ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

rigTools.dummyNaming(
						obj = legRRig.upLegRbn ,
						attr = 'rbn' ,
						dummy = 'upLegRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

rigTools.dummyNaming(
						obj = legRRig.lowLegRbn ,
						attr = 'rbn' ,
						dummy = 'lowLegRbn' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

# Index left
indexLRig = pfngr.FingerRig(
								fngr = 'index' ,
								parent = armLRig.wrist_jnt ,
								armCtrl = armLRig.arm_ctrl ,
								side = 'LFT' , animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'index1LFT_tmpJnt' ,
												'index2LFT_tmpJnt' ,
												'index3LFT_tmpJnt' ,
												'index4LFT_tmpJnt' ,
												'index5LFT_tmpJnt'
											)
							)

rigTools.dummyNaming(
						obj = indexLRig ,
						attr = 'fngr' ,
						dummy = 'index' ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

ctrl = pc.Dag( armLRig.arm_ctrl.shape )
fngr = 'index'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -1
ctrl.attr('%s3CupRx' % fngr ).value = -1
ctrl.attr('%s4CupRx' % fngr ).value = -1
ctrl.attr('%s2Spread' % fngr ).value = -9
ctrl.attr('%sBaseSpread' % fngr ).value = -9

# Middle left
middleLRig = pfngr.FingerRig(
								fngr = 'middle' ,
								parent = armLRig.wrist_jnt ,
								armCtrl = armLRig.arm_ctrl ,
								side = 'LFT' ,
								animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'middle1LFT_tmpJnt' ,
												'middle2LFT_tmpJnt' ,
												'middle3LFT_tmpJnt' ,
												'middle4LFT_tmpJnt' ,
												'middle5LFT_tmpJnt'
											)
							)

rigTools.dummyNaming(
						obj = middleLRig ,
						attr = 'fngr' ,
						dummy = 'middle' ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

ctrl = pc.Dag( armLRig.arm_ctrl.shape )
fngr = 'middle'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -2.5
ctrl.attr('%s3CupRx' % fngr ).value = -2.5
ctrl.attr('%s4CupRx' % fngr ).value = -2.5

# Ring left
ringLRig = pfngr.FingerRig(
								fngr = 'ring' ,
								parent = armLRig.wrist_jnt ,
								armCtrl = armLRig.arm_ctrl ,
								side = 'LFT' ,
								animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'ring1LFT_tmpJnt' ,
												'ring2LFT_tmpJnt' ,
												'ring3LFT_tmpJnt' ,
												'ring4LFT_tmpJnt' ,
												'ring5LFT_tmpJnt'
											)
							)

rigTools.dummyNaming(
						obj = ringLRig ,
						attr = 'fngr' ,
						dummy = 'ring' ,
						charName = charName ,
						elem = elem ,
						side = 'LFT'
					)

ctrl = pc.Dag( armLRig.arm_ctrl.shape )
fngr = 'ring'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -3.5
ctrl.attr('%s3CupRx' % fngr ).value = -3.5
ctrl.attr('%s4CupRx' % fngr ).value = -3.5
ctrl.attr('%s2Spread' % fngr ).value = 4.5
ctrl.attr('%sBaseSpread' % fngr ).value = 4.5

# Pinky left
pinkyLRig = pfngr.FingerRig(
								fngr = 'pinky' ,
								parent = armLRig.wrist_jnt ,
								armCtrl = armLRig.arm_ctrl ,
								side = 'LFT' ,
								animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'pinky1LFT_tmpJnt' ,
												'pinky2LFT_tmpJnt' ,
												'pinky3LFT_tmpJnt' ,
												'pinky4LFT_tmpJnt' ,
												'pinky5LFT_tmpJnt'
											)
							)

rigTools.dummyNaming( obj = pinkyLRig ,
			attr = 'fngr' ,
			dummy = 'pinky' ,
			charName = charName ,
			elem = elem ,
			side = 'LFT' )

ctrl = pc.Dag( armLRig.arm_ctrl.shape )
fngr = 'pinky'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -4.5
ctrl.attr('%s3CupRx' % fngr ).value = -4.5
ctrl.attr('%s4CupRx' % fngr ).value = -4.5
ctrl.attr('%s2Spread' % fngr ).value = 9
ctrl.attr('%sBaseSpread' % fngr ).value = 9

# Thumb left
thumbLRig = pthmb.ThumbRig(
								parent = armLRig.wrist_jnt ,
								armCtrl = armLRig.arm_ctrl ,
								side = 'LFT' ,
								animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'thumb1LFT_tmpJnt' ,
												'thumb2LFT_tmpJnt' ,
												'thumb3LFT_tmpJnt' ,
												'thumb4LFT_tmpJnt' ,
												'thumb5LFT_tmpJnt'
											)
							)

rigTools.nodeNaming( thumbLRig ,
			charName = charName ,
			elem = elem ,
			side = 'LFT' )

ctrl = pc.Dag( armLRig.arm_ctrl.shape )
fngr = 'thumb'
ctrl.attr('%s2FistRx' % fngr ).value = -4.5
ctrl.attr('%s3FistRx' % fngr ).value = -9

# Index right
indexRRig = pfngr.FingerRig(
								fngr = 'index' ,
								parent = armRRig.wrist_jnt ,
								armCtrl = armRRig.arm_ctrl ,
								side = 'RGT' , animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'index1RGT_tmpJnt' ,
												'index2RGT_tmpJnt' ,
												'index3RGT_tmpJnt' ,
												'index4RGT_tmpJnt' ,
												'index5RGT_tmpJnt'
											)
							)

rigTools.dummyNaming(
						obj = indexRRig ,
						attr = 'fngr' ,
						dummy = 'index' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

ctrl = pc.Dag( armRRig.arm_ctrl.shape )
fngr = 'index'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -1
ctrl.attr('%s3CupRx' % fngr ).value = -1
ctrl.attr('%s4CupRx' % fngr ).value = -1
ctrl.attr('%s2Spread' % fngr ).value = -9
ctrl.attr('%sBaseSpread' % fngr ).value = -9

# Middle right
middleRRig = pfngr.FingerRig(
								fngr = 'middle' ,
								parent = armRRig.wrist_jnt ,
								armCtrl = armRRig.arm_ctrl ,
								side = 'RGT' ,
								animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'middle1RGT_tmpJnt' ,
												'middle2RGT_tmpJnt' ,
												'middle3RGT_tmpJnt' ,
												'middle4RGT_tmpJnt' ,
												'middle5RGT_tmpJnt'
											)
							)

rigTools.dummyNaming(
						obj = middleRRig ,
						attr = 'fngr' ,
						dummy = 'middle' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

ctrl = pc.Dag( armRRig.arm_ctrl.shape )
fngr = 'middle'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -2.5
ctrl.attr('%s3CupRx' % fngr ).value = -2.5
ctrl.attr('%s4CupRx' % fngr ).value = -2.5

# Ring right
ringRRig = pfngr.FingerRig(
							fngr = 'ring' ,
							parent = armRRig.wrist_jnt ,
							armCtrl = armRRig.arm_ctrl ,
							side = 'RGT' ,
							animGrp = anim ,
							skinGrp = skin ,
							stillGrp = still ,
							charSize = size ,
							tmpJnt = (
										'ring1RGT_tmpJnt' ,
										'ring2RGT_tmpJnt' ,
										'ring3RGT_tmpJnt' ,
										'ring4RGT_tmpJnt' ,
										'ring5RGT_tmpJnt'
										)
							)

rigTools.dummyNaming(
						obj = ringRRig ,
						attr = 'fngr' ,
						dummy = 'ring' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

ctrl = pc.Dag( armRRig.arm_ctrl.shape )
fngr = 'ring'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -3.5
ctrl.attr('%s3CupRx' % fngr ).value = -3.5
ctrl.attr('%s4CupRx' % fngr ).value = -3.5
ctrl.attr('%s2Spread' % fngr ).value = 4.5
ctrl.attr('%sBaseSpread' % fngr ).value = 4.5

# Pinky right
pinkyRRig = pfngr.FingerRig(
								fngr = 'pinky' ,
								parent = armRRig.wrist_jnt ,
								armCtrl = armRRig.arm_ctrl ,
								side = 'RGT' ,
								animGrp = anim ,
								skinGrp = skin ,
								stillGrp = still ,
								charSize = size ,
								tmpJnt = (
												'pinky1RGT_tmpJnt' ,
												'pinky2RGT_tmpJnt' ,
												'pinky3RGT_tmpJnt' ,
												'pinky4RGT_tmpJnt' ,
												'pinky5RGT_tmpJnt'
											)
							)

rigTools.dummyNaming(
						obj = pinkyRRig ,
						attr = 'fngr' ,
						dummy = 'pinky' ,
						charName = charName ,
						elem = elem ,
						side = 'RGT'
					)

ctrl = pc.Dag( armRRig.arm_ctrl.shape )
fngr = 'pinky'
ctrl.attr('%s2FistRx' % fngr ).value = -9
ctrl.attr('%s3FistRx' % fngr ).value = -9
ctrl.attr('%s4FistRx' % fngr ).value = -9
ctrl.attr('%s2CupRx' % fngr ).value = -4.5
ctrl.attr('%s3CupRx' % fngr ).value = -4.5
ctrl.attr('%s4CupRx' % fngr ).value = -4.5
ctrl.attr('%s2Spread' % fngr ).value = 9
ctrl.attr('%sBaseSpread' % fngr ).value = 9

# Thumb right
thumbRRig = pthmb.ThumbRig(
							parent = armRRig.wrist_jnt ,
							armCtrl = armRRig.arm_ctrl ,
							side = 'RGT' ,
							animGrp = anim ,
							skinGrp = skin ,
							stillGrp = still ,
							charSize = size ,
							tmpJnt = (
										'thumb1RGT_tmpJnt' ,
										'thumb2RGT_tmpJnt' ,
										'thumb3RGT_tmpJnt' ,
										'thumb4RGT_tmpJnt' ,
										'thumb5RGT_tmpJnt'
										)
							)

rigTools.nodeNaming( thumbRRig ,
			charName = charName ,
			elem = elem ,
			side = 'RGT' )

ctrl = pc.Dag( armRRig.arm_ctrl.shape )
fngr = 'thumb'
ctrl.attr('%s2FistRx' % fngr ).value = -4.5
ctrl.attr('%s3FistRx' % fngr ).value = -9

# Tongue
tongueRig = pfk.FkRig(
							parent = 'jaw1LWR_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'tongue1_jnt' ,
										'tongue2_jnt' ,
										'tongue3_jnt' ,
										'tongue4_jnt' ,
										'tongue5_jnt' ,
										'tongue6_jnt'
									] ,
							name = 'tongue' ,
							side = '' ,
							ax='y' ,
							shape='circle'
						)

# Lower teeth
lowerTeethRig = pfkg.FkGroupRig(
									parent = 'jaw3LWR_jnt' ,
									animGrp = 'anim_grp' ,
									charSize = size ,
									tmpJnt = [
												'lowerTeeth_jnt'
											] ,
									name = 'lowerTeeth' ,
									side = '' ,
									shape='cube'
								)

# Upper teeth
upperTeethRig = pfkg.FkGroupRig(
									parent = 'jaw1UPR_jnt' ,
									animGrp = 'anim_grp' ,
									charSize = size ,
									tmpJnt = [
												'upperTeeth_jnt'
											] ,
									name = 'upperTeeth' ,
									side = '' ,
									shape='cube'
								)


# Left thumbToe
thumbToeRig = pfk.FkRig(
							parent = 'toeLFT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'thumbToe1LFT_jnt' ,
										'thumbToe2LFT_jnt' ,
										'thumbToe3LFT_jnt'

									] ,
							name = 'thumbToe' ,
							side = 'LFT' ,
							ax='y' ,
							shape='circle'
						)

# Left indexToe
indexToeRig = pfk.FkRig(
							parent = 'toeLFT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'indexToe1LFT_jnt' ,
										'indexToe2LFT_jnt' ,
										'indexToe3LFT_jnt'

									] ,
							name = 'indexToe' ,
							side = 'LFT' ,
							ax='y' ,
							shape='circle'
						)

# Left middleToe
middleToeRig = pfk.FkRig(
							parent = 'toeLFT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'middleToe1LFT_jnt' ,
										'middleToe2LFT_jnt' ,
										'middleToe3LFT_jnt'

									] ,
							name = 'middleToe' ,
							side = 'LFT' ,
							ax='y' ,
							shape='circle'
						)

# Left ringToe
ringToeRig = pfk.FkRig(
							parent = 'toeLFT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'ringToe1LFT_jnt' ,
										'ringToe2LFT_jnt' ,
										'ringToe3LFT_jnt'

									] ,
							name = 'ringToe' ,
							side = 'LFT' ,
							ax='y' ,
							shape='circle'
						)

# Left pinkyToe
pinkyToeRig = pfk.FkRig(
							parent = 'toeLFT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'pinkyToe1LFT_jnt' ,
										'pinkyToe2LFT_jnt' ,
										'pinkyToe3LFT_jnt'

									] ,
							name = 'pinkyToe' ,
							side = 'LFT' ,
							ax='y' ,
							shape='circle'
						)

# Right thumbToe
thumbToeRig = pfk.FkRig(
							parent = 'toeRGT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'thumbToe1RGT_jnt' ,
										'thumbToe2RGT_jnt' ,
										'thumbToe3RGT_jnt'

									] ,
							name = 'thumbToe' ,
							side = 'RGT' ,
							ax='y' ,
							shape='circle'
						)

# Right indexToe
indexToeRig = pfk.FkRig(
							parent = 'toeRGT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'indexToe1RGT_jnt' ,
										'indexToe2RGT_jnt' ,
										'indexToe3RGT_jnt'

									] ,
							name = 'indexToe' ,
							side = 'RGT' ,
							ax='y' ,
							shape='circle'
						)

# Right middleToe
middleToeRig = pfk.FkRig(
							parent = 'toeRGT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'middleToe1RGT_jnt' ,
										'middleToe2RGT_jnt' ,
										'middleToe3RGT_jnt'

									] ,
							name = 'middleToe' ,
							side = 'RGT' ,
							ax='y' ,
							shape='circle'
						)

# Right ringToe
ringToeRig = pfk.FkRig(
							parent = 'toeRGT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'ringToe1RGT_jnt' ,
										'ringToe2RGT_jnt' ,
										'ringToe3RGT_jnt'

									] ,
							name = 'ringToe' ,
							side = 'RGT' ,
							ax='y' ,
							shape='circle'
						)

# Right pinkyToe
pinkyToeRig = pfk.FkRig(
							parent = 'toeRGT_jnt' ,
							animGrp = 'anim_grp' ,
							charSize = size ,
							tmpJnt = [
										'pinkyToe1RGT_jnt' ,
										'pinkyToe2RGT_jnt' ,
										'pinkyToe3RGT_jnt'

									] ,
							name = 'pinkyToe' ,
							side = 'RGT' ,
							ax='y' ,
							shape='circle'
						)


if placement.exists :
	mc.delete( placement )
