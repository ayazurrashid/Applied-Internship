from collections import deque
stack =[1,2,3,4,5,6,7,8,9,10]
print(stack)
stack.append(11)
print(stack)
stack.pop()
print(stack)

print("===========queue===========")
queue=deque([1,2,3,4,5,6,7,8,9,10])
print(queue)
queue.append(11)
print(queue)
queue.pop()
print(queue)