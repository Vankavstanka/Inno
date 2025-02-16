def search_by_number(deliveries, number):
    """
    Линейный поиск по номеру доставки
    """
    for delivery in deliveries:
        if delivery.number == number:
            return delivery
    return None


def search_by_time(deliveries, time_value):
    """
    Бинарный поиск по времени доставки
    """
    low = 0
    high = len(deliveries) - 1

    while low <= high:
        mid = (low + high) // 2
        if deliveries[mid].time == time_value:
            return mid
        elif deliveries[mid].time < time_value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
