-- count check
Select count(*) from `sample_ecommerce_data_csv` ;
-- checking Payment method
 select  * from `sample_ecommerce_data_csv` where `payment method` not in ('Credit Card','PayPal','Cash','Debit Card');
-- checking for null values in any ID col
-- Select count(*) from `sample_ecommerce_data_csv` where (`Customer ID`,`Transaction id`,`Product id`) is  null;
Select count(`Customer ID`,`Transaction id`,`Product id`) from `sample_ecommerce_data_csv` where (`Customer ID`,`Transaction id`,`Product id`) is  null;
 
%sql
-- Write queries to extract insights such as top-performing products on bases of Quantity sold
SELECT
    `Product ID`,SUM(`Quantity Sold`) AS Total_Quantity_Sold
FROM
    `sample_ecommerce_data_csv`
GROUP BY
  1
ORDER BY
    Total_Quantity_Sold DESC;
 
%sql
--Write queries to extract insights such as sales trends
SELECT
    DATE_TRUNC('month', `Transaction Date`) AS Month,
    SUM(`Product Price` * `Quantity Sold`) AS Monthly_Revenue,
    SUM(`Quantity Sold`) AS Monthly_Quantity_Sold
FROM
    `sample_ecommerce_data_csv`
GROUP BY
    Month
ORDER BY
    Month;
 
 
%sql
--Write queries to extract insights such as  customer behavior as per payment method
SELECT
    `Payment Method`,
    COUNT(*) AS Number_of_Transactions,
    SUM(`Product Price` * `Quantity Sold`) AS Total_Revenue
FROM
    `sample_ecommerce_data_csv`
GROUP BY
    `Payment Method`
ORDER BY
    Total_Revenue DESC;
 