import minecraft.minecraft as minecraft
import logos
mc=minecraft.Minecraft.create()

#------------FLATTEN AND BASIC BUILD UP------------#

#World Create Blocks
sky = [-128,0,-128,128,128,128,00]
mc.setBlocks(sky)
ground = [-128,-128,-128,128,-1,128,07]
mc.setBlocks(ground)
grass = [-128,-1,-128,128,-1,128,02]
mc.setBlocks(grass)

# Exterior Wall & Hollow
wall = [-128,0,-128,128,15,128,35,1]
mc.setBlocks(wall)
hollow = [-125,0,-125,125,15,125,00]
mc.setBlocks(hollow)

#Pathways
path1 = [75,-1,-125,85,-1,125,4]
mc.setBlocks(path1)
path2 = [-75,-1,-125,-85,-1,125,4]
mc.setBlocks(path2)
path3 = [-125,-1,75,125,-1,85,4]
mc.setBlocks(path3)
path4 = [-125,-1,-75,125,-1,-85,4]
mc.setBlocks(path4)
path5 = [-125,-1,-35,125,-1,-20,4]
mc.setBlocks(path5)
path6 = [-125,-1,20,125,-1,35,4]
mc.setBlocks(path6)
path7 = [-35,-1,-125,-20,-1,125,4]
mc.setBlocks(path7)
path8 = [35,-1,-125,20,-1,125,4]
mc.setBlocks(path8)

#Central Moat
moat = [-75,-10,-75,75,-1,75,9]
mc.setBlocks(moat)

#------------ADD LOGOS TO WALLS------------#

logos.wall1()
logos.wall2()
logos.wall3()
logos.wall4()

#------------AREA NUMBERS ADDED TO WALLS------------#

#Number 1 in wall at area 1
x = -56
y = 10
z = -126

mc.setBlock(x,y,z,35,7)
x=x+1
for i in range (8):
    mc.setBlock(x,y,z,35,7)
    y=y-1
x = -57
for i in range (5):
    mc.setBlock(x,y,z,35,7)
    x=x+1

#Number 2 in wall at area 2
x = -3
y = 9
z = -126

mc.setBlock(x,y,z,35,7)
y=y+1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x+1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x-1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x+1
for i in range (2):
    mc.setBlock(x,y,z,35,7)
    y=y+1

#Number 3 in wall at area 3
x = 52
y = 9
z = -126

mc.setBlock(x,y,z,35,7)
y=y+1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x+1
for i in range (8):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x-1
for i in range (2):
    mc.setBlock(x,y,z,35,7)
    y=y+1

y = y + 2
x = x + 2

for i in range (5):
    mc.setBlock(x,y,z,35,7)
    x=x + 1


#Number 4 in wall at area 4
x = 102
y = 10
z = -126

for i in range (3):
    mc.setBlock(x,y,z,35,7)
    y=y-1

for i in range (6):
    mc.setBlock(x,y,z,35,7)
    x=x+1

x=x-1
y=y+3

for i in range (7):
    mc.setBlock(x,y,z,35,7)
    y=y-1

#Number 5 in wall at area 5
x = 126
y = 9
z = -29

mc.setBlock(x,y,z,35,7)
y=y+1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    z=z-1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    z=z+1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    z=z-1
for i in range (2):
    mc.setBlock(x,y,z,35,7)
    y=y+1

#Number 6 in Area 6
x = 126
y = 9
z = 53

mc.setBlock(x,y,z,35,7)
y=y+1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    z=z-1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    z=z+1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    z=z-1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y+1

#Number 7 in wall at area 7
x = 80
y = 9
z = 126

mc.setBlock(x,y,z,35,7)
y=y+1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x-1

x=x+1
y=y-1
mc.setBlock(x,y,z,35,7)

for i in range (6):
    mc.setBlock(x,y,z,35,7)
    x=x+1
    y=y-1

#Number 8 for area 8
x = 3
y = 7
z = 126

mc.setBlock(x,y,z,35,7)
y=y+1
mc.setBlock(x,y,z,35,7)
y=y+1
mc.setBlock(x,y,z,35,7)
y=y+1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x-1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x+1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x-1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y+1

#Number 9 for area 9
x = -52
y = 7
z = 126

mc.setBlock(x,y,z,35,7)
y=y+1
mc.setBlock(x,y,z,35,7)
y=y+1
mc.setBlock(x,y,z,35,7)
y=y+1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x+1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x-1
for i in range (4):
    mc.setBlock(x,y,z,35,7)
    y=y-1
