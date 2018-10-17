friends = ['Khateeb','Amir','Sakib','Sajad','younis','abc']
even = [1,2,3,4,5,6,7,8,9,10]
# general
for f in friends:
	print(f)
#nested for and if
for x in even:
	if x%2==0:
		print(x," is even number")
	else:
		print(x," is odd numbers")

# range() function
for x in range(len(friends)):
	print(friends[x])
# range with continue
for x in range(len(even)):
	if x == 5:
		continue
	print("continue",even[x])

# range with break
for x in range(len(even)):
	if x == 5:
		break
	print("break",even[x])