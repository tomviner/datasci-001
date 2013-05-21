SELECT count(DISTINCT term)
FROM (
        SELECT *
        FROM "Frequency"
        WHERE docid="10398_txt_earn"
            AND count=1
    UNION ALL
        SELECT *
        FROM "Frequency"
        WHERE docid="925_txt_trade"
            AND count=1
);