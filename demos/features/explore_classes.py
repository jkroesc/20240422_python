class Person:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        city: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def full_name(self) -> str:
        return self.first_name + " " + self.last_name


john = Person("John", "Smith", 30, "New York")
print(john.full_name())
