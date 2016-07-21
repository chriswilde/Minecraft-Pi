import minecraft.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

introAreaListItem = 0
area1ListItem = 0
area2ListItem = 0
area3ListItem = 0
area4ListItem = 0
area5ListItem = 0
area6ListItem = 0
area7ListItem = 0
area8ListItem = 0
area9ListItem = 0
area10ListItem = 0
sandboxListItem = 0
castleListItem = 0

while True:
        pos = mc.player.getTilePos()
        if -125 <= pos.x <= -85 and -125 <= pos.z <= -85:
                introAreaList = ["HELLO WORLD!",
                                 "WE ARE BUILD-IT.",
                                 "Welcome to our Minecraft Module.",
                                 "This world has been created to help you learn how to code.",
                                 "It is divided into areas.",
                                 "Every area has been designed to help you develop different skills.",
                                 "Take a walk around the world and find out what's going on.","Thanks, and Enjoy :-)"]
                mc.postToChat(introAreaList[introAreaListItem])
                time.sleep(4)
                if introAreaListItem < 7:
                        introAreaListItem = introAreaListItem+1
                else:
                        introAreaListItem = 0
                        time.sleep(6)
                continue
        
        elif -75 <= pos.x <= -35 and -125 <= pos.z <= -85:
                area1List = ["Welcome to Area 1.",
                             "Your coding journey will begin here.",
                             "In this area you will learn how to hack Minecraft chat pane, just like we are doing now!",
                             "You will:",
                             "Hack the chat pane,",
                             "Make it display random messages,",
                             "And",
                             "Interact with a user!",
                             "That is all"]
                mc.postToChat(area1List[area1ListItem])
                time.sleep(3)
                if area1ListItem < 8:
                        area1ListItem = area1ListItem+1
                else:
                        area1ListItem = 0
                        time.sleep(6)
                continue
        
        elif -20 <= pos.x <= 20 and -125 <= pos.z <= -85:
                area2List = ["This is Area 2.",
                             "It looks like a massive target.",
                             "Because it is a massive target!!",
                             "In this area you will learn how to teleport.",
                             "You will learn how 3D environments work,",
                             "And work with variables to send Steve to coordinates on the",
                             "X",
                             "Y",
                             "& Z Axes!",
                             "NEXT!"]
                mc.postToChat(area2List[area2ListItem])
                time.sleep(3)
                if area2ListItem < 9:
                        area2ListItem = area2ListItem+1
                else:
                        area2ListItem = 0
                        time.sleep(6)
                continue

        elif 35 <= pos.x <= 75 and -125 <= pos.z <= -85:
                area3List = ["In Area 3 you will learn how to set blocks using code.",
                             "You will craft without having to craft",
                             "You will start to consider how this code works.",
                             "You will create a simple hide and seek game in this area.",
                             "You will also create a GLITCH.",
                             "Finally You will create a small stack too.",
                             "You may leave now ;-)",
                             ]
                mc.postToChat(area3List[area3ListItem])
                time.sleep(3)
                if area3ListItem < 6:
                        area3ListItem = area3ListItem+1
                else:
                        area3ListItem = 0
                        time.sleep(6)
                continue

        elif 85 <= pos.x <= 125 and -125 <= pos.z <= -85:
                area4List = ["Welcome to Area 4.",
                             "Crafting using code can become repetitive.",
                             "In this area you will learn all about the WHILE loop.",
                             "We will use this tool to create columns.",
                             "And then create some nice patterns.",
                             "This tool can also be used to build rows and even steps! ",
                             "Thanks for listening.",]
                mc.postToChat(area4List[area4ListItem])
                time.sleep(3)
                if area4ListItem < 6:
                        area4ListItem = area4ListItem+1
                else:
                        area4ListItem = 0
                        time.sleep(6)
                continue

        elif 85 <= pos.x <= 125 and -75 <= pos.z <= 20:
                area5List = ["My Friend. THIS is area 5!",
                             "Here you will learn about the FOR loop.",
                             "FOR loops will give you a little more control my friend.",
                             "My friend, you will also learn the art of nesting.",
                             "Placing loops inside of loops will allow you to:",
                             "Become a virtual window fitter,",
                             "Create walls with code,",
                             "and",
                             "Create a range of other shapes too.",
                             "Thank you my friend <3"]
                mc.postToChat(area5List[area5ListItem])
                time.sleep(3)
                if area5ListItem < 9:
                        area5ListItem = area5ListItem+1
                else:
                        area5ListItem = 0
                        time.sleep(6)
                continue

        elif 85 <= pos.x <= 125 and 35 <= pos.z <= 75:
                area6List = ["In Area 6 things get a little interesting.",
                             "Rather than changing the world to your will,",
                             "You will program Steve to react to the environment,",
                             "And also,",
                             "Get the environment to react to Steve.",
                             "We will code the Flower Poop",
                             "Turn Steve into Elsa from Frozen,",
                             "And even",
                             "Change blocks based on Steve's position.",
                             "You will like it."]
                mc.postToChat(area6List[area6ListItem])
                time.sleep(3)
                if area6ListItem < 9:
                        area6ListItem = area6ListItem+1
                else:
                        area6ListItem = 0
                        time.sleep(6)
                continue

        elif 35 <= pos.x <= 125 and 85 <= pos.z <= 125:
                area7List = ["Welcome to Area 7.",
                             "Imagine crafting a wall where you stood in the blink of an eye.",
                             "You will learn how to do this here.",
                             "You will learn to break things down into smaller parts.",
                             "A skill called DECOMPOSITION.",
                             "And also save chunks of code as PROCEDURES."]
                mc.postToChat(area7List[area7ListItem])
                time.sleep(3)
                if area7ListItem < 5:
                        area7ListItem = area7ListItem+1
                else:
                        area7ListItem = 0
                        time.sleep(6)
                continue

        elif -20 <= pos.x <= 20 and 85 <= pos.z <= 125:
                area8List = ["Area 8 is a little different.",
                             "Here you will learn how to code cuboids.",
                             "And also how to destroy areas with air...",
                             "...And TNT!",]
                mc.postToChat(area8List[area8ListItem])
                time.sleep(3)
                if area8ListItem < 3:
                        area8ListItem = area8ListItem+1
                else:
                        area8ListItem = 0
                        time.sleep(6)
                continue
        
        elif -75 <= pos.x <= -35 and 85 <= pos.z <= 125:
                area9List = ["This is Area 9.",
                             "Here you will learn how to create more complex structures.",
                             "you will combine lists, loops and block types to craft:",
                             "A prison,",
                             "A hollow glass cube",
                             "A tunnel,",
                             "A tower,",
                             "A pyramid,",
                             "And a sphere."]
                mc.postToChat(area9List[area9ListItem])
                time.sleep(3)
                if area9ListItem < 8:
                        area9ListItem = area9ListItem+1
                else:
                        area9ListItem = 0
                        time.sleep(6)
                continue

        elif -125 <= pos.x <= -85 and 85 <= pos.z <= 125:
                area10List = ["Area 10 is our final learning area.",
                              "Here you will make Steve affect the real world.",
                              "You will build a variety of circuits,",
                              "And Steve's actions in the Minecraft world will power them.",
                              "You will turn on lights,",
                              "Develop a security system",
                              "and play a piano!"]
                mc.postToChat(area10List[area10ListItem])
                time.sleep(3)
                if area10ListItem < 6:
                        area10ListItem = area10ListItem+1
                else:
                        area10ListItem = 0
                        time.sleep(6)
                continue

        elif -125 <= pos.x <= -85 and -75 <= pos.z <= 75:
                sandboxList = ["This is a Sandbox area.",
                               "It is empty",
                               "You will fill it with test structures.",
                               "That is why it is empty.",]
                mc.postToChat(sandboxList[sandboxListItem])
                time.sleep(3)
                if sandboxListItem < 3:
                        sandboxListItem = sandboxListItem+1
                else:
                        sandboxListItem = 0
                        time.sleep(6)
                continue

        elif -20 <= pos.x <= 20 and -20 <= pos.z <= 20:
                castleList = ["This is a castle.",
                              "It was crafted using code.",
                              "All of the skills used to craft it are described in our tutorials.",
                              "Our hope is that you can create things even more awesome than this.",
                              "You are Build-IT",
                              "Be AWESOME my friend :-)"]
                mc.postToChat(castleList[castleListItem])
                time.sleep(3)
                if castleListItem < 5:
                        castleListItem = castleListItem+1
                else:
                        castleListItem = 0
                        time.sleep(6)
                continue
        else:
                time.sleep(5)
                continue
