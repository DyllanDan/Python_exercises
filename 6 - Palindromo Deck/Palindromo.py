class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class Deck:
    def __init__(self):
        self.right = None
        self.left = None
        self._size = 0

    def empty(self):
        return self._size == 0

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


    def is_palindromo(self, word):
        deck_1 = Deck()
        deck_2 = Deck()
        for letters in word:
            deck_1.push_left(letters)
            deck_2.push_right(letters)

        str_1 = ""
        str_2 = ""
        while deck_1.left and deck_2.left:
            str_1 += str(deck_1.left.data)
            deck_1.left = deck_1.left.next
            str_2 += str(deck_2.left.data)
            deck_2.left = deck_2.left.next

        return str_1 == str_2

    def is_palindromo_2(self, word):
        deck_1 = Deck()
        for letters in word:
            deck_1.push_left(letters)

        while deck_1.left:
            if deck_1.left.data != deck_1.right.data:
                return False
            deck_1.left = deck_1.left.next
            deck_1.right = deck_1.right.previous

        return True


D = Deck()

print(D.is_palindromo_2("roma éamor"))