#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser ()
    parser.add_argument ("-t1", "--Test1", nargs='?', type=str, default='Test_1', help="Test Argpass")
    parser.add_argument ("-t2", "--Test2", nargs='?', type=str, default='Test_2', help="Test Argpass")
    args = parser.parse_args ()

    while True:
        try:
            text = input ()
        except EOFError as e:
            break
        text = text + ' args: ' + args.Test1 + ' ' + args.Test2
        print (text.replace ('_', ' * '))

