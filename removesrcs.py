#!/usr/bin/env python

import sys
import os.path

from pymobi.mobi import BookMobi


def main_cli(inmobi, outmobi, outsrcs):
    if os.path.isfile(inmobi):
        book = BookMobi(inmobi)
        book.removeSrcs(outmobi, outsrcs)

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 3:
        print('%s <input mobi file> <output mobi file> [output srcs]' % sys.argv[0])
        sys.exit(0)
    in_mobifile = sys.argv[1]
    out_mobifile = sys.argv[2]
    if argc > 3:
        out_srcsfile = sys.argv[3]
    else:
        out_srcsfile = None
    main_cli(in_mobifile, out_mobifile, out_srcsfile)
