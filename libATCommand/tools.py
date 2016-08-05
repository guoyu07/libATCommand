#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from serial.tools import list_ports as _list_ports


def list_ports():
    return [tuple(i) for i in _list_ports.comports()]
