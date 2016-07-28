#!/usr/bin/env python
# coding=UTF-8
'''
The MIT License (MIT)

Copyright (c) 2015 Jasm Sison

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

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

import wave
from contextlib import closing

def bits(f):
    bytes = (ord(b) for b in f.read())
    for b in bytes:
        for i in xrange(8):
            yield (b >> i) & 1

def read_bits_from_payload(filename):
    with closing(open(filename, 'r')) as payload:
    for b in bits(payload):
        yield b # TODO yield each bit and write bit away to lsb of wav frame

def write_steg_frames(params, inwav_file, payload_filename, result_filename):
    nchannels, sampwidth, framerate, nframes, comptype, compname = params
    frames = inwav_file.readframes(nframes-1)
    read_bits_from_payload(payload_filename)


'''
Methods to expose this functionality to the command-line
'''
def steg_hide_naive(audio_filename, payload_filename, result_filename):
    with closing(wave.open(audio_filename, 'r')) as inwav_file:
        write_steg_frames(w.getparams(), inwav_file, payload_filename, result_filename)

def steg_reveal_naive(steg_audio, out):
    pass

import argparse

parser = argparse.ArgumentParser(description='This python program applies LSB Steganography to an audio file')

def main(av):
    #bgroup = parser.add_argument_group("Shift right to zero-fill before Xor, strategy")
    #bgroup.add_argument('-sin-max', help='Provide the original audio')
    #bgroup.add_argument('-cos-max', help='Shift to the right, in a cosine fashion with max amplitude')
    #bgroup.add_argument('-b', help='Shift to the right by b bits') # naive
    #bgroup.add_argument('-period', help='Period in frames, if the strategy is cyclic') #compulsory if periodic, TODO figure it out later

    bgroup = parser.add_argument_group("Hide binary with steg")
    bgroup.add_argument('-audio', help='Provide the original audio')
    bgroup.add_argument('-in', help='The payload file to be hidden in the audio')
    bgroup.add_argument('-steg-out', help='The resulting steganographic audio')

    bgroup = parser.add_argument_group("Reveal binary")
    bgroup.add_argument('-steg-audio', help='The steganographic audio')
    bgroup.add_argument('-out', help='The original input')

    args = parser.parse_args(av[1:])

    if len(av) == 8:
        steg_hide_naive(args.audio, args.in, args.steg_out)
    elif len(av) == 6:
        steg_reveal_naive(args.steg_audio, args.out)
    else:
        print "Usage: '", av[0], "-h' for help", "\n", args

if __name__ == "__main__":
    from sys import argv as av
    main(av)

