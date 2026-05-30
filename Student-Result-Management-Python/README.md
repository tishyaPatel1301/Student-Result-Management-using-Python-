# 🎓 Student Result Management System — Python

A console-based application to manage student results including marks entry, grade calculation, and rank generation.  
Built using core Python concepts — no external libraries required.

---

## ✨ Features

- ➕ Add student with marks for 5 subjects
- 📋 Display all students in tabular format
- 🔍 Search student by roll number
- ✏️ Update student marks
- 🗑️ Delete student record
- 📊 Class summary (topper, average, pass/fail count)
- 🏆 Full rank list sorted by average
- 💾 Data saved to `students.json` — persists after exit

---

## 🧮 Grading System

| Average | Grade |
|---------|-------|
| 90–100  | A+    |
| 80–89   | A     |
| 70–79   | B     |
| 60–69   | C     |
| 50–59   | D     |
| Below 50| F     |

Pass criteria: Average ≥ 40

---

## 🛠️ Concepts Used

| Concept | Usage |
|---|---|
| Dictionaries | Storing student records |
| JSON file I/O | Saving and loading data |
| Functions | One function per feature |
| Loops & Conditionals | Menu logic and validation |
| List comprehensions | Summary calculations |
| `sorted()` + `lambda` | Rank list generation |

---

## ⚙️ How to Run

```bash
python main.py
```
No external libraries needed. Works with Python 3.6+

---

## 📸 Sample Output

```
----------------------------------------------------
     🎓 STUDENT RESULT MANAGEMENT SYSTEM
----------------------------------------------------
  1. Add Student
  2. Display All Students
  ...

Roll     Name                 Total    Avg      Grade    Result
----------------------------------------------------
101      Tishya Patel         432      86.4     A        PASS
102      Raj Shah             378      75.6     B        PASS
```

---

## 📂 Files

| File | Description |
|---|---|
| `main.py` | Main source code |
| `students.json` | Auto-generated data file |

---

## 👩‍💻 Author

**Tishya Patel**  
B.E. CSE | NLJIET, Ahmedabad | GTU  
🔗 [LinkedIn](https://www.linkedin.com/in/tishya-patel)
