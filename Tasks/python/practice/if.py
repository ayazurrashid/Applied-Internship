name ="Ayaz Ur Rashid"
task ='complete first five chapters of python doc.'
rating = 11
print('name: ',name)
print('task: ',task)
if rating>7 and rating <=10:
	print("Excellent ",name)
elif rating>=5 and rating <=7:
	print("good", name)
elif rating>=3 and rating <5:
	print("average",name)
elif rating==1 or rating==2:
	print("below average",name)
else:
	print("rating out of context")
# member function
chapters =['lists','sets','tuples','dictionaries','functons']
term ="five"
user =input("Please enter the name: ")
if term in task:
	print("five chapters are: ",chapters)
if user not in name:
	print("not found")
else:
	print("name found",name)