print("***********************************",'\n')
print(" "*10+"\033[1;34;40mPalindrome Test\033[0m\n")
print("***********************************")
usr = input("Enter a string:  ")
rev = ''
flag = False

for i in range(len(usr)-1,-1,-1):
    rev += usr[i]

print("Reverse is: ",rev,end=' ')

for i in range(len(usr)):
    if rev[i] == usr[i]:
        flag = True
    else: flag = False

if flag == False: print("which is \033[1;91;40mnot a palindrome\033[0m")
else: print("which is a \033[1;92;40mpalindrome\033[0m")
