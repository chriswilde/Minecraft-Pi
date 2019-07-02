#CARSEL

x1 = -15
y1 = 0
z1 = -15
x2 = 15
y2 = 12
z2 = 15
    
mc.setBlocks(x1-5,y1-10,z1-5,x2+5,y2-12,z2+5,44)
def hall(x1,y1,z1,x2,y2,z2,block):
    xoriginal = x1 
    yoriginal = y1
    zoriginal = z1
    #main hall of the castle:
    hall = [x1,y1,z1,x2,y2,z2,block]
    mc.setBlocks(hall)
    hollow = [(x1+1),(y1+1),(z1+1),(x2-1),(y2-1),(z2-1),00]
    mc.setBlocks(hollow)
    #Crenelations
    while x1 < x2:
        x1 = x1+2
        mc.setBlock(x1,y2+1,z1,block)
    x1=xoriginal
    while z1 < z2:
        z1 = z1+2
        mc.setBlock(x1,y2+1,z1,block)
    z1 = zoriginal 
    while x1 < x2:
        x1 = x1+2
        mc.setBlock(x1,y2+1,z2,block)
    x1=xoriginal
    while z1 < z2:
        z1 = z1+2
        mc.setBlock(x2,y2+1,z1,block)
    z1 = zoriginal

hall(x1,y1,z1,x2,y2,z2,24)

def hallsillsx(x,y,z):
    for i in range(5):
        for i in range(2):
            mc.setBlock(x,y,z,89)
            x=x+1
        mc.setBlock(x,y,z,89)
        x=x+2

hallsillsx(x1+6,y1+2,z2)

def windowsx(x,y,z):
    for i in range (5):
        for i in range(5):
            mc.setBlock(x,y,z,102)
            y=y+1
        x=x+1
        y=y-5
        for i in range(6):
            mc.setBlock(x,y,z,102)
            y=y+1
        x=x+1
        y=y-6
        for i in range(5):
            mc.setBlock(x,y,z,102)
            y=y+1
        x=x+2
        y=y-5

windowsx(x1+6,y1+3,z2)

def hallsillsz(x,y,z):
    for i in range(5):
        for i in range(2):
            mc.setBlock(x,y,z,89)
            z=z+1
        mc.setBlock(x,y,z,89)
        z=z+2

hallsillsz(x1,y1+2,z1+6)
hallsillsz(x2,y1+2,z1+6)

def windowsz(x,y,z):
    for i in range (5):
        for i in range(5):
            mc.setBlock(x,y,z,102)
            y=y+1
        z=z+1
        y=y-5
        for i in range(6):
            mc.setBlock(x,y,z,102)
            y=y+1
        z=z+1
        y=y-6
        for i in range(5):
            mc.setBlock(x,y,z,102)
            y=y+1
        z=z+2
        y=y-5

windowsz(x1,y1+3,z1+6)
windowsz(x2,y1+3,z1+6)

def doorway(x,y,z):
    while x < 3:
        while y < 5:
            mc.setBlock(x,y,z,0)
            y = y+1
        x=x+1
        y=1
        while y < 6:
            mc.setBlock(x,y,z,0)
            y = y+1
        x=x+1
        y=1
        while y < 7:
            mc.setBlock(x,y,z,0)
            y = y+1
        x=x+1
        y=1
        while y < 6:
            mc.setBlock(x,y,z,0)
            y = y+1
        x=x+1
        y=1
        while y < 5:
            mc.setBlock(x,y,z,0)
            y = y+1
        x=x+1
        y=1

doorway(x1+13,y1+1,z1)

def drawbridge(x,y,z):
    for i in range (7):
        for i in range (60):
            mc.setBlock(x,y,z,17)
            z = z-1
        x=x+1
        z=z+60

drawbridge(x1+12,y1,z1-1)
        
def tower(x1,y1,z1,x2,y2,z2,block):
    xoriginal = x1
    yoriginal = y1
    zoriginal = z1
    #Build and hollow out Tower structure
    tower = [x1,y1,z1,x2,y2,z2,block]
    mc.setBlocks(tower)
    hollow = [(x1+1),(y1+1),(z1+1),(x2-1),(y2-1),(z2-1),00]
    mc.setBlocks(hollow)
    #Floors Within Towers
    floor1 = [(x1+1),(y1+4),(z1+1),(x2-2),(y1+4),(z2-1),17]
    mc.setBlocks(floor1)
    floor2 = [(x1+1),(y1+8),(z1+2),(x2-1),(y1+8),(z2-1),17]
    mc.setBlocks(floor2)
    floor3 = [(x1+2),(y1+12),(z1+1),(x2-1),(y1+12),(z2-1),17]
    mc.setBlocks(floor3)
    #Stairways within Towers
    x1 = x1 + 5
    z1 = z1 + 5   
    for i in range(4):
        z1=z1-1
        y1=y1+1
        mc.setBlock(x1,y1,z1,114,3)
    for i in range (4):
        x1=x1-1
        y1=y1+1
        mc.setBlock(x1,y1,z1,114,1)
    for i in range(4):
        z1=z1+1
        y1=y1+1
        mc.setBlock(x1,y1,z1,114,2)
    #Reset to original values
    x1 = xoriginal
    y1 = yoriginal
    z1 = zoriginal
    #crenelations
    for i in range(3):
        x1 = x1+2
        mc.setBlock(x1,y2+1,z1,block)   
    for i in range(3):
        z1 = z1+2
        mc.setBlock(x1,y2+1,z1,block)
    for i in range(3):
        x1 = x1-2
        mc.setBlock(x1,y2+1,z1,block)   
    for i in range(3):
        z1 = z1-2
        mc.setBlock(x1,y2+1,z1,block)

tower(x1-3,y1,z1-3,x1+3,y2+6,z1+3,24)
tower(x2-3,y1,z1-3,x2+3,y2+6,z1+3,24)
tower(x1-3,y1,z2-3,x1+3,y2+6,z2+3,24)
tower(x2-3,y1,z2-3,x2+3,y2+6,z2+3,24)

def towerDoors(x,y,z,block):
    for i in range(2):
        mc.setBlock(x,y,z,block)
        y = y+1

towerDoors(x1+2,y1+1,z1+3,00)
towerDoors(x1+2,y1+1,z2-3,00)
towerDoors(x2-2,y1+1,z2-3,00)
towerDoors(x2-2,y1+1,z1+3,00)
towerDoors(x1+2,y2+1,z1+3,00)
towerDoors(x1+2,y2+1,z2-3,00)
towerDoors(x2-2,y2+1,z1+3,00)
towerDoors(x2-2,y2+1,z2-3,00)

def towerwindows(x,y,z):
        for i in range (3):
            for i in range (3):
                mc.setBlock(x,y,z,102)
                y=y+1
            y=y+3

towerwindows(-18,2,15)
towerwindows(-18,2,-15)
towerwindows(18,2,15)
towerwindows(18,2,-15)
towerwindows(-15,2,18)
towerwindows(-15,2,-18)
towerwindows(15,2,18)
towerwindows(15,2,-18)

mc.player.setPos(0,0,0)
