import minecraft.minecraft as minecraft
mc=minecraft.Minecraft.create()
def wall1():
    x = 126
    y = 1
    z = -122
    mc.setBlocks(x,y,z-4,x,y+13,z+36,35,1)
    mc.setBlocks(x,y+1,z,x,y+13,z+35,35,0)
    mc.setBlock(x,y+9,z+2,35,1)

    z = z + 2
    y = y + 8

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    z = z + 4

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    y = y - 3
    z = z + 1
    mc.setBlock(x,y,z,35,7)
    z = z + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    z = z - 2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    z = z - 1
    y = y - 1
    mc.setBlock(x,y,z,35,7)

    z = z + 4
    y = y + 2

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    y = y + 1
    z = z - 1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    z = z + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    z = z - 2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    y = y - 4

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    z = z + 3
    y = y + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        z = z + 1

    z = z - 2

    for i in range(5):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y = y + 1
    z = z - 1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        z = z + 1

    z = z + 1
    y = y + 3

    for i in range(1):
        mc.setBlock(x,y,z,35,1)
        y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,1)
        z = z + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y = y + 1
    z = z - 2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    z = z - 1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        z = z + 1

    y = y + 4
    z = z - 20

    mc.setBlock(x,y,z,35,7)

    z = z - 10
    y = y + 2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    z = z - 1
    y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    z = z - 1
    y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    mc.setBlock(x,y,z,35,1)

    z = z + 1

    for i in range(8):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    mc.setBlock(x,y,z,35,1)

    z = z + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z + 1

    z = z-1
    y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z + 1

    y = y - 1
    mc.setBlock(x,y,z,35,8)
    z = z - 1
    y = y - 1
    mc.setBlock(x,y,z,35,8)
    z = z - 1
    y = y - 1
    mc.setBlock(x,y,z,35,8)
    z = z - 1
    y = y + 1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z - 1
    z = z + 1
    y = y + 1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z - 1
    z = z + 2
    y = y + 1
    mc.setBlock(x,y,z,35,8)

def wall2():
    x = 122
    y = 1
    z = 126
    mc.setBlocks(x+4,y,z,x-36,y+13,z,35,1)
    mc.setBlocks(x,y+1,z,x-35,y+13,z,35,0)
    mc.setBlock(x-2,y+9,z,35,1)

    x = x - 2
    y = y + 8

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    x = x - 4

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    y = y - 3
    x = x - 1
    mc.setBlock(x,y,z,35,7)
    x = x - 2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    x = x + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    x = x + 1
    y = y - 1
    mc.setBlock(x,y,z,35,7)

    x = x - 4
    y = y + 2

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    y = y + 1
    x = x + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    x = x - 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    x = x + 2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    y = y - 4

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    x = x - 3
    y = y + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        x = x - 1

    x = x + 2

    for i in range(5):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y = y + 1
    x = x + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        x = x - 1

    x = x - 1
    y = y + 3

    for i in range(1):
        mc.setBlock(x,y,z,35,1)
        y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,1)
        x = x - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y = y + 1
    x = x + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    x = x + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        x = x - 1

    y = y + 4
    x = x + 20

    mc.setBlock(x,y,z,35,7)

    x = x + 10
    y = y + 2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    x = x + 1
    y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    x = x + 1
    y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    mc.setBlock(x,y,z,35,1)

    x = x - 1

    for i in range(8):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    mc.setBlock(x,y,z,35,1)

    x = x - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x -1

    x = x + 1
    y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x - 1

    y = y - 1
    mc.setBlock(x,y,z,35,8)
    x = x + 1
    y = y - 1
    mc.setBlock(x,y,z,35,8)
    x = x + 1
    y = y - 1
    mc.setBlock(x,y,z,35,8)
    x = x + 1
    y = y + 1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x + 1
    x = x - 1
    y = y + 1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x + 1
    x = x - 2
    y = y + 1
    mc.setBlock(x,y,z,35,8)

