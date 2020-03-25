#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""slugger.py"""

import argparse
from os import system
from platform import system as OS
import re
from sys import argv


# Argument handling.
parser = argparse.ArgumentParser()

parser.add_argument(
    # Handled in __main__
    '-r', '--raw',
    action='store_true',
    dest='raw',
    help='print raw output',
)

parser.add_argument(
    '-d', '--delimiter',
    dest='delim',
    help='character seperating words',
)

args = parser.parse_args()

if args.delim:
    DELIM = args.delim
else:
    DELIM = '-'


EXCEPTIONS = []
PULLWORDS = []


for file in ('exceptions.txt', 'pullwords.txt'):
    try:  # To read config files.
        with open(file, 'r') as wordlist:
            for line in wordlist.readlines():
                PULLWORDS.append(line.strip())
    except FileNotFoundError:
        print(f'\nERROR: File "{file}" not found\n\nCreate it with the command:')
        print({
            'Darwin':  f'  touch {file}',
            'Linux':   f'  touch {file}',
            'Windows': f'  type nul > {file}',
        }[OS()])
        exit(1)


def scrub_chars(title):
    """Keep only [^C] chars."""
    return re.sub('[^a-zA-Z0-9 ~-]', ' ', title, flags=re.MULTILINE)


def reduce_chars(title):
    """Reduce [C] chars to single DELIM. Uses 0th index in case DELIM is
       provided as multi-char string"""
    return re.sub('[ ~-]+', DELIM[0], title, flags=re.MULTILINE).strip(' -')


def filter_pullwords(title):
    """Remove words from PULLWORDS. Also removes words less than min_length,
       unless they are in EXCEPTIONS. Does not remove ints."""
    min_length = 3
    words = []
    for word in title.split():
        if word.isnumeric():
            words.append(word)
        elif word not in PULLWORDS:
            if len(word) >= min_length or word in EXCEPTIONS:
                words.append(word)
    return ' '.join(words)


def slugger(title_raw):
    """Convert string of words to URL slug."""
    return reduce_chars(scrub_chars(filter_pullwords(title_raw))).lower()


def copy_to_clipboard(string):
    """Copy string to system clipboard."""
    system({
        'Darwin':  f'echo "{string}" | pbcopy',
        'Linux':   f'echo "{string}" | xsel --clipboard',
        'Windows': f'echo {string}| clip',
    }[OS()])
    print(f'copied "{string}" to clipboard')


if __name__ == '__main__':
    if args.raw:
        print(slugger(input('Enter title: ')))
        exit(0)

    try:  # To handle interrupts gracefully.
        while True:
            USER_INPUT = input('Enter title: ')

            if USER_INPUT in ('exit', 'q', 'quit'):
                exit(0)
            elif USER_INPUT == '':
                pass
            else:
                copy_to_clipboard(slugger(USER_INPUT))
    except KeyboardInterrupt:
        exit(1)
