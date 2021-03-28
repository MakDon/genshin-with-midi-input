import pygame.midi

import time
import win32api
import win32con
import win32gui

action_press = 144
action_unpress = 128
letter = {'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74, 'k': 75, 'l': 76,
          'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88,
          'y': 89, 'z': 90}
mapping = {'48': 'z', '50': 'x', '52': 'c', '53': 'v', '55': 'b', '57': 'n', '59': 'm', '60': 'a', '62': 's', '64': 'd',
           '65': 'f', '67': 'g', '69': 'h', '71': 'j', '72': 'q', '74': 'w', '76': 'e', '77': 'r', '79': 't', '81': 'y',
           '83': 'u'}


def press(note):  # 48 83
    if note in mapping.keys():
        win32api.keybd_event(letter[mapping[note]], 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    return


def unpress(note):  # 48 83
    if note in mapping.keys():
        win32api.keybd_event(letter[mapping[note]], 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    return


def pop_window(name):
    handle = win32gui.FindWindow(0, name)
    if handle == 0:
        return False
    else:
        win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND,
                             win32con.SC_RESTORE, 0)
        win32gui.SetForegroundWindow(handle)
        while win32gui.IsIconic(handle):
            continue
        return True


if __name__ == "__main__":
    pygame.midi.init()
    input_id = pygame.midi.get_default_input_id()
    input = pygame.midi.Input(input_id)
    pop_window("原神")
    while True:
        if input.poll():
            input_key = input.read(1)[0]
            if input_key[0][0] == action_press:
                press(str(input_key[0][1]))
            elif input_key[0][0] == action_unpress:
                unpress(str(input_key[0][1]))
        else:
            time.sleep(0.0001)
