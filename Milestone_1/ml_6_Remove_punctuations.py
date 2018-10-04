print("*********************************************\n")
print(" "*10+"\033[1;96;40mRemoving Punctuations\033[0m \n")
print("*********************************************\n")

usr = input("\033[1;34;40mEnter a string with punctuatuions: \033[0m").lower()

punc = ['!','/','(',')',',','-','[',']','{','}',';',':','\\','<','>','.','\/','?','@','#','$','%','^','&','*','_','~']
 
string2 = ''

for letter in usr:
    if letter not in punc:
        string2 += letter

print("\n\033[1;36;40mEntered string without punctuations:\033[0m\r")
print(string2)


