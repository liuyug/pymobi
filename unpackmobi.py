#!/usr/bin/env python

import sys
import os.path

from pymobi.mobi import BookMobi


def main_cli(infile, outfile):
    if os.path.isfile(infile):
        book = BookMobi(infile)
        book.unpackMobi(outfile)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('%s <mobi file> <output html>' % sys.argv[0])
        sys.exit(0)
    main_cli(sys.argv[1], sys.argv[2])
