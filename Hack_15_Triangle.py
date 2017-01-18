import minecraft.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

mc.player.setPos(85,1,10)

x = 95
y = 2
z = 8
endPosition = z + 5
startPosition = z

for i in range (3):
    while z < endPosition:
        mc.setBlock(x,y,z,103)
        z=z+1
        time.sleep(0.2)

    startPosition = startPosition + 1
    z = startPosition
    y = y + 1
    endPosition = endPosition - 1
    
