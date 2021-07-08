def bubble_sort(alist):
    '''Bubble Sort Algorithm'''
    for j in range(len(alist) - 1):
        count = 0
        for i in range(len(alist) - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            continue
        return count

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    count = bubble_sort(li)
    print(li)
    print(count)