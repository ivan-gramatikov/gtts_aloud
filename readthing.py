from gtts import gTTS
import subprocess
import sys
import os

saved_text = sys.argv[1]
saved_mp3 = sys.argv[2]

with open(saved_text, 'r') as f:
    readthis = f.read()

tts = gTTS(readthis)
tts.save(sys.argv[2])
args = ['vlc', saved_mp3]
subprocess.call(args)
