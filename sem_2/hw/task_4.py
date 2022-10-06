num_of_elems = int(input('Number of elements: '))
pos_1 = int(input('Enter the value for the 1st position: '))
pos_2 = int(input('Enter the value for the 2st position: '))


def create_ordered_list(n):
    nums = list()
    for i in range(-n, n + 1):
        nums.append(i)
    return nums


numbers = create_ordered_list(num_of_elems)


def mult_elem_by_pos(pos1, pos2, nums, n):
    if (0 <= (pos1 - 1) < n * 2 + 1) and (0 <= (pos2 - 1) < n * 2 + 1):
        return nums[pos1 - 1] * nums[pos2 - 1]
    else:
        return 'wrong position was entered!'


mult_result = mult_elem_by_pos(pos_1, pos_2, numbers, num_of_elems)

print(numbers)
print(mult_result)

