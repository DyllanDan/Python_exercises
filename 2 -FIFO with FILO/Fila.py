#push para atrás
#pop excluí o primeiro elemento
#empty (true/false)
#top ou peek é o primeiro da fila
#size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __len__(self):
        return self._size

    def empty(self):
        return len(self) == 0

    def push(self, elem):
        node = Node(elem)
        if self.empty():
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node
        self._size += 1

    def peek(self):
        if self.empty()
            return "Fila vazia"
        return self.first.data

    def pop(self):
        if self.empty()
            return "Fila vazia"
        elem = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        self._size -= 1
        return elem
    def __repr__(self):
        if self.empty()
            return "Fila vazia"

        s = ""
        p = self.first
        while (p):
            s += str(p.data)
            p = p.next
            if (p)
                s += '->'
        return s


