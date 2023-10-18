# Menu driven program to implement queue
queue = []
while True:
    choice = int(input('''Menu: 1.Enque 2.Deque 3.Peek 4.Exit
Enter Choice: '''))
    if choice == 1:
        data = input("Enter data to enque: ")
        queue.append(data)
        print(queue)
    elif choice == 2:
        if queue == []:
            print("Underflow!! condition")
        else:
            queue.pop(0)
            print("Element removed!")
            print(queue)
    elif choice == 3:
        if queue == []:
            print("Underflow!! condition")
        else:
            print(str(queue[0]) + " is at front")
    elif choice == 4:
        break
