import pyautogui_template
import pyautogui

def get_key(column, row):
    print column, row
    key = keys[15 * row + column]

    pyautogui_template.key_press(key)

keys = [
    ';','`','!','@','#','"','&','*','(',')', '+', '-','_', 'Ctrl', 'Enter',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\\','7','8','9','BackSpace',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','{','}','4','5','6','Shift',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','?','/','1','2','3','Space',
]

while True:
    pos = pyautogui.position()
    print pos

    column = (pos[0] - 65) / 84
    row = (pos[1] - 52) / 28

    if column > 14 or row > 3:
        pass
    else:
        get_key(column, row)