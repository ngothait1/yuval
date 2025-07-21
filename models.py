from utils import inputNumber

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def getName(self) -> str:
        return self._name

    def getAge(self) -> int:
        return self._age

    def __str__(self) -> str:
        return f"Name: {self._name}\nAge: {self._age}"

    def to_dict(self) -> dict:
        return {
            "Type": "Person",
            "Name": self._name,
            "Age": self._age
        }


class Student(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.field_of_study: str = input("Field of study: ")
        self.year_of_study: int = inputNumber("Year of study")
        self.score_avg: float = float(input("Average score: "))

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\nType: Student\nField: {self.field_of_study}\nYear: {self.year_of_study}\nAverage: {self.score_avg}"

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "Type": "Student",
            "Field of Study": self.field_of_study,
            "Year": self.year_of_study,
            "Average": self.score_avg
        })
        return base


class Employee(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.field_of_work: str = input("Field of work: ")
        self.year_of_study: int = inputNumber("Years of experience")
        self.score_avg: float = float(input("Performance average: "))

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\nType: Employee\nField: {self.field_of_work}\nYear: {self.year_of_study}\nAverage: {self.score_avg}"

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "Type": "Employee",
            "Field of Work": self.field_of_work,
            "Year": self.year_of_study,
            "Average": self.score_avg
        })
        return base
