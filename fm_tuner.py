#!/usr/bin/python

import sys
from subprocess import Popen, PIPE

print('Number of arguments:', len(sys.argv))
if len(sys.argv) != 2:
    exit(1)
print('Argument List:', str(sys.argv))
freq = sys.argv[1]
print('Tuning to:', freq)
p1 = Popen(['rtl_fm -f ' + str(freq) + 'e6 -s 200k -r 48000 -l 20'], stdout=PIPE, stderr=PIPE)
p2 = Popen(['aplay -r 48000 -f S16_LE'], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
output, err = p2.communicate()
print(output, err)
exit(0)
