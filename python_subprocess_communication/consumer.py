#!/usr/bin/env python
import sys, os, signal
from subprocess import Popen, PIPE, TimeoutExpired
import shlex

class Utility:
    def generate_Popen_cmd(command: str):
        '''
        It may not be obvious how to break a shell command into a sequence of arguments, especially in complex cases. shlex.split() can illustrate how to determine the correct tokenization for args
        :return:
        '''
        return shlex.split (command)



class Child:
    def __init__(self, run_child_command, shell=True, stdin=PIPE, stdout=PIPE, bufsize=1, preexec_fn=os.setsid):
        cmd_list = [sys.executable, '-u']
        for x in run_child_command.split (' '):
            cmd_list.append (x)

        self.child_process = Popen (cmd_list,
                                    stdin=PIPE, stdout=PIPE,
                                    bufsize=1, universal_newlines=True, preexec_fn=os.setsid)

    def is_listening(self, speech):
        '''
        child process listens to speeches you tell to it
        :param speech: anything that you tell to Child process
        :return: None
        '''
        print (speech, file=self.child_process.stdin)
        self.child_process.stdin.flush ()

    def is_talking(self):  #
        '''
        Child process talks , returns string or any returnables
        :return: anything child want to share with you
        '''
        return self.child_process.stdout.readline ().rstrip ('\n')

    def destroy(self):
        try:
            outs, errs = self.child_process.communicate (timeout=1)
        except TimeoutExpired:
            self.child_process.kill ()
            outs, errs = self.child_process.communicate ()

if __name__ == '__main__':
    c1 = Child ("child_1.py -t2 123")  # Child 1
    c2 = Child ('child_2.py -t1 abc -t2 def')  # Child 2

    while (True):
        command = input ('Input Sentence: ')
        if command == 'exit':
            c1.destroy ()
            c2.destroy ()
            break
        c1.is_listening (command)  # user is talking to c1
        c1_talk = c1.is_talking ()
        print ('c1 says: ', c1_talk)  # c1's response printing

        c2_talk = c2.is_listening (c1_talk)  # passing c1's response to c2
        print ('c2 says: ', c2.is_talking ())  # c2's response printing

