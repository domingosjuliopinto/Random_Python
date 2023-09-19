#Program for vacuum cleaner to clean between two locations
previous_locR = 'none'
previous_locL = 'none'
locR = 'dirty'
locL = 'dirty'
current_location = input("Enter starting location , right or left : ")
current_status = 'none'
loop=1

def suck(current_location):
    print("This location is dirty \nSucking the dirt from "+current_location+" location.\nThis Location is clean now")
    current_status = 'clean'
    return current_status

if(current_location == 'right') or (current_location == 'left'):
    pass
else:
    retry = 1
    while(retry == 1):
        current_location = input("You entered wrong starting location.\nRe-Enter starting location , right or left : ")
        if(current_location == 'right') or (current_location == 'left'):
            retry=0
        else:
            pass
    
while(loop==1):
    if current_location == 'right':
        current_status = locR
        previous_locR = locR
        if current_status =='dirty':
            locR = suck(current_location)
        else:
            print("This location is clean")
        print("Moving to left location\n")
        current_location='left'
        
    if current_location == 'left':
        current_status = locL
        previous_locL = locL
        if current_status =='dirty':
            locL = suck(current_location)
        else:
            print("This location is clean")
        print("Moving to right location\n")
        current_location='right'

    if  previous_locR == 'clean' and previous_locL == 'clean':
        print("Both the locations are clean.\nVacuum Cleaner is stoping")
        loop=0
