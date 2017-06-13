from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

mc.player.setPos (80,1,125)

#Rectangular Wall
x = 60
y = 1
z = 100

for i in range (39):
    for i in range (12):
        mc.setBlock(x,y,z,01)
        y=y+1
        time.sleep(0.1)
    x=x+1
    y=1
#Crenelations
x = 60
y = 13
z = 100

for i in range(20):
    mc.setBlock(x,y,z,01)
    x=x+2
    time.sleep(0.1)
#Sills
x = 62
y = 3
z = 100

for i in range(9):
    for i in range(3):
        mc.setBlock(x,y,z,89)
        x=x+1
        time.sleep(0.1)
    x=x+1
#windows
x = 62
y = 4
z = 100

for i in range (9):
    for i in range(5):
        mc.setBlock(x,y,z,102)
        y=y+1
        time.sleep(0.1)
    x=x+1
    y=4
    for i in range(6):
        mc.setBlock(x,y,z,102)
        y=y+1
        time.sleep(0.1)
    x=x+1
    y=4
    for i in range(5):
        mc.setBlock(x,y,z,102)
        y=y+1
        time.sleep(0.1)
    x=x+2
    y=4
#Torches
x = 61
y = 5
z = 99

for i in range(10):
    mc.setBlock(x,y,z,50)
    x=x+4
    time.sleep(0.1)
