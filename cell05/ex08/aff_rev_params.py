#!/usr/bin/python3

import sys

rever_arg = sys.argv[1:][::-1]
if len(sys.argv) > 3:
    print('\n'.join(rever_arg))
else:
    print("none")