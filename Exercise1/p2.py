

###f-strings###

#defining variables

# wrong format
# n = 10/3, a = 108%7, b = 2^3

# right format 1
n = 10/3
a = 108%7
b = 2**3 # Use ** for exponentiation

# right format 2
# n, a, b = 10/3, 108%7, 2**3



#f-strings
#fstr variables can be defined independently
#note the format for reference
fstr1 = f'n={n} a={a} b={b}'
print (fstr1)
fstr2 = f'n={n:.4f} a={a} b={b}'#4 decimal places for n below the decimal point
print(fstr2)