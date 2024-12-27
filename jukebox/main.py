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

from jukebox import main
import alle_jahre_wieder
import froh_und_munter
import leise_rieselt_der_schnee
import morgen_kinder_wirds_was_geben as mk
import silent_night

while True:
    main(song=alle_jahre_wieder.song, speed=0.15)
    main(song=leise_rieselt_der_schnee.song)
    main(song=froh_und_munter.song, speed=0.12)
    main(song=silent_night.song)
    main(song=mk.song, speed=0.15, continue_playing=False)
