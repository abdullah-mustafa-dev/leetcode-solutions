WITH all_products AS (
    -- Step 1: Get every unique product ID once
    SELECT DISTINCT product_id 
    FROM Products
),
latest_prices AS (
    -- Step 2: Get the new_price for each product on its latest valid date
    SELECT product_id, new_price
    FROM Products
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date)
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
)
-- Step 3: Join all products to their valid price, default to 10 if NULL
SELECT 
    ap.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM all_products ap
LEFT JOIN latest_prices lp ON ap.product_id = lp.product_id;