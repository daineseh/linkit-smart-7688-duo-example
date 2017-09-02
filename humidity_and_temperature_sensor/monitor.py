#!/usr/bin/env python

import serial

s = None

def setup():
    global s
    s = serial.Serial("/dev/ttyS0", 57600)

def loop():
    print s.readline(),

if __name__ == '__main__':
    setup()
    while True:
        loop()

