students = []

while True:
    print("1.Add students")
    print("2.show students")
    print("3.exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        print("add student info")

        student_id = int(input("enter id of Student:"))
        name = input("name of the student:")
        marks = int(input("enter student marks:"))

        student = {
            "id": student_id,
            "name": name,
           "marks": marks
        }

        students.append(student)
        print("added successfully")

    elif choice == 2:
        if len(students) == 0:
            print("Students info not found")

        else:
            for student in students:
                print("id:", student["id"])
                print("name:", student["name"])
                print("marks:", student["marks"])

    elif choice == 3:
        print("program ended")
        break

    else:
        print("invalid choice")
