# %d in x is already replaced by 10.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# %s in y are already replaced.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r is quite handy. x is automatically surrounded by ''
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

# string with formatters can be stored, and the real value can replace the formatters anytime.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# the concatenation of two strings.
print w + e
