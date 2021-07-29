import random
import time

def is_sorted(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True

def bogo_sort(li):
    while not is_sorted(li):
        random.shuffle(li)
    return li

if __name__ == '__main__':
    l = []
    for i in range(10):
        l.append(random.randint(0, 999))
    print(l)

    start = time.time()
    print(bogo_sort(l))
    end = time.time()
    for i in range(len(l) - 1):
        assert l[i] <= l[i + 1]
    print(end - start)