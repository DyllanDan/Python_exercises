def string_inverter(string, num):
    string = list(string)
    if num <= (len(string) - 1) / 2:
        a = string[num]
        b = string[len(string) - 1 - num]
        string[num] = b
        string[len(string) - 1 - num] = a
        string = string_inverter("".join(string), num + 1)
    return "".join(string)




#treating the problem with swap
#to changing the elements was necessary transform te string to a list
#"num" determines the inicial position of the inverting process
text = "abcd"
print(text)
print(string_inverter(text, 0))
