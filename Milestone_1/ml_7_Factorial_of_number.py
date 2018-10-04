print("*"*40,'\n')
print(" "*10+"\033[1;34;40mFactorial of a number\033[0m\n")
print("*"*40)

num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i

print("\nThe Factorial of the number is: ",fact)

print("\n")

