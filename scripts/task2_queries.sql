
-- ApexPlanet Data Analytics Internship - Task 2
-- SQL queries for Superstore sales analysis

-- 1. View sample records
SELECT *
FROM superstore
LIMIT 10;

-- 2. Filter Technology records
SELECT order_id, product_name, sales, profit
FROM superstore
WHERE category = 'Technology'
ORDER BY sales DESC
LIMIT 10;

-- 3. Total sales by category
SELECT category, SUM(sales) AS total_sales
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 4. Category sales and profit
SELECT category,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 5. Categories with sales above 100,000
SELECT category, SUM(sales) AS total_sales
FROM superstore
GROUP BY category
HAVING SUM(sales) > 100000
ORDER BY total_sales DESC;

-- 6. Overall sales statistics
SELECT COUNT(*) AS total_records,
       SUM(sales) AS total_sales,
       AVG(sales) AS average_sales,
       MIN(sales) AS minimum_sales,
       MAX(sales) AS maximum_sales,
       SUM(profit) AS total_profit
FROM superstore;

-- 7. Monthly sales trends
SELECT strftime('%Y-%m', order_date) AS sales_month,
       SUM(sales) AS total_sales
FROM superstore
GROUP BY strftime('%Y-%m', order_date)
ORDER BY sales_month;

-- 8. Top 10 customers by revenue
SELECT customer_id, customer_name,
       SUM(sales) AS total_revenue
FROM superstore
GROUP BY customer_id, customer_name
ORDER BY total_revenue DESC
LIMIT 10;

-- 9. Product category performance
SELECT category,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit,
       COUNT(*) AS total_records
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 10. Sales above the dataset average
SELECT order_id, product_name, sales
FROM superstore
WHERE sales > (SELECT AVG(sales) FROM superstore)
ORDER BY sales DESC
LIMIT 10;

-- 11. Category sales using a CTE
WITH category_sales AS (
    SELECT category, SUM(sales) AS total_sales
    FROM superstore
    GROUP BY category
)
SELECT category, total_sales
FROM category_sales
ORDER BY total_sales DESC;

-- 12. Rank sales within each category
SELECT category, product_name, sales,
       RANK() OVER (
           PARTITION BY category
           ORDER BY sales DESC
       ) AS sales_rank
FROM superstore
LIMIT 20;

-- 13. Previous record's sales using LAG
SELECT order_date, sales,
       LAG(sales) OVER (ORDER BY order_date) AS previous_sales
FROM superstore
LIMIT 20;

-- 14. Next record's sales using LEAD
SELECT order_date, sales,
       LEAD(sales) OVER (ORDER BY order_date) AS next_sales
FROM superstore
LIMIT 20;

-- 15. Three-month moving average
WITH monthly_sales AS (
    SELECT strftime('%Y-%m', order_date) AS sales_month,
           SUM(sales) AS total_sales
    FROM superstore
    GROUP BY strftime('%Y-%m', order_date)
)
SELECT sales_month, total_sales,
       ROUND(AVG(total_sales) OVER (
           ORDER BY sales_month
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ), 2) AS moving_average
FROM monthly_sales
ORDER BY sales_month;

-- 16. Cumulative monthly sales
WITH monthly_sales AS (
    SELECT strftime('%Y-%m', order_date) AS sales_month,
           SUM(sales) AS total_sales
    FROM superstore
    GROUP BY strftime('%Y-%m', order_date)
)
SELECT sales_month, total_sales,
       SUM(total_sales) OVER (
           ORDER BY sales_month
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS cumulative_sales
FROM monthly_sales
ORDER BY sales_month;

-- 17. Repeat-month customer indicator
WITH customer_months AS (
    SELECT DISTINCT customer_id,
           strftime('%Y-%m', order_date) AS order_month
    FROM superstore
),
customer_activity AS (
    SELECT customer_id, COUNT(*) AS active_months
    FROM customer_months
    GROUP BY customer_id
)
SELECT COUNT(*) AS total_customers,
       SUM(CASE WHEN active_months > 1 THEN 1 ELSE 0 END)
           AS repeat_month_customers,
       ROUND(
           100.0 * SUM(CASE WHEN active_months > 1 THEN 1 ELSE 0 END)
           / COUNT(*), 2
       ) AS repeat_month_customer_percentage
FROM customer_activity;

-- 18. Create a reusable category sales view
CREATE VIEW IF NOT EXISTS category_sales_view AS
SELECT category,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM superstore
GROUP BY category;

-- 19. Query the category sales view
SELECT *
FROM category_sales_view
ORDER BY total_sales DESC;

-- 20. Explain a date-filtering query
EXPLAIN QUERY PLAN
SELECT order_id, order_date, sales
FROM superstore
WHERE order_date = '2025-01-01';