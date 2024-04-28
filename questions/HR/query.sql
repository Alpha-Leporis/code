 -- 1. Count the Employees
/*
The data for the number employed at several famous IT companes is maintained in the COMPANY table. 
Write a query to print the ID's of the companies that have more than 10000 employees. In ascending order of ID.

Input Format:
	
				COMPANY

Name 		Type			Description

ID		Integer		A company ID in the Inclusrve range [1, 1000]. This is the primary key.

Name		String		A company name. This field contains between 1 and 100 characters (inclusive).

Employees	Integer		The total number of employees in the company.


output format:
The result should contain the ID's of all the companies that have more than 10000 employees, in ascending order in the following formate:

COMPANY.ID

Sample Input:
			COMPANY
ID		NAME		EMPLOYEES
1		Adobe		28085
2		Flipkart	35543
3		Amazon		1089
4		Paytm		9982
5		Boomyshow	5589
6		oracle		4003
7		NIIT		57782
8		Samsung		2000
9		TCS		10046
10		Wipro		3500

Sample Input:
1
2
7
9
*/

-- Solution: This query selects the IDs from the COMPANY table where the number of Employees is greater than 10000.
--           It then orders the results by ID in ascending order, as required.

SELECT ID
FROM COMPANY
WHERE Employees > 10000
ORDER BY ID ASC;



/*
2. Question 2
Create a query for an online streaming service. It should return a list of clients, their number of streams, and the total amount of traffic.

The result should have the following columns: mac_address | streams |
total_traffic.

• mac_address - client MAC address
• streams - total number of streams for a specific dient
• total_ traffic - total traffic amount of all streams for a specific client

The result should be sorted in descending order by total_traffic.

Note:
• Only streams of "720p" quality or higher should be included in the result.
*/

-- Solution:

SELECT 
    mac_address,
    COUNT(*) AS streams,
    SUM(traffic_amount) AS total_traffic
FROM 
    streams_table
WHERE 
    quality >= '720p'
GROUP BY 
    mac_address
ORDER BY 
    total_traffic DESC;

/*
As part of HackerAd's advertising system analytics, they need a list of the customers who have the most failures and successes in ad campaigns.

There should be exactly two rows that contain type, customer, campaign, total.

• type contains 'success' in the first row and 'failure' in the second. These relate to events.status
• customer is the customersfirst_name and customers.last_name. separated by a single space.
• campaign is a comma-separated list of campaigns.name that are associated with the customer, ordered ascending.
• total is the number of associated events.

Report only 2 customers, the two with the most successful and the most failing campaigns.
*/

-- query solution:

SELECT c.name AS company_name, 
(c.revenue - c.expenses) AS profit
FROM comapnies c
JOIN campaigns ca ON c.id = ca.company_id
WHERE (ca.revenue - ca.expenses) > 0
ORDER BY profit DESC
LIMIT 2;

/*

A financial analysis firm is building a tool to analyze the sum of the cash flows from bond investments, Create a query to extract insights on the cash flow per investor.

The required statistics are a list of all investors and their total, minimum, maximum, and average cash flows from investments.

The result should have the following columns: email | investments |
min_case_flow | max_case_flow | avg_cash_flow.

email - investor email
investments - total number of investments by a specific investor
min_case_flow - minimum cash flow from investments for a specific investor
max_case_flow - maximum cash flow frominvestments for a specific investor
avg_cash_flow - average cash flow from investments for a specific investor.
rounded to two decimal places

The result should be sorted in ascending order by email.

Note:
• Only investors who have a total cash flow greater than 1,000,000 should be induded in the results.
*/

-- query solution:
SELECT email, COUNT(*) AS investments, 
    MIN(case_flow) AS min_case_flow,
    MAX(case_flow) AS max_case_flow, 
    ROUND(AVG(case_flow), 2) AS avg_case_flow
FROM bond_investments
GROUP BY email
ORDER BY email ASC;

/*
An online shop needs a new deal history feature. Create a query that returns a list of the top three seller profiles with the highest total deals in June, 2022.

The result should have the following columns: first_name | last_name | email | total.

• total - the total amount of all deals for a specific profile

The result should be sorted in descending order by total.

The result should be limited to the first three records.

Note:
• Only deals for June 2022 should be included in the report
*/

-- query solution:

SELECT 
    first_name,
    last_name,
    email,
    SUM(amount) AS total
FROM 
    deals
JOIN 
    sellers ON deals.seller_id = sellers.id
WHERE 
    MONTH(deal_date) = 6 AND YEAR(deal_date) = 2022
GROUP BY 
    sellers.id
ORDER BY 
    total DESC
LIMIT 3;


/*

As part of the development of the "HackerCoin" cryptocurrency exchange
platform, create a query that returns a list of Ethereum wallets and their
 balances based on transaction amounts.

Due to the dummy data nature of the development process, some wallets may end up with a negative balance. 
Be sure to exclude them from the report.

The result should have the following columns: address | transactions | balance.

• address- wallet address.
• transactions- the number of confirmed transactions in a specific wallet; a confirmed transaction 
is one with confirmations >= 10.
• balance - the sum of all the amount for all confirmed transactions in a specific wallet.

The result should be sorted in descending order by balance.

Note:
• only transactions vwth ten or more confirmations should be inclucled in the report.
• only wallets a balance greater than zero shuld be included in the result.

*/

