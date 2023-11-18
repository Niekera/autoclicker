import keyboard
import mouse
import time


clickstatus=False

def switch():
    global clickstatus
    if (clickstatus==False):
        print('clicker is on')
        clickstatus=True

    else:
        print('clicker is off')
        clickstatus=False

keyboard.add_hotkey('F6', switch)

while True:
    if clickstatus:
        mouse.double_click(button='left')
        time.sleep(0.01)


