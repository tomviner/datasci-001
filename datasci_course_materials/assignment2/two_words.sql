SELECT count(*)
FROM (
    SELECT COUNT(DISTINCT docid)
    FROM "Frequency"
    WHERE term IN ("transactions", "world")
    GROUP BY docid
    HAVING COUNT(DISTINCT term) = 2
);

-- SELECT COUNT(DISTINCT a.docid)
--     FROM Frequency as a
--     INNER JOIN
--         Frequency as b
--     ON a.docid = b.docid
--     WHERE a.term="transactions"
--         AND b.term="world"
-- ;