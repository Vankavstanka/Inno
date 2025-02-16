class LIFO:
    """
    Последний добавленный запрос обрабатывается первым
    """
    def __init__(self):
        self.lifo = []

    def push(self, delivery):
        self.lifo.append(delivery)

    def pop(self):
        if not self.is_empty():
            return self.lifo.pop()
        return None

    def look(self):
        if not self.is_empty():
            return self.lifo[-1]
        return None

    def is_empty(self):
        return len(self.lifo) == 0


class FIFO:
    """
    Первый добавленный запрос обрабатывается первым
    """
    def __init__(self):
        self.fifo = []

    def push(self, delivery):
        self.fifo.append(delivery)

    def pop(self):
        if not self.is_empty():
            return self.fifo.pop(0)
        return None

    def is_empty(self):
        return len(self.fifo) == 0
