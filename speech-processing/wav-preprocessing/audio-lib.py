# -*- coding: utf8 -*-
# Import the package and create an audio effects chain function.
from pysndfx import AudioEffectsChain
import os
import nlpaug.augmenter.audio as naa
import librosa, os

def wav_length_adjuster(original_wav, noise_wav, threshold, noised_wav_file):
    '''
    Making original_wav of length threshold ms, adding noise from noise file, at front and rear end of original_wav
    :param original_wav:
    :param noise_wav: any noise file or silence file etc.
    :param threshold: audio length in milisecond
    :param noised_wav_file: output wav
    :return:
    '''
    noise = AudioSegment.from_wav (noise_wav)
    original_audio = AudioSegment.from_wav (original_wav)

    if (len (original_audio) < threshold):
        x = threshold - len (original_audio)
        a = int (x / 2)
        b = x - a
        original_audio = noise[0:a] + original_audio[:] + noise[0:b]
        original_audio.export (noised_wav_file, format="wav")

    elif (len (original_audio) > threshold):
        extra = len (original_audio) - threshold
        original_audio = original_audio[:-extra]
        original_audio.export (noised_wav_file, format="wav")

def speed_aug(in_filepath, out_filepath):
    data, sr = librosa.load (in_filepath)
    aug = naa.SpeedAug (zone=(0.25, 0.75), factor=(.8, 1.2),
                        coverage=1)  # making speeder factor=(1.3,2.1), 0 - <1 making slower
    augmented_data = aug.augment (data)
    librosa.output.write_wav (out_filepath, augmented_data, sr)


def volume_aug(in_filepath, out_filepath):
    data, sr = librosa.load (in_filepath)
    aug = naa.LoudnessAug (zone=(0.1, 0.9), factor=(1.5, 2.9), coverage=1)
    augmented_data = aug.augment (data)
    librosa.output.write_wav (out_filepath, augmented_data, sr)


def pitch(in_filepath, out_filepath):
    data, sr = librosa.load (in_filepath)
    aug = naa.PitchAug (sampling_rate=sr, factor=(2, 3), zone=(0.1, 0.9), coverage=1)
    augmented_data = aug.augment (data)
    librosa.output.write_wav (out_filepath, augmented_data, sr)


def reverb(infile, outfile):
    """

    :param infile: in file path
    :param outfile: out file path
    :return:
    """
    fx = (
        AudioEffectsChain ()
            # .highshelf()
            .reverb ()  # useful for ASR-kaldi
        # .phaser()  # useful for ASR-kaldi
        # .delay() # XXXXXXXXXXXXXXXXXXXXX not useful for ASR
        # .lowshelf()
    )

    # Apply phaser and reverb directly to an audio file.
    fx (infile, outfile)

    # Or, apply the effects directly to a ndarray.
    from librosa import load
    y, sr = load (infile, sr=None)
    y = fx (y)

    # Apply the effects and return the results as a ndarray.
    y = fx (infile)

    # Apply the effects to a ndarray but store the resulting audio to disk.
    fx (y, outfile)


def phaser(infile, outfile):
    """

    :param infile: in file path
    :param outfile: out file path
    :return:
    """
    fx = (
        AudioEffectsChain ()
            # .highshelf()
            # .reverb()  # useful for ASR-kaldi
            .phaser ()  # useful for ASR-kaldi
        # .delay() # XXXXXXXXXXXXXXXXXXXXX not useful for ASR
        # .lowshelf()
    )

    # Apply phaser and reverb directly to an audio file.
    fx (infile, outfile)

    # Or, apply the effects directly to a ndarray.
    from librosa import load
    y, sr = load (infile, sr=None)
    y = fx (y)

    # Apply the effects and return the results as a ndarray.
    y = fx (infile)

    # Apply the effects to a ndarray but store the resulting audio to disk.
    fx (y, outfile)
