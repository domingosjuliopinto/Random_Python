import time
process = {}
n = int(input("Enter no of processes: "))
for i in range(n):
    process[i+1] = int(input(f"Enter timestamp of process {i+1}: "))
p = list(map(int, input("Enter processes requiring shared resource: ").split(" ")))
while p!=[]:
    selected_time=99
    selected_process=-1
    for pi in p:
        if process[pi]<selected_time:
            selected_time = process[pi]
            selected_process = pi
        for i in range(n):
            if i + 1 == pi:
                continue
            print(f"Process {pi} sends timestamp({process[pi]}) to Process {i+1}")
        print()
    print(f"Process {selected_process} has lowest timestamp = {selected_time}")
    for i in range(n):
        if i + 1 == selected_process:
            continue
        print(f"Process {i+1} sends OK to Process {selected_process}")
    print(f"Process {selected_process} is accessing shared resource\n")
    time.sleep(5)
    p.remove(selected_process)
