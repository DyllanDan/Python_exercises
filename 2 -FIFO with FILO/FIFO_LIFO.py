# FIFO -> First in First out
# [0] gets out
class FIFO:
    def __init__(self):
        self.info = []

    def __len__(self):
        return len(self.info)

    def ad(self, element):
        self.info.append(element)

    def out(self):
        self.info.pop(0)



q = FIFO()

q.ad('a')
q.ad('b')
q.out()
print(q.info)

#LIFO -> Last in First out
# [len()] gets out
class LIFO_1:
    def __init__(self):
        self.info = []

    def __len__(self):
        return len(self.info)

    def ad(self, element):
        self.info.append(element)
    def out(self):
        self.info.pop(len(self.info) - 1)


lf = LIFO_1()
lf.ad("abc")
lf.ad("cde")
lf.ad("fgh")

print(lf.__len__())
lf.out()
print(lf.info)