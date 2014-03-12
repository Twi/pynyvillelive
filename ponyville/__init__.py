"""
Copyright (c) 2014, Nicole Brennan
All rights reserved.

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

    1. The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software
    in a product, an acknowledgment in the product documentation would be
    appreciated but is not required.

    2. Altered source versions must be plainly marked as such, and must not be
    misrepresented as being the original software.

    3. This notice may not be removed or altered from any source
    distribution.
"""

import exceptions
import requests
import structures

def now_playing(shortcode=None):
    """
    inputs: shortcode of station or None
    outputs: if shortcode is None, list of all Stations
             else Station indexed by shortcode

    ***THIS MAY TAKE A LONG TIME***
    """
    if shortcode == None:
        json = requests.get("http://ponyvillelive.com/api/nowplaying").json()

        if json["status"] == "error":
            raise exceptions.APIError("The nowplaying page is acting up. "
                    "Bug Silver about this, it is not my fault.")

        json = json["result"]

        stations = []

        for shortcode in json:
            station = json[shortcode]
            print shortcode
            stations.append(structures.Station(station))

        return stations

    else:
        # Get one station
        json = requests.get("http://ponyvillelive.com/api/nowplaying/index/station/%s" %
                shortcode).json()

        if json["status"] == "error":
            raise exceptions.APIError("The nowplaying page is acting up. "
                    "Bug Silver about this, it is not my fault.")

        json = json["result"]

        return structures.Station(json)

def get_song(songid):
    """
    input: songid
    output: Song object
    """
    return structures.Song(songid)

