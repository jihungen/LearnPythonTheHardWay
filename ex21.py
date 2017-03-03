def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# The order of calls (called "inside out") is a bit different from the recursion.
what = add(iq, subtract(weight, multiply(height, divide(age, 2))))

print "That becomes: ", what, "Can you do it by hand?"

what_new = subtract(add(24, divide(34, 100)), 1023)

print "That becomes: ", what_new, ", isn't it?"
