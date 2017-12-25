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

# media_controls(action=None)
# reading_controls(action=None)
# presentation_control(action=None)
