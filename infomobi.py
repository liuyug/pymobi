#!/usr/bin/env python

import sys
import os.path

from pymobi.mobi import BookMobi


def main_cli(path):
    if os.path.isfile(path):
        book = BookMobi(path)
        print('Title: %s' % book['title'])
        print('Author: %s' % book['author'])
        print('Creation time: %s' % book['creationDate'])
        print('Mobi Type: %s' % book['mobiType'])
        print('Mobi Version: %s' % book['version'])
        print('Encoding: %s' % book['encoding'])
        print('Compression: %s' % book['compression'])
        print('Encryption: %s' % book['encryption'])


if __name__ == '__main__':
    main_cli(sys.argv[1])
