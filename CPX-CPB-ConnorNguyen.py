# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel
import random

NUM_PIXELS = 4

pixels = neopixel.NeoPixel(board.NEOPIXEL, NUM_PIXELS, brightness=0.2, auto_write=False)

def spin_colors(duration):
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(NUM_PIXELS)]
    
    for _ in range(duration):
        for i in range(NUM_PIXELS):
            pixels[i] = colors[i]

        # Shift the colors
        colors.insert(0, colors.pop())

        pixels.show()
        time.sleep(0.5)

# Main loop
while True:
    spin_colors(5)  # Spin colors in a circle for 5 seconds