for i in range (7):
    mc.setBlock(x,y,z,35,7)
    x=x+1
for i in range (2):
    mc.setBlock(x,y,z,35,7)
    y=y+1

#Number 10 in wall at area 10
mc.setBlocks(-94,0,126,-124,12,126,35,1)

def one(x,y,z):
    mc.setBlock(x,y,z,35,7)
    x=x-1
    for i in range (7):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    x = x + 2
    for i in range (5):
        mc.setBlock(x,y,z,35,7)
        x=x-1

one(-97,10,126)

def zero (x,y,z):
    for i in range(4):
        x=x-1
        mc.setBlock(x,y,z,35,7)
    for i in range(7):
        y=y-1
        mc.setBlock(x,y,z,35,7)
    for i in range(4):
        x=x+1
        mc.setBlock(x,y,z,35,7)
    for i in range(7):
        y=y+1
        mc.setBlock(x,y,z,35,7)


zero(-103,10,126)

#------------AREAS WITH EXEMPLARS------------#

#------------AREA 1 - CHAT-------------#


area1= [-75,0,-125,-35,0,-85,24]
mc.setBlocks(area1)

def c (x,y,z):
    for i in range(4):
        mc.setBlock(x,y,z,103)
        x=x+1
    x=x-5
    y=y-1
    for i in range(5):
        mc.setBlock(x,y,z,103)
        y=y-1
    x=x+1
    
    for i in range(4):
        mc.setBlock(x,y,z,103)
        x=x+1

c(-72,8,-110)

def h (x,y,z):
    for i in range(7):
        mc.setBlock(x,y,z,103)
        y=y-1
    x=x+1
    y=y+4
    for i in range(3):
        mc.setBlock(x,y,z,103)
        x=x+1
    y=y+3
    for i in range(7):
        mc.setBlock(x,y,z,103)
        y=y-1
    

h (-62, 8, -110)

def a (x,y,z):
    for i in range(3):
        mc.setBlock(x,y,z,103)
        x=x+1
    for i in range(6):
        y=y-1
        mc.setBlock(x,y,z,103)
    x=x-4
    for i in range(6):
        mc.setBlock(x,y,z,103)
        y=y+1
    y=y-3
    for i in range(3):
        x=x+1
        mc.setBlock(x,y,z,103)
        
a(-50,8,-110)

def t (x,y,z):
    for i in range(5):
        mc.setBlock(x,y,z,103)
        x=x+1
    x = x-3
    for i in range(6):
        y=y-1
        mc.setBlock(x,y,z,103)

t(-42,8,-110)

    
#------------AREA 2 - TARGET FOR TELEPORTS------------#

white = [-20,0,-125,20,0,-85,35,0]
mc.setBlocks(white)
black = [-16,0,-121,16,0,-89,35,15]
mc.setBlocks(black)
blue = [-12,0,-117,12,0,-93,35,3]
mc.setBlocks(blue)
red = [-8,0,-113,8,0,-97,35,14]
mc.setBlocks(red)
red = [-4,0,-109,4,0,-101,35,4]
mc.setBlocks(red)

#------------AREA 3 - SETTING BLOCKS PLINTHS------------#
area3= [35,0,-125,75,0,-85,17,0]
mc.setBlocks(area3)

craft = [45,1,-95,49,1,-99,58]
mc.setBlocks(craft)
craft = [60,1,-95,64,1,-99,58]
mc.setBlocks(craft)
mc.setBlock(47,3,-112,103)
mc.setBlock(62,2,-112,103)
mc.setBlock(62,3,-112,103)
craft = [45,1,-110,49,1,-114,58]
mc.setBlocks(craft)
craft = [60,1,-110,64,1,-114,58]
mc.setBlocks(craft)

#------------AREA 4 - WHILE LOOP TOWER PLINTHS------------#
area4= [85,0,-125,125,0,-85,24]
mc.setBlocks(area4)

#Clear towers from area 4
area4= [85,1,-125,125,70,-85,00]
mc.setBlocks(area4)

#Columns in Area 4
xPos = 92
yPos = 1
zPos = -107

while yPos < 100:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1

xPos = 97
yPos = 1
zPos = -107

while yPos < 100:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 01
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1

xPos = 102
yPos = 1
zPos = -107

while yPos < 100:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 01
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 46
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1

xPos = 107
yPos = 1
zPos = -107

