import sys

given_file = sys.argv[1]
file = open(given_file, "r")
print file.read()

# Read each line

# Algorithm

file.close()