import sys
import json
import collections


STATES = (
    ('Alabama', 'AL'),
    ('Alaska', 'AK'),
    ('Arizona', 'AZ'),
    ('Arkansas', 'AR'),
    ('California', 'CA'),
    ('Colorado', 'CO'),
    ('Connecticut', 'CT'),
    ('Delaware', 'DE'),
    ('Florida', 'FL'),
    ('Georgia', 'GA'),
    ('Hawaii', 'HI'),
    ('Idaho', 'ID'),
    ('Illinois', 'IL'),
    ('Indiana', 'IN'),
    ('Iowa', 'IA'),
    ('Kansas', 'KS'),
    ('Kentucky', 'KY'),
    ('Louisiana', 'LA'),
    ('Maine', 'ME'),
    ('Maryland', 'MD'),
    ('Massachusetts', 'MA'),
    ('Michigan', 'MI'),
    ('Minnesota', 'MN'),
    ('Mississippi', 'MS'),
    ('Missouri', 'MO'),
    ('Montana', 'MT'),
    ('Nebraska', 'NE'),
    ('Nevada', 'NV'),
    ('New Hampshire', 'NH'),
    ('New Jersey', 'NJ'),
    ('New Mexico', 'NM'),
    ('New York', 'NY'),
    ('North Carolina', 'NC'),
    ('North Dakota', 'ND'),
    ('Ohio', 'OH'),
    ('Oklahoma', 'OK'),
    ('Oregon', 'OR'),
    ('Pennsylvania', 'PA'),
    ('Rhode Island', 'RI'),
    ('South Carolina', 'SC'),
    ('South Dakota', 'SD'),
    ('Tennessee', 'TN'),
    ('Texas', 'TX'),
    ('Utah', 'UT'),
    ('Vermont', 'VT'),
    ('Virginia', 'VA'),
    ('Washington', 'WA'),
    ('West Virginia', 'WV'),
    ('Wisconsin', 'WI'),
    ('Wyoming', 'WY'),
)


def make_sent_dict(fp):
    scores = {} # initialize an empty dictionary
    for line in fp.readlines():
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def state_score_gen(tweet_file, sent_scores):
    for line in tweet_file.readlines():
        tw = json.loads(line)
        if 'delete' in tw:
            continue
        text = tw.get('text')
        place = tw.get('place')

        if not text or not place:
            continue

        country = place.get('country')
        addr = place.get('full_name')

        if country != "United States" or not addr:
            continue

        for state, code in STATES:
            if state.lower() in addr.lower() or addr.endswith(' ' + code):
                score = sum(sent_scores.get(word, 0) for word in text.split())
                yield code, score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = make_sent_dict(sent_file)

    scores = collections.defaultdict(int)

    for code, score in state_score_gen(tweet_file, sent_scores):
        scores[code] += score

    best_state_code, score = max(scores.items(), key=lambda x:x[1])
    print best_state_code

if __name__ == '__main__':
    main()
