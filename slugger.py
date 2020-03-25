#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""slugger.py"""

from os import system
from platform import system as OS
import re
from sys import argv


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


def hyphenate(title):
    """Reduce [C] chars to a dash."""
    return re.sub('[ ~-]+', '-', title, flags=re.MULTILINE).strip(' -')


def filter_pullwords(title):
    """Remove words from PULLWORDS. Also removes words less than min_length,
       unless they are in EXCEPTIONS. Does not remove ints."""
    min_length = 3
    words = []
    for word in title.split():
        try:  # To preserve ints.
            words.append(str(int(word)))
        except ValueError:
            if word not in PULLWORDS:
                if len(word) >= min_length or word in EXCEPTIONS:
                    words.append(word)
    return ' '.join(words)


def slugger(title_raw):
    """Convert string of words to URL slug."""
    return hyphenate(scrub_chars(filter_pullwords(title_raw))).lower()


def copy_to_clipboard(string):
    """Copy string to system clipboard."""
    system({
        'Darwin':  f'echo "{string}" | pbcopy',
        'Linux':   f'echo "{string}" | xsel --clipboard',
        'Windows': f'echo {string}| clip',
    }[OS()])
    print(f'copied "{string}" to clipboard')


if __name__ == '__main__':
    try:  # To handle arguments.
        if argv[1] == '-r' or argv[1] == '--raw':
            print(slugger(input('Enter title: ')))
            exit(0)
    except IndexError:  # In lieu of proper arg handling...
        pass
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
