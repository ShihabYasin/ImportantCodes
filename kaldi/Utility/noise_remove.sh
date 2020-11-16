#!/bin/bash
# Give sample noise(*.wav) in dir "noise_sound"
# Create "wav_decode" folder
# this .sh will generate clean wavs in dir "wav_decode" .
# Output file format: {prev_name}_clean.wav

FILE="noise_sound/noise.wav"
DIR="noise_sound"

if [ "$(ls -A $DIR)" ]; then
	if [ -f "$FILE" ]; then
		echo "Noise Reduction Applied."
		#Generate a noise profile in sox:
		sox noise_sound/noise.wav -n noiseprof noise.prof
		#Clean the noise from the audio		
		for f in wav_decode/*.wav; do
			sox "$f" "$f"_clean.wav noisered noise.prof 0.21  # Noise Reduction Threshold 
		done
	else 
		echo "No Noise Reduction. $FILE does not exist to do Noise Reduction."
	fi 
fi

exit 1


# test change