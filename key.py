import pyautogui
import datetime
import time
click_mode = input('mode:(1:before working, 2:working)')
target_position = pyautogui.position()
print('get position')
loop = True
if click_mode == '1':
    target_time = 50
elif click_mode == '2':
    target_time =19
else:
    loop = False
    print('invalid mode')
while (loop):
    now = datetime.datetime.now()
    if click_mode == '1':
        if target_time <= now.minute:
            pyautogui.click(target_position)
            click_mode = 2
            target_time = 19
    elif click_mode == '2':
        if target_time == now.hour:
            pyautogui.click(target_position)
            break
    time.sleep(240)
    pyautogui.click(pyautogui.position())

#     pyautogui.typewrite("awake!")