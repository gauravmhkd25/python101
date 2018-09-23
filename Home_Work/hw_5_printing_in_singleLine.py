print("*"*62)
print(" "*5,"Concatenating strings",end = '\f')
print("with escape sequence")
print("*"*62)
s1 = 'Gaurav'
s7 = 'M'
s8 = 'h'
s9 = 'k'
s10 = 'd'

print(s1, end = ' ')
print(s7 + s8 + s9 + s10)

print("\033[2;37;40m #The above print statement is with 'end = ' ' normal space'\033[0;37;40m\n")


print(s1 , end = '\n')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end =  \\n " newLine\033[0;37;40m\n')

print(s1, end = '\t')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end = \\t " tab\033[0;37;40m\n')

print(s1, end = '\a')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end = \\a " bell\033[0;37;40m\n')

print(s1, end = '\b')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end = \\b " backSpace\033[0;37;40m\n')

print(s1, end = '\f')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end = \\f " formfeed\033[0;37;40m\n')

print(s1, end = '\r')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end = \\r " carraige return\033[0;37;40m\n')

print(s1, end = '\v')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end = \\t " vertical tab\033[0;37;40m\n')

print(s1, end = '\'')
print(s7 + s8 + s9 + s10)
print('\033[2;37;40m #The above print statement is with "end = \\' " vertical tab\033[0;37;40m\n')
