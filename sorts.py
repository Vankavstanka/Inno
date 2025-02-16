def sort_by_weight(deliveries):
    """
    Сортировка по весу
    """
    if len(deliveries) <= 1:
        return deliveries

    mid = len(deliveries) // 2
    left = sort_by_weight(deliveries[:mid])
    right = sort_by_weight(deliveries[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].weight <= right[j].weight:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_by_time(deliveries, low=0, high=None):
    """
    Сортировка по времени
    """
    if high is None:
        high = len(deliveries) - 1

    if low < high:
        pivot_index = partition(deliveries, low, high)
        sort_by_time(deliveries, low, pivot_index - 1)
        sort_by_time(deliveries, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high].time
    i = low - 1
    for j in range(low, high):
        if arr[j].time <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def heap_sort_by_number(deliveries):
    """
    Сортировка списка доставок по полю number
    """
    n = len(deliveries)

    for i in range(n // 2 - 1, -1, -1):
        heapify(deliveries, n, i)

    for i in range(n - 1, 0, -1):
        deliveries[i], deliveries[0] = deliveries[0], deliveries[i]
        heapify(deliveries, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left].number > arr[largest].number:
        largest = left

    if right < n and arr[right].number > arr[largest].number:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
