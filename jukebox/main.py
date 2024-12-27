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
import die_gedanken_sind_frei
import froh_und_munter
import kling_gloeckchen_kling
import leise_rieselt_der_schnee
import morgen_kinder_wirds_was_geben as mk
import silent_night

while True:
    main(song=die_gedanken_sind_frei.song, verses=4, speed=0.15)
    main(song=kling_gloeckchen_kling.song, verses=3)
    main(song=alle_jahre_wieder.song, verses=3, speed=0.15)
    main(song=leise_rieselt_der_schnee.song, verses=3)
    main(song=froh_und_munter.song, verses=5, speed=0.12)
    main(song=silent_night.song, verses=3)
    main(song=mk.song, verses=3, speed=0.15, continue_playing=False)
