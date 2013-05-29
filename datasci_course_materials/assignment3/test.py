
# diff <(python inverted_index.py data/books.json) solutions/inverted_index.json

# $('body').text().match(/python \w+\.py \w+\.json/g)
name_pairs = [
    ("inverted_index", "books"),
    ("join", "records"),
    ("friend_count", "friends"),
    ("asymmetric_friendships", "friends"),
    ("unique_trims", "dna"),
    ("multiply", "matrix"),
]

for py, json in name_pairs:
    cmd = r"""
    if [ -a "{0}.py" ]
        then
        echo python {0}.py data/{1}.json
        diff \
            <(python {0}.py data/{1}.json | sort) \
            <(cat solutions/{0}.json | sort) \
        # | (head -90; tail -20)
        echo
    fi
    """.format(py, json)
    print cmd


# usage:
# python test.py | bash
# or
# watch 'python test.py | bash'

