#VARIABLES
# -- Creating 2 stacks - undo_stack & redo_stack
undo_stack = []
redo_stack = []

running = True



#Adding an operation to undo_stack via append
undo_stack.append("Opened new project")

#Output
print(f"Redo Stack: {redo_stack} \nUndo Stack: {undo_stack}")

def undo():
    """If the undo stack is not empty then it removes the last item in the undo stack via pop and then adds the parameter to the end of the redo stack via append. Both stacks are then outputted"""

    if len(undo_stack) > 0:
        operation = undo_stack.pop()
        redo_stack.append(operation)
        print(f"Redo Stack: {redo_stack} \nUndo Stack: {undo_stack}\n")
    else:
        print("Sorry, the undo stack is empty")


def redo():
    """if the redo stack is not empty, it removes the last item in the redo stack via pop and then adds the parameter to the end of the undo stack via append. Both stacks are then outputted"""

    if len(redo_stack) > 0:
        operation = redo_stack.pop()
        undo_stack.append(operation)
        print(f"Redo Stack: {redo_stack} \nUndo Stack: {undo_stack}\n")
    else:
        print("Sorry, the redo stack is empty")

#The while loop will keep running until the user enters EXIT
while running == True:

    #Input from user
    user_input = input("Enter 'undo', 'redo', 'add', or 'EXIT': ")

    #Input Validation
    while user_input != "undo" and user_input != "redo" and user_input != "add" and user_input != "EXIT":
        user_input = input("That is not a valid input please enter 'undo', 'redo', 'add', or 'EXIT': ")

    #If-elif-else statements
    if user_input == "undo":

        #Run undo function w/ the operation_input as the argument
        undo()


    elif user_input == "redo":
        #Run redo function w/ the operation_input as the argument
        redo() 

    elif user_input == "add":
        #Ask the user what they want to add and the add that input to the undo stack
        operation_input = input("What operation do you want to add: ")
        undo_stack.append(operation_input)
        print(f"Redo Stack: {redo_stack} \nUndo Stack: {undo_stack}\n")


    else:
        #If EXIT was chosen running will become false meaning the while loop is no longer true and the loop will end
        running = False
        break       

    

