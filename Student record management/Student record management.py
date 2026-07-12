print("===== STUDENT RECORD MANAGEMENT =====")

students = [
    ("Khushi", 106, 99),
    ("Raj", 109, 78),
    ("Yash", 110, 89)
]

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Show Topper")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter Name: ")
        roll = int(input("Enter Roll No: "))
        marks = int(input("Enter Marks: "))

        students.append((name, roll, marks))
        print("Student Added Successfully!")

    # View Students
    elif choice == "2":
        print("\nStudent Records")
        for student in students:
            print(student)

    # Search Student
    elif choice == "3":
        search_name = input("Enter Name to Search: ")
        found = False

        for student in students:
            if student[0].lower() == search_name.lower():
                print("Student Found:", student)
                found = True
                break

        if not found:
            print("Student Not Found!")

    # Delete Student
    elif choice == "4":
        delete_name = input("Enter Name to Delete: ")
        found = False

        for student in students:
            if student[0].lower() == delete_name.lower():
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found!")

    # Show Topper
    elif choice == "5":
        topper = students[0]

        for student in students:
            if student[2] > topper[2]:
                topper = student

        print("\nTopper Details")
        print("Name :", topper[0])
        print("Roll :", topper[1])
        print("Marks:", topper[2])

    # Exit
    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")