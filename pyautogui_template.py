import pyautogui
import Tkinter as tk
import temp

virtual_keyboard = tk.Tk()

# print pyautogui.confirm('This displays text and has an OK and Cancel button.')
# print pyautogui.alert('This displays some text with an OK button.')
# print pyautogui.prompt('This lets the user type in a string and press OK.')

def media_controls(action=None):

    pyautogui.click(x=100, y=200)

    if action == "move_forward":
        pyautogui.hotkey('ctrl', 'right')
    if action == "move_back":
        pyautogui.hotkey('ctrl', 'left')
    if action == "vol_up":
        pyautogui.hotkey('ctrl', 'up')
    if action == "vol_down":
        pyautogui.hotkey('ctrl', 'down')

    pyautogui.click(x=1000, y=500)

def reading_controls(action=None):

    pyautogui.click(x=100, y=200)

    if action == "page_down":
        pyautogui.press('pgdn')
    if action == "page_up":
        pyautogui.press('pgup')
    if action == "zoom_in":
        pyautogui.hotkey('ctrl', 'add')
    if action == "zoom_out":
        pyautogui.hotkey('ctrl', 'subtract')

    pyautogui.click(x=1000, y=500)


def presentation_control(action=None):

    pyautogui.click(x=100, y=200)

    if action == "start":
        pyautogui.press('f5')
    if action == "stop":
        pyautogui.press('escape')
    if action == "move_forward":
        pyautogui.press('right')
    if action == "move_backward":
        pyautogui.press('left')

    pyautogui.click(x=1000, y=500)

def key_press(key):

    print temp.prev_key

    action = key.lower()

    spec_keys = ['ctrl', 'shift']

    if action not in spec_keys and temp.prev_key not in spec_keys :
        pos = pyautogui.position()
        pyautogui.click(x=1000, y=500)
        pyautogui.press(action)
        pyautogui.moveTo(x=pos[0], y=pos[1])
    else:
        if temp.prev_key != "":
            print temp.prev_key, action
            pos = pyautogui.position()
            pyautogui.click(x=1000, y=500)
            pyautogui.hotkey(temp.prev_key, action)
            temp.prev_key = ""
            pyautogui.moveTo(x=pos[0], y=pos[1])

        else:
            print temp.prev_key, action
            temp.prev_key = action

keys = [
    ';','`','!','@','#','"','&','*','(',')', '+', '-','_', 'Ctrl', 'Enter',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\\','7','8','9','BackSpace',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','{','}','4','5','6','Shift',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','?','/','1','2','3','Space',
]


virtual_keyboard.title("Keyboard")
virtual_keyboard.resizable(0,0)

row_num = 1
col_num = 0

for key in keys:

    command = lambda x=key : key_press(x)

    tk.Button(virtual_keyboard, text=key, width=7, command=command).grid(row=row_num, column=col_num)

    col_num += 1

    if col_num > 14:
        row_num += 1
        col_num = 0


entry = tk.Entry(virtual_keyboard, width=180)
virtual_keyboard.mainloop()

# media_controls(action=None)
# reading_controls(action=None)
# presentation_control(action=None)
