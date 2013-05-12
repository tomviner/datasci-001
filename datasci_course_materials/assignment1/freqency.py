from __future__ import division
import sys
import json


def text_gen(tweet_file):
    for line in tweet_file.readlines():
        tw = json.loads(line)
        try:
            text = tw['text']
        except KeyError:
            # eg delete
            continue
        yield text

def term_gen(texts):
    for text in texts:
        for word in text.split():
            yield word


def main():
    tweet_file = open(sys.argv[1])
    texts = text_gen(tweet_file)
    terms = list(term_gen(texts))
    total_terms = len(terms)

    for word in set(terms):
        freq = terms.count(word) / total_terms
        print word.encode('utf-8'), freq


if __name__ == '__main__':
    main()
