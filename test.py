class node:
    def __init__(self,data, prev = None, next = None):
            self.data = data
            if prev is None:
                self.prev = None
            else:
                self.prev = prev
            if next is None:
                self.next = None
            else:
                self.next = next

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    head = node(l[0])
    p = head
    for i in range(1, len(l)):
        p.next = node(l[i])
        p = p.next
    return head


def printList(H):
    s = ''
    p = H
    while p != None:
        s += str(p.data) + ' '
        p = p.next
    return print(s)


def mergeOrderesList(p, q):
    if int(p.data) < int(q.data):
        temp = p
        Pnext = p.next
        Qnext = q
    else:
        temp = q
        Pnext = p
        Qnext = q.next
    head = temp
    while Pnext != None or Qnext != None:
        if Pnext != None and Qnext != None:
            if(int(Pnext.data) < int(Qnext.data)):
                temp.next = Pnext
                temp = temp.next
                Pnext = Pnext.next
            else:
                temp.next = Qnext
                temp = temp.next
                Qnext = Qnext.next
        elif Pnext != None:
            temp.next = Pnext
            temp = temp.next
            Pnext = Pnext.next
        elif Qnext != None:
            temp.next = Qnext
            temp = temp.next
            Qnext = Qnext.next
    return head


inp = input("Enter 2 Lists : ").split(' ')
L1 = inp[0].split(',')
L2 = inp[1].split(',')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)