#!/bin/bash

cp ser.c serr.c

#gcc serr.c -o ser $(pkg-config --cflags --libs sdl2)
gcc serr.c -o ser
