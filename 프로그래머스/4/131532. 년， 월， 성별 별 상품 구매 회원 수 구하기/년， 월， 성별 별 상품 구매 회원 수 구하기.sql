# USER_INFO 테이블
# ONLINE_SALE 테이블
# 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성

SELECT 
    YEAR(SALES_DATE) AS YEAR,
    MONTH(SALES_DATE) AS MONTH,
    GENDER,
    COUNT(DISTINCT OS.USER_ID) AS USERS
FROM ONLINE_SALE OS
LEFT JOIN USER_INFO UI ON UI.USER_ID = OS.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;