import random
import time

def bubble_sort(unsorted_list):
    '''Bubble Sort Algorithm'''
    for i in range(len(unsorted_list)):

        for j in range(0, len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list

if __name__ == '__main__':
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    print(l)
    start = time.time()
    print(bubble_sort(l))
    end = time.time()
    for i in range(len(l) - 1):
        assert l[i] <= l[i + 1]
    print(end - start)
