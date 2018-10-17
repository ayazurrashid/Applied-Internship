n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
avg=(sum(student_marks[query_name])/len(student_marks[query_name]))
print("%.2f" % avg)# changing the decimal format to 2digits