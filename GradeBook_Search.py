#Dictionary Creation
student_grades = {"James Doe": "A", "Mary Jane": "B", "Alex Smith": "C", "Lisa Ray": "A", "John Green": "D", "Anna White": "B"}


#Functions

def search_by_name(name):
    """Checks to see if the name is in the dictionary, and if so, it returns the person's grade"""

    #Making the search case-insensitive via title()
    new_name = name.title()

    #Checking to see if the name is in the dictionary
    if new_name in student_grades:
        #outputs the corresponding grade
        print(f"\n{new_name} has the grade: {student_grades[new_name]}")
    else:
        print("\nThe student name entered does not exist.")


def search_by_grade(grade_type):
    """Adds all the names with that grade to a list and outputs all of the names as well as the number of people who have that grade."""
    
    #Creates a list of all names (keys) that have that specific grade (value) via a one-line for loop (list comprehension)
    names_with_grade = [name for name, grade in student_grades.items() if grade.upper() == grade_type.upper()] #Uses .upper as a way to make program case-insensitive

    #Checks to see if the newly created list is empty or not
    if names_with_grade:
        #Outputs all the names in the list using for loop
        print(f"\nStudents with the grade {grade_type.upper():}")
        for name in names_with_grade:
            print(f"-{name}")
        
        #Outputs how many students recieved the grade
        print(f"\nThe total number of students who recieved the grade {grade_type.upper()}: {len(names_with_grade)}")

    else:
        print("\nNo students received the grade entered.")


#Main

#While True, the program will keep repeating.

while True:

    #Prompt the teacher to search by either name or grade type. It is case-insensitive via upper()
    search_choice = input("\n\nSearch by student name (N) or grade type (G). To end the program enter 'EXIT': ").strip().upper()


    if search_choice == "N":
        #Search by student name
        name = input("Please enter the student's name: ").strip()

        #Call the function for searching by name
        search_by_name(name)

    elif search_choice == "G":
        #Search by grade type
        grade = input("Please enter the grade: ").strip()

        #Call the function for searching by grade
        search_by_grade(grade)

    elif search_choice == "EXIT":
        print("Thank you for using our program. Goodbye!")

        #End program using break
        break

    else:
        print("Invalid input. Please enter N for student name, G for grade type, or EXIT to end program")

