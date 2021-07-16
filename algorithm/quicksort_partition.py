def swap_elements(my_list, index1, index2):
    temp = 0
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp  

def partition(my_list, start, end):
    i = start
    b = start
    p = end

    while i < p:
        if my_list[i] < my_list[p]:
            swap_elements(my_list, i, b)
            b += 1 
        i += 1

    swap_elements(my_list, b, p)
    p = b
    return p

list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)