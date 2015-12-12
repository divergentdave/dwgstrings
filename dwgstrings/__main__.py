#!/usr/bin/env python

from . import dump_text

def main():
  if len(sys.argv) != 2:
    print "Usage: %s file.dwg or %s file.dxf" % (sys.argv[0], sys.argv[0])
    sys.exit(1)

  dump_text(sys.argv[1])

if __name__ == '__main__':
  main()
