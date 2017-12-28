import pyautogui
import Tkinter as tk
import temp

virtual_keyboard = tk.Tk()

# print pyautogui.confirm('This displays text and has an OK and Cancel button.')
# print pyautogui.alert('This displays some text with an OK button.')
# print pyautogui.prompt('This lets the user type in a string and press OK.')

def media_controls(action=None):

    if action == "move_forward":
        pyautogui.hotkey('ctrl', 'right')
    if action == "move_back":
        pyautogui.hotkey('ctrl', 'left')
    if action == "vol_up":
        pyautogui.hotkey('ctrl', 'up')
    if action == "vol_down":
        pyautogui.hotkey('ctrl', 'down')

def reading_controls(action=None):

    if action == "page_down":
        pyautogui.press('pgdn')
    if action == "page_up":
        pyautogui.press('pgup')
    if action == "zoom_in":
        pyautogui.hotkey('ctrl', 'add')
    if action == "zoom_out":
        pyautogui.hotkey('ctrl', 'subtract')

def presentation_controls(action=None):

    if action == "start":
        pyautogui.press('f5')
    if action == "stop":
        pyautogui.press('escape')
    if action == "move_forward":
        pyautogui.press('right')
    if action == "move_back":
        pyautogui.press('left')

def key_press(key):

    # print pyautogui.position()

    action = key.lower()

    spec_keys = ['ctrl', 'shift']

    if action not in spec_keys and temp.prev_key not in spec_keys :
        print action
        # pos = pyautogui.position()
        # pyautogui.click(x=1000, y=500)
        pyautogui.press(action)
        # pyautogui.moveTo(x=pos[0], y=pos[1])
    else:
        if temp.prev_key != "":
            print temp.prev_key, action
            # pos = pyautogui.position()
            # pyautogui.click(x=1000, y=500)
            pyautogui.hotkey(temp.prev_key, action)
            temp.prev_key = ""
            # pyautogui.moveTo(x=pos[0], y=pos[1])

        else:

            # To check the dimensions of each key
            # pyautogui.moveTo(x=65, y=163)
            # pyautogui.click()
            print temp.prev_key, action
            temp.prev_key = action

# keys = [
#     ';','`','!','@','#','"','&','*','(',')', '+', '-','_', u"\u2303", u"\u23CE",
#     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\\','7','8','9',u"\u232B",
#     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','{','}','4','5','6',u"\u21E7",
#     'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','?','/','1','2','3',u"\u2423",
# ]
#
# keys_mapping = [
#     ';','`','!','@','#','"','&','*','(',')', '+', '-','_', 'Ctrl', 'Enter',
#     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\\','7','8','9','BackSpace',
#     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','{','}','4','5','6', 'Shift',
#     'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','?','/','1','2','3', 'Space',
# ]
#
#
# virtual_keyboard.title("Keyboard")
# virtual_keyboard.resizable(0,0)
#
# row_num = 1
# col_num = 0
#
# for key in keys:
#
#     command = lambda x=key : key_press(x)
#
#     tk.Button(virtual_keyboard, text=key, command=command, width=2).grid(row=row_num, column=col_num);
#
#     col_num += 1
#
#     if col_num > 14:
#         row_num += 1
#         col_num = 0
#
# entry = tk.Entry(virtual_keyboard, width=60)
#
# virtual_keyboard.call('wm', 'attributes', '.', '-topmost', True)
#
# virtual_keyboard.mainloop()

# media_controls(action=None)
# reading_controls(action="page_down")
# presentation_control(action=None)
