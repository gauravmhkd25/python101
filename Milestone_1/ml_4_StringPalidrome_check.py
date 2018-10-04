print("***********************************",'\n')
print(" "*10+"\033[1;34;40mPalindrome Test\033[0m\n")
print("***********************************")
#header with allignment and coloured text

usr = input("Enter a string:  ")
#accepting user string

rev = ''
#initailising a rev variable(to store reverse) to null

flag = False
#flag to indicate if the string is palindrome, initialised to Flase

for i in range(len(usr)-1,-1,-1):
    rev += usr[i]
#loop to obtain reverse of the user string

print("Reverse is: ",rev,end=' ')
#printing reversed string

for i in range(len(usr)):
    if rev[i] == usr[i]:
        flag = True #when the comparison is a hit, flag is set to true
    else: flag = False #else it is false
#comparing actual string to the reversed string

if flag == False: print("which is \033[1;91;40mnot a palindrome\033[0m") #printing not a palindrome if flag is false
else: print("which is a \033[1;92;40mpalindrome\033[0m") #printing: it is a palindrome if flag is true

    
#result:✔  
#$ py ml_4_StringPalidrome_check.py
#***********************************

#          Palindrome Test

#***********************************
#Enter a string:  Nurses run
#Reverse is:  nur sesrun which is a palindrome

#2
#***********************************

#          Palindrome Test

#***********************************
#Enter a string:  1010101
#Reverse is:  1010101 which is a palindrome

#3
#$ py ml_4_StringPalidrome_check.py
#***********************************

#          Palindrome Test

#***********************************
#Enter a string:  oporop
#Reverse is:  poropo which is not a palindrome



