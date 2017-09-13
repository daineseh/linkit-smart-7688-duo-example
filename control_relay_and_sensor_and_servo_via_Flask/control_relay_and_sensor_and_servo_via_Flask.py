#!/usr/bin/env python

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


@app.route("/api/switchServo")
def servo():
    status = request.args.get("status")
    if not status:
        abort(404)
    status = status.encode("ascii")
    if status not in enum_values:
        abort(404)

    if (status == '1'):
        s.write("servo1")
    elif (status == '0'):
        s.write("servo0")
    return json.dumps({"status": 200, "message": s.readline().strip()})


@app.route("/api/switchRelay")
def relay():
    status = request.args.get("status")
    if not status:
        abort(404)
    status = status.encode("ascii")
    if status not in enum_values:
        abort(404)

    if (status == '1'):
        s.write("relay1")
    elif (status == '0'):
        s.write("relay0")
    return json.dumps({"status": 200, "message": s.readline().strip()})


@app.route("/api/getSensor")
def sensor():
    status = request.args.get("status")
    if not status:
        abort(404)
    status = status.encode("ascii")
    if status not in enum_values:
        abort(404)

    s.write("sensor")
    return json.dumps({"status": 200, "message": s.readline().strip()})


@app.route('/')
def main():
    return json.dumps({"status":200, "message": "OK"})


if __name__ == '__main__':
    setup()
    app.debug = True
    app.run(host = inet_addr, port=5000)

