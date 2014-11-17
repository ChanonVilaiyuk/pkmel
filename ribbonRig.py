import pkmel.ribbon as ribbon
import pkmel.core as pc

ax = 'z+'
name = 'necklaceC'
side = 'RGT'

sels = mc.ls( sl=True )

root = sels[0]
end = sels[1]

size = pc.distance( root , end )

rbn = ribbon.RibbonIkLow( size , ax )

rigTools.dummyNaming(
						rbn ,
						attr = 'rbn' ,
						dummy = name ,
						charName = '' ,
						elem = '' ,
						side = side
					)

mc.parentConstraint( root , rbn.rbnAnim_grp )
mc.pointConstraint( root , rbn.rbnRoot_ctrl )
mc.pointConstraint( end , rbn.rbnEnd_ctrl )