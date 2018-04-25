#%d is an integar string
x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know  %s and those who %s" % (binary, do_not) #twice used
#print everything in the text
print x
print y

print"I said: %r. " % x #first
print"I also said: '%s'." % y #twice here

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#joke_evaluation has a string therefore %hilarious
print joke_evaluation %hilarious  #used string in string here too but once

w = "This is the left side of..."
e = "a string with right side."
#I didnt understand why to print this at first
print w + e
