# Student Result Management System
# Language: Python
# Concepts: Dictionaries, File I/O (JSON), Functions, Loops
# Author: Tishya Patel | B.E. CSE | NLJIET

import json
import os

FILENAME = "students.json"

# ── File Operations ───────────────────────────────────────────
def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

# ── Helpers ───────────────────────────────────────────────────
def print_line():
    print("-" * 52)

def print_header():
    print_line()
    print("     🎓 STUDENT RESULT MANAGEMENT SYSTEM")
    print_line()

def calculate_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 50: return "D"
    else: return "F"

def calculate_result(avg):
    return "PASS" if avg >= 40 else "FAIL"

def get_subjects():
    subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
    marks = {}
    for sub in subjects:
        while True:
            try:
                m = float(input(f"  Enter marks for {sub} (0-100): "))
                if 0 <= m <= 100:
                    marks[sub] = m
                    break
                else:
                    print("  Marks must be between 0 and 100.")
            except ValueError:
                print("  Please enter a valid number.")
    return marks

# ── 1. Add Student ────────────────────────────────────────────
def add_student(data):
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ").strip()

    if roll in data:
        print(f"Student with Roll No {roll} already exists.")
        return

    name = input("Enter Student Name : ").strip()
    print("\nEnter subject marks:")
    marks = get_subjects()

    total = sum(marks.values())
    avg = total / len(marks)
    grade = calculate_grade(avg)
    result = calculate_result(avg)

    data[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": round(avg, 2),
        "grade": grade,
        "result": result
    }

    save_data(data)
    print(f"\n✅ Student '{name}' added successfully!")
    print(f"   Total: {total} | Average: {avg:.2f} | Grade: {grade} | Result: {result}")

# ── 2. Display All Students ───────────────────────────────────
def display_all(data):
    if not data:
        print("\nNo students found.")
        return

    print(f"\n{'Roll':<8} {'Name':<20} {'Total':<8} {'Avg':<8} {'Grade':<8} {'Result'}")
    print_line()
    for roll, s in data.items():
        print(f"{roll:<8} {s['name']:<20} {s['total']:<8} {s['average']:<8} {s['grade']:<8} {s['result']}")
    print(f"\nTotal students: {len(data)}")

# ── 3. Search Student ─────────────────────────────────────────
def search_student(data):
    roll = input("\nEnter Roll Number to search: ").strip()
    if roll not in data:
        print(f"No student found with Roll No: {roll}")
        return

    s = data[roll]
    print(f"\n📋 Student Details:")
    print(f"   Roll No  : {roll}")
    print(f"   Name     : {s['name']}")
    print(f"   Marks    :")
    for sub, mark in s["marks"].items():
        print(f"              {sub:<12}: {mark}")
    print(f"   Total    : {s['total']}")
    print(f"   Average  : {s['average']}")
    print(f"   Grade    : {s['grade']}")
    print(f"   Result   : {s['result']}")

# ── 4. Update Marks ───────────────────────────────────────────
def update_student(data):
    roll = input("\nEnter Roll Number to update: ").strip()
    if roll not in data:
        print(f"No student found with Roll No: {roll}")
        return

    print(f"Updating marks for: {data[roll]['name']}")
    marks = get_subjects()

    total = sum(marks.values())
    avg = total / len(marks)
    grade = calculate_grade(avg)
    result = calculate_result(avg)

    data[roll]["marks"] = marks
    data[roll]["total"] = total
    data[roll]["average"] = round(avg, 2)
    data[roll]["grade"] = grade
    data[roll]["result"] = result

    save_data(data)
    print(f"\n✅ Marks updated! New Average: {avg:.2f} | Grade: {grade} | Result: {result}")

# ── 5. Delete Student ─────────────────────────────────────────
def delete_student(data):
    roll = input("\nEnter Roll Number to delete: ").strip()
    if roll not in data:
        print(f"No student found with Roll No: {roll}")
        return

    name = data[roll]["name"]
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ")
    if confirm.lower() == "yes":
        del data[roll]
        save_data(data)
        print(f"✅ Student '{name}' deleted successfully.")
    else:
        print("Deletion cancelled.")

# ── 6. Class Summary ─────────────────────────────────────────
def class_summary(data):
    if not data:
        print("\nNo students found.")
        return

    averages = [s["average"] for s in data.values()]
    passed = sum(1 for s in data.values() if s["result"] == "PASS")
    failed = len(data) - passed

    print(f"\n📊 Class Summary:")
    print(f"   Total Students : {len(data)}")
    print(f"   Passed         : {passed}")
    print(f"   Failed         : {failed}")
    print(f"   Class Average  : {sum(averages)/len(averages):.2f}")
    print(f"   Highest Avg    : {max(averages)}")
    print(f"   Lowest Avg     : {min(averages)}")

    # topper
    topper_roll = max(data, key=lambda r: data[r]["average"])
    print(f"   Class Topper   : {data[topper_roll]['name']} (Avg: {data[topper_roll]['average']})")

# ── 7. Rank List ─────────────────────────────────────────────
def rank_list(data):
    if not data:
        print("\nNo students found.")
        return

    ranked = sorted(data.items(), key=lambda x: x[1]["average"], reverse=True)
    print(f"\n🏆 Rank List:")
    print(f"{'Rank':<6} {'Roll':<8} {'Name':<20} {'Avg':<8} {'Grade'}")
    print_line()
    for rank, (roll, s) in enumerate(ranked, 1):
        print(f"{rank:<6} {roll:<8} {s['name']:<20} {s['average']:<8} {s['grade']}")

# ── Main Menu ─────────────────────────────────────────────────
def main():
    data = load_data()

    while True:
        os.system("clear" if os.name != "nt" else "cls")
        print_header()
        print("  1. Add Student")
        print("  2. Display All Students")
        print("  3. Search Student")
        print("  4. Update Student Marks")
        print("  5. Delete Student")
        print("  6. Class Summary")
        print("  7. Rank List")
        print("  0. Exit")
        print_line()

        choice = input("  Enter choice: ").strip()

        if   choice == "1": add_student(data)
        elif choice == "2": display_all(data)
        elif choice == "3": search_student(data)
        elif choice == "4": update_student(data)
        elif choice == "5": delete_student(data)
        elif choice == "6": class_summary(data)
        elif choice == "7": rank_list(data)
        elif choice == "0":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
