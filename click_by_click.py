import pyautogui
import time
import keyboard

def click_at_cursor(interval=0.00001):
    """
    Clicks at the current cursor position with a specified interval between clicks.

    Args:
    interval (float): Time interval in seconds between clicks.
    """
    paused = False

    def toggle_pause():
        nonlocal paused
        paused = not paused
        print("Paused" if paused else "Resumed")

    def exit_program():
        print("Exiting...")
        quit()

    keyboard.add_hotkey('esc', toggle_pause)
    keyboard.add_hotkey('f10', exit_program)

    try:
        while True:
            if not paused:
                x, y = pyautogui.position()  # Get the current cursor position
                pyautogui.click(x, y)  # Click at that position
                time.sleep(interval)  # Wait for the specified interval
    except KeyboardInterrupt:
        print("Program has been stopped.")

if __name__ == "__main__":
    interval = float(input("Enter the interval between clicks (seconds): "))
    click_at_cursor(interval)
