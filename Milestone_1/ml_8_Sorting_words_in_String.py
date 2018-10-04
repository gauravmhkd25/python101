print("*"*60,end='\n')
print(" "*5+"\033[1;32;40m Sorting Words in a string Alphabetically\033[0m\n")
print("*"*60,end='\n')

usr = input("Enter a string: ").split(' ')
usr.sort()

print("Sorted words in the string: \n")
for word in usr:
    print(word,end=' ')

