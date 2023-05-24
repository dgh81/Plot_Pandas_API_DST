# Use \n for newLine - Remember \n is 1 in the string lenght!
print(len("Hello\nWorld")) # 11 not 10

fileHandler = open('text.txt')

for line in fileHandler:
    # Use second argument end to specify the ending character (default is \n)
    print(line, end="")
    # OBS! When this loop is done, fileHandler is at the bottom of the file, and the next code (print(x)) wont print anything.

#RESET:
# Fix for the OBS above:
fileHandler = open('text.txt')

# Load all chars into var
x = fileHandler.read()
print(x)

# Print char by index
print(x[:11])

#RESET:
fileHandler = open('text.txt')
for line in fileHandler:
    if line.startswith("Python"):
        print(line)

# Try / catch
try:
    # RESET:
    fileHandler = open(input('filepath:'))
    for line in fileHandler:
        print(line)
except:
    print('Error in filepath')
    quit()
