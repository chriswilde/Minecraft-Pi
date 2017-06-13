from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

mc.player.setPos(80,1,125)

def wall(x,y,z):
    for i in range (39):
        for i in range (12):
            mc.setBlock(x,y,z,01)
            y=y+1
            time.sleep(0.1)
        x=x+1
        y=y-12

def crenelations(x,y,z):
    for i in range(20):
        mc.setBlock(x,y,z,01)
        x=x+2
        time.sleep(0.1)

def sills(x,y,z):
    for i in range(9):
        for i in range(2):
            mc.setBlock(x,y,z,89)
            x=x+1
        mc.setBlock(x,y,z,89)
        x=x+2
        time.sleep(0.1)
        
def windows(x,y,z):
    for i in range (9):
        for i in range(5):
            mc.setBlock(x,y,z,102)
            y=y+1
        x=x+1
        y=y-5
        time.sleep(0.1)
        for i in range(6):
            mc.setBlock(x,y,z,102)
            y=y+1
        x=x+1
        y=y-6
        time.sleep(0.1)
        for i in range(5):
            mc.setBlock(x,y,z,102)
            y=y+1
        x=x+2
        y=y-5
        time.sleep(0.1)

def torches(x,y,z):
    for i in range(10):
        mc.setBlock(x,y,z,50)
        x=x+4
        time.sleep(0.1)

wall(60,1,108)
crenelations(60,13,108)
sills(62,3,108)
windows(62,4,108)
torches(61,5,109)
