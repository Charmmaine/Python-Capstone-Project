# HR Insights Project 

## Overview
This project analyzes simulated HR (Human Resources) data to answer five key
business questions that real companies care about:

1. How many employees work in each department?
2. What is the average salary across the company?
3. How many employees have left the company (attrition)?
4. Are satisfied employees less likely to leave?
5. What is the salary difference between male and female employees?

Since real company HR data isn't publicly available, this project generates
**synthetic (fake) data** — 500 simulated employees — using Python. The data
isn't random for its own sake: realistic patterns are deliberately built in,
such as a gender pay gap and a link between low satisfaction and higher
attrition, so the analysis has meaningful patterns to actually uncover.

## Tools Used
- **Python** — data generation and scripting
- **SQLite** (via Python's built-in `sqlite3` module) — data storage and
  querying. No separate database installation is required.

## How It Works
1. **Generate data** — A loop creates 500 fake employees, each with a
   department, gender, salary, satisfaction score (1–5), and attrition
   status. Salary and attrition are influenced by department, tenure,
   gender, and satisfaction to simulate realistic workplace patterns.
2. **Store data** — Each employee is inserted into a SQLite database
   (`hr_data.db`) as a row in an `employees` table.
3. **Analyze data** — Instead of manual Python loops, all five insights are
   calculated using SQL queries (`SELECT`, `GROUP BY`, `COUNT`, `AVG`),
   letting the database handle the aggregation directly.
4. **Demonstrate CRUD** — The script shows all four core database
   operations:
   - **Create** — inserting new employee records
   - **Read** — querying data to generate the five insights
   - **Update** — applying a 5% raise to the HR department
   - **Delete** — removing a single employee record by ID

## Requirements
- Python 3 (no additional packages needed — `sqlite3` is built in)

## How to Run
```bash
python hr_sql.py
```

Running the script will:
- Create (or overwrite) a database file called `hr_data.db` in the same
  folder
- Print all five insights to the terminal
- Print confirmation of the Update and Delete operations

## Sample Output
```
--- 1. Headcount per Department ---
Sales: 141
Support: 102
Engineering: 100
Marketing: 72
Finance: 49
HR: 36

--- 2. Average Salary ---
$68,987.40

--- 3. Attrition ---
Left: 74 / 500 (14.8%)

--- 4. Satisfaction: Stayed vs Left ---
Stayed: 3.47 (n=426)
Left: 2.57 (n=74)

--- 5. Average Salary by Gender ---
Female: $68,168.31 (n=243)
Male: $69,761.87 (n=257)
Gap: $1,593.55
```

## Notes
- Data is regenerated from scratch every time the script runs (the table is
  dropped and rebuilt), so results are reproducible thanks to a fixed random
  seed (`random.seed(42)`).
- This project uses **synthetic data**, not real company data. It's built to
  demonstrate the analysis process, SQL querying, and CRUD operations that
  would apply to a real HR dataset.

## Possible Next Steps
- Replace the synthetic data generator with a real, cleaned HR dataset
- Add more insight queries (e.g., performance vs. salary, tenure trends)
- Connect the database to a visualization tool (e.g., a dashboard)