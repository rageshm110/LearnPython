#!python2

name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "Oops you don't undersatnd inches, then it's %d centimeters" % (height * 2.54)
print "He's %d pounds heavy. that is ~%d kgs" % (weight, round(weight * 0.454))
print "He's got %s eyses and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight,age+height+weight)