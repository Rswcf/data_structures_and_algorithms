import random
import time

def merge_sort(alist):

    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    # left_li，right_li 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[: mid])
    right_li = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result


if __name__ == '__main__':
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    print(l)

    start = time.time()
    sorted_li = merge_sort(l)
    print(sorted_li)
    end = time.time()
    for i in range(len(sorted_li) - 1):
        assert sorted_li[i] <= sorted_li[i + 1]
    print(end - start)
