#!python2

#number of cars
cars = 100
#passenger capacity in each car
space_in_a_car = 4.0
#no of drivers available today
drivers = 30
#Total niumber f passengers
passengers = 90
#Idle cars today
cars_not_driven = cars -  drivers
#Cars being driven today
cars_driven = drivers
#Today's car pool capacity, number of passengers that can be transported
carpool_capacity =  cars_driven * space_in_a_car
# To transport all the available paasengers, average passengers allocated to each car.
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available."
print "There are only", drivers," drivers availabale."
print "There will be", cars_not_driven," empty cars today."
print "We can transport", carpool_capacity," people today."
print "We need to put about ", average_passengers_per_car,"in each car."