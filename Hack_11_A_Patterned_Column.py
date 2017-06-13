from mcpi.minecraft import Minecraft
mc = Minecraft.create()

xPos = 97
yPos = 1
zPos = -102

while yPos < 100:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 01
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1

    
