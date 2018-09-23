#this program contains variable(s) associated to a person
name = 'Gaurav'
height = 1.74
age = 22

print(name,",Who is",age,"years old, is",height,'m tall')
#output: Gaurav ,Who is 22 years old, is 1.74 m tall

print("\033[2;37;40m #There are 3 variables included in the above sentence: name, age & height\033[0;37;40m")
#output: #There are 3 variables included in the above sentence: name, age & height

print("\033[2;37;40m #At the time of allocation, they hold a distinct address\033[0;37;40m")
#output:  #At the time of allocation, they hold a distinct address

print("The address allocated to \033[1;31;40m name\033[0m is:  \033[1;31;40m %s\033[0m"%(id(name)))
#output: The address allocated to  name is:   4172032

print("The address allocated to \033[1;32;40m age\033[0m is: \033[1;32;40m %s\033[0m"%(id(age)))
#output: The address allocated to  age is:  1658210272

print("The address allocated to \033[1;36;40m height\033[0m is: \033[1;36;40m %s\033[0m"%(id(height)))
#output: The address allocated to  height is:  12658064

print("If another variable holds the same value as any other variable does, then the address of both the variables will be the same")
#output: If another variable holds the same value as any other variable does, then the address of both the variables will be the same

usn = 22

print("\033[2;37;40m #Declared another variable: usn = 2\033[0;37;40m")
#output:  #Declared another variable: usn = 2

print(name,",Who is",age,"years old, is",height,'m tall and his USN is equal to his age i.e.',usn)
#output:  Gaurav ,Who is 22 years old, is 1.74 m tall and his USN is equal to his age i.e. 22

print("Here the adress allocated to '\033[1;32;40m usn\033[0m' is: \033[1;32;40m %s\033[0m"%(id(usn)),"same as '\033[1;32;40m age\033[0m' because they both contain the same value and hence no new address is allocated")
#output: Here the adress allocated to ' usn' is:  1658210272 same as ' age' because they both contain the same value and hence no new address is allocated.
