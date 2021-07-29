import random
import time

def quick_sort(alist, first=0, last=None):
    '''Quick Sort Algorithms'''
    if last is None:
        last = len(alist) - 1

    if first >= last:
        return
    n = len(alist)

    pivot = alist[first]
    low = first
    high = last

    while low < high:
        # shift the high to the left
        while low < high and alist[high] >= pivot:
            high -= 1
        alist[low] = alist[high]

        # shift the low to the right
        while low < high and alist[low] < pivot:
            low += 1
        alist[high] = alist[low]
    # When low == high, quit
    alist[low] = pivot

    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low - 1)
    # 对low右边的列表执行快速排序
    quick_sort(alist, low + 1, last)

    return alist


if __name__ == '__main__':
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    print(l)

    start = time.time()
    sorted_li = quick_sort(l)
    print(sorted_li)
    end = time.time()
    for i in range(len(sorted_li) - 1):
        assert sorted_li[i] <= sorted_li[i + 1]
    print(end - start)
