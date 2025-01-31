#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
// Copyright (c) 2024, Oliver Merkel.
// Please see the AUTHORS file for details.
// All rights reserved.
//
// Use of this code is governed by a
// MIT license that can be found in the LICENSE file.
"""

# Hardware setup:
#   Passive buzzer GND to Raspberry Pi Pico GND
#   Passive buzzer + Pin to GPIO Pin 15

from machine import Pin, PWM, Timer
from utime import sleep

led = Pin("LED", Pin.OUT)
timer = Timer()


def blink(timer):
    led.toggle()


timer.init(freq=20., mode=Timer.PERIODIC, callback=blink)

lookup_duration = [ "_", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2",
    "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16", "1" ]

scale = {
    "title": "Scale",
    "score": [('c4', '1/4'), ('d4', '1/4'), ('e4', '1/4'), ('f4', '1/4'),
         ('g4', '1/4'), ('a4', '1/4'), ('b4', '1/4'), ('c5', '1/4')]
}


def setup():
    SPEAKER_PIN = 15
    speaker = PWM(Pin(SPEAKER_PIN))
    speaker.duty_u16(1000)

    speaker.freq(10)
    sleep(0.1)
    return speaker


def length_to_duration(length):
    return lookup_duration.index(length)


def main(song=scale, speed=0.2, continue_playing=False, verses=1):
    speaker = setup()
    midi_mapping = {
        "c": 0, "c#": 1, "d": 2, "d#": 3, "e": 4, "f": 5, "f#": 6,
        "g": 7, "g#": 8, "a": 9, "a#": 10, "b": 11,
    }
    title = song["title"]
    print(f"Playing {title}...")
    while True:
        for verse in range(verses):
            print(f"Verse #{verse+1}")
            for note, length in song["score"]:
                d = length_to_duration(length)
                print(note, length, d, end=", "),
                if note != "-":
                    midi_note = midi_mapping[note[:-1]] + (1+int(note[-1]))*12
                    freq_hz = int(440*(2**(1/12))**(midi_note-69))
                    speaker.freq(freq_hz)
                    speaker.duty_u16(1000)
                sleep(0.9 * speed * d)
                speaker.duty_u16(0)
                sleep(0.1 * speed * d)
            print()
        speaker.duty_u16(0)
        sleep(2)
        if not continue_playing:
            break


if __name__=="__main__":
    main(speed=0.14, continue_playing=False)
