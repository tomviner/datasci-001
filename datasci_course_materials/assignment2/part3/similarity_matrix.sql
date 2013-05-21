SELECT sum(a.count * b.count)
FROM (
    SELECT *
    FROM "Frequency"
    WHERE docid="10080_txt_crude"
    ) as a,
    (
    SELECT *
    FROM "Frequency"
    WHERE docid="17035_txt_earn"
    ) as b
WHERE a.term = b.term;
