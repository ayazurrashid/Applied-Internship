grades=[]
for _ in range(0,int(input())):
	grades.append([input(), float(input())])
second_highest = sorted(list(set([marks for name, marks in grades])))[1]
print('\n'.join([a for a,b in sorted(grades) if b == second_highest]))