name = 'Swapnil Thormothe'
age = 24 #not a lie
height = 75.0 #inches
height_feet = height / 12
weight = 85 #kgs
weight_US = weight / 0.453592
eyes = 'brown'
teeth = 'white'
hair = 'black'

print"Let's talk about %s." % name
print"He's %d inches tall." % height
print"That means he is %d feet tall" %height_feet
print"He's %s kgs heavy." % weight
print"Actually that's too heavy as we say in US, %d pounds!!" % weight_US
print"He's got %d eyes and %d hair" % (eyes,hair)
print"His teeth are usully %d depending on the coffee." % teeth

#this time is tricky try to get it all right
print"If I add %d, %d and %d I get %d." %(age, height, weight, age + height + weight)
