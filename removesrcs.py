#!/usr/bin/env python

import os.path
import argparse

from pymobi.mobi import BookMobi


def main_cli(inmobi, outmobi, outsrcs):
    if os.path.isfile(inmobi):
        book = BookMobi(inmobi)
        book.removeSrcs(outmobi, outsrcs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inmobi', help='input mobi file')
    parser.add_argument('outmobi', help='output mobi file')
    parser.add_argument('outsrcs', nargs='?', help='output srcs file')
    args = parser.parse_args()
    main_cli(args.inmobi, args.outmobi, args.outsrcs)
