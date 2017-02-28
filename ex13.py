from sys import argv

script, first, second, third = argv
fouth = raw_input("The fouth one will receive from the prompt: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fouth variabele is:", fouth

# When put more arguments, it crashes like that with fewer arugments.
script, new_first, new_second = argv

print "The script is called:", script
print "The new first variable is:", new_first
print "The new second variable is:", new_second
