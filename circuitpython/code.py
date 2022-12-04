import time
import board
import keypad
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#KEY    #Mapping    Row     Column
#1       4          GP7     GP6
#2       3          GP7     GP5
#3       2          GP7     GP4
#4       1          GP7     GP3
#5       0          GP7     GP2
#6       10
#7
#8
#9
#0
#Q       9          GP8     GP6
#W       8          GP8     GP5
#E       7          GP8     GP4
#R       6          GP8     GP3
#T       5          GP8     GP2

kbd = Keyboard(usb_hid.devices)

mappings = {
    4: Keycode.ONE,
    3: Keycode.TWO,
    2: Keycode.THREE,
    1: Keycode.FOUR,
    0: Keycode.FIVE,
    10: Keycode.SIX,
    11: Keycode.SEVEN,
    12: Keycode.EIGHT,
    13: Keycode.NINE,
    14: Keycode.ZERO,
    20: Keycode.Y,
    21: Keycode.U,
    22: Keycode.I,
    23: Keycode.O,
    24: Keycode.P,
    9: Keycode.Q,
    8: Keycode.W,
    7: Keycode.E,
    6: Keycode.R,
    5: Keycode.T,
    19: Keycode.A,
    18: Keycode.S,
    17: Keycode.D,
    16: Keycode.F,
    15: Keycode.G,
    30: Keycode.H,
    31: Keycode.J,
    32: Keycode.K,
    33: Keycode.L,
    34: Keycode.ENTER,
    29: Keycode.SHIFT,
    28: Keycode.Z,
    27: Keycode.X,
    26: Keycode.C,
    25: Keycode.V,
    35: Keycode.B,
    36: Keycode.N,
    37: Keycode.M,
    38: Keycode.PERIOD,
    39: Keycode.SPACE
}

km = keypad.KeyMatrix(
    row_pins=(board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14), #rows
    column_pins=(board.GP2, board.GP3, board.GP4, board.GP5, board.GP6) #cols
)

switch = DigitalInOut(board.GP16)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
print("starting")
while True:
    while switch.value: #Disable if GP16 and GND are connected
        event = km.events.get()
        if event:
            #help(event)
            print(event)
            print(event.key_number)
            print(mappings.get(event.key_number))
            key = mappings.get(event.key_number)
            if event.pressed:
                kbd.press(key)
            else:
                kbd.release(key)
    time.sleep(0.5)

