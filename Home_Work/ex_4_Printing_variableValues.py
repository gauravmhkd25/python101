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
print("to drive them,",drivers," drivers arevailable.")
print("If the number of drivers are less, then",noDrive,"cars will not be driven.")
print("Today",carpool,"people can be transported.")
print("There are", passengers,"passengers to carpool today.")
print("There will be atleast",avg_passenger_per_car,"in each car.")

