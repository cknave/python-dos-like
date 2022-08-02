#!/usr/bin/env python
from random import randrange

import dos_like
from dos_like.dos import *


def main():
    setvideomode(videomode_320x200)

    while not shuttingdown():
        waitvbl()
        for _ in range(50):
            setcolor(randrange(256))
            line(randrange(320), randrange(200), randrange(320), randrange(200))
            setcolor(randrange(256))
            fillcircle(randrange(320), randrange(200), randrange(30))
            setcolor(randrange(256))
            circle(randrange(320), randrange(200), randrange(30))


dos_like.start(main)
