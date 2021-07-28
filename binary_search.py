def binary_search(sorted_list, item):

    n =len(sorted_list)
    if n > 0:
        mid = n // 2
        if sorted_list[mid] == item:
            return True
        elif item < sorted_list[mid]:
            return binary_search(sorted_list[:mid], item)
        else:
            return binary_search(sorted_list[mid + 1:], item)

    return False

def binary_search_2(sorted_list, item):

    n = len(sorted_list)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last)//2
        if sorted_list[mid] == item:
            return True
        elif item < sorted_list[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False


if __name__ == '__main__':
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 55))
    print(binary_search(li, 100))
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 100))


