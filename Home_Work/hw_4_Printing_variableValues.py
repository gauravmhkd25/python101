cars = 50 
space = 4.0
#no. of seats in a car

drivers = 30
passengers = 90
noDrive = cars - drivers
#no. of cars not driven

driven = drivers
carpool = driven * space 
avg_passenger_per_car = passengers/driven

print("Number of available cars is ",cars)
#output: Number of available cars is  50

print("to drive them,",drivers," drivers arevailable.")
#output: to drive them, 30  drivers arevailable.

print("If the number of drivers are less, then",noDrive,"cars will not be driven.")
#output: If the number of drivers are less, then 20 cars will not be driven.

print("Today",carpool,"people can be transported.")
#output: Today 120.0 people can be transported.

print("There are", passengers,"passengers to carpool today.")
#output: There are 90 passengers to carpool today.

print("There will be atleast",avg_passenger_per_car," passengers in each car.")
#output: There will be atleast 3.0 passengers in each car.
