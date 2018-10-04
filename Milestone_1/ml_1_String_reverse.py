print("*********************************************","\n")
print("\033[1;32;40m Reversing a String \033[0m\n")
print("*********************************************")

string=input("Enter a string: ")

string2=''

for i in range(len(string)-1,-1,-1):
    string2+=string[i]

print("The reversed string is: "+string2)
