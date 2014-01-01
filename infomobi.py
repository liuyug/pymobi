#!/usr/bin/env python

import argparse
import os.path

from pymobi.mobi import BookMobi


def main_cli(args):
    if os.path.isfile(args.book):
        book = BookMobi(args.book)
        if not args.all and not args.n and not args.p and not args.m and not args.e:
            for key, value in book.book.items():
                print('%s: %s' % (key.capitalize(), value))
        if args.all or args.n:
            for key, value in book.header.items():
                print('%s: %s' % (key.capitalize(), value))
        if args.all or args.p:
            for key, value in book.palmdoc.items():
                print('%s: %s' % (key.capitalize(), value))
        if args.all or args.m:
            for key, value in book.mobi.items():
                print('%s: %s' % (key.capitalize(), value))
        if args.all or args.e:
            for key, value in book.mobi_exth.items():
                print('%s: %s' % (key, value))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('book', help='mobi book')
    parser.add_argument('-a', '--all', help='display all meta data', action='store_true')
    parser.add_argument('-n', action='store_true', help='display header')
    parser.add_argument('-p', action='store_true', help='display palmdoc header')
    parser.add_argument('-m', action='store_true', help='display mobi header')
    parser.add_argument('-e', action='store_true', help='display mobi exth data')
    pargs = parser.parse_args()
    main_cli(pargs)