while yPos < 100:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 01
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 46
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 22
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1

xPos = 112
yPos = 1
zPos = -107

while yPos < 100:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 01
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 46
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 22
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 89
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1

xPos = 117
yPos = 1
zPos = -107

while yPos < 100:
    blockType = 103
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 01
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 46
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 22
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 89
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    blockType = 247
    mc.setBlock(xPos, yPos, zPos, blockType)
    yPos = yPos + 1
    
#Plinths for example towers
moss = [91,0,-101,93,0,-103,48]
mc.setBlocks(moss)
moss = [96,0,-101,98,0,-103,48]
mc.setBlocks(moss)
moss = [101,0,-101,103,0,-103,48]
mc.setBlocks(moss)
moss = [106,0,-101,108,0,-103,48]
mc.setBlocks(moss)
moss = [111,0,-101,113,0,-103,48]
mc.setBlocks(moss)
moss = [116,0,-101,118,0,-103,48]
mc.setBlocks(moss)

#Plinths for user towers
moss = [91,0,-106,93,0,-108,48]
mc.setBlocks(moss)
moss = [96,0,-106,98,0,-108,48]
mc.setBlocks(moss)
moss = [101,0,-106,103,0,-108,48]
mc.setBlocks(moss)
moss = [106,0,-106,108,0,-108,48]
mc.setBlocks(moss)
moss = [111,0,-106,113,0,-108,48]
mc.setBlocks(moss)
moss = [116,0,-106,118,0,-108,48]
mc.setBlocks(moss)

#------------AREA 5 - NESTED LOOPS FOR SHAPES------------#
area5 = [85,0,-75,125,0,20,24]
mc.setBlocks (area5)
air = [85,1,-75,125,1,20,00]
mc.setBlocks (air)

#Tower with for statement with windows added
Tower1 = [97, 1, -73,113,32,-58,22]
mc.setBlocks (Tower1)
hollow= [98,2,-72,112,31,-59,0]
mc.setBlocks(hollow)
x = 97
y = 9
z = -72
for floor in range (6):
    for window in range (4):
        mc.setBlock(x,y,z,102)
        mc.setBlock(x,y+1,z,102)
        mc.setBlock(x,y,z+1,102)
        mc.setBlock(x,y+1,z+1,102)
        z=z+4
    z = -72
    y = y+4

mc.setBlocks(97,1,-63,97,6,-68,00)#Doorway
mc.setBlocks(97,5,-71,97,6,-72,102)#window1
mc.setBlocks(97,5,-60,97,6,-59,102)#window2

#User example tower without windows
Tower2= [97,1,-53,113,32,-38,22]
mc.setBlocks(Tower2)
hollow= [98,2,-52,112,31,-39,00]
mc.setBlocks(hollow)

mc.setBlocks(97,1,-48,97,6,-43,00)#Doorway
mc.setBlocks(97,5,-52,97,6,-51,102)#window1
mc.setBlocks(97,5,-40,97,6,-39,102)#window2

#Plinths for shape making & Square code
mc.setBlocks(119,1,-25,110,1,-16,22)
mc.setBlocks(115,2,-23,115,7,-18,103)
mc.setBlocks(119,1,-10,110,1,-1,22)
mc.setBlocks(115,2,-8,115,7,-3,103)
mc.setBlocks(119,1,5,110,1,14,22)

#Triangle code
x = 115
y = 2
z = 8

endPosition = 13
startPosition = 8
for i in range (3):
    while z < endPosition:
        mc.setBlock(x,y,z,103)
        z = z + 1

    startPosition = startPosition + 1
    z = startPosition 
    y = y + 1
    endPosition = endPosition - 1

#User Plinths
mc.setBlocks(90,1,-25,99,1,-16,22)
mc.setBlocks(90,1,-10,99,1,0,22)
mc.setBlocks(90,1,5,99,1,14,22)


#------------AREA 6 - USER AND BLOCK DATA------------#

area6= [85,0,35,125,0,75,24]
mc.setBlocks(area6)

fence= [85,0,35,125,0,75,85]
mc.setBlocks(fence)

air= [86,0,36,124,0,74,00]
mc.setBlocks(air)

entrance= [85,0,52,85,0,54,00]
mc.setBlocks(entrance)

wall = [95,0,45,115,0,65,01]
mc.setBlocks(wall)

obsidian = [96,0,46,114,0,64,246]
mc.setBlocks(obsidian)

nether = [101,1,51,109,2,59,247]
mc.setBlocks(nether)

