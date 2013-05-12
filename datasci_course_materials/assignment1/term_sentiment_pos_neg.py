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

def word_score(positive_tweets, negative_tweets, word):
    """
    returns count of matching positive tweets
          / count of matching negative tweets
    using 1 if either is 0
    """
    pos = len([text
            for text in positive_tweets
                if word in text])
    neg = len([text
            for text in negative_tweets
                if word in text])
    return (pos or 1) / (neg or 1)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = make_sent_dict(sent_file)

    texts = list(text_gen(tweet_file))

    positive_tweets = [text
        for text in texts
            if any(sent_scores.get(word, 0) > 0 for word in text.split())
        ]
    negative_tweets = [text
        for text in texts
            if any(sent_scores.get(word, 0) < 0 for word in text.split())
        ]

    for word in set(unknown_word_gen(sent_scores, texts)):
        score = word_score(positive_tweets, negative_tweets, word)
        print word.encode('utf-8'), score


if __name__ == '__main__':
    main()
