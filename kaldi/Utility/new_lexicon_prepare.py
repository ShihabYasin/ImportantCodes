import contextlib
import itertools
from jiwer import wer

def generate_new_lex_from_threshold(wer_threshold=.9):
    """
    Read 3_WERbasedFiltering/res9.txt etc. as per threshold given. It will generate graphemes list to remove from
    original lexicon, then will generate new_lexicon.txt @results/4_new_lexicon/
    Input: @current directory.
    1. lexicon.txt
    2. train_text-sorted.txt
    3. results/3_WERbasedFiltering/res'+wer_threshold_str+'.txt'
    Output:
    1. results/4_new_lexicon/grapheme_to_remove.txt'
    2. results/4_new_lexicon/new_lexicon.txt
    """
    word_set_from_original_lexicon = [""]
    word_set_defective = [""]
    with open('train_text-sorted.txt') as lex:
        for l in lex:
            ll = l.strip('\n')
            lll = ll.split(' ')
            nl = lll[1:]
            for x in nl:
                word_set_from_original_lexicon.insert(0, x)

    word_set_from_original_lexicon_saved = word_set_from_original_lexicon.copy()
    wer_threshold_str = str(wer_threshold)[2:]
    with open('results/3_WERbasedFiltering/res'+wer_threshold_str+'.txt') as lex:
        for l in lex:
            ll = l.strip('\n')
            lll = ll.split(' ')
            nl = lll[2:]
            for x in nl:
                word_set_defective.insert(0, x)

    for x in word_set_defective:
        try:
            word_set_from_original_lexicon.remove(x)
        except:
            # print('No more removal possible, ok to go! :  '+x)
            pass

    new_list = list(set(word_set_from_original_lexicon_saved) - set(word_set_from_original_lexicon))
    import os
    os.system('rm results/4_new_lexicon/grapheme_to_remove.txt')
    with open('results/4_new_lexicon/grapheme_to_remove.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            for x in new_list:
                print(x)

    word_map = {}
    with open('results/4_new_lexicon/grapheme_to_remove.txt') as lex:
        for l in lex:
            if l is not '' or ' ' or '\n':
                l = l.strip('\n')
                word_map.update({l: 1})

    dir = 'results/4_new_lexicon/new_lexicon.txt'
    import os
    os.system("rm %s" % dir)
    with open('lexicon.txt') as lex:
        for l in lex:
            l = l.strip('\n')
            ll = l.split(' ')[0]
            if ll in word_map and word_map[ll] == 1:
                pass
            else:
                with open(dir, 'a') as f:
                    with contextlib.redirect_stdout(f):
                        print(l)

def generate_new_train_text(wer_threshold=.9):
    """
    Read 3_WERbasedFiltering/res9.txt etc. as per threshold given.
    Input: @current directory.
    1. train_text-sorted.txt
    2. results/3_WERbasedFiltering/res'+wer_threshold_str+'.txt'
    :param wer_threshold:
    :return: @current dir new_train_text.txt
    """
    wer_threshold_str = str(wer_threshold)[2:]
    with open('train_text-sorted.txt', 'r') as f0, open('new_train_text.txt','w') as f, open('results/3_WERbasedFiltering/res'+wer_threshold_str+'.txt','r') as f1:
        with contextlib.redirect_stdout(f):
            word_map = {}
            for l in f1:
                l = l.strip('\n')
                ll = l.split(' ')
                if ll[1] in word_map:
                    pass
                else:
                    word_map.update({ll[1]: 1})



            for x in f0:
                x = x.strip('\n')
                original_line = x[:]
                ind = x.split(' ')[0]
                if ind in word_map:
                    pass
                else:
                    print(original_line)
def generate_new_decode_utt2spk(wer_threshold=.9):
    """
    Read 3_WERbasedFiltering/res9.txt etc. as per threshold given.
    Input: @current directory.
    1. train_text-sorted.txt
    2. results/3_WERbasedFiltering/res'+wer_threshold_str+'.txt'
    :param wer_threshold:
    :return: @current dir new_train_text.txt
    """
    wer_threshold_str = str(wer_threshold)[2:]
    with open('decode_utt2spk', 'r') as f0, open('new_decode_utt2spk','w') as f, open('results/3_WERbasedFiltering/res'+wer_threshold_str+'.txt','r') as f1:
        with contextlib.redirect_stdout(f):
            word_map = {}
            for l in f1:
                l = l.strip('\n')
                ll = l.split(' ')
                if ll[1] in word_map:
                    pass
                else:
                    word_map.update({ll[1]: 1})

            for x in f0:
                x = x.strip('\n')
                original_line = x[:]
                ind = x.split(' ')[0]
                if ind in word_map:
                    pass
                else:
                    print(original_line)
# generate_new_lex_from_threshold(.9)
# generate_new_train_text()
# generate_new_decode_utt2spk(.9)

with open('results/3_WERbasedFiltering/res9.txt') as f:
    for x in f:
        x= x.strip('\n')
        x = x.split(' ')[1]
        print(x)

exit (1)










