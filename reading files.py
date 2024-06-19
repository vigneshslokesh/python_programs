
employee_file = open("employees.txt", "r") #opening a file
for employee in employee_file.readlines():
    print(employee)
#.readable() giving away boolean values
#getting the information from the file
#.read() reads everything
#readlines() reads in form of list
#print(employee_file.readline())
#for loop can be used to read each items in the file

employee_file.close() #closing the file

