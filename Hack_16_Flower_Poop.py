import minecraft.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    xPos = mc.player.getPos().x
    yPos = mc.player.getPos().y
    zPos = mc.player.getPos().z
    mc.setBlock(xPos,yPos,zPos,37)
    time.sleep(0.1)
    xPos = mc.player.getPos().x
    yPos = mc.player.getPos().y
    zPos = mc.player.getPos().z
    mc.setBlock(xPos,yPos,zPos,38)
    time.sleep(0.1)
