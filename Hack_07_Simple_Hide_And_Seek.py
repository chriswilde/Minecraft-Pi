import minecraft.minecraft as minecraft
import random
mc = minecraft.Minecraft.create()

xPos = random.randint(35,75)
yPos = 0
zPos = random.randint(-125,-85)

mc.setBlock(xPos,yPos,zPos,103)
mc.postToChat("Find Me at: x = "+str(xPos)+" z = "+str(zPos))
