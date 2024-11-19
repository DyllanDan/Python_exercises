class oFFtLF:
    def __init__(self):
        self.lifo_1 =[]
        self.lifo_2 =[]

    def add_element(self, element):
        self.lifo_1.append(element)

    def remove_elements(self):
        if not self.lifo_2:
            while self.lifo_1:
                self.lifo_2.append(self.lifo_1.pop())
                #.pop() removes and return the last element, then .append() puts this element on the second list

        if not self.lifo_2:
            return None

        return self.lifo_2.pop()
        #after moving the elements to filo_2, the last one (wich is the first one on filo_1) is removed


filas = oFFtLF()
filas.remove_elements()

