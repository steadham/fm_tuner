#!/usr/bin/python

import sys
import re
from subprocess import Popen, PIPE

print('Number of arguments:', len(sys.argv))
if len(sys.argv) != 2:
    exit(1)
print('Argument List:', str(sys.argv))
freq = sys.argv[1]
print('Tuning to:', freq)
p1 = Popen(['rtl_fm', '-f ' + str(freq) + 'e6', '-s 200k', '-r 48000'], stdout=PIPE)
p2 = Popen('aplay -r 48000 -f S16_LE', stdin=p1.stdout, stdout=PIPE, shell=True)
(output, err) = p2.communicate()
print('output:', output, 'err:', err)
tuned_to = re.search('Tuned to .+ Hz\.', output).group(0)
freq = int(re.search('\d+', tuned_to).group(0)) / 1000000 - .3
print('Tuned to: ', str(freq))
exit(0)
