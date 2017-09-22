#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Denariium requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['denariium.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/denariium.png'])
    ]

setup(
    name="Denariium",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'tribus_hash',
        'protobuf',
        'dnspython',
        'jsonrpclib',
        'PySocks>=1.6.6',
    ],
    packages=[
        'denariium',
        'denariium_gui',
        'denariium_gui.qt',
        'denariium_plugins',
        'denariium_plugins.audio_modem',
        'denariium_plugins.cosigner_pool',
        'denariium_plugins.email_requests',
        'denariium_plugins.hw_wallet',
        'denariium_plugins.keepkey',
        'denariium_plugins.labels',
        'denariium_plugins.ledger',
        'denariium_plugins.trezor',
        'denariium_plugins.digitalbitbox',
        'denariium_plugins.virtualkeyboard',
    ],
    package_dir={
        'denariium': 'lib',
        'denariium_gui': 'gui',
        'denariium_plugins': 'plugins',
    },
    package_data={
        'denariium': [
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['denariium'],
    data_files=data_files,
    description="Lightweight Denarius Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="http://denariium.org",
    long_description="""Lightweight Denarius Wallet"""
)
