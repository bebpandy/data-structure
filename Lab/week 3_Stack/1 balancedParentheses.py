class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def match(op, cl):
    opeN = '([{'
    closE = ')]}'
    return opeN.index(op) == closE.index(cl)
    
inp = str(input('Enter Input : '))
li = list(inp)
s = Stack()
error = 0

for i in inp:
    if i in '([{' :
        s.push(i)
    elif i in ')]}':
        if s.size() > 0:
            if not match(s.pop(), i):  # i == close ,  s.pop() == open
                error = 1
            else:
                error = 2

if s.size() > 0:
    error = 3

if error == 1:
    print('Parentheses : Unmatched ! ! !')  
elif error == 2:
    print('Parentheses : Matched ! ! !')

