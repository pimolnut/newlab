class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []


inp = input("Enter input : ").split()
S = Stack()
count = 0
for i in inp:
    S.push(i)
    if S.size() >= 3 and S.stack[-1] == S.stack[-2] == S.stack[-3]:
        S.pop()
        S.pop()
        S.pop()
        count += 1

if S.size() == 0:
    print(S.size())
    print('Empty')
else:
    print(S.size())

# join = ''.join(S.stack)
# print(join)
if count >= 2:
    for k in reversed(S.stack):
        print(k, end="")

    print(f'combo : {count} ! ! !')
if count < 2:
    for k in reversed(S.stack):
        print(k,end="")




