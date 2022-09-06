class Queue:
    def __init__(self, data = None):
        if data == None:
            self.item = []
        else:
            self.item = data

    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)


Act = {0: 'Eat',
       1: 'Game',
       2: 'Learn',
       3: 'Movie'}
place = {0: 'Res.',
         1: 'ClassR.',
         2: 'SuperM.',
         3: 'Home'}

My_Q = Queue()
Your_Q = Queue()
My_Act = Queue()
Your_Act = Queue()
myAct = []
myLocation = []
yourAct = []
yourLocation = []
printitem = []
printitem1 = []
count = 0

inp = input("Enter Input : ").split(',')
for i in inp:
    My_Q.enqueue(i.split()[0])
    Your_Q.enqueue(i.split()[1])
join = ', '.join(My_Q.item)
join1 = ', '.join(Your_Q.item)
print(f'My Queue = {join}')
print(f'Your Queue = {join1}')

for j in My_Q.item:
    # print(j)
    myAct.append(Act[int(j[0])])
    myLocation.append(place[int(j[2])])
    a = f'{Act[int(j[0])]}:{place[int(j[2])]}'
    printitem.append(a)
print(f'My Activity:Location = {", ".join(printitem)}')

for k in Your_Q.item:
    yourAct.append(Act[int(k[0])])
    yourLocation.append(place[int(k[2])])
    b = f'{Act[int(k[0])]}:{place[int(k[2])]}'
    printitem1.append(b)
print(f'Your Activity:Location = {", ".join(printitem1)}')

for item in range(len(myAct)):
    if myAct[item] == yourAct[item] and myLocation[item] != yourLocation[item]:
        count += 1
    elif myLocation[item] == yourLocation[item] and myAct[item] != yourAct[item]:
        count += 2
    elif myLocation[item] == yourLocation[item] and myAct[item] == yourAct[item]:
        count += 4
    elif myLocation[item] != yourLocation[item] and myAct[item] != yourAct[item]:
        count -= 5

if count >= 7 :
    print(f"Yes! You're my love! : Score is {count}.")
elif count < 7 and count > 0:
    print(f"Umm.. It's complicated relationship! : Score is {count}.")
else:
    print(f"No! We're just friends. : Score is {count}.")