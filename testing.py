import win32gui, win32api, win32con
import time

hwnd = win32gui.FindWindow(None, 'BlueStacks App Player')
hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
hwndChild2 = win32gui.GetWindow(hwndChild, win32con.GW_CHILD)

s = "Clash of Clans"

def PressKeys(chars):
    for i in chars:
        win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, ord(i.upper()), 0)

#PressKeys(s)











import keyboard
import pyautogui
import pyperclip

def get_mouse_coords_and_copy():
    x, y = pyautogui.position()
    coords = f"pyautogui.click({x}, {y})"
    pyperclip.copy(coords)
    print(f"Copied coordinates to clipboard: {coords}")

keyboard.add_hotkey('o', get_mouse_coords_and_copy)

# Keep the program running
keyboard.wait()

pyautogui.displayMousePosition()