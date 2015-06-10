#!/usr/bin/env python

import sys
import subprocess

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1:]
        subprocess.check_call(command)
        command_complete_string = "command completed: '"
        command_complete_string += ' '.join(command)
        command_complete_string += "'"
        notify_command = ['notify-send', command_complete_string]
        subprocess.check_call(notify_command)
