from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

mc.player.setPos(85,1,-5)

x = 95
y = 2
z = -8

for i in range (6):
    for i in range (6):
        mc.setBlock(x,y,z,103)
        z=z+1
        time.sleep(0.2)
    y=y+1
    z=z-6
