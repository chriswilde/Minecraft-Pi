import minecraft.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

mc.player.setPos(70,14,-46)

x = 97
y = 9
z = -52
startPosition = z

for floor in range (6):
    for window in range (4):
        mc.setBlock(x,y,z,102)
        mc.setBlock(x,y+1,z,102)
        mc.setBlock(x,y,z+1,102)
        mc.setBlock(x,y+1,z+1,102)
        z=z+4
        time.sleep(0.2)
    z = startPosition
    y = y+4