-- query solution:

SELECT 
    w.address AS address,
    COUNT(t.wallet_id) AS transactions,
    SUM(t.amount) AS balance
FROM 
    wallets w
JOIN
    transactions t ON w.id = t.wallet_id
WHERE 
    t.confirmations >= 10
GROUP BY 
    w.address
HAVING 
    SUM(t.amount) > 0
ORDER BY 
    balance DESC;


/*

2. Youngest Employees

There are two data tables with employee information: EMPLOYEE and
EMPLOYEE_UIN. Query the tables to generate a list of all employees who are less than 25years old first in order of NAME, then of ID, both ascending. The result should include the UIN followed by the NAME.

Note: While the secondary sort is by ID. the result includes UIN but not ID.

*/

-- query Solution:

SELECT 
    EMPLOYEE_UIN.uin,
    EMPLOYEE.NAME
FROM 
    EMPLOYEE
JOIN 
    EMPLOYEE_UIN AS EMPLOYEE.ID ON EMPLOYEE.uin
WHERE
    TIMESTAMPDIFF(YEAR, EMPLOYEE.BIRTHDATE, CURDATE()) < 25
    -- TIMESTAMPDIFF(YEAR, EMPLOYEE.date_of_birth, CURDATE()) < 25
ORDER BY 
    EMPLOYEE.NAME ASC, EMPLOYEE.ID ASC;


/*
As part of HackerSniff's DPI (Deep Packet Inspection) software
analytics, a team needs a list of all the protocols for which incoming
traffic is higher than outgoing.

The result should be in the following format: protocol, traffic_in,
traffic_ out.

• Results should be sorted ascending by protocol.

*/

-- query solution:

select * from (
select protocol, max(traffic_in) as Traffic_In, max(traffic_out) as Traffic_Out from network_taffic group by protocol
) traffic where Traffic_In > Traffic_Out order by protocol asc;


/*
Return a list of all students with at least one occurrence of a backlog item.
The result should be in the following format: student.name
*/

-- query solution:

SELECT DISTINCT S.NAME FROM STUDENT S
JOIN BACKLOG B ON S.ID = B.STUDENT_ID;

/*
An MMORPG game is under development. for the profile and inventory
mechanics,it needs a query that calculates a list ot game accounts 
whose inventoty is overloaded With game items.

The result should have the following columns: username | email | items |
total_weight.
• username - account username
• email - account email address
• items - total number of items in inventory
• total_weight- total weight of items in inventory

The result should be sorted in descending order by total_weight, then in
ascending order by username.
*/

-- query solution:

SELECT 
    username,
    email,
    COUNT(item_id) AS items,
    SUM(weight) AS total_weight
FROM 
    inventory
JOIN 
    accounts ON inventory.account_id = accounts.id
GROUP BY 
    username, email
HAVING 
    total_weight > :threshold
ORDER BY 
    total_weight DESC, username ASC;


/*
Ketty gives Eve a task to generate a report
containing three columns: Name, Grade and
Mark. Ketty doesn't want the NAMES of those
students who received a grade lower than 8.
The report must be in descending order by
grade. If there is more than one student with
the same grade (8-10) assigned to them, order
those particular students by their name
alphabetically.
*/

-- query solution:

select if(grade<8,null,name),grade,mark
from students join grades
where marks between min_marks and max_marks
order by grade desc,name asc,marks asc;



/*
Create a query that returns  a list of the three  longest  incoming and outgoing calls 
Result should have columns type, fullname, phone and duration 

There are two tables contacts and calls table.

Call table has 3 columns id  type  duration.

| id | type     | duration |
|----|----------|----------|
| 1  | incoming | 120      |
| 2  | incoming | 180      |
| 3  | outgoing | 150      |
| 4  | outgoing | 200      |



Contact has 4 columns contact_id,  first_name, last_name and phone.

| contact_id | first_name | last_name | phone        |
|------------|------------|-----------|--------------|
| 1          | John       | Doe       | 123-456-7890 |
| 2          | Jane       | Smith     | 987-654-3210 |


Result:

| type     | fullname   | phone        | duration |
|----------|------------|--------------|----------|
| Incoming | John Doe   | 123-456-7890 | 180      |
| Incoming | John Doe   | 123-456-7890 | 120      |
| Outgoing | Jane Smith | 987-654-3210 | 200      |
| Outgoing | Jane Smith | 987-654-3210 | 150      |


*/

-- QUERY solution

SELECT 
    'Incoming' AS type,
    CONCAT(c.first_name, ' ', c.last_name) AS fullname,
    c.phone,
    calls.duration
FROM 
    calls
JOIN 
    contacts c ON calls.type = 'incoming' AND calls.id = c.contact_id
ORDER BY 
    calls.duration DESC
LIMIT 3

UNION

SELECT 
    'Outgoing' AS type,
    CONCAT(c.first_name, ' ', c.last_name) AS fullname,
    c.phone,
    calls.duration
FROM 
    calls
JOIN 
    contacts c ON calls.type = 'outgoing' AND calls.id = c.contact_id
ORDER BY 
    calls.duration DESC
LIMIT 3;




