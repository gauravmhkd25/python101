print("**************************************\n")
print(" "*10+"\033[1;34;40mCounting Vowels\033[0m \n")
print("**************************************\n")
#Header with allignment and colored text


usr_str = input("Enter a string for vowel count: ").lower()
#accepting user string and converting them to lower case

a=0
e=0
i=0
o=0
u=0
#initializing each vowel variable to 0, used to count the vowels

vowels=['a','e','i','o','u']
#list of vowels to which user string is compared

for b in usr_str:
    for j in vowels:
        if b == j:
            if j == 'a': #if char in string is a
                a+=1     #increment a with 1
            elif j == 'e':
                e+=1
            elif j == 'i':
                i+=1
            elif j == 'o':
                o+=1
            elif j == 'u':
                u+=1
#looping to compare each letter in the string with item of vowel list
#if it is a hit, the count of that particular variable is incremented 

sumV=a+e+i+o+u
#adding individual count

print("the vowels and their count: \n a = %s\n e = %s\n i = %s\n o = %s\n u = %s"%(a,e,i,o,u))
print("Total vowel count: "+sumV);
#printing the result with the count, no. of times each variable appeared in the user string
#printing total vowels present

#result: ✔
#$ py ml_2_Vowel_count.py
#**************************************

#          Counting Vowels

#**************************************

#Enter a string for vowel count: What in the world are you doing!?, Counting Vowe                  ls
#the vowels and their count:
# a = 2
# e = 3
# i = 3
# o = 5
# u = 2
#Total vowel count: 15


