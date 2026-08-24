from playsound4 import playsound
from rich import print
import math
import random
import time
import os

folders = os.listdir("./sfx")
sounds = {}
allSounds = []
print(folders)
for folder in folders:
    soundsInFolder = []
    sfxs = os.listdir(f"./sfx/{folder}")
    for sfx in sfxs:
        print(sfx)
        soundsInFolder.append(sfx)
        allSounds.append(f"./sfx/{folder}/{sfx}")
        print(f"{soundsInFolder}\n{allSounds}")
    sounds.update({folder:soundsInFolder})
print(sounds)



while True:
    snoozy = random.randint(3,10)
    print(f"Snoozing for {snoozy} seconds\n")
    time.sleep(snoozy)
    soundThatllBePlayed = random.randint(0, len(allSounds)-1)
    print(f"Playing [violet]\"{allSounds[soundThatllBePlayed].split("/")[-1]}\"")
    playsound(allSounds[soundThatllBePlayed])
    