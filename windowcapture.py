import numpy as np
import win32gui, win32ui, win32con
import time
import pyautogui
import pygetwindow as gw
from PIL import ImageGrab

class WindowCapture:

    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    # constructor
    def __init__(self, window_name):
        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y


    
    def get_screenshot(self):
        try:
            # get the window
            window = gw.getWindowsWithTitle("World of Metin2")[0]  

            # if the window is minimized
            if window.isMinimized:  
                window.restore()  # restore it

            # get the screenshot
            screenshot = pyautogui.screenshot()

            # Crop the screenshot to the window area (if necessary)
            # (you can comment these lines out to capture the whole screen)
            #screenshot = screenshot.crop((window.left, window.top, window.right, window.bottom))

            # convert the screenshot into a numpy array
            img = np.array(screenshot)

        except Exception as e:
            print(f"Screenshot failed with error: {e}")
            print("Retrying in 1 second...")
            time.sleep(1)  # Adjust delay as needed
            return self.get_screenshot()  # Recursive retry

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        img = img[...,:3]

        # make image C_CONTIGUOUS to avoid errors
        img = np.ascontiguousarray(img)

        return img



    # find the name of the window you're interested in.
    # once you have it, update window_capture()
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    def list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)