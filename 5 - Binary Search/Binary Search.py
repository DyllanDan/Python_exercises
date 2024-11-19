#Search that returns the value position in a list with sorted values
def binary_search(lista, value):
    start = 0
    end = len(lista) - 1
    middle = int((start + end) / 2)
    c = middle
    if lista[middle] == value:
        return middle

    if lista[middle] > value:
        while middle != start - 1:
            if lista[middle] == value:
                return middle
            else:
                middle = middle - 1

    elif lista[c] < value:
        print(c)
        while c != end + 1:
            if lista[c] == value:
                return c
            else:
                c = c + 1


ob = [1, 5, 15, 20, 24, 45, 67, 76]

print(binary_search(ob, 8))