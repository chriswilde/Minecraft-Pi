from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

xPos = 0
yPos = 1
zPos = -105

time.sleep(5)
mc.player.setPos (xPos, yPos, zPos)
