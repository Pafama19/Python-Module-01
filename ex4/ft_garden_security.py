class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        if (self._height < 0):
            print(f"{self._name} Error, height can't be negative")
            self._height = 0.0
        self._age = age
        if (self._age < 0):
            print(f"{self._name} Error, age can't be negative")
            self._age = 0

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height update: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("age update rejected")
        else:
            self._age = new_age
            print(f"Age update: {self._age} days")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-1)
    plant.set_age(-1)
    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
