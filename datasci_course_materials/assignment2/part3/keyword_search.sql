DROP VIEW qwerty;

CREATE VIEW qwerty AS
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count
;

SELECT MAX(sim)
FROM (
    SELECT sum(a.count * b.count) as sim
    FROM (
        SELECT *
        FROM "qwerty"
        WHERE docid = 'q'
        ) as a,
        (
        SELECT *
        FROM "qwerty"
        ) as b
    WHERE a.term = b.term
    GROUP BY b.docid
    -- ORDER BY -sim
    -- LIMIT 1
);
