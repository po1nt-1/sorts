import operator
import random
import time

import __gen


tim_comparisons_count = 0
tim_transpositions_count = 0
tim_total_time = 0

merge_comparisons_count = 0
merge_transpositions_count = 0
merge_total_time = 0


minrun = 32


def merge_sort(L, compare=operator.lt):
    global merge_comparisons_count
    global merge_transpositions_count
    global merge_total_time
    merge_comparisons_count = 0
    merge_transpositions_count = 0
    merge_total_time = 0

    time_start = time.time()

    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        result = __merge_for_merge(left, right, compare)

        merge_total_time = time.time() - time_start
        return result


def __merge_for_merge(left, right, compare):
    global merge_comparisons_count
    global merge_transpositions_count

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        merge_comparisons_count += 1
        if compare(left[i], right[j]):
            merge_transpositions_count += 1
            result.append(left[i])
            i += 1
        else:
            merge_transpositions_count += 1
            result.append(right[j])
            j += 1
    while i < len(left):
        merge_transpositions_count += 1
        result.append(left[i])
        i += 1
    while j < len(right):
        merge_transpositions_count += 1
        result.append(right[j])
        j += 1
    return result


def __InsSort(arr, start, end):
    global tim_comparisons_count
    global tim_transpositions_count

    for i in range(start+1, end+1):
        elem = arr[i]
        j = i-1
        while j >= start and elem < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            tim_comparisons_count += 1
            tim_transpositions_count += 1
        arr[j+1] = elem
    return arr


def __merge_for_timsort(arr, start, mid, end):
    global tim_comparisons_count
    global tim_transpositions_count

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
        tim_comparisons_count += 1
        if first[ind1] < last[ind2]:
            tim_transpositions_count += 1

            arr[ind] = first[ind1]
            ind1 += 1
        else:
            tim_transpositions_count += 1

            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        tim_transpositions_count += 1

        tim_comparisons_count += 1
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        tim_transpositions_count += 1

        tim_comparisons_count += 1
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def tim_sort(arr):
    global tim_comparisons_count
    global tim_transpositions_count
    global tim_total_time
    tim_comparisons_count = 0
    tim_transpositions_count = 0
    tim_total_time = 0

    arr2 = arr.copy()

    n = len(arr)
    for start in range(0, n, minrun):
        tim_comparisons_count += 1
        end = min(start+minrun-1, n-1)
        arr = __InsSort(arr, start, end)

    curr_size = minrun

    while curr_size < n:
        for start in range(0, n, curr_size*2):
            tim_comparisons_count += 2
            mid = min(n-1, start+curr_size-1)
            end = min(n-1, mid+curr_size)
            arr = __merge_for_timsort(arr, start, mid, end)
        curr_size *= 2

    time_start = time.time()
    arr2.sort()
    tim_total_time = (time.time() - time_start) * 10

    return arr
