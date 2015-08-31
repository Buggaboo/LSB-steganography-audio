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

UNCONFIRMED_MAGIC_NUMBER_WAV_HEADER_FRAMES = 44

'''
xor bits of the payload to the current frame
'''
def lsb_steg_single_channel_op(bits, frame):
    # bits size determines how much to shift by
    # shift_by_n = bits.bit_length()
    # shit... you're screwing with one channel
#    frame >> shift_by_n
#    frame << shift_by_n # the LSBs are zeroed out
    pass

def lsb_steg_dual_channel_op(bits_left, bits_right, frame):
    pass

'''
Methods to expose this functionality to the command-line
'''
def binary_steg_hide_naive(audio, binary, result, steg_bit_depth):
    with wave.open(audio) as w:
        wresult = wave.open(result, 'wb+')

        # retain params
	params = w.getparams()
        wresult.setparams(params)
	print params
	nchannels, sampwidth, framerate, nframes, comptype, compname = params

        # TODO calculate if the payload will actually fit, depending on the LSB Steg strategy
        bits = []
        samplewidth = w.getsamplewidth() # also, by default WAV is little endian, i.e. least significant bits have the lowest addresses

	# try not to damage the metadata
	w.getnframes(UNCONFIRMED_MAGIC_NUMBER_WAV_HEADER_FRAMES)

	# decompose payload (this depends on the strategy)
        # TODO use bitarray thingy library, this also depends on the nchannels

	# superduper inefficient in-memory operation
        # IDEA use decorator to plugin LSB Steg algorithm
        newframes = []

#	for i in range(w.getnframes()):
#	    newframes.append(lsb_steg_op(bits[i], w.readframes(1), ))

	# collate steg'd results
#        wresult.writeframesraw(''.join(newframes))
        
        wresult.close()
        #w.close()


def binary_steg_reveal_naive(steg_audio, out, steg_bit_depth):
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
    bgroup = parser.add_argument_group("Shift right to zero-fill before Xor, strategy")
    #bgroup.add_argument('-sin-max', help='Provide the original audio')
    #bgroup.add_argument('-cos-max', help='Shift to the right, in a cosine fashion with max amplitude')
    bgroup.add_argument('-b', help='Shift to the right by b bits') # naive
    #bgroup.add_argument('-period', help='Period in frames, if the strategy is cyclic') #compulsory if periodic, TODO figure it out later

    bgroup = parser.add_argument_group("Hide binary with steg")
    bgroup.add_argument('-audio', help='Provide the original audio')
    bgroup.add_argument('-binary', help='The binary file to be obfuscated in the audio')
    bgroup.add_argument('-steg-out', help='The resulting steganographic audio')

    bgroup = parser.add_argument_group("Reveal binary")
    bgroup.add_argument('-steg-audio', help='The steganographic audio')
    bgroup.add_argument('-out', help='The original binary')

    args = parser.parse_args(av[1:])

    if len(av) == 8:
	binary_steg_hide_naive(args.audio, args.binary, args.steg_out, args.b)
    elif len(av) == 6:
        binary_steg_reveal_naive(args.steg_audio, args.out, args.b)
    else:
        print "Usage: '", av[0], "-h' for help", "\n", args

if __name__ == "__main__":
    from sys import argv as av
    main(av)

