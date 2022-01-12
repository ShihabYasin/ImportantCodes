from scipy.io.wavfile import read
import soundfile as sf
import os
from pathlib import Path

'''
Check for corrupted wav data files as a pre-processing step for many speech tasks.
'''

def get_all_file_paths_with_extension(data_dir, extension):
    if not os.path.isdir (data_dir):
        return []
    data_path = Path (data_dir)
    audio_paths = list (map (str, list (data_path.glob ('*' + extension))))
    return audio_paths

def check_audio_status(audio_paths, samplerate=44100, subtype='PCM_16', channels=1):
    defected_list = []
    corrupted_list = []
    valid_audio_paths = []
    for audio_path in audio_paths:
        try:
            _, _ = read (audio_path)
            ob = sf.SoundFile (audio_path)
            if ob.samplerate == samplerate and ob.channels == channels and ob.subtype == subtype:
                valid_audio_paths.append (audio_path)
                continue
            else:
                # print(f"Defected {os.path.basename (audio_path)}, " f"sample rate: {ob.samplerate}, channels: {ob.channels}, subtype: {ob.subtype}")
                defected_list.append (os.path.basename (audio_path))
        except Exception:
            corrupted_list.append (os.path.basename (audio_path))
    # print (defected_list)
    # print (corrupted_list)
    return defected_list + corrupted_list

def get_all_folders(dirname):
    subfolders = [f.path for f in os.scandir (dirname) if f.is_dir ()]
    all_folders = []
    for dirname in list (subfolders):
        new_subfolders = [f.path for f in os.scandir (dirname) if f.is_dir ()]
        for x in new_subfolders:
            all_folders.append (x)
    return all_folders

def check(download_folder):
    for folder in get_all_folders (download_folder):
        parsed_paths = get_all_file_paths_with_extension (folder, '.wav')
        corrupted_files_list = check_audio_status (parsed_paths)
        if check_audio_status (parsed_paths):
            folder = folder.split ('/')
            folder = os.path.join (folder[-1], folder[-2])
            print (folder)
            print (corrupted_files_list)


if __name__ == '__main__':
    wav_files = '/ASR'  # folder containing wav files
    check (wav_files)
