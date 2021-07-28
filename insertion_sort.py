import random
import time

def insertion_sort(unsorted_list):
    '''Insertion Sort Algorithms'''
    for i in range(1, len(unsorted_list)):
        while i != 0:
            if unsorted_list[i] < unsorted_list[i - 1]:
                unsorted_list[i], unsorted_list[i - 1] = unsorted_list[i - 1], unsorted_list[i]
                i -= 1
            else:
                break

    return unsorted_list

if __name__ == '__main__':
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    print(l)

    start = time.time()
    print(insertion_sort(l))
    end = time.time()
    for i in range(len(l) - 1):
        assert l[i] <= l[i + 1]
    print(end - start)
