import glob
import re, os

list_mismatched_char = []

with open ('mismatched_char.txt', 'r') as f_mismatched_char:
    for char_seq in f_mismatched_char:
        list_mismatched_char.append (char_seq.strip ().split (' ', 1))


def _replace_mismatched_chars_in_file(in_file_path, out_file_path):
    try:
        os.remove (out_file_path)
    except FileNotFoundError as e:
        print (e)

    with open (in_file_path, 'r') as f_ins:
        for _ln in f_ins:
            _ln = _ln.strip ()

            if _ln:  # and len (set (_ln.split ())) > 4:
                for m_char in list_mismatched_char:
                    old_str = m_char[0]
                    new_str = m_char[1]
                    if new_str == '*':
                        _ln = _ln.replace (old_str, '')
                    elif new_str == "#-split":
                        _ll_ln = _ln.split (old_str)
                        _ln = ' | '.join (x for x in _ll_ln)
                    elif new_str == "#-1":
                        _ln = _ln.replace (old_str, 'ৌ')
                        _ln = _ln.replace ('েৌ', 'ৌ')

                    elif '$' in new_str:
                        new_str = new_str.replace ('$', ' ')
                        _ln = _ln.replace (old_str, new_str)
                    else:
                        _ln = _ln.replace (old_str, new_str)

            if _ln:  # and len (set (_ln.split ())) > 4:
                _llsp_ln = _ln.split ('|')
                for _ln_llsp_ln in _llsp_ln:
                    _ln_llsp_ln = _ln_llsp_ln.strip ()
                    _ln_sn = len (_ln_llsp_ln.split ())
                    if _ln_llsp_ln and _ln_sn > 4 and _ln_sn < 22:
                        print (_ln_llsp_ln, file=open (out_file_path, 'a'))


def _large_text_file_reader(__file_name):
    try:
        for _line in open (__file_name, "r"):
            yield _line.strip ()
    except Exception as e:
        print (e, file=open ('log_char_mismatched.txt', 'a'))
        yield (f'error')


cn = 0
for f in sorted (glob.glob ('filtered_files_dir/*.txt')):
    for line in _large_text_file_reader (f):
        if "error" in line:
            print ("error", file=open ('log_char_mismatched.txt', 'a'))
            continue
        else:
            _replace_mismatched_chars_in_file (in_file_path=f,
                                               out_file_path='char_replaced_dir/' + os.path.basename (f))
