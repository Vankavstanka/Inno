class Delivery:
    def __init__(self, number, source, destination, weight, time):

        self.number = number # номер доставки
        self.source = source # пункт отправления
        self.destination = destination # пункт назначения
        self.weight = weight # вес
        self.time = time # время доставки

    def __str__(self):
        return (f"Доставка №{self.number}, "
                f"из '{self.source}' в '{self.destination}', "
                f"вес: {self.weight}, время: {self.time}")
