from playsound4 import playsound
from rich import print
import math
import random
import time
import os

folders = os.listdir("./sfx") # Makes a list with the subfolders in the SFX folder
sounds = {} # This dictionary contains the sounds sepperated by which folder they're in
allSounds = [] # This list contains all of the sounds
print(folders)
for folder in folders:
    soundsInFolder = [] # This list contains the sounds in the current folder so that it can be put together with the folder name
    sfxs = os.listdir(f"./sfx/{folder}")
    for sfx in sfxs:
        print(sfx)
        soundsInFolder.append(sfx)
        allSounds.append(f"./sfx/{folder}/{sfx}")
        print(f"{soundsInFolder}\n{allSounds}")
    if folder == "Flowery": # Make Flowery Yellow
        sounds.update({f"[yellow]{folder}[/yellow]":soundsInFolder})
    else:
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
        print(f"Chance of {thing}: {chance}%")
        totPercent += chance
    print(f"Total Percent: {round(totPercent)}%")
    print()

lastPlayedSounds = []
def showLPS(lps):
    print(f"Prevously played spounds:")
    for sound in lps:
        print(f"\t{sound}")

while True:
    showYourPercentage()
    if len(lastPlayedSounds) > 0:
        showLPS(lastPlayedSounds)
    snoozy = random.randint(0,30) # Delay between sounds
    shiny = ""
    if snoozy > 5 and random.randint(1,2) == 2:
        snoozy += random.randint(-5,7)
        shiny = "[blue]SUPER [/blue]"
    print(f"{shiny}Snoozing for {snoozy} seconds")
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

    if playedSoundSplit[2] == "Flowery": # Make Flowery Yellow
        lastPlayedSounds.append(f"[violet]\"{playedSoundSplit[-1]}\"[/violet] from [yellow]Flowery[/yellow]")
    else:
        lastPlayedSounds.append(f"[violet]\"{playedSoundSplit[-1]}\"[/violet] from {playedSoundSplit[2]}")
    if len(lastPlayedSounds) > 5:
        lastPlayedSounds.pop(0)
    os.system("cls") # Clears the console