def wall3():
    x = -126
    y = 1
    z = 122
    mc.setBlocks(x,y,z+4,x,y+13,z-36,35,1)
    mc.setBlocks(x,y+1,z,x,y+13,z-35,35,0)
    mc.setBlock(x,y+9,z-2,35,1)

    z = z - 2
    y = y + 8

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    z = z - 4

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    y = y - 3
    z = z - 1
    mc.setBlock(x,y,z,35,7)
    z = z - 2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    z = z + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    z = z + 1
    y = y - 1
    mc.setBlock(x,y,z,35,7)

    z = z - 4
    y = y + 2

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    y = y + 1
    z = z + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    z = z - 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    z = z + 2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z + 1

    y = y - 4

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    z = z - 3
    y = y + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        z = z - 1

    z = z + 2

    for i in range(5):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y = y + 1
    z = z + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        z = z - 1

    z = z - 1
    y = y + 3

    for i in range(1):
        mc.setBlock(x,y,z,35,1)
        y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,1)
        z = z - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y = y + 1
    z = z + 2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    z = z + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        z = z - 1

    y = y + 4
    z = z + 20

    mc.setBlock(x,y,z,35,7)

    z = z + 10
    y = y + 2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    z = z + 1
    y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    z = z + 1
    y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    mc.setBlock(x,y,z,35,1)

    z = z - 1

    for i in range(8):
        mc.setBlock(x,y,z,35,7)
        z = z - 1

    mc.setBlock(x,y,z,35,1)

    z = z - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z -1

    z = z + 1
    y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z - 1

    y = y - 1
    mc.setBlock(x,y,z,35,8)
    z = z + 1
    y = y - 1
    mc.setBlock(x,y,z,35,8)
    z = z + 1
    y = y - 1
    mc.setBlock(x,y,z,35,8)
    z = z + 1
    y = y + 1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z + 1
    z = z - 1
    y = y + 1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        z = z + 1
    z = z - 2
    y = y + 1
    mc.setBlock(x,y,z,35,8)
def wall4():
    x = -122
    y = 1
    z = -126
    mc.setBlocks(x-4,y,z,x+36,y+13,z,35,1)
    mc.setBlocks(x,y+1,z,x+35,y+13,z,35,0)
    mc.setBlock(x+2,y+9,z,35,1)

    x = x + 2
    y = y + 8

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    x = x + 4

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    y=y-3
    x=x+1
    mc.setBlock(x,y,z,35,7)
    x=x+2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    x=x-2

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    x=x-1
    y=y-1
    mc.setBlock(x,y,z,35,7)

    x=x+4
    y=y+2

    for i in range(1):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y = y - 1

    y=y+1
    x=x-1

    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    x=x+1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    x=x-2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x - 1

    y=y-4

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y = y + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    x=x+3
    y=y+2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        x = x + 1

    x = x-2

    for i in range(5):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y=y+1
    x=x-1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        x = x + 1

    x=x+1
    y=y+3

    for i in range(1):
        mc.setBlock(x,y,z,35,1)
        y = y + 1

    for i in range(4):
        mc.setBlock(x,y,z,35,1)
        x = x + 1

    for i in range(2):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    y=y+1
    x=x-2

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        y = y - 1

    x=x-1

    for i in range(3):
        mc.setBlock(x,y,z,35,1)
        x = x + 1

    y=y+4
    x=x-20

    mc.setBlock(x,y,z,35,7)

    x=x-10
    y=y+2

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    x=x-1
    y=y+1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    x=x-1
    y=y+1

    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    mc.setBlock(x,y,z,35,1)

    x=x+1

    for i in range(8):
        mc.setBlock(x,y,z,35,7)
        x = x + 1

    mc.setBlock(x,y,z,35,1)

    x=x+1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x + 1

    x = x-1
    y=y-1

    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x + 1

    y=y-1
    mc.setBlock(x,y,z,35,8)
    x = x-1
    y=y-1
    mc.setBlock(x,y,z,35,8)
    x = x-1
    y=y-1
    mc.setBlock(x,y,z,35,8)
    x = x-1
    y=y+1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x - 1
    x=x+1
    y=y+1
    for i in range(2):
        mc.setBlock(x,y,z,35,8)
        x = x - 1
    x=x+2
    y=y+1
    mc.setBlock(x,y,z,35,8)

