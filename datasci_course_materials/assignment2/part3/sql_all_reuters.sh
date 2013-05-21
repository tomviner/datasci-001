watch -n1 '
    for f in *.sql; do
        echo "$f\n    $(sqlite3 reuters.db < $f |
            tee $(basename $f .sql).txt)";
        # sleep 10;
     done
'