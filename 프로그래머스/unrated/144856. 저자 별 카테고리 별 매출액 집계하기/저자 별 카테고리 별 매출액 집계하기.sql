SELECT a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY, SUM(c.SALES * a.PRICE) AS TOTAL_SALES
FROM BOOK a
JOIN AUTHOR b
ON a.AUTHOR_ID = b.AUTHOR_ID
JOIN BOOK_SALES c
ON a.BOOK_ID = c.BOOK_ID
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
GROUP BY AUTHOR_ID, AUTHOR_NAME, CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC