import minecraft.minecraft as minecraft
mc = minecraft.Minecraft.create()

xPos = 62
yPos = 2
zPos = -97
blockType = 103

mc.setBlock(xPos, yPos, zPos, blockType)
yPos = yPos + 1
mc.setBlock(xPos, yPos, zPos, blockType)
