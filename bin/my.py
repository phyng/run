#!/usr/bin/env python
# coding: utf-8

"""
when use `sudo ln -s */index.py /usr/bin/my`
and run `my` on `~`
    os.getcwd() == `~`
    sys.argv[0] == `/usr/bin/my`
    sys.path[0] == '*/index.py'
"""

import os
import sys
import importlib

BASE_DIR = os.path.dirname(__file__)


def main():
    args = sys.argv
    if len(args) == 1:
        os.system('ls -l --color {}  | grep -E ".py"'.format(sys.path[0]))
        return
    try:
        lib = importlib.import_module(args[1])
    except ImportError:
        print 'ImportError'
    else:
        lib.main(*args[2:])


if __name__ == '__main__':
    main()
