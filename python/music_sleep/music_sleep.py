from pynput.keyboard import Key, Controller
from time import sleep
from os import system

kb = Controller()

def Sleep(minutes):
    seconds = minutes * 60
    for s in range(seconds):
        sleep(1)
        system("cls")
        print("Time left: " + seconds - s)
    print("Pausing...")
    pause()

def pause():
    sleep(5)
    kb.tap(Key.space)
    sleep(0.5)

    kb.press(Key.cmd)
    kb.tap(Key.down)
    sleep(0.2)
    kb.tap(Key.down)
    kb.release(Key.cmd)

Sleep(input("time to sleep???? :"))