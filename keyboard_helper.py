import constants
import numpy as np

def get_key(pos):
    # print column, row

    pos = np.array(pos) + np.array(constants.window_offset)

    column = (pos[0] - 65) / 42
    row = (pos[1] - 420) / 28

    if column > 14 or row > 3 or column < 0 or row < 0:
        pass
    else:
        key = keys_mapping[15 * row + column]
        return key

    # pyautogui_template.key_press(key)

keys_mapping = [
    ';','`','!','@','#','"','&','*','(',')', '+', '-','_', 'Ctrl', 'Enter',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\\','7','8','9','BackSpace',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','{','}','4','5','6', 'Shift',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','?','/','1','2','3', 'Space',
]
