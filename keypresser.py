from pyautogui import press
import time

k = input('Enter the key to press: ')
n = int(input('Enter the number of times to press it: '))
time.sleep(5)

for i in range(1, n+1):
    time.sleep(.100)
    press(k)


