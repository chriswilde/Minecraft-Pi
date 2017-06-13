from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    pos = mc.player.getTilePos()

    if 100 <= pos.x <= 115 and 50 <= pos.z <= 60:
        mc.setBlocks(101,1,51,109,2,59,48)

    elif 100 <= pos.x <= 110 and 60 <= pos.z <= 65:
        mc.setBlocks(101,1,51,109,2,59,57)

    elif 95 <= pos.x <= 100 and 50 <= pos.z <= 60:
        mc.setBlocks(101,1,51,109,2,59,103)

    elif 100 <= pos.x <= 110 and 45 <= pos.z <= 50:
        mc.setBlocks(101,1,51,109,2,59,74)

    else:
        mc.setBlocks(101,1,51,109,2,59,247)
