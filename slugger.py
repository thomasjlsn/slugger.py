#!/usr/bin/env python3
"""slugger.py"""

from os import name, system
import re
from sys import argv


PULLWORDS = []

with open('pullwords.txt', 'r') as pw:
    # Populate PULLWORDS list.
    for line in pw.readlines():
        PULLWORDS.append(line.strip())


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
    """Remove words from PULLWORDS list."""
    return [x for x in title_list if x not in PULLWORDS]


def slugger(title_raw):
    """Convert string of words to URL slug."""
    return hyphenate(swap_chars(scrub_chars(
        ' '.join(
            filter_pullwords(
                title_raw.lower().split()))))).strip(' -')


def copy_to_clipboard(slug):
    """Copy output of slugger() to system clipboard."""
    if name == 'posix':  # Linux
        system(f'echo "{slug}" | xsel --clipboard')
    elif name == 'nt':  # Windows
        system(f'echo {slug}| clip')
    print(f'copied "{slug}" to clipboard')


if __name__ == '__main__':
    try:
        while True:
            USER_INPUT = input('Enter title: ')

            if USER_INPUT in ('exit', 'q', 'quit'):
                exit(0)

            try:
                if argv[1] == '-r' or argv[1] == '--raw':
                    print(slugger(USER_INPUT))
                    exit(0)
            except IndexError:
                pass  # in lieu of proper arg handling...

            copy_to_clipboard(slugger(USER_INPUT))
    except KeyboardInterrupt:
        exit(1)
