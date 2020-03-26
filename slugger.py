#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""slugger.py"""

import argparse
from os import system
from platform import system as OS
from re import sub, MULTILINE
from urllib.parse import quote


# Argument handling.
parser = argparse.ArgumentParser()

parser.add_argument(
    '-d', '--delimiter',
    dest='delim',
    help='character seperating words in slug',
)

parser.add_argument(
    '-i', '--input',
    dest='input_string',
    help='input string',
)

parser.add_argument(
    '-m', '--minlen',
    dest='minlen',
    help='minimum length of words in slug',
)

parser.add_argument(
    '-r', '--raw',
    action='store_true',
    dest='raw',
    help='print raw output',
)

parser.add_argument(
    '-s', '--skip',
    action='store_true',
    dest='skip_filter',
    help='skip removal of pullwords, overrides "-m" argument',
)

parser.add_argument(
    '-u', '--url-encode',
    action='store_true',
    dest='urlencode',
    help='percent encode characters instead of stripping them',
)

args = parser.parse_args()


DELIM = args.delim if args.delim else '-'
MINLEN = args.minlen if args.minlen else 3

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


def sanitize(title):
    """Keep only [^C] chars."""
    if args.urlencode:
        return quote(title.lower())
    else:
        return sub('[^a-z0-9 ~-]', ' ', title.lower(), flags=MULTILINE)


def reduce_chars(title):
    """Reduce [C] chars to single DELIM."""
    return sub('[ ~-]+', DELIM, title, flags=MULTILINE).strip(' -' + DELIM)


def filter_pullwords(title):
    """Remove words from PULLWORDS. Also removes words less than min_length,
       unless they are in EXCEPTIONS. Does not remove ints."""
    if args.skip_filter:
        return title
    else:
        return ' '.join([
            w for w in title.split() if (
                w not in PULLWORDS and len(w) >= int(MINLEN)
            ) or (
                w in EXCEPTIONS or w.isnumeric()
            )
        ])


def slugger(title_raw):
    """Convert string of words to URL slug."""
    return reduce_chars(sanitize(filter_pullwords(title_raw)))


def copy_to_clipboard(string):
    """Copy string to system clipboard."""
    system({
        'Darwin':  f'echo "{string}" | pbcopy',
        'Linux':   f'echo "{string}" | xsel --clipboard',
        'Windows': f'echo {string}| clip',
    }[OS()])
    if not args.raw:
        print(f'copied "{string}" to clipboard')


if __name__ == '__main__':
    if args.input_string:
        if args.raw:
            print(slugger(args.input_string))
        else:
            copy_to_clipboard(slugger(args.input_string))
        exit(0)

    try:  # To handle interrupts gracefully.
        while True:
            USER_INPUT = input('Enter string: ')

            if USER_INPUT in ('exit', 'q', 'quit'):
                exit(0)
            elif USER_INPUT == '':
                pass
            else:
                copy_to_clipboard(slugger(USER_INPUT))
    except KeyboardInterrupt:
        exit(1)
