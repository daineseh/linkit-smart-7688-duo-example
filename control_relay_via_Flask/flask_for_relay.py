#!/usr/bin/env python

# Usage: Type the url in a browser that turn on/off the relay.
#        http://<IP Address>/api/switchRelay?status=[0|1]

from flask import Flask, request, abort
import json
import os
import serial

s = None
#f = os.popen('ifconfig br-lan | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # AP model
f = os.popen('ifconfig apcli0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # Station model  
inet_addr = f.read()  
app = Flask(__name__)
enum_values = ['0', '1']

def setup():
    global s
    # open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
    # the baudrate is set to 57600 and should be the same as the one
    # specified in the Arduino sketch uploaded to ATMega32U4.
    s = serial.Serial("/dev/ttyS0", 57600)

@app.route("/api/switchRelay")
def relay():
    status = request.args.get("status").encode("ascii")
    if not status:
        abort(404)
    if status not in enum_values:
        abort(404)
    s.write(status)
    return json.dumps({"status": 200, "message": "Completed the switchRelay action."})

@app.route('/')
def main():
    return json.dumps({"status":200, "message": "OK"})

if __name__ == '__main__':
    setup()
    app.debug = True
    app.run(host = inet_addr, port=5000)

