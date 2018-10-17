#string formatting
def print_formatted(number):
	width=len(str('{:b}'.format(number)))
	for i in range(1,number+1):
	    d=str(i)
	    o=str('{:o}'.format(i))
	    X=str('{:X}'.format(i))
	    b=str('{:b}'.format(i))
	    print(str.rjust(d,width),str.rjust(o,width),str.rjust(X,width),str.rjust(b,width))
print_formatted(input("Enter the limit"))