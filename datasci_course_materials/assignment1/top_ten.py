import sys
import json
import collections


def hashtag_gen(tweet_file):
    for line in tweet_file.readlines():
        tw = json.loads(line)
        if 'delete' in tw:
            continue

        entities = tw.get('entities')
        if not entities:
            continue

        hashtags = [tag.get('text') for tag in entities.get('hashtags', [])]
        if not hashtags:
            continue

        for hashtag in hashtags:
            yield hashtag


def main():
    tweet_file = open(sys.argv[1])

    counter = collections.Counter(hashtag_gen(tweet_file))

    for tag, n in counter.most_common(10):
        print tag.encode('utf-8'), float(n)

if __name__ == '__main__':
    main()
