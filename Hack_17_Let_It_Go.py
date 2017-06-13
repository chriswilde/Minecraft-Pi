from mcpi.minecraft import Minecraft
import time
import minecraft.block as block
mc = Minecraft.create()


while True:
    xPos = mc.player.getPos().x
    yPos = mc.player.getPos().y - 1
    zPos = mc.player.getPos().z
    if mc.getBlockWithData(xPos,yPos,zPos) == block.GLOWING_OBSIDIAN:
        mc.setBlock(xPos,yPos,zPos,79)
