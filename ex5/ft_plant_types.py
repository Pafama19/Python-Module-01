class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name.capitalize()
        self._height = height
        if (self._height < 0):
            print(f"{self._name} Error, height can't be negative")
            self._height = 0.0
        self._days = days
        if (self._days < 0):
            print(f"{self._name} Error, age can't be negative")
            self._days = 0

    def show(self) -> str:
        return(print(f"{self._name}: {self._height}cm, {self._days} days old"))

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._days)

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
            self._days = new_age
            print(f"Age update: {self._age} days")


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloomed = True

    def show(self) -> None:
        super().show()
        if self._bloomed == True:
            print(f" Color: {self._color}\n {self._name} is blooming beautifully!")
        elif self._bloomed == False:
            print(f" Color: {self._color}\n {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, diameter: float) -> None:
        super().__init__(name, height, days)
        self._diameter = diameter
    
    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height} long and {self._diameter}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, season: str, nutri_value: float) -> None:
        super().__init__(name, height, days)
        self._season = season
        self._nutri_value = nutri_value

    def grow(self) -> None:
            self._height += 0.8

    def age(self) -> None:
        self._days += 1
        self._nutri_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._season}\n Nutritional value: {round(self._nutri_value)}")

    def nutritional_value(self, days_grow) -> None:
        i = 1
        print(f"[make {self._name.lower()} grow and age for {days_grow} days]")
        while i in range(1, days_grow + 1):
            self.grow()
            self.age()
            i += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    flower = Flower("rose", 15.0, 10, "red")
    tree = Tree("oak", 200.0, 365, 5.0)
    vegetable = Vegetable("tomato", 5.0, 10, "April", 0)
    print("=== Flower")
    flower.show()
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree.show()
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable.show()
    vegetable.nutritional_value(40)
    vegetable.show()


if __name__ == "__main__":
    ft_plant_types()
