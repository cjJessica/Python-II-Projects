#Importing what is needed for deques
from collections import deque

#Creating deque that has a list of tasks
task_manager_dq = deque(["Clean room", "Feed dogs", "Wash car"])
print(task_manager_dq)


#NEW TASK
print("\nBefore I can clean my room, I first need to do laundry")

# -- Adding a task to the beginning of the deque using appendleft
task_manager_dq.appendleft("Laundry")
print(task_manager_dq)


#NEW TASK
print("\nAfter I wash my car, I should go to the gas station near the car wash")

# -- Adding a task to the end of the deque using append
task_manager_dq.append("Get gas")
print(task_manager_dq)


#TASK COMPLETED
print("\n I just did the first task on my list: my laundry")

# -- Deleting the first task from deque using popleft
task_manager_dq.popleft()
print(task_manager_dq)


#TASK COMPLETED
print("\nI went out of order and fed my dogs")

# -- Deleting a specific task from deque using remove
task_manager_dq.remove("Feed dogs")
print(task_manager_dq)

