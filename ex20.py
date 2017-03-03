from sys import argv

script, input_file = argv

# print everything in a file.
def print_all(f):
    print f.read()

# rewind the file object(? or pointer) to the beginning of the file.
def rewind(f):
    f.seek(0)

# the file object seems to read one line and move to the next line.
# readline contains \n
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
