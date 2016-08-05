#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import serial
import time

if __name__ == '__main__':
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM7'
    ser.open()
    ser.write(b'AT\r')
    while True:
        print(ser.readline().decode())

    ser.close()
