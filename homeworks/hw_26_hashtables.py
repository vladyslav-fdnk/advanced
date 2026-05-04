def binary_search_recursive(sequences: list[int], target: int, low: int, high: int, steps: int = 0) -> int:
    if low > high:
        print(f"Not found in {steps} steps")
        return -1

    steps += 1
    mid = (low + high) // 2
    guess = sequences[mid]

    if guess == target:
        # print(f"Found {target} in {steps} steps")
        return mid
    elif guess > target:
        return binary_search_recursive(sequences, target, low, mid - 1, steps)
    else:
        return binary_search_recursive(sequences, target, mid + 1, high, steps)


def fibonacci_search(arr, target):
    n = len(arr)

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1



class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return None

    def __contains__(self, key):
        index = self._hash(key)

        for k, _ in self.table[index]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self.count



if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]

    print("Binary Search:", binary_search_recursive(arr, 7, 0, len(arr) - 1))
    print("Fibonacci Search:", fibonacci_search(arr, 7))

    ht = HashTable()
    ht.add("a", 1)
    ht.add("b", 2)

    print("a in ht:", "a" in ht)
    print("c in ht:", "c" in ht)
    print("len(ht):", len(ht))