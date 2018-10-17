#simple function with single arg
print("**********function***********")
def interns(name):
	print(name,"is an intern at Applied Informatics")

interns("Ayaz")
interns("Danish")
interns("Shahid")

print("**********function with return***********")
# returning value
def interns(name):
	return(name + " is an intern at Applied Informatics")
print("<====returned values====>")
print(interns("Ayaz"))
print(interns("Danish"))
print(interns("Shahid"))

#-----------------------------
print("**********function to create a list***********")
def make_list(a,l=[]):
	l.append(a)
	print("List created",l)
make_list(1)
make_list(2)
make_list(3)
# function with defualt arg
# c is default
print("**********function with default arguments***********")
def myfunct(a,b,c=5):
	total=(a*b)+c
	print("A+B*c =",total)

myfunct(2,10)
myfunct(2,10,6) #push the new value for c

# function with keyword arg
# c is default
print("**********function with keyword arg*************")
def mytask(a,b):
	c=a*b
	print("kwagr:a+b*c =",c)

mytask(a=2,b=10)

# variable no. of arguments *varr
print("**************************************")
print("***********function with variable no. of arguments *varr*********************")
def myvar(*varr):
    print("the elements arguments:",varr)
    print(type(varr))
    for i in varr:
    	print('the element is: ',i)
myvar(30,40,50)

# variable no. of  keyword agrs **kwargs
print("*********************function with variable no. of arguments **kwargs*************************")
def task(**kwargs):
	print("the elements of dict: ",kwargs)
	print(type(kwargs))
	for i in kwargs:
		print("the key is: ",i)
		print("the value is: ",kwargs[i])
task(name='ayaz',age=24)



print("**********lambda expression function***********")
multi = lambda x,y:x*y

print(multi(10,5))