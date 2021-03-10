
class Task:
    def __init__(self, id: int) -> None:
        self.id = id
        pass

    def __eq__(self, other) -> bool:
        return self.id == other.id


class Machine:
    def __init__(self, id: int) -> None:
        self.id = id


class Strategy:
    def run():
        pass
