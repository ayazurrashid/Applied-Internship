n = int(input("Enter The Limit For Set: "))
s = set(map(int, input().split()))
N = int(input("Enter The No. of Operations: "))
for i in range(N):
	x = list(input().split())
	eval('s.{0}({1})'.format(*x+['']))
print(sum(s))