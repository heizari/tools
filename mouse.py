import pyautogui
import datetime
import time
position = pyautogui.position()
start_time = datetime.datetime.now()
last_move = start_time.hour
dx = 1
print(position)
print(last_move)

# while True:
#     time.sleep(10)
#     dx = -dx
#     position = pyautogui.position()
#     pyautogui.moveTo(position.x + dx, position.y,duration=0)
#     print('move')
