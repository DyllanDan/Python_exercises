def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        num = fibonacci(num - 1) + fibonacci(num - 2)
    return num

list = []
for i in range(1, 6):
    n = fibonacci(i)
    list.append(n)

print(list)