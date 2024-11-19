#estabelece um pivô
#ordena sublistas com base no pivo
def pivo(list):
    if len(list) <= 1:
        return list
    pivo_elem = list.pop()
    right = []
    left = []
    for elem in list:
        if elem <= pivo_elem:
            left.append(elem)
        else:
            right.append(elem)
    return pivo(left) + [pivo_elem] + pivo(right)


nums = [60, 1, 30, 5, 2, 10, 45, 20, 46, 12, 14]

print(nums)
print(pivo(nums))