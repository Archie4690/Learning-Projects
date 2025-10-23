students = { 
     "Archie": 10
}

def showSummary():
    print("\n--- Student Grade Summary ---")
    for student, grade in students.items():
        print(f"{student}: {grade}")
    while True:
        moveOn = input("Return to homepage? (Y/N) ")
        if moveOn.lower().strip() == "y":
            return
        elif moveOn.lower().strip() == "n":
            showSummary()
        else:
            print("Y or N")

def removeStudent():
    studentName = input("Who do you want to remove? \n")
    if studentName in students:
        del students[studentName]
        print(f"{studentName} successfully removed. ")
    else:
        print("This is not a valid username. ")
        removeStudent()
    while True:
        moveOn = input("Return to homepage? (Y/N) ")
        if moveOn.lower().strip() == "y":
            return
        elif moveOn.lower().strip() == "n":
            removeStudent()
        else:
            print("Y or N")
        
def addStudent(students):
    studentName = input("What is the student's name? ")
    while True: 
        grade = input("And what grade did they get? ")
        if grade.isdigit():
            grade = int(grade)
            if 0 <= grade <= 100:
                students[studentName] = grade
                while True:
                    moveOn = input("Student Added successfully! Return to homepage? (Y/N) ")
                    if moveOn.lower().strip() == "y":
                        return
                    elif moveOn..strip()lower() == "n":
                        addStudent(students)
                    else:
                         print("Y or N")
            else:
                print("Please enter a grade between 0 and 100")
        else:
            print("Please enter a digit")
        

def main():
    while True:
        print("\n--- Student Grades Manager ---")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            addStudent(students)
        elif choice == "2":
            removeStudent()
        elif choice == "3":
            showSummary()
        elif choice == "4":
            quit()
        else:
            print("Invalid Option")
            return

main()