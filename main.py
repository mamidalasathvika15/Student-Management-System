import csv
import os
from datetime import datetime

# -----------------------------
# Enroll a new student
# -----------------------------
def enroll_student():
    file_exists = os.path.isfile("students.csv")
    
    with open("students.csv", mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["ID", "Name", "Class", "Email"])  # header

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        student_class = input("Enter Class: ")
        email = input("Enter Email: ")

        writer.writerow([student_id, name, student_class, email])
        print(f"\n✅ Student '{name}' enrolled successfully!")

# -----------------------------
# View all students
# -----------------------------
def view_students():
    if not os.path.isfile("students.csv"):
        print("\n❌ No student records found.")
        return

    with open("students.csv", mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

        if len(students) <= 1:
            print("\n📁 Student list is empty.")
            return

        print("\n📄 List of Enrolled Students:")
        print("-" * 60)
        print(f"{'ID':<10} {'Name':<20} {'Class':<10} {'Email'}")
        print("-" * 60)

        for row in students[1:]:  # Skip header
            if len(row) < 4:
                continue  # skip incomplete or empty rows
            print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10} {row[3]}")

# -----------------------------
# Mark attendance
# -----------------------------
def mark_attendance():
    if not os.path.isfile("students.csv"):
        print("❌ No students to mark attendance for.")
        return

    with open("students.csv", mode='r') as student_file:
        reader = csv.reader(student_file)
        students = list(reader)

    if len(students) <= 1:
        print("📁 No enrolled students found.")
        return

    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input == "":
        date_input = datetime.now().strftime("%Y-%m-%d")

    attendance_records = []

    print(f"\n📆 Marking attendance for {date_input}")
    print("-" * 40)
    for student in students[1:]:  # skip header
        if len(student) < 2:
            continue
        student_id = student[0]
        name = student[1]
        status = input(f"Is {name} (ID: {student_id}) present? (P/A): ").strip().upper()
        status = "Present" if status == "P" else "Absent"
        attendance_records.append([date_input, student_id, status])

    file_exists = os.path.isfile("attendance.csv")
    with open("attendance.csv", mode='a', newline='') as attendance_file:
        writer = csv.writer(attendance_file)
        if not file_exists:
            writer.writerow(["Date", "ID", "Status"])
        writer.writerows(attendance_records)

    print("\n✅ Attendance recorded successfully.")

# -----------------------------
# View attendance
# -----------------------------
def view_attendance():
    if not os.path.isfile("attendance.csv"):
        print("❌ No attendance records found.")
        return

    date_filter = input("Enter date to filter (YYYY-MM-DD) or press Enter to show all: ").strip()

    with open("attendance.csv", mode='r') as file:
        reader = csv.reader(file)
        records = list(reader)

        if len(records) <= 1:
            print("📁 No attendance data available.")
            return

        print("\n📄 Attendance Records:")
        print("-" * 50)
        print(f"{'Date':<12} {'Student ID':<12} {'Status'}")
        print("-" * 50)

        found = False
        for row in records[1:]:  # Skip header
            if len(row) < 3:
                continue
            date, student_id, status = row
            if date_filter == "" or date_filter == date:
                print(f"{date:<12} {student_id:<12} {status}")
                found = True

        if not found:
            print(f"No records found for date: {date_filter}")

# -----------------------------
# Add grades
# -----------------------------
def add_grades():
    if not os.path.isfile("students.csv"):
        print("❌ No students found to assign grades.")
        return

    student_id = input("Enter Student ID to add grades: ")

    with open("students.csv", mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

        student_exists = any(row[0] == student_id for row in students[1:] if len(row) >= 1)
        if not student_exists:
            print(f"❌ Student ID {student_id} not found.")
            return

    subject = input("Enter subject name: ")
    grade = input("Enter grade or marks: ")

    file_exists = os.path.isfile("grades.csv")
    with open("grades.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID", "Subject", "Grade"])
        writer.writerow([student_id, subject, grade])

    print(f"✅ Grade for subject '{subject}' added for Student ID {student_id}.")

# -----------------------------
# View grades
# -----------------------------
def view_grades():
    if not os.path.isfile("grades.csv"):
        print("❌ No grades recorded yet.")
        return

    student_id = input("Enter Student ID to view grades (or press Enter to view all): ").strip()

    with open("grades.csv", mode='r') as file:
        reader = csv.reader(file)
        grades = list(reader)

        if len(grades) <= 1:
            print("📁 Grade list is empty.")
            return

        print("\n📄 Grade Records:")
        print("-" * 40)
        print(f"{'Student ID':<12} {'Subject':<15} {'Grade'}")
        print("-" * 40)

        found = False
        for row in grades[1:]:  # Skip header
            if len(row) < 3:
                continue
            sid, subject, grade = row
            if student_id == "" or student_id == sid:
                print(f"{sid:<12} {subject:<15} {grade}")
                found = True

        if not found:
            print(f"No grades found for Student ID: {student_id}")

# -----------------------------
# Main menu
# -----------------------------
def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Enroll New Student")
        print("2. View All Students")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Add Grades")
        print("6. View Grades")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            enroll_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            mark_attendance()
        elif choice == '4':
            view_attendance()
        elif choice == '5':
            add_grades()
        elif choice == '6':
            view_grades()
        elif choice == '7':
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

# -----------------------------
# Run the program
# -----------------------------
if __name__ == "__main__":
    main_menu()
