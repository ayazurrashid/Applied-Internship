n=input()
eng_roll=set(map(int,input().split()))
b=input()
fren_roll=set(map(int,input().split()))
total=eng_roll.symmetric_difference(fren_roll)
sorted_total=sorted(total)
for i in sorted_total:
    print(i)