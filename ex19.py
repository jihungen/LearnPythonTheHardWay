# The function that reads some numbers and print them with text.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# pass the numbers directly.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# pass the variables with numbers.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# pass the numbers with math.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# pass the variables with math (with numbers).
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def computers(mac_count, chromebook_count):
    print "I have %d Macs! I'm rich!" % mac_count
    print "I have %d Chromebooks! I may not be rich, but I can use them very efficiently!" % chromebook_count
    print "Let's use them!"

computers(10, 5)
