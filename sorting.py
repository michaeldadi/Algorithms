# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Selection sort
def selection_sort(arr, size):
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = j

        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])

    return arr


# Merge sort
def merge_sort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        l = arr[:r]
        m = arr[r:]

        merge_sort(l)
        merge_sort(m)

        i = j = k = 0

        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = m[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(m):
            arr[k] = m[j]
            j += 1
            k += 1

    return arr


# Quicksort
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1


# Counting sort
def counting_sort(arr):
    size = len(arr)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

    return arr


# Radix sort
def radix_sort(arr):
    max_element = max(arr)

    place = 1
    while max_element // place > 0:
        counting_sort_helper(arr, place)
        place *= 10

    return arr


def counting_sort_helper(arr, place):
    size = len(arr)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

    return arr


# Heap sort
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])

        heapify(arr, n, largest)


# Bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])

    return arr


# Bucket sort
def bucket_sort(arr):
    bucket = []

    for i in range(len(arr)):
        bucket.append([])

    for j in arr:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(arr)):
        bucket[i] = insertion_sort(bucket[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1

    return arr
