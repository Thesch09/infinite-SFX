from playsound4 import playsound
from rich import print
import math
import random
import time
import os

folders = os.listdir("./sfx") # Makes a list with the subfolders in the SFX folder
sounds = {} # This dictionary contains the sounds sepperated by which folder they're in
allSounds = [] # This list contains all of the sounds
folderSynonyms = {}

print(folders)
for folder in folders:
    soundsInFolder = [] # This list contains the sounds in the current folder so that it can be put together with the folder name
    sfxs = os.listdir(f"./sfx/{folder}")
    for sfx in sfxs:
        s_f_x = sfx.split(".")
        
        if s_f_x[-1] == "wav" or s_f_x[-1] == "mp3":
            print(sfx)
            print(s_f_x)
            soundsInFolder.append(sfx)
            allSounds.append(f"./sfx/{folder}/{sfx}")
        elif s_f_x[-1] == "txt":
            with open(f"./sfx/{folder}/{sfx}") as txt:
                folderSynonyms.update({folder:txt.readline().split("\n")[0]})
                print(folderSynonyms)
    print(f"{soundsInFolder}\n{allSounds}")
    sounds.update({folder:soundsInFolder})
print(sounds)
print()

# Chance of sounds
totSound = len(allSounds)
def showYourPercentage(): # Shows how likely it is a sound will play
    print(f"Total amount of sounds: {totSound}")
    print(f"Chance of a specific sound playing: {100/totSound}%")
    totPercent = 0
    for thing in sounds:
        chance = 100/totSound*len(sounds[thing])
        if thing in folderSynonyms:
            print(f"Chance of {folderSynonyms[thing]}: {chance}%")
        else:
            print(f"Chance of {thing}: {chance}%")
        totPercent += chance
    print(f"Total Percent: {round(totPercent)}%")
    print()

lastPlayedSounds = []
def showLPS(lps):
    print(f"Prevously played spounds:")
    for sound in lps:
        print(f"\t{sound}")

# On start set up time between sound
def setupSettings():
    global minDelay
    global maxDelay
    minDelay = 0
    maxDelay = 30
    message = ""
    for i in range(2):
        inputInvalid = True
        currentChange = 0
        while inputInvalid:
            os.system("cls") # Clears the console
            print(f"Welcome to VoidliiBoi's [bold]Infinite SFX[/bold]!")
            print()
            print(message)
            if i == 0:
                print("Please input the minimum delay between sounds")
                print("[bright_black]Minimum 0, default 0")
            else:
                print("Please input the maximum delay between sounds")
                print(f"[bright_black]Minimum {minDelay}, default 30")
            currentChange = input()
            if currentChange == "":
                if i == 0:
                    currentChange = 0
                else:
                    currentChange = 30
                message = "Set to default"
                break
            try:
                currentChange = int(currentChange)
                if currentChange < minDelay:
                    message = f"Input is less than {minDelay}, try again"
                else:
                    message = f"No errors found, yippee!"
                    inputInvalid = False
            except ValueError:
                message = "Input is not a whole number, or not a number at all"

        if i == 0:
            minDelay = currentChange
        else:
            maxDelay = currentChange
    print("Do you like the current delays?")
    print(f"[bright_black]Currently minimum {minDelay} and maximum {maxDelay} seconds between each sound")
    print("[bright_black]Type \"NO\" to restart")
    if input().lower() == "no":
        os.system("cls") # Clears the console
        setupSettings()

setupSettings()

while True:
    showYourPercentage()
    if len(lastPlayedSounds) > 0:
        showLPS(lastPlayedSounds)
    snoozy = random.randint(minDelay,maxDelay) # Delay between sounds
    shiny = ""
    if snoozy > 5 and random.randint(1,2) == 2:
        snoozy += random.randint(-5,7)
        shiny = "[blue]SUPER [/blue]"
    print(f"{shiny}Snoozing for {snoozy} seconds")
    print(f"[bright_black]Minimum {minDelay}, maximum {maxDelay}")
    time.sleep(snoozy)
    loudy = 50 # The loudness of the sound
    if random.randint(1,2) == 2:
        loudy += random.randint(-25,50)
        if loudy > 100:
            loudy = 100
    soundThatllBePlayed = random.randint(0, len(allSounds)-1)
    playedSoundSplit = allSounds[soundThatllBePlayed].split("/")
    print(f"Playing [violet]\"{playedSoundSplit[-1]}\"[/violet] with {loudy}% volume\n") # What's that soundèmon?
    playsound(allSounds[soundThatllBePlayed],loudy)

    fodlerName = playedSoundSplit[2]
    if playedSoundSplit[2] in folderSynonyms:
        fodlerName = folderSynonyms[playedSoundSplit[2]]
    lastPlayedSounds.append(f"[violet]\"{playedSoundSplit[-1]}\"[/violet] from {fodlerName}")

    if len(lastPlayedSounds) > 5:
        lastPlayedSounds.pop(0)
    os.system("cls") # Clears the console