# This file changes sound amplitude (avg ). AUDIO NORMALIZATION .
# dBFS: Decibel to FULL SCALE , 0 dBFS ( average amplitude ) is maximum
import os
from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS):
    print('Current dBFS: ' + str(sound.dBFS) )
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)



arr = os.listdir('audio_in/01005/')

for x in arr:
    print(x)
    sound = AudioSegment.from_file("audio_in/01005/"+ x, "wav")
    normalized_sound = match_target_amplitude(sound, -18.0)  # -18 dBFS as Norm Limit
    normalized_sound.export("audio_out/"+ x, format="wav")


# sound = AudioSegment.from_file("audio_in/01005/1.wav", "wav")
# normalized_sound = match_target_amplitude(sound, -18.0)  # -18 dBFS as Norm Limit
# normalized_sound.export("audio_out/1.wav", format="wav")

exit (1)