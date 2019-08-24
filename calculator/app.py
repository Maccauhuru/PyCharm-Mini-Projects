import re

print("Python Mini Calculator App")
print("Type quit to exit the program")

# initialize variables
previous = 0
run = True


def perform_calc():
    global run
    equation = input("Enter number")
    if equation == 'quit':
        run = False
    else:
        print("You typed", equation)


while run:
    perform_calc()
