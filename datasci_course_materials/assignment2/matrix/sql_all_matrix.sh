watch -n1 '
    for f in *.sql; do
        echo "$f\n    $(sqlite3 matrix.db < $f |
            tee $(basename $f .sql).txt)";
     done
'