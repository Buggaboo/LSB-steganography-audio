LSB Steganography on non-lossy digital audio files
==================================================

Inspired by the TV-series: Mr. Robot.

Setup
-----

```bash
virtualenv env
source env/bin/activate
pip install ...TODO
```

Usage
-----

```bash
source env/bin/activate
python lsb_steg_audio.py ...
```

Roadmap
-------

WAV
* wav, skip initial 44 kbytes of metadata (microsoft format)
* Determine LSBW (least significant bit width, apparently WAV is little endian), before people start hearing it, although a histogram could easily reveal it...
* Will provide parameter to adjust LSBW, or even variable bit width, e.g. sinusoidal, harmonics, stochastic by hash?


TIFF
* WAV to TIFF conversion

FLAC
* WAV to FLAC conversion

Ogg-vorbis
* 100% retention (TODO determine how), wav to ogg == ogg to wav
* invariant to psychoacoustic model?

MP3
* 100% retention (TODO determine how), idem
* invariant to psychoacoustic model?

Extras
* unit test with audio sample
* histogram comparison, i.e. before steg, after steg.
* payload compression (nah, KISS)

Experimental
* load frames to GPGPU, collate results, then write collated results to file

Run tests
---------
```bash
python -m doctest -v lsb_steg_audio.py # work in progress (2015-08)
```
