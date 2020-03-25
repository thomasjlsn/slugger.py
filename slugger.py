#!/usr/bin/env python3
"""slugger.py"""

from os import name, system
import re
from sys import argv


NIX = name == 'posix'
WIN = name == 'nt'

EXCEPTIONS = []
PULLWORDS = []


for f in ('exceptions.txt', 'pullwords.txt'):
    try:
        with open(f, 'r') as pw:
            for line in pw.readlines():
                PULLWORDS.append(line.strip())
    except FileNotFoundError:
        print(f'\nERROR: File "{f}" not found\n\nCreate it with the command:')
        if NIX:
            print(f'  touch {f}')
        elif WIN:
            print(f'  type nul > {f}')
        exit(1)


def swap_chars(title):
    """Swap [N] chars for dashes."""
    return re.sub('[~—|]', '-', title, flags=re.MULTILINE)


def scrub_chars(title):
    """Keep only [^N] chars."""
    return re.sub('[^a-zA-Z0-9 ~-]', '', title, flags=re.MULTILINE)


def hyphenate(title):
    """Reduce [N] chars to a dash."""
    return re.sub('[ -]+', '-', title, flags=re.MULTILINE)


def filter_pullwords(title_list):
    """Remove words from PULLWORDS. Also removes words less than min_length,
       unless they are in EXCEPTIONS"""
    min_length = 3

    words = []
    for w in title_list:
        try:  # Preserve ints
            words.append(str(int(w)))  # WTF python?????
        except ValueError:
            if w not in PULLWORDS:
                if len(w) >= min_length or w in EXCEPTIONS:
                    words.append(w)
    return words


def slugger(title_raw):
    """Convert string of words to URL slug."""
    return hyphenate(swap_chars(scrub_chars(
        ' '.join(
            filter_pullwords(
                title_raw.lower().split()))))).strip(' -')


def copy_to_clipboard(slug):
    """Copy output of slugger() to system clipboard."""
    if NIX:
        system(f'echo "{slug}" | xsel --clipboard')
    elif WIN:
        system(f'echo {slug}| clip')
    print(f'copied "{slug}" to clipboard')


if __name__ == '__main__':
    try:
        while True:
            USER_INPUT = input('Enter title: ')

            if USER_INPUT in ('exit', 'q', 'quit'):
                exit(0)
            elif USER_INPUT == '':
                pass
            else:
                try:
                    if argv[1] == '-r' or argv[1] == '--raw':
                        print(slugger(USER_INPUT))
                        exit(0)
                except IndexError:
                    pass  # in lieu of proper arg handling...

                copy_to_clipboard(slugger(USER_INPUT))
    except KeyboardInterrupt:
        exit(1)
