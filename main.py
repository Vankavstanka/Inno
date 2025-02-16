from manager import DeliveryManager
from delivery import Delivery

def main():
    manager = DeliveryManager()

    while True:
        print("\n=== ЛОГИСТИЧЕСКАЯ СИСТЕМА ===")
        print("1. Добавить доставку")
        print("2. Удалить доставку")
        print("3. Изменить доставку")
        print("4. Показать все доставки")
        print("5. Сортировать по весу")
        print("6. Сортировать по времени")
        print("7. Сортировать по номеру")
        print("8. Поиск по номеру")
        print("9. Поиск по времени (сначала отсортировать по времени!)")
        print("10. Добавить срочную доставку")
        print("11. Обработать срочную доставку")
        print("12. Добавить обычную доставку")
        print("13. Обработать обычную доставку")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            try:
                number = int(input("Введите номер доставки (int): "))
                source = input("Введите пункт отправления (str): ")
                dest = input("Введите пункт назначения (str): ")
                weight = float(input("Введите вес груза (float): "))
                time = int(input("Введите время доставки (int): "))
                manager.add_delivery(number, source, dest, weight, time)
            except ValueError:
                print("Неправильный формат введённых данных.")

        elif choice == '2':
            try:
                number = int(input("Введите номер доставки для удаления: "))
                manager.remove_delivery(number)
            except ValueError:
                print("Номер должен быть целым.")

        elif choice == '3':
            try:
                number = int(input("Введите номер доставки для изменения: "))
                print("Оставьте поля пустыми, если не хотите их менять.")
                new_source = input("Новое место отправления (или Enter): ")
                new_destination = input("Новое место назначения (или Enter): ")

                new_weight_str = input("Новый вес (или Enter): ")
                new_time_str = input("Новое время (или Enter): ")

                new_weight = float(new_weight_str) if new_weight_str else None
                new_time = int(new_time_str) if new_time_str else None

                manager.update_delivery(
                    number,
                    new_source if new_source else None,
                    new_destination if new_destination else None,
                    new_weight,
                    new_time
                )
            except ValueError:
                print("Неправильный формат введённых данных.")

        elif choice == '4':
            manager.show_deliveries()

        elif choice == '5':
            manager.sort_by_weight()

        elif choice == '6':
            manager.sort_by_time()

        elif choice == '7':
            manager.sort_by_number()

        elif choice == '8':
            try:
                number = int(input("Введите номер доставки для поиска: "))
                manager.find_by_number(number)
            except ValueError:
                print("Номер должен быть целым.")

        elif choice == '9':
            try:
                time_value = int(input("Введите время доставки для бинарного поиска: "))
                manager.find_by_time(time_value)
            except ValueError:
                print("Значение должно быть целым.")

        elif choice == '10':
            try:
                number = int(input("Введите номер доставки: "))
                source = input("Введите пункт отправления: ")
                dest = input("Введите пункт назначения: ")
                weight = float(input("Введите вес груза: "))
                time = int(input("Введите время доставки: "))
                d = Delivery(number, source, dest, weight, time)
                manager.add_urgent(d)
            except ValueError:
                print("Неправильный формат введённых данных.")

        elif choice == '11':
            manager.process_urgent()

        elif choice == '12':
            try:
                number = int(input("Введите номер доставки: "))
                source = input("Введите пункт отправления: ")
                dest = input("Введите пункт назначения: ")
                weight = float(input("Введите вес груза: "))
                time = int(input("Введите время доставки: "))
                d = Delivery(number, source, dest, weight, time)
                manager.add_normal(d)
            except ValueError:
                print("Неправильный формат введённых данных.")

        elif choice == '13':
            manager.process_normal()

        elif choice == '0':
            print("Завершение работы программы.")
            break

        else:
            print("Неверный пункт меню. Повторите выбор.")


if __name__ == "__main__":
    main()
