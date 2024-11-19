def recursive_sum(list):
    if not list:
        return None

    else:
        if len(list) == 1:
            return list[len(list) - 1]

        else:
            num = list.pop() + recursive_sum(list) #take the last item, and sum with the list with this item

        return num


list = [1,2,"b",2,"c",4.3]

#print(recursive_sum(list))

def recursive_sum_2(list):
    num_list =[]

    for item in list:
        if type(item) == int or type(item) == float:
            num_list.append(item)

    return recursive_sum(num_list)


print(recursive_sum_2(list))