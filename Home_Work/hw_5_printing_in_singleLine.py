print("*"*35)
print(" "*5,"Concatenating strings")
print("*"*35)
s1 = 'G'
s2 = 'a'
s3 = 'u'
s4 = 'r'
s5 = 'a'
s6 = 'v'
s7 = 'M'
s8 = 'h'
s9 = 'k'
s10 = 'd'

print(s1 + s2 + s3 + s4 + s5 + s6, end = ' ')
print(s7 + s8 + s9 + s10)

print("\033[2;37;40m #The above print statement is with 'end = ' ' '\033[0;37;40m")


print(s1 + s2 + s3 + s4 + s5 + s6, end = '\n')
print(s7 + s8 + s9 + s10)

print('\033[2;37;40m #The above print statement is without "end = ' ' "\033[0;37;40m')




