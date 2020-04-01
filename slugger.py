#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""slugger.py"""

import argparse
from os import system
from platform import system as OS
from re import findall, sub, MULTILINE
from urllib.parse import quote
from time import strftime as date


# Argument handling.
PARSER = argparse.ArgumentParser()

PARSER.add_argument(
    '-c', '--confirm',
    action='store_true',
    dest='confirm',
    help='prompt for confirmation when removing segments from string',
)

PARSER.add_argument(
    '-d', '--delimiter',
    dest='delim',
    help='character seperating words in slug',
)

PARSER.add_argument(
    '-i', '--input',
    dest='input_string',
    help='input string',
)

PARSER.add_argument(
    '-m', '--minlen',
    dest='minlen',
    help='minimum length of words in slug',
)

PARSER.add_argument(
    '-r', '--raw',
    action='store_true',
    dest='raw',
    help='print raw output',
)

PARSER.add_argument(
    '-s', '--skip',
    action='store_true',
    dest='skip_filter',
    help='skip removal of pullwords, overrides "-m" argument',
)

PARSER.add_argument(
    '-u', '--url-encode',
    action='store_true',
    dest='urlencode',
    help='percent encode characters instead of stripping them',
)

ARGS = PARSER.parse_args()


DELIM = ARGS.delim if ARGS.delim else '-'
MINLEN = ARGS.minlen if ARGS.minlen else 3

EXCEPTIONS = set()
PULLWORDS = set()


try:
    with open('exceptions.txt', 'r') as wordlist:
        for line in wordlist.readlines():
            EXCEPTIONS.add(line.strip())
except FileNotFoundError:
    with open('exceptions.txt', 'a') as wordlist:
        pass  # Make the file

try:
    with open('pullwords.txt', 'r') as wordlist:
        for line in wordlist.readlines():
            PULLWORDS.add(line.strip())
except FileNotFoundError:
    with open('pullwords.txt', 'a') as wordlist:
        pass  # Make the file


def expand_years(string):
    """Expand years abbreviated with an apostrophie."""
    years = findall(r"\'[0-9]{2}", string)
    if not years:
        return string
    for year in years:
        if int(year[1:3]) > int(date('%y')):
            string = sub(year, sub(r"'", '19', year), string)
        elif ARGS.confirm:
            response = input(f'Fix year "{year}": ')
            if response == '':
                string = sub(year, sub(r"'", '20', year), string)
            else:
                string = sub(year, response, string)
        else:
            string = sub(year, sub(r"'", '20', year), string)
    return string


def sanitize(string):
    """Keep only [^C] chars."""
    if ARGS.urlencode:
        return quote(string.lower())
    return sub(r'[^a-z0-9 ~-]', ' ', string.lower(), flags=MULTILINE)


def reduce_chars(string):
    """Reduce [C] chars to single DELIM."""
    return sub(r'[ ~-]+', DELIM, string, flags=MULTILINE).strip(' -' + DELIM)


def filter_pullwords(string):
    """Remove words from PULLWORDS. Also removes words less than min_length,
       unless they are in EXCEPTIONS. Does not remove ints."""
    if ARGS.skip_filter:
        return string
    elif ARGS.confirm:
        words = []
        for word in string.split():
            if (word not in PULLWORDS and len(word) >= int(MINLEN)):
                words.append(word)
            else:
                try:
                    response = input(f'Keep "{word}"? (y/n): ')
                    if response.lower()[0] == 'y':
                        words.append(word)
                except IndexError:  # Assume blank input is a yes
                    words.append(word)
        return ' '.join(words)

    return ' '.join([
        word for word in string.split() if (
            word not in PULLWORDS and len(word) >= int(MINLEN)
        ) or (
            word in EXCEPTIONS or word.isnumeric()
        )
    ])


def slugger(string_raw):
    """Convert string of words to URL slug."""
    string = sub("[']", '', expand_years(string_raw))
    string = filter_pullwords(string)
    string = sanitize(string)
    string = reduce_chars(string)
    return string


def copy_to_clipboard(string):
    """Copy string to system clipboard."""
    system({
        'Darwin':  f'echo "{string}" | pbcopy',
        'Linux':   f'echo "{string}" | xsel --clipboard',
        'Windows': f'echo {string}| clip',
    }[OS()])
    if not ARGS.raw:
        print(f'copied "{string}" to clipboard')


if __name__ == '__main__':
    if ARGS.input_string:
        if ARGS.raw:
            print(slugger(ARGS.input_string))
        else:
            copy_to_clipboard(slugger(ARGS.input_string))
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
