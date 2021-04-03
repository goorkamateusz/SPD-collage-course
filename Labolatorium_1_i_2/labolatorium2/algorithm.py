
class Algorithm:
    def __str__(self) -> str:
        return self.name

    def __eq__(self, oth) -> bool:
        return str(self) == str(oth)
