# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import pydub
import os, ntpath, shutil, random
import sys
import pandas as pd
from pydub import AudioSegment
from os import listdir
from os.path import isfile, join
import math, os, ntpath, shutil
from pydub import AudioSegment

# For Jupyter calling
import IPython.display as ipd
import ipywidgets as widgets

sys.path.append ('v3/lib/python3.7/site-packages/')

current_file = None
curr_dir = os.getcwd () + '/'
data_folder = 'out_tts'
original_dir = 'wavs_tts/'
modified_dir = 'out_tts' + '/'
temp_dir = 'tmp/'
output_stat = 'tts_text/tts_stat'
next_button = widgets.Button (description='Next')
edit_button = widgets.Button (description='Edit')
save_button = widgets.Button (description='Save')


def _copy_from_file_list(filename='silence-stat.txt', count=-1, dest='wavs'):
    """

    :param filename:
    :param count: -1 for all files to copy
    :return:
    """

    with open (filename) as f:
        lines = f.readlines ()
    if count == -1:
        count = len (lines)
    cnt = 0
    for line in lines:
        if cnt > count:
            break
        print (line[14:])
        shutil.copy2 (line[14:-1], dest)
        cnt += 1
    print ("Total copied files:", cnt)


def _detect_leading_silence(sound, peak_amplitude, percentile, diff_dBFS=10, min_voice_dBFS=-40.0, chunk_size=10,
                            logfile='stat.txt'):
    """
    :param sound: sound is a pydub.AudioSegment
    :param diff_dBFS: difference between prev and curr sound chunk dBFS
    :param min_voice_dBFS: min sound dBFS to consider as sound
    :param chunk_size: chunk_size in ms
    :return: iterate over chunks until find the first chunk one with sound, return that position(ms), return -1 default (all silence)
    """
    assert chunk_size > 0  # to avoid infinite loop
    assert diff_dBFS > 0
    trim_ms = 0  # starting from 0 ms
    duration = len (sound);

    prev_dBFS = sound[trim_ms:trim_ms + chunk_size].dBFS
    prev_diff_dBFS = 0
    trim_ms += chunk_size
    while trim_ms + chunk_size <= duration:
        curr_dBFS = sound[trim_ms:trim_ms + chunk_size].dBFS
        curr_peak_amplitude = sound[trim_ms:trim_ms + chunk_size].max
        # print(len(sound)-trim_ms, abs(abs(prev_dBFS) - abs(curr_dBFS)),curr_dBFS, (curr_peak_amplitude/peak_amplitude), file=open(logfile,'a'))
        if not math.isinf (abs (prev_dBFS)) and not math.isinf (abs (curr_dBFS)) and not math.isnan (
                prev_dBFS) and not math.isnan (curr_dBFS):
            # print(prev_dBFS, curr_dBFS, trim_ms)
            if abs (abs (prev_dBFS) - abs (curr_dBFS)) >= diff_dBFS and curr_dBFS > min_voice_dBFS and (
                    curr_peak_amplitude / peak_amplitude) >= percentile:
                # print(len(sound)-trim_ms,"dBFSdiff:",abs(abs(prev_dBFS) - abs(curr_dBFS)),'/',diff_dBFS, "curr_dBFS:",curr_dBFS, \
                #       "min_voice_dBFS:", min_voice_dBFS,"peak_amplitude%:", (curr_peak_amplitude / peak_amplitude), \
                #       percentile, file=open(logfile, 'a'))
                return trim_ms  # return previous chunk

            if prev_diff_dBFS >= diff_dBFS and curr_dBFS > min_voice_dBFS and (
                    curr_peak_amplitude / peak_amplitude) >= percentile:
                # print(prev_diff_dBFS, diff_dBFS, curr_dBFS, min_voice_dBFS, (curr_peak_amplitude / peak_amplitude),percentile, file=open(logfile, 'a'))
                return trim_ms  # return previous chunk

        prev_diff_dBFS = abs (abs (prev_dBFS) - abs (curr_dBFS))
        prev_dBFS = curr_dBFS

        trim_ms += chunk_size

    return -1  # silence file, unvoiced file


def _internal_silence_remove(sound, start_trim, end_trim, chunk_size, silence_threshold_dBFS, logfile='stat.txt'):
    trim_ms = start_trim
    _sound = AudioSegment.empty ()
    while trim_ms + chunk_size <= end_trim:
        curr_dBFS = sound[trim_ms:trim_ms + chunk_size].dBFS
        # print(curr_dBFS,trim_ms,file=open(logfile,'a'))
        if curr_dBFS <= silence_threshold_dBFS:
            # print("Deleted: ",curr_dBFS,silence_threshold_dBFS,trim_ms, file=open(logfile,"a"))
            pass
        else:
            _sound += sound[trim_ms:trim_ms + chunk_size]

        trim_ms += chunk_size
    return _sound


