from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    time.sleep(5)
    text = raw_input("What should we say?")
    time.sleep (5)
    mc.postToChat (text)
