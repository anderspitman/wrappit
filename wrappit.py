#!/usr/bin/env python

import sys
import subprocess
import yaml

def run_commands(commands):
    for command in commands:
        subprocess.check_call(command.split())

if __name__ == '__main__':
    if len(sys.argv) > 2:
        config_filepath = sys.argv[1]
        command = sys.argv[2:]
        with open(config_filepath) as config_file:
            config = yaml.safe_load(config_file)

        if config['before'] is not None:
            run_commands(config['before'])
        subprocess.check_call(command)
        if config['after'] is not None:
            run_commands(config['after'])
