import sys
import json


def make_sent_dict(fp):
    scores = {} # initialize an empty dictionary
    for line in fp.readlines():
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def print_sents(tweet_file, sent_scores):
    for line in tweet_file.readlines():
        tw = json.loads(line)
        if 'delete' in tw:
            continue
        try:
            text = tw['text']
        except KeyError:
            # eg delete
            continue
        print sum(sent_scores.get(word, 0) for word in text.split())


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = make_sent_dict(sent_file)
    print_sents(tweet_file, sent_scores)

if __name__ == '__main__':
    main()
