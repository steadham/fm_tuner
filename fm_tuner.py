#!/usr/bin/python

import sys
from subprocess import call

print('Number of arguments:', len(sys.argv))
if len(sys.argv) != 2:
    exit(1)
print('Argument List:', str(sys.argv))
freq = sys.argv[1]
print('Tuning to:', freq)
call(['rtl_fm', '-f ' + str(freq) + 'e6', '-s 200k', '-r 48000', '-f 20' '|', 'aplay', '-r 48000', '-f S16_LE'])
print('called')
exit(0)
