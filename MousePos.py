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