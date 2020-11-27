#!/usr/bin/python
# -*- coding: UTF-8 -*-
import glob
import sounddevice as sd
import soundfile as sf
from datetime import datetime
import os, os.path
import os, random

# Wake-Uo-Word Detection

# if os.path.exists('wav_decode/audio_frame_test.wav'):
#     os.remove('wav_decode/audio_frame_test.wav')

files = glob.glob('wav_decode/*')
for f in files:
    print('removing '+ f)
    os.remove(f)
if os.path.exists('noise.prof'):
    os.remove('noise.prof')

from pydub import AudioSegment

model='tri3a'
samplerate=44100  # Hertz
# duration = 1.75  # seconds
def stt_predict(model):
    os.system('sudo ./call_decode_system.sh')
    with open('one-best-hypothesis-'+model+'.txt') as f:
        return f.readline().split(' ', 1)[1]

while True:
    mydata = sd.rec(int(samplerate * random.choice([1.50, 1.70,1.40,1.60, 1.30])), samplerate=samplerate,channels=1, blocking=True)
    sf.write('wav_decode/audio_frame_test.wav', mydata, samplerate)
    ## NOISE REMOVE IF NEED
    sound = AudioSegment.from_file('wav_decode/audio_frame_test.wav', "wav")
    print('Current dBFS  '+str(sound.dBFS))
    if (sound.dBFS <= -22 and sound.dBFS >= -35 and (str(sound.dBFS) != '-inf') ):  # Suppose noise is within sound.dBFS <= -22 and sound.dBFS >= -35
        print('Generating noise.prof')
        sf.write('wav_decode/audio_frame_noise.wav', mydata, samplerate)
        os.system('sox wav_decode/audio_frame_noise.wav -n noiseprof noise.prof')
        continue
    if os.path.exists('noise.prof'):
         os.system('sox wav_decode/audio_frame_test.wav wav_decode/audio_frame_clean.wav noisered noise.prof 0.21')

    ## Noise -- end



    ans = stt_predict(model) # Pass model

    if ('Hey' in ans) and ('Google' in ans) and (ans.find('Hello') < ans.rfind('Google')):
        print("Wake Up Word FOUND")
        # WUWservicehandler()   # break
    else:
        print('FOUND: ' + ans)



    # break #  Debug mood
