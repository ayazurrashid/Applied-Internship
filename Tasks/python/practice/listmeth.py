N = int(input())
L = []
for i in range(0, N):
    meth =input().split()
    if meth[0] == 'insert':
        L.insert(int(meth[1]), int(meth[2]))
    elif meth[0] == 'print':
        print(L)
    elif meth[0] == 'remove':
        L.remove(int(meth[1]))
    elif meth[0] == 'append':
        L.append(int(meth[1]))
    elif meth[0] == 'sort':
        L.sort()
    elif meth[0] == 'pop':
        L.pop()
    elif meth[0] == 'reverse':
        L.reverse()