#!/usr/bin/env python

from __future__ import print_function

import os
import sys
from . import dump_text, exceptions


def main():
    if len(sys.argv) != 2:
        print("Usage: dwgstrings file.dwg or dwgstrings file.dxf",
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print("Error: '%s': No such file" % sys.argv[1], file=sys.stderr)
        sys.exit(1)

    try:
        dump_text(sys.argv[1])
    except exceptions.TeighaNotInstalledError:
        print("Error: Teigha File Converter must be installed to read .dwg "
              "files. It can be downloaded at "
              "https://www.opendesign.com/guestfiles/teighafileconverter",
              file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
