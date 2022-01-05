import time
import random
import winsound
import pyautogui

def main():
    pyautogui.hotkey('win', 'shift', 'ctrl', 'b')
    while(1):
        startTime = time.time()
        time.sleep(random.randint(200, 270))
        beep()        
        pyautogui.hotkey('win', 'shift', 'ctrl', 'b')

def beep():
        winsound.Beep(440, 150)
        time.sleep(0.15)
        winsound.Beep(600, 150)
        time.sleep(0.15)
        winsound.Beep(850, 150)
        time.sleep(0.15)
        winsound.Beep(440, 150)
        time.sleep(0.15)
        winsound.Beep(600, 150)

if __name__ == "__main__":
    main()