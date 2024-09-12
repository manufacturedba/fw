# SPDX-FileCopyrightText: 2022 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT
# Motorized fader demo
import time
import board
import analogio


# Slide pot setup
fader = analogio.AnalogIn(board.A0)
#fader_position = fader.value  # ranges from 0-65535
count = 1
total = fader.value
# fader_pos = fader.value // 256  # make 0-255 range
# last_fader_pos = fader_pos

while True:
    total = total + fader.value
    count += 1
    fader_position = total // count
    print("Fader Position: ", fader_position)
    time.sleep(1)