class MinStack:
    # My solution
    def __init__(self):
        self.items = []
        self.sorted = []

    def push(self, val: int) -> None:
        self.items.append(val)
        self.sorted.append(val)
        if len(self.sorted) > 1 and self.sorted[-1] > self.sorted[-2]:
            self.sorted[-1], self.sorted[-2] = self.sorted[-2], self.sorted[-1]

    def pop(self) -> None:
        self.sorted.remove(self.items.pop()) # remove() method is not constant time

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.sorted[-1]

class MinStack2:
    # Inspired by the Discussion
    # The insight is to keep track of the minimum value so far and push it,
    # along with the number we are pushing, onto the stack.
    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        min_val = val
        if self.items:
            min_val = min(self.items[-1][1], val)
        self.items.append((val, min_val))

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def main():
    obj = MinStack2()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin() == -3)
    obj.pop()
    print(obj.top() == 0)
    print(obj.getMin() == -2)

if __name__ == '__main__':
    main()
