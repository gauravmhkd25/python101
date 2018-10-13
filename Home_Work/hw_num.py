import re

pat = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
pat2 = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
with open('num.txt','r') as myfile:
    data=myfile.read()
    print("results:")
    numbers=pat.findall(data)+pat2.findall(data)

seen = set()
uniq = []

for x in numbers:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
str=''
numb=[]
for val in uniq:
    for i in val:
        if i != '-':
            str+=i
    numb.append(str)
    str=''
print(numb)

for i in numb:
    print(i)


