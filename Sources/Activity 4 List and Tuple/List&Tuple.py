import os
import pickle

# Initialize an empty list for student records
records = []

# Function to calculate final grade (60% class standing + 40% major exam)
def calculate_final_grade(class_standing, major_exam):
    return (0.6 * class_standing) + (0.4 * major_exam)

# Menu Functions
def open_file(filename):
    global records
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            records = pickle.load(file)
        print("File loaded successfully.")
    else:
        print("File not found.")

def save_file(filename):
    with open(filename, 'wb') as file:
        pickle.dump(records, file)
    print("Records saved successfully.")

def save_as_file():
    filename = input("Enter new filename: ")
    save_file(filename)

def show_all_records():
    for record in records:
        print(record)

def order_by_last_name():
    sorted_records = sorted(records, key=lambda r: r[1][1])  # Sorting by last name
    for record in sorted_records:
        print(record)

def order_by_grade():
    sorted_records = sorted(records, key=lambda r: calculate_final_grade(r[2], r[3]), reverse=True)
    for record in sorted_records:
        print(record)

def show_student_record(student_id):
    for record in records:
        if record[0] == student_id:
            print(record)
            return
    print("Student not found.")

def add_record():
    student_id = input("Enter Student ID (6-digit number): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    record = (student_id, (first_name, last_name), class_standing, major_exam)
    records.append(record)
    print("Record added successfully.")

def edit_record(student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            print("Editing record:", record)
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record(student_id):
    global records
    records = [record for record in records if record[0] != student_id]
    print("Record deleted successfully.")

# Main Menu
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            open_file(filename)
        elif choice == '2':
            filename = input("Enter filename to save: ")
            save_file(filename)
        elif choice == '3':
            save_as_file()
        elif choice == '4':
            show_all_records()
        elif choice == '5':
            order_by_last_name()
        elif choice == '6':
            order_by_grade()
        elif choice == '7':
            student_id = input("Enter Student ID: ")
            show_student_record(student_id)
        elif choice == '8':
            add_record()
        elif choice == '9':
            student_id = input("Enter Student ID: ")
            edit_record(student_id)
        elif choice == '10':
            student_id = input("Enter Student ID: ")
            delete_record(student_id)
        elif choice == '11':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main_menu()
