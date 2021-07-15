def swap_elements(my_list, index1, index2):
    temp = 0
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp  

def partition(my_list, start, end):
    pivot = my_list[-1]
    b_index = 0
    for i in range(len(my_list)-1):
        if my_list[i] < pivot:
            swap_elements(my_list, b_index, i)
            b_index += 1 
        else:
            pass
    swap_elements(my_list, b_index, -1)
    return b_index

list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)