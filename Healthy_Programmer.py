# Healthy Programmer
# Pygame module to play audio
# Time module to display time
# Date time module to display date with time
import time
from pygame import mixer
import datetime

# These are initial time variable for water , eyes exercise and physical exercise.
init_water = time.time()
init_eyes = time.time()
init_physical = time.time()

d = datetime.datetime.now()
c = time.asctime(time.localtime())

name = input('Enter your name...\n')
print(f'Welcome to office {name.upper()}.')


# Wishes to employee.
if 6 > d.hour < 12:
    print(f'Good Morning {name.upper()}')

elif 12 > d.hour < 4:
    print(f'Good Afternoon {name.upper()}')

else:
    print(f"Good Evening {name.upper()}")
print(f'Your reporting time is [{c}]')


# musiconloop() function to play audio.
def musiconloop(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


# water() funtion to play water music.
# Water - water.mp3 (3.5 litres) - drank -  Every 40 min
def water():
    print('This is water reminder...Have water..Enter \'drank\' to stop music OR Enter \'q\' to quit')
    musiconloop('water.mp3')
    while True:
        rem = input('')
        if rem == 'drank':
            mixer.music.stop()
            break
        elif rem == 'q':
            quit()


# eyes() function to play eyes exercise music.
# Eyes - eyes.mp3 - every 30 min - doneeyes - Every 30 min
def eyes():

    print('This is eyes exercise reminder...Do eye exercise...Enter \'doneeyes\' to stop music OR Enter \'q\' to quit.')
    musiconloop('eyes.mp3')
    while True:
        rem = input()
        if rem == 'doneeyes':
            mixer.music.stop()
            break
        elif rem == 'q':
            quit()


# physicalex() function to play physical exercise music.
# Physical exercise - physical.mp3 - every 50 min - donephy - log
def physicalex():
    print('This is physical exercise reminder...Do some stretching...Enter \'donephy\' to stop music OR Enter \'q\' to quit.')
    musiconloop('physical.mp3')
    while True:
        rem = input()
        if rem == 'donephy':
            mixer.music.stop()
            break
        elif rem == 'q':
            quit()


# loop for execute above three function and write into text file.
while True:

    now = time.time()

    if now - init_water > 40*60:
        water()
        init_water = time.time()
        with open('water.txt', 'a') as w:
            w.write(f'Drank water at : {datetime.datetime.now()} \n')

    elif now - init_eyes > 30*60:
        eyes()
        init_eyes = time.time()
        with open('eyes.txt', 'a') as e:
            e.write(f'Eye relaxed at : {datetime.datetime.now()} \n')

    elif now - init_physical > 50*60:
        physicalex()
        init_physical = time.time()
        with open('physicalex.txt', 'a') as p:
            p.write(f'Physical exercise done at : {datetime.datetime.now()} \n')
