import json
import datetime
import time

# file to store task
Task_File= 'tasks.json'

# making the list to store the task
tasks=[]

# load task from the file
def loadtask ():
    global tasks
    try:
        with open (Task_File,'r') as file:
            tasks=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        tasks=[]

# save the file
def savetask():
    with open (Task_File,'w') as file:
        json.dump(tasks,file)
    

# for diplay the menu of the todo list
def displaymenu ():
    print("Welcome to the todo list")
    print("1) View task")
    print("2) Add task")
    print("3) Remove task")
    print("4) Update task")
    print("5) Exiting the todo application")

# for view task in todo list 
def viewtask():
    if not tasks:
        print("No task is present in the list.")
    else:
        print(f"Your task is:")
        
        for index,task in enumerate(tasks,start=1):
            task_description = f"{task['description']}" # this line extract the description of the task or assign it
            if 'time' in task:# time keywords in description
                task_description += f"(Reminder at {task['time']})"# if task has a reminder time it add a reminder time to the description
            print(f"{index}. {task_description}")
            

# for adding new task in the list 
def addtask():
    description =input("Enter the task:")
    remindertime=input("Enter reminder time (YYYY-MM-DD HH:MM) ")
    task={'description':description} # it create dictionary named task with one key-value pair: 'description' set to the user-provided description
    if remindertime:
        task['time']=remindertime #If a reminder time was provided, adds it to the task dictionary with the key 'time'
    tasks.append(task)    # add task dict to the tasks list
    print(f"Task {description} is added")
    
    
# for removing task from the list
def removetask():
    viewtask()
    try:
        task_num=int (input("Enter the task that you want to remove:"))
        if 1<= task_num <= len(tasks):  # 1<=task mean task should be atleast 1 or task_num <= len(task) it ensure that task is not greater than total task in the list
            removetask=tasks.pop(task_num-1) # it task_num -1 means list in python stared with 0 or we use this
            print(f"{removetask} is removed from your list")
        else:
            print("Invalid number ")
    except ValueError :
        print("Enter that number which is present on the list.")
        
# updating the task 
def updatetask():
    viewtask()
    try:
        
        task_num=int (input("Ente the task that you want to update:"))
        if 1<= task_num <= len(tasks):
            task=tasks[task_num-1]
            new_description = input(f"Enter new description (or press Enter to keep '{task['description']}'): ")
            if new_description:
                task['description']=new_description
            new_time = input(f"Enter new reminder time (YYYY-MM-DD HH:MM) or press Enter to keep current: ")
            if new_time:
                task['time']= new_time
            elif 'time' in task:
                del task['time']
            print(f"Task {task['description']} updated")
        else :
            print("invalid task number")
    except ValueError:
        print("Please enter a valid number")

    
# for choice 
def userchoice (choice):
    if (choice ==1):
        viewtask()
        return True
    elif choice==2:
        addtask()
        return True
    elif choice==3:
        removetask()
        return True
    elif choice==4:
        updatetask()
        return True
    elif choice==5:
        print("Exiting the todo list , Goodbye")
        return False
    else:
        print("Invalid number ")
        return True

# function to check for reminder
def checkreminder():
    now = datetime.datetime.now()
    for task in tasks:
        if 'time' in task and task['time'] != 'Notified':
            try:
                task_time = datetime.datetime.strptime(task['time'], '%Y-%m-%d %H:%M')
                if now >= task_time:
                    print(f"Reminder: {task['description']} (Reminder time was {task['time']})")
                    task['time'] = 'Notified'
                    savetask()
            except ValueError as e:
                print(f"Error parsing time for task '{task['description']}': {e}")





# main function for running whole application
def main ():
    loadtask()
    while True:
        checkreminder()
        displaymenu()
        choice=int (input("Enter your choice:"))
        if not userchoice(choice):
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
