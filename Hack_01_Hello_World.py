from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(5)
mc.postToChat("Hello World")
