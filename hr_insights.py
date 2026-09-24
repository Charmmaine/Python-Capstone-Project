import random
import sqlite3
 
random.seed(42)

conn = sqlite3.connect("hr_data.db")
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        department TEXT,
        gender TEXT,
        salary REAL,
        satisfaction INTEGER,
        left_company INTEGER
    )
""")

departments = ["Sales", "Engineering", "Support", "Marketing", "HR", "Finance"]
dept_base_salary = {"Sales": 58000, "Engineering": 92000, "Support": 48000,
                     "Marketing": 61000, "HR": 55000, "Finance": 70000}
 
print("Generating and inserting 500 employees...")
 
for i in range(500):
    dept = random.choices(departments, weights=[28, 22, 20, 12, 8, 10])[0]
    gender = random.choice(["Male", "Female"])
    tenure_years = min(int(random.expovariate(1 / 900)), 4000) / 365
 
    salary = dept_base_salary[dept] + tenure_years * 1200 + random.gauss(0, 4500)
    if gender == "Male":
        salary *= 1.06
    salary = round(max(salary, 32000), -2)
 
    satisfaction = max(1, min(5, round(random.gauss(3.4, 1.0))))
    leave_prob = {1: 0.62, 2: 0.42, 3: 0.20, 4: 0.08, 5: 0.04}[satisfaction]
    left = 1 if (random.random() < leave_prob and tenure_years > 0.2) else 0
 
    # This is the CREATE operation - INSERT adds one row to the table
    cursor.execute(
        "INSERT INTO employees (department, gender, salary, satisfaction, left_company) "
        "VALUES (?, ?, ?, ?, ?)",
        (dept, gender, salary, satisfaction, left)
    )
 
conn.commit()  # saves the inserts to the database file
print("Done.\n")
 
print("--- 1. Headcount per Department ---")
cursor.execute("""
    SELECT department, COUNT(*) as headcount
    FROM employees
    GROUP BY department
    ORDER BY headcount DESC
""")
for dept, count in cursor.fetchall():
    print(f"{dept}: {count}")
 
print("\n--- 2. Average Salary ---")
cursor.execute("SELECT AVG(salary) FROM employees")
avg_salary = cursor.fetchone()[0]
print(f"${avg_salary:,.2f}")
 
print("\n--- 3. Attrition ---")
cursor.execute("SELECT COUNT(*) FROM employees WHERE left_company = 1")
left_count = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM employees")
total_count = cursor.fetchone()[0]
print(f"Left: {left_count} / {total_count} ({left_count/total_count*100:.1f}%)")
 
print("\n--- 4. Satisfaction: Stayed vs Left ---")
cursor.execute("""
    SELECT left_company, AVG(satisfaction), COUNT(*)
    FROM employees
    GROUP BY left_company
""")
for left_flag, avg_sat, count in cursor.fetchall():
    label = "Left" if left_flag == 1 else "Stayed"
    print(f"{label}: {avg_sat:.2f} (n={count})")
 
print("\n--- 5. Average Salary by Gender ---")
cursor.execute("""
    SELECT gender, AVG(salary), COUNT(*)
    FROM employees
    GROUP BY gender
""")
gender_salaries = {}
for gender, avg_sal, count in cursor.fetchall():
    print(f"{gender}: ${avg_sal:,.2f} (n={count})")
    gender_salaries[gender] = avg_sal
gap = gender_salaries["Male"] - gender_salaries["Female"]
print(f"Gap: ${gap:,.2f}")

print("\n--- UPDATE demo: giving HR department a 5% raise ---")
cursor.execute("""
    UPDATE employees
    SET salary = salary * 1.05
    WHERE department = 'HR'
""")
conn.commit()
print(f"{cursor.rowcount} HR employees got a raise.")

print("\n--- DELETE demo: removing employee with id 1 ---")
cursor.execute("DELETE FROM employees WHERE id = 1")
conn.commit()
print(f"{cursor.rowcount} employee record deleted.")

conn.close()
print("\nAll done. Data saved in hr_data.db")