from __future__ import division
import sys
import json
import itertools
import collections


def make_sent_dict(fp):
    scores = {} # initialize an empty dictionary
    for line in fp.readlines():
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def text_gen(tweet_file):
    for line in tweet_file.readlines():
        tw = json.loads(line)
        try:
            text = tw['text']
        except KeyError:
            # eg delete
            continue
        yield text

def unknown_word_gen(sent_scores, texts):
    for text in texts:
        for word in text.split():
            if word not in sent_scores:
                yield word

def word_score(text_scores, word):
    """
    returns count of matching positive tweets
          / count of matching negative tweets
    using 1 if either is 0
    """
    pos_n = neg_n = 0
    for text, is_pos, is_neg in text_scores:
        if word in text:
            pos_n += is_pos
            neg_n += is_neg
    return (pos_n or 1) / (neg_n or 1)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = make_sent_dict(sent_file)

    texts = list(text_gen(tweet_file))

    # text_scores is a list of triplets:
    # the tweet text and 2 flags
    # (text, is positive, is negative)
    # note tweets can be both positive and negative
    text_scores = [
        (
            text,
            any(sent_scores.get(word, 0) > 0 for word in text.split()),
            any(sent_scores.get(word, 0) < 0 for word in text.split()),
        )
        for text in texts
    ]

    for word in set(unknown_word_gen(sent_scores, texts)):
        score = word_score(text_scores, word)
        print word.encode('utf-8'), score


if __name__ == '__main__':
    main()
