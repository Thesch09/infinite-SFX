from playsound4 import playsound
from rich import print
import math
import random
import time
import os

folders = os.listdir("sfx")
sounds = {}
allSounds = []
print(folders)
for folder in folders:
    soundsInFolder = []
    sfxs = os.listdir(f"sfx/{folder}")
    for sfx in sfxs:
        print(sfx)
        soundsInFolder.append(sfx)
        allSounds.append(f"sfx/{folder}/{sfx}")
        print(f"{soundsInFolder}\n{allSounds}")
    sounds.update({folder:soundsInFolder})
print(sounds)



while True:
    time.sleep(random.randint(1,5))
    soundThatllBePlayed = random.randint(0, len(allSounds)-1)
    playsound(allSounds[soundThatllBePlayed])
    print(allSounds[soundThatllBePlayed])
    