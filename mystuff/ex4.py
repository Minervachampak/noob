#The cars
cars = 100
#Space in a car is to be defined
space_in_a_car = 4.0
#total number of drivers
drivers = 30
#The total passengers
passengers = 90
#cars_not_driven defined
cars_not_driven = cars - drivers
#1 car per driver
cars_driven = drivers
#total capacity
carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers/cars_driven

#print in a desired format
print"There are %d cars available" % cars
print"There are only",drivers,"drivers available"
print"There will be",cars_not_driven,"empty cars today"
print"We can transport",carpool_capacity,"people today"
print"We have",passengers,"to carpool today"
print"We need to put about",average_passengers_per_car,"in each car."
