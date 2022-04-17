#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0111

from datetime import datetime


def log(*msgs):
    msg_str = "".join(str(msg) for msg in msgs)
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]', msg_str)
