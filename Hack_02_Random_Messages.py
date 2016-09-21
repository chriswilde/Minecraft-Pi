import minecraft.minecraft as minecraft
import time
import random
mc = minecraft.Minecraft.create()

while True:
    chat = ["Message 1", "Message 2", "Message 3"]
    thing = random.randint (0,2)
    mc.postToChat (chat[thing])
    time.sleep(3)
