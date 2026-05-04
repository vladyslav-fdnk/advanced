class Stack:   #task_1
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.items:
            raise IndexError('Stack is empty')
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# text = "hello"
#
# stack = Stack()
#
#
# for char in text:
#     stack.push(char)
#
#
# result = []
#
# while not stack.is_empty():
#     result.append(stack.pop())
#
# print("".join(result))

def is_balanced(stack_):   #task_2
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    open_pairs = ['(','[','{']
    close_pairs = [')',']','}']

    for char in stack_:
        if char in open_pairs:
            stack.append(char)

        elif char in close_pairs:
            if not stack:
                return False

            top=stack.pop()

            if top != pairs[char]:
                return False
    return len(stack) == 0

# print(is_balanced("()[]{}"))
# print(is_balanced("([)]"))
# print(is_balanced("((()))"))


class Stack:   #task_3
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.items:
            raise IndexError('Stack is empty')
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, element):
        temp_stack = []
        found = None

        while self.items:
            item = self.items.pop()

            if item == element:
                found = item
                break
            else:
                temp_stack.append(item)

        while temp_stack:
            self.items.append(temp_stack.pop())

        if found is None:
            raise ValueError("Element not found in stack")

        return found


# stack = Stack()
#
# stack.items = [1, 2, 3, 4, 5]
#
# print(stack.get_from_stack(3))
# # print(stack.get_from_stack(10))
# print(stack.items)

class Queue:
    def __init__(self):
        self.items = []

    def get_from_stack(self, element):
        temp_queue = []
        found = None
        size = len(self.items)

        for _ in range(size):
            item = self.items.pop(0)

            if item == element:
                found = item

            temp_queue.append(item)

        self.items = temp_queue

        if found is None:
            raise ValueError("Element not found in queue")

        return found

# queue = Queue()
#
# queue.items = [1, 2, 3, 4, 5]
#
# print(queue.get_from_stack(3))
# # print(queue.get_from_stack(10))
# print(queue.items)