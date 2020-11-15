import contextlib
import itertools
from jiwer import wer

def GT_substring_filter_from_PT_word_level():
    """See if ground text is a substring of predicted text comparing word level substring matching."""
    with open ('train_text-sorted.txt') as f1, open ('one-best-hypothesis-tri2a-training-data-sorted.txt') as f2:
        for lineno, (line1, line2) in enumerate (zip (f1, f2), 1):
            if line1 != line2:
                ground_truth = line1.strip ('\n')
                ground_truth_list = ground_truth.split (' ')[1:]
                # print(ground_truth_list)
                hypothesis = line2.strip ('\n')
                hypothesis_list = hypothesis.split (' ')[1:]
                # checking if hypothesis_list has all words of ground_truth_list
                result = all(elem in ground_truth_list for elem in hypothesis_list)
                if result:
                    # print ("Yes, hypothesis_list contains all elements in ground_truth_list")
                    pass
                else:
                    # print ("No, hypothesis_list does not contain all elements in ground_truth_list")
                    print('GT '+ ground_truth)
                    print('PT '+ hypothesis)

def GT_substring_filter_from_PT_transcription_level():
    """See if ground text is a substring of predicted text comparing phoneme-transcription level substring matching."""
    def listToString(s):
        # initialize an empty string
        str1 = ""
        # traverse in the string
        for ele in s:
            str1 += ele + ' '
            # return string
        return str1

    word_map = {}

    with open ('lexicon.txt') as lex:
        for l in lex:
            ll = l.strip ('\n')
            lll = ll.split (' ')
            word_map.update ({lll[0]: lll[1:]})

    with open ('results/1_GT_substring_filter_from_PT_using_WordMatch/one-best-hypothesis-tri2a-training-data-sorted-v1.txt') as f2:
        for line1 in f2:
            line2 = next(f2)
            if line1 != line2:
                ground_truth = line1.strip ('\n')
                ground_truth_list = ground_truth.split (' ')[1:]
                # print(ground_truth_list)
                hypothesis = line2.strip ('\n')
                hypothesis_list = hypothesis.split (' ')[1:]
                # print(hypothesis_list)

                GT = []
                PT = []
                for j in hypothesis_list:
                    if j in word_map:
                        PT = PT + word_map[j]
                    else:
                        # print ('Key not found:' + j)
                        pass
                PT_str = listToString (PT)

                for j in ground_truth_list:
                    if j in word_map:
                        GT_1_word = listToString(word_map[j])
                        if GT_1_word in PT_str:
                            pass
                        elif GT_1_word =='' or GT_1_word==' ':
                            pass
                        else:
                            # print(GT_1_word +' Not found in '+ PT_str)
                            print(line1.strip('\n'))
                            print(line2.strip('\n'))
                            break

def phoneme_transcription_based_substring_match(wer_threshold=.9):
    """Finds %WER sentences based on phonemetranscription edit distance compare"""

    def listToString(s):
        # initialize an empty string
        str1 = ""
        # traverse in the string
        for ele in s:
            str1 += ele + ' '
            # return string
        return str1

    word_map = {}

    with open ('lexicon.txt') as lex:
        for l in lex:
            ll = l.strip ('\n')
            lll = ll.split (' ')
            word_map.update ({lll[0]: lll[1:]})

    with open ('results/2_GT_substring_filter_from_PT_using_TranscriptionMatch/one-best-hypothesis-tri2a-training-data-sorted-v2.txt') as f1:
        for line1 in f1:
            line2 = next(f1)
            if line1 != line2:
                ground_truth = line1.strip ('\n')
                ground_truth_list = ground_truth.split (' ')[1:]
                # print(ground_truth_list)
                hypothesis = line2.strip ('\n')
                hypothesis_list = hypothesis.split (' ')[1:]

                GT = []
                PT = []

                for j in ground_truth_list:
                    if j in word_map:
                        GT = GT + word_map[j]
                    else:
                        # print ('Key not found:' + j)
                        pass

                for j in hypothesis_list:
                    if j in word_map:
                        PT = PT + word_map[j]
                    else:
                        # print ('Key not found:' + j)
                        pass

                error = wer (listToString (GT), listToString (PT), words_to_filter=["", " ","\n"])

                if error > wer_threshold:
                    print (line1.strip ('\n'))
                    print (line2.strip ('\n'))

def find_possible_corrupted_corpora_sentences(wer_threshold=.9):
    """
    This function will generate possible corrupted corpora sentences based on %WER threshold given.

    Give Input @current dir (sorted format)
    1. one-best-hypothesis-tri2a-training-data-sorted.txt
    2. lexicon.txt
    3. "train_text-sorted.txt
    Output:
    1. 'results/3_WERbasedFiltering/res'+ wer_threshold_str+'.txt'  << corrupted train_text prediction
    """
    import os
    os.system('rm results/1_GT_substring_filter_from_PT_using_WordMatch/one-best-hypothesis-tri2a-training-data-sorted-v1.txt')
    with open('results/1_GT_substring_filter_from_PT_using_WordMatch/one-best-hypothesis-tri2a-training-data-sorted-v1.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            GT_substring_filter_from_PT_word_level()
    os.system('rm results/2_GT_substring_filter_from_PT_using_TranscriptionMatch/one-best-hypothesis-tri2a-training-data-sorted-v2.txt')
    with open('results/2_GT_substring_filter_from_PT_using_TranscriptionMatch/one-best-hypothesis-tri2a-training-data-sorted-v2.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            GT_substring_filter_from_PT_transcription_level()

    wer_threshold_str = str(wer_threshold)[2:]
    dir = 'results/3_WERbasedFiltering/res'+ wer_threshold_str+'.txt'
    os.system("rm %s" % dir)
    with open(dir,'w') as f:
        with contextlib.redirect_stdout(f):
            phoneme_transcription_based_substring_match(wer_threshold=.95)

find_possible_corrupted_corpora_sentences(wer_threshold=.9)
exit (1)










