# HR Employee Database & Insights System

A SQL-based CRUD application built with Python and SQLite for managing
employee records and analyzing HR insights such as attrition, satisfaction,
and pay equity.

## What This Project Does
This project simulates an HR employee database and gives users full control
over the data through all four core database operations — **Create, Read,
Update, and Delete (CRUD)** — while also surfacing five key business
insights automatically calculated with SQL.

## Who Would Use This
- **HR Generalists** — create new employee records, look up individual
  employees, update details as things change
- **HR Managers / People Ops** — use the insights (attrition rate,
  satisfaction trends, headcount) to guide retention decisions
- **Compensation & Benefits teams** — review the gender pay gap insight to
  assess pay equity
- **Finance / Department Heads** — use headcount and salary data for
  budgeting and workforce planning
- **Leadership** — reviews summarized insights to inform high-level
  decisions on retention and compensation policy

## Tools Used
- **Python** — core logic and data generation
- **SQLite** (`sqlite3`, built into Python) — database storage and querying

## Project Files
| File | Description |
|---|---|
| `hr_crud_interactive.py` | Interactive CRUD system — a typed menu in the terminal lets the user Create, Read, Update, and Delete employee records one at a time. |
| `hr_sql.py` | Generates the dataset and prints the 5 key insights directly to the terminal, plus a scripted demo of Update and Delete. |
| `hr_data.db` | The SQLite database file, created automatically when either script runs. |

## How CRUD Is Implemented
- **Create** — Inserts a new employee record into the database with
  department, gender, salary, and satisfaction score provided by the user.
- **Read** — Looks up a single employee by ID, or runs SQL aggregate
  queries (`GROUP BY`, `AVG`, `COUNT`) to generate the 5 insights.
- **Update** — Modifies an existing employee's salary and/or satisfaction
  score by ID.
- **Delete** — Removes a single employee record by ID.

Every operation is backed by a real SQL statement (`INSERT`, `SELECT`,
`UPDATE`, `DELETE`) executed against the SQLite database — not just
changes held temporarily in memory.

## The 5 Key Insights
1. Headcount per department
2. Average company-wide salary
3. Attrition rate (% of employees who left)
4. Average satisfaction: employees who stayed vs. employees who left
5. Gender salary gap (average male vs. female salary)

## Requirements
Nothing extra to install — `sqlite3` and `random` are both built into
Python.

## How to Run

**Interactive CRUD menu (recommended for demonstrating CRUD):**
```bash
python hr_crud_interactive.py
```
Presents a numbered menu (1–5). Type a number, then type in the requested
details (employee ID, salary, etc.), to perform that operation live and
see the result immediately.

**Insights + scripted CRUD demo:**
```bash
python hr_sql.py
```
Generates the dataset, prints all 5 insights to the terminal, and runs one
example Update (a raise for the HR department) and one example Delete.

## Data Note
The employee data is **synthetically generated**, not pulled from a real
company. Realistic patterns are deliberately built in — such as a gender
pay gap and a link between low satisfaction and higher attrition — so the
CRUD operations and insight queries have meaningful, non-random data to
work with. A fixed random seed (`random.seed(42)`) ensures the same 500
employees are generated every time the database is rebuilt.

## Next Steps
- Replace the synthetic data generator with a real dataset (e.g. the IBM
  HR Employee Attrition dataset on Kaggle)
- Add data validation (e.g. prevent negative salaries, invalid department
  names)
- Add authentication so only authorized HR staff can perform Update/Delete