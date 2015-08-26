LSB Steganography on non-lossy digital audio files
==================================================

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

Wav
* wav, skip initial 44 kbytes of metadata
* Determine LSBW (least significant bit width), before people start hearing it, although a histogram could easily reveal it...
* Will provide parameter to adjust LSBW, or even variable bit width, e.g. sinusoidal, harmonics, cyclic, stochastic?


TIFF
* WAV to TIFF conversion

FLAC
* WAV to FLAC conversion

Ogg-vorbis
* 100% retention, non-lossy conversion

MP3
* 100% retention, store payload within the audible range?

Extras
* unit test with audio sample
* histogram comparison, i.e. before steg, after steg.
