SELECT count(*)
FROM (
    SELECT SUM(count) as term_count
    FROM "Frequency"
    GROUP BY docid
    HAVING term_count > 300
);
