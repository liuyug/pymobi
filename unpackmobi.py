#!/usr/bin/env python

import os.path
import argparse

from pymobi.mobi import BookMobi


def main_cli(infile, outfile):
    if os.path.isfile(infile):
        book = BookMobi(infile)
        book.unpackMobi(outfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inmobi', help='input mobi file')
    parser.add_argument('outhtml', help='output html file')
    args = parser.parse_args()
    main_cli(args.inmobi, args.outhtml)
