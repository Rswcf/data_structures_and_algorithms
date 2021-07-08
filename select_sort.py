def select_sort(alist):
    '''Select Sort Algorithms'''
    for min_index in range(len(alist) - 1):
        for i in range(min_index + 1, len(alist)):
            if alist[min_index] > alist[i]:
                alist[min_index], alist[i] = alist[i], alist[min_index]

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44,  55, 20]
    print(li)
    select_sort(li)
    print(li)