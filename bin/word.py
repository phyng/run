# coding: utf-8

import sh
import re
import os
import requests
from pyquery import PyQuery as pq


class Word(object):
    """
    Word help:
        word generate
    """
    def __init__(self):
        pass

    def get_system_dict(self):
        path = '/usr/share/dict/american-english'
        with open(path) as f:
            words = f.read().split('\n')
        return set(words)

    def generate(self, *args):
        url = args[0]
        document = pq(url)
        text = document.text()
        words = list(re.findall(r'[a-zA-Z]+', text))
        words = set([i.lower() for i in words])
        words = self.get_system_dict() & words
        print len(words)

def main(*args):
    word = Word()
    if args and hasattr(word, args[0]):
        getattr(word, args[0])(*args[1:])
    else:
        print help(word)


if __name__ == '__main__':
    word = Word()
    word.generate()
