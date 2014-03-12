.. pynyvillelive documentation master file, created by
   sphinx-quickstart on Wed Mar 12 15:39:12 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pynyvillelive
=============

Contents:

.. toctree::
   :maxdepth: 2

pynyvillelive is an API wrapper for Ponyville Live's JSON api.

Example usage:

    import ponyville
    
    for station in ponyville.now_playing():
        print repr(station)

Features
--------

- Simplicity in design
- Ease of use
- No unexpected weird things

Installation
------------

Install $project by running:

    sudo python setup.py install

Contribute
----------

- Issue Tracker: http://github.com/bookhorse/pynyvillelive/issues
- Source Code: http://github.com/bookhorse/pynyvillelive

The project is licensed under the Zlib license. 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