def _volume_adjust(sound, min_volume_dBFS=-26.00):
    """

    :param sound: sound is a pydub.AudioSegment
    :param output_dir:
    :param min_volume_dBFS: Minimum volume level (dBFS) to match
    :return:
    """
    volume = sound.dBFS
    if volume == float ("inf") or volume == float ("-inf"):
        return "__vol_inf__", sound
    if volume < min_volume_dBFS:
        sound = sound + math.ceil (-volume + min_volume_dBFS)  # increase in volume(dBFS) by an int DB amount
    return "", sound


def _trim_silence(filepath="01.wav", output_dir="out/", output_stat='stat.txt',
                  forward_diff_dBFS=9.0, forward_min_voice_dBFS=-40.0,
                  backward_diff_dBFS=3.0, backward_min_voice_dBFS=-50.0, left_add_chunk=10, right_add_chunk=2,
                  internal_silence_threshold_dBFS=-54.00, no_word_threshold=150, chunk_size=10):
    sound = AudioSegment.from_file (filepath, format="wav")
    peak_amplitude = sound.max
    start_trim = _detect_leading_silence (sound, peak_amplitude=peak_amplitude, percentile=.1,
                                          diff_dBFS=forward_diff_dBFS, min_voice_dBFS=forward_min_voice_dBFS,
                                          chunk_size=chunk_size)
    end_trim = _detect_leading_silence (sound.reverse (), peak_amplitude=peak_amplitude, percentile=.1,
                                        diff_dBFS=backward_diff_dBFS, min_voice_dBFS=backward_min_voice_dBFS,
                                        chunk_size=chunk_size, logfile='end_trim.txt')
    # print("start_trim: ",start_trim,"end_trim: ",len(sound)-end_trim)
    if start_trim == -1 or end_trim == -1:
        print ("__silence__: ", filepath, file=open (output_stat, "a"))
    else:
        duration = len (sound)
        # print(filepath, start_trim - left_add_chunk * chunk_size, duration - end_trim + right_add_chunk * chunk_size,file=open(output_stat, "a"))
        if start_trim - left_add_chunk * chunk_size >= 0:
            start_trim = start_trim - left_add_chunk * chunk_size
        else:
            start_trim = 0

        if duration - end_trim + right_add_chunk * chunk_size <= duration:
            end_trim = duration - end_trim + right_add_chunk * chunk_size
        else:
            end_trim = duration
        # print(start_trim,end_trim)

        _dir, _filename = ntpath.split (filepath)
        # _sound = sound[start_trim:end_trim]
        _sound = _internal_silence_remove (sound, start_trim, end_trim, chunk_size,
                                           silence_threshold_dBFS=internal_silence_threshold_dBFS, logfile='isr.txt')
        __volume_inf__, _sound = _volume_adjust (sound=_sound, min_volume_dBFS=-26.00)
        if len (_sound) < no_word_threshold:
            print ("__no_word__: ", filepath, file=open (output_stat, "a"))
        elif "__vol_inf__" == __volume_inf__:
            print ("__vol_inf__: ", filepath, file=open (output_stat, "a"))
        else:
            # pass
            _sound.export (output_dir + _filename, format="wav")


def show_spectogram(filepath, title='', start_trim=0.0, end_trim=0.0, show_fig=True, show_button=True):
    '''
    Show Spectogram of the sound wav
    :return: None
    '''
    if show_fig == True:
        y_orig, sr_orig = librosa.load (filepath, sr=None, mono=False)
        audio = AudioSegment.from_file (filepath)
        # plt.figure(figsize=(20, 2))
        fig = plt.figure (figsize=(20, 2))
        ax = fig.add_subplot (1, 1, 1)
        librosa.display.waveplot (y_orig, sr=sr_orig, max_points=9000, x_axis='s')
        plt.minorticks_on ()
        major_ticks = np.arange (0, audio.duration_seconds, 0.1)
        ax.set_xticks (major_ticks)
        if start_trim != end_trim:
            plt.axvspan (start_trim, end_trim, color='red', alpha=0.5)
        plt.grid (b=True, which='major', color='#999999', linestyle='-', axis='x')
        # plt.grid(b=True)
        plt.show ()
    if show_button == True:
        with pd.option_context ('display.max_rows', 100, 'display.max_columns', 10):
            ipd.display (ipd.Audio (filepath))


