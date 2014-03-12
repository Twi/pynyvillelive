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

class Base(object):
    def __init__(self, api_dict):
        self.api_dict = api_dict

    def __getattr__(self, name):
        if name in self.api_dict:
            return self.api_dict[name]
        else:
            sup = super(object, self)
            if hasattr(sup, name):
                return getattr(sup, name)
            else:
                raise AttributeError("%s is not an attribute" % name)

class Station(Base):
    def __init__(self, api_dict):
        Base.__init__(self, api_dict)

        self.now_playing = Song(self.song_id)

        self.play_history = []

        for song in self.song_history:
            self.play_history.append(Song(song["id"]))

    def __repr__(self):
        return "<%s: \"%s\": %s>" %\
                (self.__class__.__name__, self.code, self.name)

class Song(Base):
    def __init__(self, songid):
        json = requests.get("http://ponyvillelive.com/api/song/index/id/%s" %
                songid).json()
        if json["status"] == "error":
            raise exceptions.SongLookupError()

        json = json["result"]

        Base.__init__(self, json)

    def __repr__(self):
        return "<%s: %s>" %\
                (self.__class__.__name__, self.text)

