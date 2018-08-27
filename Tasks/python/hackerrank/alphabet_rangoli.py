import string
def print_rangoli(size):
    cen = size - 1
    for i in range(size - 1, 0, -1):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[cen - j] = row[cen + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))   

    for i in range(0, size):
        row = ['-'] * (2 * size - 1)
        for j in range(0, size - i):
            row[cen - j] = row[cen + j] = string.ascii_lowercase[j + i]
        print('-'.join(row)) 

n=int(input())
print_rangoli(n)