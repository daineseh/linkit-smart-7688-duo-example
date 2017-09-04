#!/usr/bin/env python

import serial
import sys

s = None

def setup():
    global s
    # open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
    # the baudrate is set to 57600 and should be the same as the one
    # specified in the Arduino sketch uploaded to ATMega32U4.
    s = serial.Serial("/dev/ttyS0", 57600)


def is_invaild_value(str_value):
    if not str_value.isdigit():
        return True
    
    value = int(str_value)
    if value == 0:
        return False
    elif value == 1:
        return False
    elif ((value >= 700) and (value <= 2300)):
        return False
    else:
        return True


# Value Definition
# 0: Stop the servo
# 1: Start the servo
# 700~1400: CW
# 1400~2300: CCW
def main():
    if len(sys.argv) < 2 or is_invaild_value(sys.argv[1]):
        print("$relay.py [0 | 1 | 700~2300]")
        print("Value Definition:")
        print("="*18)
        print("  0: Stop the servo")
        print("  1: Start the servo")
        print("  700~1400: CW")
        print("  1400~2300: CCW")
        return
    s.write(sys.argv[1])


if __name__ == '__main__':
    setup()
    main()

