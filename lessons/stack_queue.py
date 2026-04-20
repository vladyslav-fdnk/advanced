from collections import deque

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

top=stack[-1]
# print(top)

reamoved=stack.pop()
# print(reamoved)
# print(stack)


class Stack:
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

    def peek(self):
        if not self.items:
            raise IndexError('Stack is empty')
        return self.items[-1]

    def __len__(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# print(stack.peek())
# print(len(stack))

stack.pop()
stack.pop()
stack.pop()
# print(stack.peek())


class StackGeneric[T]:
    def __init__(self):
        self._items: list[T] = []

    def push(self, val:T):
        self._items.append(val)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def peek(self) -> T:
        return self._items[-1]

    def __len__(self):
        return len(self._items)

stack_of_int =StackGeneric[int]()
stack_of_int.push(1)
stack_of_int.push(2)
# print(stack_of_int.peek())

stack_of_str = StackGeneric[str]()
stack_of_str.push('a')
stack_of_str.push('b')
stack_of_str.push('c')
# print(stack_of_str.peek())


from collections import deque
class Queue:
    def __init__(self):
        self._items= deque()

    def enqueue(self, val):
        self._items.append(val)

    def dequeue(self):
        if not self._items:
            raise IndexError('Queue is empty')
        return self._items.popleft()

    def peek(self):
        if not self._items:
            raise IndexError('Queue is empty')
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


queue =Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print('1st',queue.peek())
queue.dequeue()
print('1st',queue.peek())


def serve_customers(customers: list[int]):
    queue = deque()
    order=1
    while queue:
        customer=queue.popleft()
        print(f'Serving customer {customer} with order {order}')
        order+=1

serve_customers(['Alice','Bob','Carol'])

dec=deque()
dec.append("Alice")
dec.append("Bob")
dec.append("Carol")
dec.appendleft("Zara")
dec.appendleft("David")
dec.appendleft("Terry")
print(dec)

dec.popleft()
dec.pop()
print(dec)

dec.extendleft(['Alice','Bob','Carol'])
print(dec)

dec.rotate(2)
print(dec)

# from queue import Queue

recent_logs=deque(maxlen=3)
recent_logs.append('Log 1')
recent_logs.append('Log 2')
recent_logs.append('Log 3')
recent_logs.append('Log 4')
recent_logs.append('Log 5')
recent_logs.append('Log 6')
print('logs', recent_logs)