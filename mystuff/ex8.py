#This type of code used to pre-assign some strings in later stages as
#the type in the initial stages
formatter = "%r %r %r %r"
#print (1,2,3,4) as a strings which is already been defined as string in the formatter function
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#3rd string is same as using ' ' but using " " will give output in " " format
print formatter % (
                   "I had this thing.",
                   "That you could type up right.",
                   "But it did not sing",
                   "So I said goodnight."
)
