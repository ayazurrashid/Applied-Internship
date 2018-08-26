s = input()
list_of_funcs = ['s.isalnum()', 's.isalpha()', 's.isdigit()','s.islower()','s.isupper()']
for i in list_of_funcs:
	j=eval(i)
	print(j)