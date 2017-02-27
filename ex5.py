name = 'Yoo Jeehoon'
age = 32 # not a lie
height = 178 # cm
height_in_inches = height * 0.393701
weight = 63 # kg
weight_in_lbs = weight * 2.20462
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %r inches tall." % height_in_inches
print "He's %d kg heavy." % weight
print "He's %r pounds heavy." % weight_in_lbs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
