CREATE DATABASE telecom_db;
USE telecom_db;
select * from telecom_customers;
SELECT COUNT(*) AS total_records FROM telecom_customers;

USE telecom_db;

-- 1. Remove the partial 791-row table
DROP TABLE IF EXISTS telecom_customers;

-- 2. Create the clean table structure
CREATE TABLE telecom_customers (
    customerID VARCHAR(25) PRIMARY KEY,
    gender VARCHAR(15),
    SeniorCitizen INT,
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    tenure INT,
    PhoneService VARCHAR(10),
    MultipleLines VARCHAR(30),
    InternetService VARCHAR(25),
    OnlineSecurity VARCHAR(30),
    OnlineBackup VARCHAR(30),
    DeviceProtection VARCHAR(30),
    TechSupport VARCHAR(30),
    StreamingTV VARCHAR(30),
    StreamingMovies VARCHAR(30),
    Contract VARCHAR(25),
    PaperlessBilling VARCHAR(10),
    PaymentMethod VARCHAR(40),
    MonthlyCharges DOUBLE,
    TotalCharges DOUBLE,
    Churn VARCHAR(10)
);
SET GLOBAL local_infile = 1;


-- 3. Bulk import all 7,043 rows in < 1 second
LOAD DATA LOCAL INFILE 'D:/Codenera/Telecom_Churn_Project/Telco_Customer_Churn_Dataset.csv'
INTO TABLE telecom_customers
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- 4. Verify the exact count
SELECT COUNT(*) AS total_records FROM telecom_customers;


USE telecom_db;

SET SQL_SAFE_UPDATES = 0;
UPDATE telecom_customers SET Churn = TRIM(REPLACE(Churn, '\r', ''));
SET SQL_SAFE_UPDATES = 1;

SELECT COUNT(*) AS total_customers 
FROM telecom_customers;

SELECT Churn, COUNT(*) AS customer_count 
FROM telecom_customers 
GROUP BY Churn;

SELECT ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_bill 
FROM telecom_customers;

SELECT Churn, ROUND(AVG(MonthlyCharges), 2) AS avg_bill 
FROM telecom_customers 
GROUP BY Churn;

SELECT customerID, Contract, MonthlyCharges 
FROM telecom_customers 
ORDER BY MonthlyCharges DESC 
LIMIT 10;

SELECT Contract, COUNT(*) AS total_customers 
FROM telecom_customers 
GROUP BY Contract;

SELECT Contract, COUNT(*) AS churned_customers 
FROM telecom_customers 
WHERE Churn = 'Yes' 
GROUP BY Contract;

SELECT InternetService, COUNT(*) AS total_customers 
FROM telecom_customers 
GROUP BY InternetService;

SELECT PaymentMethod, COUNT(*) AS churned_customers 
FROM telecom_customers 
WHERE Churn = 'Yes' 
GROUP BY PaymentMethod 
ORDER BY churned_customers DESC;

SELECT Contract, ROUND(AVG(tenure), 1) AS avg_months_stayed 
FROM telecom_customers 
GROUP BY Contract;
