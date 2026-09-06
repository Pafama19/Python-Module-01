class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        if self.name == "Rose":
            self.height += 0.8
        elif self.name == "Tomato":
            self.height += 0.3
        else:
            self.height += 0.1

    def age(self) -> None:
        self.days += 1


def ft_garden_growth() -> None:
    plant = Plant("rose", 25.0, 30)
    i: int = 1
    first_height: float = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()
    while (i <= 7):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        plant.show()
        i += 1
    print(f"Growth this week: {round(plant.height - first_height, 1)}cm")


if __name__ == "__main__":
    ft_garden_growth()
