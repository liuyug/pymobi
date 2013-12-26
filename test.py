#!/usr/bin/env python

import sys
import os.path

from pymobi.mobi import BookMobi
from pymobi.util import hexdump


def main_cli(path):
    if os.path.isfile(path):
        book = BookMobi(path)
        print('==== book ====')
        for key, value in book.book.items():
            print('%s: %s' % (key, value))
        print('==== header ====')
        for key, value in book.header.items():
            print(key, value)
        print('==== palmdoc ====')
        for key, value in book.palmdoc.items():
            print(key, value)
        print('==== mobi ====')
        for key, value in book.mobi.items():
            print(key, value)
        print('==== mobi exth====')
        for key, value in book.mobi_exth.items():
            print(key, value)
        #for num in range(1, book.header['numberOfRecords']):
        #    rec = book.loadRecord(num)
        #    offset = book.records[num]
        #    print('==== record %d ====' % num)
        #    print(offset)
        #    hexdump(rec[:16])

if __name__ == '__main__':
    main_cli(sys.argv[1])
