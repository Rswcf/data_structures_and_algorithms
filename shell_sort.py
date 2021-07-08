def shell_sort(alist):
    '''Shell Sort Algorithms'''
    gap = len(alist) // 2
    while gap > 0:
        for j in range(gap, len(alist)):
            # j = gap, j = gap + 1, ..., n - 1
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)
