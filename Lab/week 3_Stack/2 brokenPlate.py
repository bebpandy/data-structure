"""
Enter Input : 1 10,5 20,3 30,3 40,4 50
10
40
30

Enter Input : 90 8,68 99,44 3,44 102,50 2
102
3
"""
class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

n = input('Enter Input : ').split(',')  
s = Stack()
for e in n:
    w,f = e.split()
    if s.size() and s.peek()[0] < int(w):
        print(s.pop()[1])
        while (s.size() and s.peek()[0] < int(w)):
            print(s.pop()[1])
    s.push((int(w),int(f)))
