list =[]
num_position = 5
for i in range(num_position):
    if i == 0:
        list.append(1)
    elif i == 1:
        list.append(1)
    else:
        n = list[len(list) - 1] + list[len(list) - 2]
        list.append(n)

print(list)