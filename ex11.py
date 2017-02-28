print "How old are you?",
# I use input so that I do not have to see single-quote that surrounds the input values.
age = input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "What do you like?",
# input() may cause the error when it is string
favorite = raw_input()

print "So, you're %r old, %r tall and %r heavy, and like %s" % (
    age, height, weight, favorite)
