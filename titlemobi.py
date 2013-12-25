#!/usr/bin/env python

import sys
import os.path

from pymobi.mobi import BookMobi


def bookrename(path):
    book = BookMobi(path)
    basename = os.path.basename(path)
    dirname = os.path.dirname(path)
    newname = '%s_%s' % (book['title'], basename)
    newpath = os.path.join(dirname, newname)
    os.rename(path, newpath)


def main_cli(path):
    if os.path.isfile(path):
        bookrename(path)
    else:
        library = os.path.join(path)
        for filename in os.listdir(library):
            ext = os.path.splitext(filename)[1]
            if ext in ['.mobi', '.azw', '.azw3']:
                filepath = os.path.join(library, filename)
                bookrename(filepath)


if __name__ == '__main__':
    main_cli(sys.argv[1])
