import cv2 as cv
import sys
from time import time, sleep
from windowcapture import WindowCapture
from Detector import Detector
import subprocess
from Bot import AppBot
"""
    Name:       Mou AI functionality
    Details:    This program will provide the Open CV functionality.
                This program will provide all the application window capture
                that will help the further functionality for object detection
    Author:     Raphael Di Ezmo
"""


# ------------------- ONLY  USED FOR DEBUGGING ----------------------
# ------------------ WILL BE CHANGED AFTERWARDS ---------------------
# This app_name will be only for Testing purposes only this could changed
# and will be dynamic for user to pick which application should be used for the
# program
# print(sys.argv[1])
app_name = 'Supreme Destiny            '
# Sample image
targeted_object = Detector('sample_obj.JPG')

# ----------------- END FOR DEBUGGING VARIABLES ----------------------
# --------------------------------------------------------------------
# Initializing the WindowCapture class
wincap = WindowCapture(app_name)
# Initializing the bot
bot = AppBot((wincap.offset_x, wincap.offset_y), (wincap.width, wincap.height))
# Initializing the Detector class
detector = Detector

# Starting thread of the bot
#bot.start()

'''
# Function that will get the window's application capturing the image content of a window
# this will produce the clone image and actions that has been done in the targeted
# application
# Parameters:
#       app_name this contains the window title of an application'''
def main(app_name):
    # time variable that will update the time inside the while loop
    time_updtr = time()

    # Runs the infinite loop until the user wants to end it
    while(True):

        # Updates the image inside the window capture
        screen_detector = wincap.capture_window()
        # *** For debugging purpose ***
        cv.imshow('Window capture', screen_detector)

        # displays the window capture and detects the targeted object
        detected_obj = targeted_object.locate(screen_detector, 0.8)
        # When the detector didn't get to detect any of the targeted objects
        bot.get_target_positions(detected_obj)

        # ---------------------- FOR DEBUGGING PURPOSES -----------------------
        print('Frames per second {}'.format(int(1 / (time() - time_updtr))))
        # # updates the time
        time_updtr = time()

        # Bot actions
        # Running the function in thread, separating from the main thread

        # press '#' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('#'):
            # Shuts down all of the opencv's created object
            cv.destroyAllWindows()
            bot.stop()
            break

main(app_name)

