# Goal: Take user input, add a $5.00 fee, and print the total.
price_input = input("What is the item price? ")
delivery_fee = 5

# input() returns a string, so adding it to an int causes a TypeError. We need to convert the input to a float first
#  the error was:"ValueError: could not convert string to float"
total = float(price_input) + delivery_fee

# we also need to convert the float var total to a string before concatenating it with the other string in the print statement
# the error was: "TypeError: can only concatenate str (not "float") to str"
print("Your total is: " + str(total))