def cut_wav(filepath, start_second, end_second, dest='tmp/'):
    '''
    Cutting signal based on dBFS
    '''
    _dir, _filename = ntpath.split (filepath)
    sound = pydub.AudioSegment.from_file (filepath, format="wav")
    sound = sound[start_second * 1000:end_second * 1000]
    # __volume_inf__, _sound = _volume_adjust(sound=sound, min_volume_dBFS=-26.00)
    # if "__vol_inf__" == __volume_inf__:
    #     _sound = sound
    #     print("__vol_inf__: ", filepath, file=open(output_stat, "a"))
    sound.export (dest + _filename, format="wav")
    # _sound.export(curr_dir + _filename, format="wav")


def on_next_button_clicked(b):
    global current_file
    ipd.clear_output ()
    already_checked = set (line.strip () for line in open ('tts_text/tts_already_checked.txt'))
    already_checked_length = len (already_checked)

    try:
        while True:
            current_file = (random.choice ([f for f in listdir ('your_list_of_wav_files') if isfile (join ('dir', f))]))
            if current_file not in already_checked:
                break
        orig_filepath = original_dir + current_file
        print (orig_filepath)
        if orig_filepath.endswith ('.wav'):
            mod_filepath = modified_dir + current_file
            if os.path.exists (orig_filepath) and os.path.exists (mod_filepath):
                sound = AudioSegment.from_file (orig_filepath, format="wav")
                show_spectogram (filepath=mod_filepath, show_fig=True, show_button=True, start_trim=0.0,
                                 end_trim=len (sound))
                # show_spectogram(orig_filepath,start_trim=0.0, end_trim=len(sound))

                with open ('tts_text/tts_already_checked.txt', 'a+') as f:
                    f.write (current_file + '\n')

            else:
                with open ('tts_text/tts_stat', 'a+') as f:
                    f.write ('{}, {} do not exist'.format (orig_filepath, mod_filepath) + '\n')
                print ('{}, {} do not exist'.format (orig_filepath, mod_filepath))

        ipd.display (next_button)

    except StopIteration:
        print ('Done')


def on_save_button_clicked(b):
    global current_file, temp_dir, modified_dir, curr_dir
    shutil.copy (curr_dir + temp_dir + current_file, curr_dir + modified_dir)
    os.remove (curr_dir + temp_dir + current_file)
    print (current_file, "Saved !!!")
    print (current_file, file=open ('tts_text/tts_edited', "a"))
    # os.system("cp "+temp_dir+current_file+ " "+modified_dir+current_file)
    # os.system("rm -rf "+temp_dir+current_file)


def wav_edit():
    global current_file
    start, end = input ('Give start & end second in float: ').split (' ')
    # start = input('start second in float: ')
    # end = input('end secondd in float: ')
    cut_wav (filepath=original_dir + current_file, start_second=float (start), end_second=float (end), dest=temp_dir)
    show_spectogram (filepath=temp_dir + current_file)
    save_button.on_click (on_save_button_clicked)
    ipd.display (save_button)


def on_edit_button_clicked(b):
    global current_file
    start, end = input ('Give start & end second in float: ').split (' ')
    # start = input('start second in float: ')
    # end = input('end secondd in float: ')
    cut_wav (filepath=original_dir + current_file, start_second=float (start), end_second=float (end), dest=temp_dir)
    show_spectogram (filepath=temp_dir + current_file)

    save_button.on_click (on_save_button_clicked)
    ipd.display (save_button)


def process():
    next_button.on_click (on_next_button_clicked)
    ipd.display (next_button)

# How to call for Jupyter
# import this_module as c;  c.process()
# c.wav_edit()


# How to pre-process bunch of wav files
# total_files_processed = 0
#
# for file in os.listdir (dir):
#     if os.path.isfile (out + file):
#         # print("FILE EXISTS: ", file)
#         continue
#     _trim_silence (filepath=dir + file, output_dir="out/", output_stat='stat.txt',
#                    forward_diff_dBFS=3.0, forward_min_voice_dBFS=-45.0,
#                    backward_diff_dBFS=3.0, backward_min_voice_dBFS=-50.0,
#                    internal_silence_threshold_dBFS=-51.00, left_add_chunk=10, right_add_chunk=20, chunk_size=10)
#     total_files_processed += 1
#
# print ("total_files_processed: ", total_files_processed, file=open ('total_report.txt', 'a'))
