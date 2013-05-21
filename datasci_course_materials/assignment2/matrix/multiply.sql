SELECT sum(a.value * b.value)
FROM a, b
WHERE a.col_num = b.row_num
    AND a.row_num = 2
    AND b.col_num = 3
GROUP BY a.row_num, b.col_num
;