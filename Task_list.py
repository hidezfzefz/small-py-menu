task_list =[]

while True:
    print("---List---Manager---")
    print("1. View list")
    print("2. add task")
    print("3. exist")

    choise = int(input("entre your choise: "))
    if choise == 1:
        if len(task_list) == 0:
            print("your list is emty")
        else: 
            for task in task_list:
                print("_ " + task)

    elif choise == 2:
       task = input("what do you want to add in the list: ")
       task_list.append(task)
       print("'" + task + "'" + "has been added!")
    elif choise == 3:
        print("exit succesfully")
        break