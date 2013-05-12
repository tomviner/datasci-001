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

def word_score(gs, word):
    """
    returns count of matching positive tweets
          - count of matching negative tweets
    using the unit scores dict
    """
    scores = [score
        for (score, texts) in gs.items()
            for text in texts
                if word in text
                if score
        ]
    counter = collections.Counter(scores)
    return (counter[1]) / (counter[-1] or 1)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = make_sent_dict(sent_file)
    def scorer(text):
        """
        scores a given tweet by summing the scores of the words
        then returns -1, 0, 1 ie unit score regardless of magnitude.
        we define this inline so it has access to sent_scores
        """
        n = sum(sent_scores.get(word, 0) for word in text.split())
        if not n:
            return n
        return abs(n)/n

    texts = list(text_gen(tweet_file))

    # create a dict:
    #   unit score -> list of texts
    # unit scores are 1-, 0, 1
    scored_texts = collections.defaultdict(list)
    for score, ts in itertools.groupby(texts, scorer):
        scored_texts[score].extend(list(ts))

    for word in set(unknown_word_gen(sent_scores, texts)):
        print word.encode('utf-8'), word_score(scored_texts, word)

if __name__ == '__main__':
    main()
