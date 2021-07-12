# def binary_search(element, some_list):
    # binary_1 = int(len(some_list)/2) 
    # binary_2 = int(binary_1/2)
    # binary_3 = int((len(some_list)+binary_1)/2)
    
    # if element == some_list[binary_1]:
    #     return binary_1
    # elif element < some_list[binary_1]:
    #     if element == some_list[binary_2]:
    #         return binary_2
    #     elif element < some_list[binary_2]:
    #         if element == some_list[binary_2-1]:
    #             return binary_2-1
    #         else:
    #             return None
    #     else:
    #         return None
    # else:
    #     if element == some_list[binary_3]:
    #         return binary_3
    #     elif element > some_list[binary_3]:
    #         if element == some_list[binary_3+1]:
    #             return binary_3+1
    #         else:
    #             return None
    #     else:
    #         return None

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))