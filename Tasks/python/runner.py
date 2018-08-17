n = int(input())
runner=[]
runner=[input() for i in range(n)]
print(runner)
top=max(runner)
while max(runner)==top:
	runner.remove(max(runner))
second_highest = max(runner)
print(second_highest)