#------------AREA 7 - WALL PATTERNS------------#
area7= [125,0,85,35,0,125,24]
mc.setBlocks(area7)

#Rectangular Wall
x = 60
y = 1
z = 89

for i in range (39):
    for i in range (12):
        mc.setBlock(x,y,z,01)
        y=y+1
    x=x+1
    y=1
#Crenelations
x = 60
y = 13
z = 89

for i in range(20):
    mc.setBlock(x,y,z,01)
    x=x+2
#Sills
x = 62
y = 3
z = 89

for i in range(9):
    for i in range(2):
        mc.setBlock(x,y,z,89)
        x=x+1
    mc.setBlock(x,y,z,89)
    x=x+2

#windows
x = 62
y = 4
z = 89

for i in range (9):
    for i in range(5):
        mc.setBlock(x,y,z,102)
        y=y+1
    x=x+1
    y=4
    for i in range(6):
        mc.setBlock(x,y,z,102)
        y=y+1
    x=x+1
    y=4
    for i in range(5):
        mc.setBlock(x,y,z,102)
        y=y+1
    x=x+2
    y=4
#Torches
x = 61
y = 5
z = 88

for i in range(10):
    mc.setBlock(x,y,z,50)
    x=x+4




#------------AREA 8 - SMALL WORLD TO FLATTEN------------#
area8= [20,0,85,-20,0,125,24]
mc.setBlocks(area8)
swground = [-20,1,85,20,19,125,07]
swsoil = [-20,20,85,20,20,125,02]
mc.setBlocks(swground)
mc.setBlocks(swsoil)

#------------AREA 9 - LISTS FOR SHAPES------------#
area9= [-35,0,85,-75,0,125,24]
mc.setBlocks(area9)

plinth1 = [-71,0,121,-58,0,108,48]
mc.setBlocks(plinth1)

cube1 = [-69,1,119,-60,10,110,20]
mc.setBlocks(cube1)

hollow = [-68,1,118,-61,9,111,00]
mc.setBlocks(hollow)

plinth2 = [-56,0,116,-48,0,108,48]
mc.setBlocks(plinth2)

Tower1 = [-54,1,114,-50,30,110,41]
mc.setBlocks(Tower1)

hollow = [-53,2,113,-51,30,111,00]
mc.setBlocks(hollow)

mc.setBlock(-52,1,109,67,2)

mc.setBlock(-52,2,110,71,2)
mc.setBlock(-52,3,110,71,11)

x = -51
y = 6
z = 110

for floors in range (5):
    for full in range (3):
        for window in range (3):
            mc.setBlock (x,y,z,20)
            y=y+1
        y=y-3
        x=x-1
    x=x+3
    y=y+5

x1 = -49
y1 = 31
z1 = 109
x2 = -55
y2 = y1
z2 = 115
block = 57

for i in range (4):
    level = [x1,y1,z1,x2,y2,z2,block]
    mc.setBlocks (level)
    x1 = x1 - 1
    y1 = y1 + 1
    z1 = z1 + 1
    x2 = x2 + 1
    y2 = y1
    z2 = z2 - 1

plinth3 = [-38,0,121,-46,0,103,48]
mc.setBlocks(plinth3)

Tunnel1 = [-40,1,119,-44,5,105,45]
mc.setBlocks(Tunnel1)

Tunnel1 = [-41,1,119,-43,4,105,00]
mc.setBlocks(Tunnel1)

plinth4 = [-71,0,106,-64,0,88,48]
mc.setBlocks(plinth4)

plinth5 = [-53,0,101,-62,0,93,48]
mc.setBlocks(plinth5)

plinth5 = [-38,0,101,-51,0,88,48]
mc.setBlocks(plinth5)

#-----------Area_10_Physical_Computing_Area-------------------"

area10 = [-125,0,125,-85,0,85,24]
mc.setBlocks(area10)

def keys(x,y,z):
    for i in range (8):
        for i in range (4):
            for i in range (16):
                mc.setBlock(x,y,z,78)
                x = x - 1
            x = x + 16
            z = z - 1
        z = z - 1

keys(-110,1,124)

x = -125
y = 1
z = 120

for i in range (2):
    for i in range(10):
        mc.setBlock(x,y,z,16)
        x=x+1
    z = z - 5
    x = x - 10
z = z-5
for i in range (3):
    for i in range(10):
        mc.setBlock(x,y,z,16)
        x=x+1
    z = z - 5
    x = x - 10
