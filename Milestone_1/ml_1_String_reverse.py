print("*********************************************","\n")
print("\033[1;32;40m Reversing a String \033[0m\n")
print(" "*5+"\033[1;32;40m Reversing a String \033[0m\n")
print("*********************************************")
#Header with allignment and coloured text 

 string=input("Enter a string: ")
#prompt user for a string
 string2=''
#a string variable to store the reversed user string

 for i in range(len(string)-1,-1,-1):
    string2+=string[i]
#using reverse for loop to obtain the letters in the string from the end of it
#and appending each letter to string2

 print("The reversed string is: "+string2)
#Appending the string in string2 as the result

 #Results:✔ <same as expected>
#$ py ml_1_String_reverse.py
#*********************************************
 #             Reversing a String
 #*********************************************
#Enter a string: Chocolates
#The reversed string is: setalocohC
