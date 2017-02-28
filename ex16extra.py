from sys import argv

script, filename = argv

input_file = open(filename)
txt = input_file.read()
input_file.close()

print txt
