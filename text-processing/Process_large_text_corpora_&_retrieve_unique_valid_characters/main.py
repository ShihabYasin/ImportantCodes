# Collect all keys
import glob
import json
import os
import pandas as pd
from datasets import Dataset

all_vocab_keys = 'all_vocab_keys.txt'
text_data_chunks = 'text_data_chunks'
json_collection = 'json_collection'
filtered_files_dir = 'filtered_files_dir'


def extract_all_chars(batch):
    all_text = " ".join (batch["label"])
    vocab = list (set (all_text))
    return {"vocab": [vocab], "all_text": [all_text]}


def prepare_vocab(data_dir: str = "utt_spk_text.tsv", prefix_audio_path=None, audio_file_type: str = ".wav",
                  get_all_chars=extract_all_chars, output_json_file="vocab.json") -> dict:
    """
    Prepare the vocabulary (collection of all letters )
    """
    vocab_dict = {}
    if ".tsv" in data_dir:
        all_data = pd.read_csv (data_dir, sep='\t', header=None)
        all_data.columns = ["audio_path", "__", "label"]  # tsv file expecting in 3 colms
        all_data = all_data.drop ("__", axis=1)

        all_data['audio_path'] = all_data['audio_path'].map (lambda audio_file_name: prefix_audio_path + audio_file_name + audio_file_type)

        all_data = Dataset.from_pandas (all_data)

        vocab_all = all_data.map (get_all_chars, batched=True, batch_size=-1, keep_in_memory=True, remove_columns=all_data.column_names)
        vocab_list = sorted (list (set (vocab_all["vocab"][0])))

        vocab_dict = {v: k for k, v in enumerate (vocab_list)}

        vocab_dict["|"] = vocab_dict[" "]
        del vocab_dict[" "]

        vocab_dict["[UNK]"] = len (vocab_dict)
        vocab_dict["[PAD]"] = len (vocab_dict)

        print (vocab_dict, file=open (output_json_file, 'w'))

    elif ".txt" in data_dir:

        vocab_list = set ()

        with open (data_dir, 'r', buffering=10000) as infile:
            for line in infile:
                line = line.strip ()
                vocab_list = vocab_list.union (set (line))

        vocab_list = sorted (list (vocab_list))
        vocab_dict = {v: k for k, v in enumerate (vocab_list)}

        vocab_dict["|"] = vocab_dict[" "]
        del vocab_dict[" "]

        vocab_dict["[UNK]"] = len (vocab_dict)
        vocab_dict["[PAD]"] = len (vocab_dict)

        print (json.dumps (vocab_dict, ensure_ascii=False), file=open (output_json_file, 'w'))
        # print (vocab_dict)

    return vocab_dict


def get_all_keys_from_json_files(dir: str = None):
    _all_json_keys = set ()

    for f in sorted (glob.glob (dir + '/*.json')):
        print (f'Processed file {f}.')
        _json_keys = (json.load (open (f, "r"))).keys ()
        _all_json_keys = _all_json_keys.union (_json_keys)

    return _all_json_keys


def check_text_file_unicode_correction(file_to_check: str = 'abc.txt', filtered_files_dir: str = 'filtered_files'):
    '''
    Main idea => Remove line that contains bad characters.
    :param file_to_check:
    :param filtered_files_dir:
    :return:
    '''

    def _large_text_file_reader(__file_name):
        try:
            for _line in open (__file_name, "r"):
                yield _line.strip ()
        except Exception as e:
            print (e, open ('log_large_text_file_reader.txt', 'a'))
            yield (f'error')

    _file_object = open (os.path.join (filtered_files_dir, os.path.basename (file_to_check)), 'a')

    for line in _large_text_file_reader (file_to_check):
        if "error" in line:
            # print("error")
            continue
        # for chars in line:
        #     print (chars, end='', file=open (os.path.join (filtered_files_dir, os.path.basename (file_to_check)), 'a'))
        elif line and line.strip ():
            _file_object.write (line + '\n')
    _file_object.close ()

if __name__ == "__main__":

    # Step -1: Check for unicode character correction
    if not os.path.exists (filtered_files_dir):
        os.mkdir (filtered_files_dir)
    else:
        for __file__path in glob.glob (filtered_files_dir + '/*'):
            os.remove (os.path.join (filtered_files_dir, os.path.basename (__file__path)))

    for file_path in glob.glob (text_data_chunks + '/*'):
        check_text_file_unicode_correction (file_to_check=file_path, filtered_files_dir=filtered_files_dir)
        print (f'Unicode correction checked: {os.path.basename (file_path)}.')

    # Step -2:  Generate small vocab json files
    if os.path.exists (json_collection):
        for f in glob.glob (json_collection + '/*'):
            os.remove (f)

    cn = 0
    for f in sorted (glob.glob ('text_data_chunks/*.txt')):
        try:
            prepare_vocab (data_dir=f, prefix_audio_path="", audio_file_type=None,
                           get_all_chars=extract_all_chars, output_json_file="json_collection/chunk-vocab-" + str (cn) + ".json")
        except Exception as e:
            print (e, open ('log.txt', 'a'))
        print (f'Processed {f}.')
        cn += 1

    # Step -3:  Merge print all unique keys from all small vocab json files.
    if os.path.exists (all_vocab_keys):
        os.remove (all_vocab_keys)
    print (get_all_keys_from_json_files ('json_collection'), file=open (all_vocab_keys, 'a'))
    print (f'Find {all_vocab_keys} file.')
