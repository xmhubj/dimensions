#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: {0} file1 [file2 [...filen]]".format(sys.argv[0]))
        sys.exit()
