from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    xPos = raw_input("Where would you like to go on the x axis?")
    yPos = raw_input("Where would you like to go on the y axis?")
    zPos = raw_input("Where would you like to go on the z axis?")

    time.sleep(5)
    mc.player.setPos (xPos, yPos, zPos)
    mc.postToChat("You are now at: x = "+xPos+", y = "+yPos+", z = "+yPos)
