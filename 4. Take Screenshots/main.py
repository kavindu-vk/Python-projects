import pyautogui
from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox

def take_screenshot():
    # Minimize the window
    root.iconify()
    time.sleep(0.5)
    
    # Get current time for unique filename
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot
    screenshot_filename = f"screenshot_{current_time}.png"
    screenshot.save(screenshot_filename)

    # Show confirmation message
    messagebox.showinfo("Screenshot Saved", f"Screenshot saved as {screenshot_filename}")

    # Restore the window
    root.deiconify()

# Set up the main application window
root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("270x100")
root.resizable(False, False)



# Set up the button to take a screenshot
button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
button.pack(pady=20)

# Run the application
root.mainloop()