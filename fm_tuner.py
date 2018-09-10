#!/usr/bin/python

import sys
from subprocess import PIPE, Popen

print('Number of arguments:', len(sys.argv))
if len(sys.argv) != 2:
    exit(1)
print('Argument List:', str(sys.argv))
freq = sys.argv[1]
print('Tuning to:', freq)
p1 = Popen(['rtl_fm', '-f ' + str(freq) + 'e6', '-s 200k', '-r 48000', '-l 20'], stdout=PIPE)
p2 = Popen(['aplay', '-r 48000', '-f S16_LE'], stdin=p1.stdout, stdout=PIPE)
output = p2.communicate()[0]
print(output)
exit(0)
