


class TextEditor:
    def __init__(self):
        self.text = ''
        self.history = []
        self.redo_stack = []

    def type(self,chunk:str):
        self.history.append(self.text)
        self.text += chunk
        self.redo_stack.clear()


    def undo(self):
        if not self.history:
            return

        self.redo_stack.append(self.text)
        self.text=self.history.pop()


    def redo(self):
        if not self.redo_stack:
            return
        self.history.append(self.text)

        self.text = self.redo_stack.pop()

    def get_text(self):
        return self.text


########### task_1 ###########

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class UnsortedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def index(self, item):
        current = self.head
        pos = 0

        while current:
            if current.data == item:
                return pos
            current = current.next
            pos += 1

        raise ValueError("Item not found")

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty list")

        current = self.head

        if current.next is None:
            value = current.data
            self.head = None
            return value

        while current.next.next:
            current = current.next

        value = current.next.data
        current.next = None
        return value

    def insert(self, pos, item):
        new_node = Node(item)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0

        while current and index < pos - 1:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Index out of range")

        new_node.next = current.next
        current.next = new_node

    def slice(self, start, stop):
        result = UnsortedList()

        current = self.head
        index = 0

        while current:
            if start <= index < stop:
                result.append(current.data)

            if index >= stop:
                break

            current = current.next
            index += 1

        return result


    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements)

