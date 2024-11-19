#Deck tem liberdade para acrescentar novos dados PELAS EXTREMIDADES
#deck (size, left, right)
#node (data, previous, next)
#Push(right or left), pop, top/peek, empty, size

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class Deck:
    def __init__(self):
        self.left = None
        self.right = None
        self._size = 0

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def push_left(self, elem):
        node = Node(elem)
        if self.left is None:
            self.left = node
            self.right = node
        else:
            self.left.previous = node
            node.next = self.left
            self.left = node
        self._size += 1

    def push_right(self, elem):
        node = Node(elem)
        if self.right is None:
            self.left = node
            self.right = node
        else:
            self.right.previous = self.right
            self.right.next = node
            self.right = node
        self._size += 1
        
    def pop_left(self):
        if self.empty():
            return "Deck vazio"

        elem = self.left.data
        if len(self) > 1:
            self.left = self.left.next
            self.left.previous = None
            self._size -= 1
        else:
            self.right = None
            self.left = None
        return elem

    def pop_right(self):
        if self.empty():
            return "Deck vazio"

        elem = self.right.data
        if len(self) > 1:
            self.right = self.right.previous
            self.right.next = None
            self._size -= 1
        else:
            self.right = None
            self.left = None
        return elem

    def peek_left(self):
        if self.empty():
            return "Deck vazio"
        return self.left.data

    def peek_right(self):
        if self.empty():
            return "Deck vazio"
        return self.right.data

    def __repr__(self):
        if self.empty():
            return "Deck Vazio"

        p = self.left
        s = "left << "
        while p:
            s += str(p.data)
            p = p.next
            if p:
                s += " | "

        s += " >> right"
        return s
