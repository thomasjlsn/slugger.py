#!/usr/bin/env python3
"""slugger.py"""

from os import name, system
from re import sub
from sys import argv


pullwords = []

with open('pullwords.txt', 'r') as pw:
    # populate pullwords list
    for line in pw.readlines():
        pullwords.append(line.strip())


def swap_chars(title):
    # swap [N] chars for dashes
    return sub('[~—|]', '-', title)


def scrub_chars(title):
    # keep only [^N] chars
    return sub('[^a-zA-Z0-9 ~]', '', title)


def hyphenate(title):
    # reduce [N] chars to a dash
    return sub('[ -]+', '-', title)


def filter_pullwords(title_list):
    # remove words from pullwords list
    return [x for x in title_list if x not in pullwords]


def slugger(title_raw):
    # convert string of words to URL slug
    return swap_chars(hyphenate(scrub_chars(
        ' '.join(
            filter_pullwords(
                title_raw.lower().split()))))).strip(' -')


def copy_to_clipboard(slug):
    if name == 'posix':  # Linux
        system(f'echo {slug} | xsel --clipboard')
    elif name == 'nt':  # Windows
        system(f'echo {slug} | clip')
    print(f'copied "{slug}" to clipboard')


if __name__ == '__main__':
    user_input = input('Enter title: ')
    try:
        if argv[1] == '-r' or argv[1] == '--raw':
            print(slugger(user_input))
            exit(0)
    except IndexError:
        pass  # in lieu of proper arg handling...

    copy_to_clipboard(slugger(user_input))
