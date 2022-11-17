def swap(i,index,lst):
    if index == 0:
        return
    if lst[i] > lst[index]:
        lst[i], lst[index] = lst[index], lst[i]
        print(f"swap {lst[i]} <-> swap {lst[index]} : ", end="")
        print(lst)
        swap(i+1, index-1, lst)
    elif lst[i] < lst[index]:
        swap(i, index-1, lst)


def sort(index,list1):
    if index == 0:
        return
    if list1[index - 1] < list1[index]:
        sort(index - 1, list1)
    else:
        list1[index - 1], list1[index] = list1[index], list1[index - 1]
        print(f"swap {list1[index-1]} <-> swap {list1[index]} : ", end="")
        print(list1)
        sort(len(list1) - 1, list1)









inp = [int(x) for x in input('Enter Input : ').split()]
# print(len(inp)-1)
swap(0,len(inp)-1, inp)
sort(len(inp)-1,inp)
print(inp)

