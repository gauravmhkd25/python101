order = "{} {} {}".format('Gaurav','Kumar','Mahakud')
#order is tha variable which stores the formatted order

print('The name is: ',end='\n ')
print(order)
#output: Gaurav kumar Mahakud
#the same formatted order is printed

print('Printing Last name first: {2} {0} {1}'.format('Gaurav','kumar','Mahakud'),end='\n')
#output: Printing Last name first: Mahakud Gaurav kumar

print("Assigning keys to strings--a='Gaurav', b='kumar', c='Mahakud'")
#output: Assigning keys to strings--a='Gaurav', b='kumar', c='Mahakud'

key_order = "{a} {b} {c}".format(a='Gaurav',b='kumar',c='Mahakud')
print(key_order)
#output: Gaurav kumar Mahakud
