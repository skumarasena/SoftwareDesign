"""Solution to an exercise in Think Python.

Author: Samantha Kumarasena
"""

#uses the functions defined below to print an nxn grid
def print_grid(n):
    for i in range(n):
    	print_row(n)
    print_end(n)

#prints each row of grid
def print_row(n):
    print '+ - - - - +' + ' - - - - +'*(n-1)
    print '|         |'+ '         |'*(n-1)
    
    #since side length of square is 4, length-1 must be printed
    for i in range(3):
    	print '|         |' + '         |'*(n-1)

#prints the bottom line of the grid
def print_end(n):
    print '+ - - - - +' + ' - - - - +'*(n-1)

#function call
print_grid(1)
