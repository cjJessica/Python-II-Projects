#Class Creation
class Employee:
    def __init__(self, name, salary, employee_id):
        self._name = name
        self._salary = salary
        self._employee_id = employee_id

    #Accessor and Mutator methods using property decorators

    #--- For name attribute
    #getter function 
    @property
    def name(self):
        return self._name
    
    #setter function
    @name.setter
    def name(self, value):
        self._name = value

    #--- For salary attribute
    #getter function
    @property
    def salary(self):
        return self._salary
    
    #setter function
    @salary.setter
    def salary(self, value):
        self._salary = value

    #--- For employee_id attribute
    #getter function
    @property
    def employee_id(self):
        return self._employee_id
    
    #setter function
    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value


# Variables 
employee_list = []
system_is_running = True


# Functions for adding, viewing, updating, and removing employees
def add_employee():
    #input for Employee object
    name_input = input("\nPlease enter the name of the employee you want to add: ")
    salary_input = input("Enter their salary: ")
    id_input = input("Enter their employee id: ")

    #Loops through the employee_list to make sure that the id_input hasn't already been used
    for employee in employee_list:
        while employee.employee_id == id_input:
            id_input = input("An employee's ID must be unique, please enter a unique ID: ")

    #Adding employee instance to employee_list
    employee_list.append(Employee(name_input, salary_input, id_input))


def view_employees():
    #Looping through each employee object in employee_list, and printing out it's attributes
    for employee in employee_list:
        print(f"\nName: {employee.name} \nSalary: {employee.salary} \nEmployee ID: {employee.employee_id}")


def update_employee():

    emp_id = input("Please enter the employee ID of the employee you want to update: ")


    #Loops through employee_list to find the employee with the desired ID
    for employee in employee_list:
        if employee.employee_id == emp_id:
            print(f"\nName: {employee.name} \nSalary: {employee.salary} \nEmployee ID: {employee.employee_id}\n")
            print("--- You can now enter new details or keep them the same ---")

            #User now can update the name, salary, ID
            employee.name = input("Please enter the name of the employee: ")
            employee.salary = input("Enter their salary: ")
            emp_id_input = input("Enter their employee id: ")


            #Loops through the employee_list to see if the the user entered a new employee_id and/or that the new employee_id hasn't already been used 
            for emp in employee_list:
                while emp.employee_id == emp_id_input and emp_id_input != emp_id:
                    emp_id_input = input("An employee's ID must be unique, please enter a unique ID: ")

            #Assigns emp_id_input to the Employee attribute, employee_id
            employee.employee_id = emp_id_input


def remove_employee():

    emp_id = input("Please enter the employee ID of the employee you want to delete: ")


    #Loops through employee_list to find the employee with the desired ID
    for employee in employee_list:
        if employee.employee_id == emp_id:
            print(f"\nName: {employee.name} \nSalary: {employee.salary} \nEmployee ID: {employee.employee_id}\n")

            #Confirms if the user wants to delete the employee
            delete_confirm = input("Are you sure you want to delete this entry YES/NO? ")  

            #If yes, the employee object will be deleted from the list
            if delete_confirm == "YES":
                employee_list.remove(employee)
                print("Entry has been deleted")

            #If anything other than YES is entered, user will be taken back to the options menu
            else:
                print("No entry has been deleted.")
                return

            
# The program will keep running until user says EXIT
while system_is_running == True: 

    #Input
    user_input = input("\nIf you want to add a new employee, please type: ADD \n If you want to view all employees, type: VIEW \n If you want to update an employee's details, type: UPDATE \n If you want to remove an employee, type: REMOVE\n If you want to exit type: EXIT\n")

    #Input validation
    while user_input != "ADD" and user_input != "VIEW" and user_input != "UPDATE" and user_input != "REMOVE" and user_input != "EXIT":
        user_input = input("Please enter a valid input: ")



    # If - Elif statements based off user input
    # --- Ends program / while loop
    if user_input == "EXIT":
        break
    # --- Calls add_employee() function when user types ADD
    elif user_input == "ADD":
        add_employee()
    # --- Calls view_employees() function when user types VIEW
    elif user_input == "VIEW":
        view_employees()
    # --- Calls update_employee() function when user types UPDATE
    elif user_input == "UPDATE":
        update_employee()
    # --- Calls remove_employee() function when user types REMOVE
    elif user_input == "REMOVE":
        remove_employee()



