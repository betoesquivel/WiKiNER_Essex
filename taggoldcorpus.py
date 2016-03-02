#!/usr/bin/env python
import nltk

def get_tokens_from_CONLL_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    tokens = [line.strip().split(' ')[0] for line in lines
              if line.strip() is not ""]
    return tokens

def print_and_add_tags_to_CONLL_file(tags, filename):
    f = open(filename, 'r')
    lines = f.readlines()
    for t, line in zip(tags, lines):
        if line.strip() is not '':
            print "{0} {1} {2}".format(t[0], t[1],
                                    line.strip().split(' ')[1])
        else:
            print ''

if __name__ == '__main__':
    tokens = get_tokens_from_CONLL_file('wikigold.conll.singledoc.txt')
    tagged_tokens = nltk.pos_tag(tokens)
    print_and_add_tags_to_CONLL_file(tagged_tokens, 'wikigold.conll.singledoc.txt')
