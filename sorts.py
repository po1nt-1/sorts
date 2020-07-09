import operator
import random
import time


minrun = 32


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return __merge(left, right, compare)


def __merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def InsSort(arr, start, end):
    for i in range(start+1, end+1):
        elem = arr[i]
        j = i-1
        while j >= start and elem < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid+1]
    last = arr[mid+1:end+1]
    len1 = mid-start+1
    len2 = end-mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def TimSort(arr):
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start+minrun-1, n-1)
        arr = InsSort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size*2):
            mid = min(n-1, start+curr_size-1)
            end = min(n-1, mid+curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr


if __name__ == "__main__":
    data = [i for i in range(1000000)]
    random.shuffle(data)
    print("до")
    print("длина перемешанного массивчика", len(data))
    print(data[:10], ". . .", end="")
    print(data[-10:-1])

    start = time.time()
    result = merge_sort(data)
    end = time.time()

    print("после")
    print("длина отсортированного массивчика(та же)", len(result))
    print(result[:10], ". . .", end="")
    print(result[-10:-1])
    print("время:", end-start)
