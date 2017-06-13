from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

xPos = 92
yPos = 1
zPos = -102

while yPos < 50:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    time.sleep (0.2)

    
