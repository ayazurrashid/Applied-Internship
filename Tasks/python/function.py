def interns(name):
	print(name,"is an intern at Applied Informatics")

interns("Ayaz")
interns("Danish")
interns("Shahid")


# returning value
def interns(name):
	return(name + " is an intern at Applied Informatics")
print("<====returned values====>")
print(interns("Ayaz"))
print(interns("Danish"))
print(interns("Shahid"))

#-----------------------------
def make_list(a,l=[]):
	l.append(a)
	print("List created",l)
make_list(1)
make_list(2)
make_list(3)




# Lambda function
print("<====Lambda function====>")
