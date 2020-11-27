# Get screaming loudness & amplitude to detect screaming

import soundfile as sf
import pyloudnorm as pyln
from pydub import AudioSegment
import os
# Result -22 is max env sound
def get_amplitude(FILE):
    sound = AudioSegment.from_file(FILE, "wav")
    # print('Amplitude (dBFS) of ('+ FILE+')  : ' + str(sound.dBFS) )
    print(FILE+"    "+str(sound.dBFS))

def get_loudness(FILE):
    data, rate = sf.read(FILE)  # load audio (with shape (samples, channels))
    meter = pyln.Meter(rate) # create BS.1770 meter
    loudness = meter.integrated_loudness(data) # measure loudness
    # print('Loudness (BS.1770): of ('+ FILE+')  : ', loudness)
    print(FILE+"    "+loudness)

# path = 'screaming_audio/'
path='env_sound_collection/'
files = os.listdir(path)
for i in files:
    if i.endswith('.wav'):
        # get_loudness(path+i)
        get_amplitude(path+i)

exit(1)