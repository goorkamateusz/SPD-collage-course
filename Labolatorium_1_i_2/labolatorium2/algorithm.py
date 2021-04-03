
class Algorithm:
    def __str__(self) -> str:
        if 'choose_rule' in self.__dict__:
            return self.name + self.choose_rule.name
        else:
            return self.name

    def __eq__(self, oth) -> bool:
        return str(self) == str(oth)
