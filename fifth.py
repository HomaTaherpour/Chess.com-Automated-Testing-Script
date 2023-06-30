import pyautogui, sys
import time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        time.sleep(2)
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(2)
except KeyboardInterrupt:
    print('\n')