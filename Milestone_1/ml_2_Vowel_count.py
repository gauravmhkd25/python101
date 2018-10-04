print("**************************************\n")
print(" "*10+"\033[1;34;40mCounting Vowels\033[0m \n")
print("**************************************\n")


usrstr=input("Enter a string for vowel count: ")
usr_str=usrstr.lower()
a=0
e=0
i=0
o=0
u=0

vowels=['a','e','i','o','u']

for b in usr_str:
    for j in vowels:
        if b == j:
            if j == 'a':
                a+=1
            elif j == 'e':
                e+=1
            elif j == 'i':
                i+=1
            elif j == 'o':
                o+=1
            elif j == 'u':
                u+=1

print("the vowels and their count: \n a = %s\n e = %s\n i = %s\n o = %s\n u = %s"%(a,e,i,o,u))

