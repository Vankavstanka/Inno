from delivery import Delivery
from stacks import LIFO, FIFO
from sorts import (
    sort_by_weight,
    sort_by_time,
    heap_sort_by_number
)
from search import (
    search_by_number,
    search_by_time
)

class DeliveryManager:

    def __init__(self):
        self.deliveries = []
        self.urgent = LIFO()
        self.normal = FIFO()

    def is_duplicate_delivery(self, number):

        # Проверяем основной список доставок
        for d in self.deliveries:
            if d.number == number:
                return True
        # Проверяем срочные доставки
        for d in self.urgent.lifo:
            if d.number == number:
                return True
        # Проверяем обычные доставки (очередь)
        for d in self.normal.fifo:
            if d.number == number:
                return True
        return False

    def add_delivery(self, number, source, destination, weight, time):
        if self.is_duplicate_delivery(number):
            print(f"Доставка с номером {number} уже существует.")
            return

        new_delivery = Delivery(number, source, destination, weight, time)
        self.deliveries.append(new_delivery)
        print(f"Добавлена доставка: {new_delivery}")

    def remove_delivery(self, number):
        to_remove = None
        for d in self.deliveries:
            if d.number == number:
                to_remove = d
                break
        if to_remove:
            self.deliveries.remove(to_remove)
            print(f"Удалена доставка: {to_remove}")
        else:
            print(f"Доставка с номером {number} не найдена.")

    def update_delivery(self, number, new_source=None, new_destination=None,
                        new_weight=None, new_time=None):
        delivery = search_by_number(self.deliveries, number)
        if delivery:
            if new_source is not None:
                delivery.source = new_source
            if new_destination is not None:
                delivery.destination = new_destination
            if new_weight is not None:
                delivery.weight = new_weight
            if new_time is not None:
                delivery.time = new_time
            print(f"Обновлена доставка: {delivery}")
        else:
            print(f"Доставка с номером {number} не найдена.")

    def sort_by_weight(self):
        self.deliveries = sort_by_weight(self.deliveries)
        print("Список доставок отсортирован по весу")

    def sort_by_time(self):
        sort_by_time(self.deliveries)
        print("Список доставок отсортирован по времени")

    def sort_by_number(self):
        heap_sort_by_number(self.deliveries)
        print("Список доставок отсортирован по номеру")

    def find_by_number(self, number):
        result = search_by_number(self.deliveries, number)
        if result:
            print(f"{result}")
        else:
            print(f"Доставка с номером {number} не найдена.")

    def find_by_time(self, time_value):
        index = search_by_time(self.deliveries, time_value)
        if index != -1:
            print(f"{self.deliveries[index]}")
        else:
            print(f"Доставка с временем {time_value} не найдена.")

    def add_urgent(self, delivery):
        if self.is_duplicate_delivery(delivery.number):
            print(f"Доставка с номером {delivery.number} уже существует.")
            return
        # Добавляем доставку в общий список и в стек срочных доставок.
        self.deliveries.append(delivery)
        self.urgent.push(delivery)
        print(f"Срочная доставка добавлена: {delivery}")

    def process_urgent(self):
        d = self.urgent.pop()
        if d:
            # Удаляем доставку из общего списка
            if d in self.deliveries:
                self.deliveries.remove(d)
            print(f"Обработка срочной доставки: {d}")
        else:
            print("Нет срочных доставок")

    def add_normal(self, delivery):
        if self.is_duplicate_delivery(delivery.number):
            print(f"Доставка с номером {delivery.number} уже существует.")
            return
        # Добавляем доставку в общий список и в очередь обычных доставок.
        self.deliveries.append(delivery)
        self.normal.push(delivery)
        print(f"Обычная доставка добавлена: {delivery}")

    def process_normal(self):
        d = self.normal.pop()
        if d:
            # Удаляем доставку из общего списка
            if d in self.deliveries:
                self.deliveries.remove(d)
            print(f"Обработка обычной доставки: {d}")
        else:
            print("Нет обычных доставок")

    def show_deliveries(self):
        if not self.deliveries:
            print("Список доставок пуст.")
        else:
            print("Список текущих доставок:")
            for d in self.deliveries:
                print("   ", d)
