class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.head == None:
            return ''
        text = str(self.head.data)
        current_node = self.head.next
        while current_node != None:
            text += f' {current_node.data}'
            current_node = current_node.next
        return text

    def get_string(self, sep=' -> '):
        if self.head == None:
            return ''
        text = str(self.head.data)
        current_node = self.head.next
        while current_node != None:
            text += f'{sep}{current_node.data}'
            current_node = current_node.next
        return text

    def print_all_nodes(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def insert_head(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def delete_head(self):
        if self.head != None:
            self.head = self.head.next
            self.size -= 1

    def insert_tail(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = newNode
        self.size += 1

    def delete_tail(self):
        if self.head == None:
            return
        elif self.head.next == None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next != None:
                current_node = current_node.next
            current_node.next = None
        self.size -= 1

    def delete_data(self, data):
        if self.head == None:
            return
        elif self.head.next == None:
            if self.head.data == data:
                self.head = None
                self.size -= 1
            else:
                return
        else:
            current_node = self.head
            if current_node.data == data:
                self.head = current_node.next
            else:
                while current_node.next.data != data:
                    current_node = current_node.next
                    if current_node.next == None:
                        return
                current_node.next = current_node.next.next
            self.size -= 1


def get_digit(number, pos):
    return (abs(number) // (10**(pos-1))) % 10


def print_buckets(buckets):
    for idx in range(len(buckets)):
        print(f'{idx}: {buckets[idx].get_string(" ")}')


input_text = input('Enter Input : ')

input_numbers = list(int(e) for e in input_text.split())
abs_input_numbers = list(abs(int(e)) for e in input_text.split())
temp_buckets = [LinkedList()]
for number in input_numbers:
    temp_buckets[0].insert_tail(Node(number))

if max(abs_input_numbers) == 0:
    round = 1
else:
    round = len(str(max(abs_input_numbers)))+1
    # round = int(math.log(max(abs_input_numbers))//math.log(10)+1+1)
    # print(len(str(max(abs_input_numbers)))+1)
    # print(round)


for i in range(round):
    new_buckets = list(LinkedList() for _ in range(10))

    for bucket in temp_buckets[::-1]:
        current_head = bucket.head
        while current_head != None:
            if current_head.data < 0:
                new_buckets[get_digit(current_head.data, i+1)].insert_tail(Node(current_head.data))
            current_head = current_head.next

    for bucket in temp_buckets:
        current_head = bucket.head
        while current_head != None:
            if current_head.data >= 0:
                new_buckets[get_digit(current_head.data, i+1)].insert_tail(Node(current_head.data))
            current_head = current_head.next

    if(i != round-1):
        print('------------------------------------------------------------')
        print(f'Round : {i + 1}')
        print_buckets(new_buckets)
    temp_buckets = new_buckets
print('-' * 30)
print(f'{i} Time(s)')
print('Before Radix Sort :', ' -> '.join(list(e for e in input_text.split())))
print('After Radix Sort :', temp_buckets[0].get_string())