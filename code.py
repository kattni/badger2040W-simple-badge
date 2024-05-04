import time
import board
import displayio
import keypad
import terminalio
import vectorio
from adafruit_display_text import bitmap_label as label

# *** BADGE CONFIGURATION ***
# Update the following to the desired name and pronouns.
NAME_STRING = "Kattni"
PRONOUN_STRING = "SHE/HER"

# If you want to change the rest of the text, you can update the following.
HELLO_STRING = "HELLO MY NAME IS"

# If your name doesn't fit, consider decreasing NAME_SCALE to 2.
# This must be a whole number, 1 or greater. Note that 1 is quite small.
NAME_SCALE = 3

# *** BADGE SETUP ***
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Display setup
display = board.DISPLAY
display_group = displayio.Group()

# Badge rectangle
background_p = displayio.Palette(1)
background_p[0] = WHITE
rectangle_white = vectorio.Rectangle(pixel_shader=background_p, width=display.width + 1,
                                     height=int(display.height * 0.45), x=0, y=int(display.height / 3))
display_group.append(rectangle_white)

# Badge top line of text
hello_text = label.Label(terminalio.FONT, text=HELLO_STRING, anchor_point=(0.5, 0.5),
                         anchored_position=(display.width / 2, 20), color=WHITE)
display_group.append(hello_text)
hello_text.scale = 2

# Badge middle line of text
name_text = label.Label(terminalio.FONT, text=NAME_STRING, anchor_point=(0.5, 0.5),
                        anchored_position=(display.width / 2, 70), color=BLACK)
display_group.append(name_text)
name_text.scale = NAME_SCALE

# Badge bottom line of text
pronoun_text = label.Label(terminalio.FONT, text=PRONOUN_STRING, anchor_point=(0.5, 0.5),
                           anchored_position=(display.width / 2, 112), color=WHITE)
display_group.append(pronoun_text)
pronoun_text.scale = 2

display.root_group = display_group

try:
    display.refresh()
except RuntimeError:
    time.sleep(3)
    display.refresh()

while True:
    pass