z = z-5
for i in range(10):
        mc.setBlock(x,y,z,16)
        x=x+1
# Traffic lights
x = -106
y = 0
z = 121

for i in range (4):
    for i in range (10):
        mc.setBlock(x,y,z,35,15)
        x=x+1
    x=x-10
    z=z-1

mc.setBlocks(-105,0,120,-104,0,119,35,14)
mc.setBlocks(-102,0,120,-101,0,119,35,1)
mc.setBlocks(-99,0,120,-98,0,119,35,5)
mc.setBlocks(-96,0,120,-85,0,119,35,0)
mc.setBlocks(-94,0,120,-93,0,119,35,15)
mc.setBlocks(-90,0,120,-89,0,119,35,15)
mc.setBlocks(-86,0,120,-85,0,119,35,15)

mc.setBlocks(-91,0,115,-98,0,108,247)

#Weasley clock triggers

mc.setBlocks(-86,0,105,-93,0,98,60)
mc.setBlocks(-97,1,105,-104,1,98,47)
mc.setBlocks(-91,0,94,-98,0,87,8)

#------------SANDBOX AREA WITH STUFF AND THINGS------------#
sandbox= [-125,0,75,-85,0,-75,24]
mc.setBlocks(sandbox)
mc.setBlocks(-126,2,27,-126,12,-25,35,1)
def s (x,y,z):
    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z=z+1
    for i in range(2):
        y=y-1
        mc.setBlock(x,y,z,35,7)
    y=y-1
    z=z-1
    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        z=z-1
    for i in range(2):
        y=y-1
        mc.setBlock(x,y,z,35,7)
    y=y-1
    z=z+1
    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z=z+1    

s(-126,10,19)

def a (x,y,z):
    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        z=z+1
    for i in range(6):
        y=y-1
        mc.setBlock(x,y,z,35,7)
    z=z-4
    for i in range(6):
        mc.setBlock(x,y,z,35,7)
        y=y+1
    y=y-3
    for i in range(3):
        z=z+1
        mc.setBlock(x,y,z,35,7)
        
a(-126,10,13)

def n (x,y,z):
    for i in range(7):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    z=z-4
    y=y+1
    for i in range(7):
        mc.setBlock(x,y,z,35,7)
        y=y+1
    z=z+3
    y=y-2
    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    z=z-1
    y=y+1
    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    z=z-1
    y=y+1
    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y=y-1

n(-126,10,9)

def d (x,y,z):
    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z=z-1
    y=y-1
    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    z=z+1
    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z=z+1
    z=z-2
    y=y+1
    for i in range(5):
        mc.setBlock(x,y,z,35,7)
        y=y+1

d(-126,10,2)

def b (x,y,z):
    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z=z-1
    y=y-1
    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    y=y-1
    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    z=z+1
    for i in range(4):
        mc.setBlock(x,y,z,35,7)
        z=z+1
    z=z-2
    for i in range(5):
        y=y+1
        mc.setBlock(x,y,z,35,7)
    y=y-2
    z=z-1
    for i in range(2):
        mc.setBlock(x,y,z,35,7)
        z=z-1
        
b(-126,10,-5)

def o (x,y,z):
    for i in range(4):
        z=z-1
        mc.setBlock(x,y,z,35,7)
    for i in range(6):
        y=y-1
        mc.setBlock(x,y,z,35,7)
    for i in range(4):
        z=z+1
        mc.setBlock(x,y,z,35,7)
    for i in range(6):
        y=y+1
        mc.setBlock(x,y,z,35,7)


o(-126,10,-12)

def x (x,y,z):
    for i in range(2):
        for i in range(2):
            mc.setBlock(x,y,z,35,7)
            y=y-1
        z=z-1
        y=y+1
    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    z=z-1
    y=y+1
    for i in range(2):
        for i in range(2):
            mc.setBlock(x,y,z,35,7)
            y=y-1
        z=z-1
        y=y+1
    z=z+1
    y=y+6
    for i in range(2):
        for i in range(2):
            mc.setBlock(x,y,z,35,7)
            y=y-1
        z=z+1
        y=y+1
    for i in range(3):
        mc.setBlock(x,y,z,35,7)
        y=y-1
    z=z+1
    y=y+1
    for i in range(2):
        for i in range(2):
            mc.setBlock(x,y,z,35,7)
            y=y-1
        z=z+1
        y=y+1

x(-126,10,-19)

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
