import random
n = int(input("Enter the number of processes: "))
processes = []
prev_request = -1
for i in range(n):
    processes.append(bool(random.getrandbits(1)))
processes[n-1] = False
print("\nCo-ordinator Process: "+ str(n) +"\nCo-ordinator Process Now Dead: "+ str(n) )
request = random.randrange(n)
print(processes)
print(request)

def bully(request):
    for j in range(request + 1, n):
        print("\n\tReply from process: " + str(j+1) + " OK" if processes[j] == 1 else "")
        if processes[j]:
            request = j
            break

while(request < n - 1 and prev_request!=request):
    print("\n\nRequesting Process : " + str(request + 1))
    for i in range(request + 1, n):
        print("\n\nSending Election To : " + str(i + 1))
    print()
    prev_request = request
    bully(request)
print("Elected Co-ordinator Process : " + str((request + 1)) + " Sending Message to All Other Process....")
for i in range(n):
    print("\n\tProcess "+ str((request + 1)) + " Elected Sending To Process : " + str((i + 1)))
    print("\nAll messages sent!!!...")
