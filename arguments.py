print("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

# It works and it print a blank new line
print()

# If pow() is given only one argument, Python raises a TypeError: "TypeError: pow() missing required argument 'exp' (pos 2)" because pow() needs at least 2 arguments
# try_pow = pow(2)

'''
Function name: round
Defined or called: CALLED
Number of arguments: 2
Argument values: 3.14159 and 2
Return value: Yes (3.14), we know because we can print the result and it will show 3.14; also the second argument is 2, which means we want to round to 2 decimal places
'''
result = round(3.14159, 2)
print(result)
