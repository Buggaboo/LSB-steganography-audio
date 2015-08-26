#!/usr/bin/env python
# coding=UTF-8
'''
Copyright © 2015, Jasm Sison - MIT-Licensed

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The Software is provided "as is", without warranty of any kind, express or implied, including but not limited
to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall
the authors or copyright holders X be liable for any claim, damages or other liability, whether in an action
of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other
dealings in the Software.

Except as contained in this notice, the name of the Robin David shall not be used in advertising or otherwise
to promote the sale, use or other dealings in this Software without prior written authorization from the Robin David.
'''

"""
How to install the dependencies on a mac
----------------------------------------
0) create a virtualenv, install the dependencies
```bash
virtualenv env
source env/binary/activate
pip install ...TODO...
```
1) Reinstall brew; if need be.
```bash
rm -rf /usr/local/Cellar /usr/local/.git && brew cleanup
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2) Add the packages to python; if need be.
```bash
mkdir -p $HOME/Library/Python/2.7/lib/python/site-packages
echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> $HOME/Library/Python/2.7/lib/python/site-packages/homebrew.pth
```
"""



'''
Methods to expose this functionality to the command-line
'''
def binary_steg_hide(audio, binary, result):
    pass
#    carrier = cv.Loadaudio(audio)
#    steg = LSBSteg(carrier)
#    steg.hideBin(binary)
#    steg.saveaudio(result)

def binary_steg_reveal(steg_audio, out):
    pass
#    inp = cv.Loadaudio(steg_audio)
#    steg = LSBSteg(inp)
#    bin = steg.unhideBin()
#    f = open(out, "wb")
#    f.write(bin)
#    f.close()

import argparse

parser = argparse.ArgumentParser(description='This python program applies LSB Steganography to an audio file')

def main(av):
    bgroup = parser. add_argument_group("Hide binary with steg")
    bgroup.add_argument('-audio', help='Provide the original audio')
    bgroup.add_argument('-binary', help='The binary file to be obfuscated in the audio')
    bgroup.add_argument('-steg-out', help='The resulting steganographic audio')

    bgroup = parser.add_argument_group("Reveal binary")
    bgroup.add_argument('-steg-audio', help='The steganographic audio')
    bgroup.add_argument('-out', help='The original binary')

    args = parser.parse_args(av[1:])

    if len(av) == 7:
	binary_steg_hide(args.audio, args.binary, args.steg_out)
    elif len(av) == 5:
        binary_steg_reveal(args.steg_audio, args.out)
    else:
        print "Usage: '", av[0], "-h' for help", "\n", args

if __name__=="__main__":
    from sys import argv as av
    main(av)

