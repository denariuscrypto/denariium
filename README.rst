Denariium - Lightweight Denarius client
==========================================

::

  Licence: MIT Licence
  Original Author: Thomas Voegtlin and Pooler
  Port Maintainer: Carsen Klock
  Language: Python 2
  Homepage: https://denariium.org/


Getting started
===============

Before you upgrade, always make sure you have saved your wallet seed on paper.

Denariium is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

    sudo apt-get install python-qt4

If you downloaded the official package (tar.gz), you can run
Denariium from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Denariium from its root directory, just do::

    ./denariium

You can also install Denariium on your system, by running this command::

    python2 setup.py install

This will download and install the Python dependencies used by
Denariium, instead of using the 'packages' directory.

If you cloned the git repository, you need to compile extra files
before you can run Denariium. Read the next section, "Development
Version".



Development version
===================

Check out the code from Github::

    git clone git://github.com/carsenk/denariium
    cd denariium

Run install (this should install dependencies)::

    python2 setup.py install

Compile the icons file for Qt::

    sudo apt-get install pyqt4-dev-tools
    pyrcc4 icons.qrc -o gui/qt/icons_rc.py

Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto
2
Create translations (optional)::

    sudo apt-get install python-pycurl gettext
    ./contrib/make_locale




Creating Binaries
=================


To create binaries, create the 'packages' directory::

    ./contrib/make_packages

This directory contains the python dependencies used by Denariium.

Mac OS X
--------

::

    # On MacPorts installs: 
    sudo python setup-release.py py2app
    
    # On Homebrew installs: 
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip
    
    sudo hdiutil create -fs HFS+ -volname "Denariium" -srcfolder dist/Denariium.app dist/denariium-VERSION-macosx.dmg

Windows
-------

See `contrib/build-wine/README` file.


Android
-------

See `gui/kivy/Readme.txt` file.
