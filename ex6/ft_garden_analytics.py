class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._growcalls = 0
            self._agecalls = 0
            self._showcalls = 0
            self._shadecalls = 0

        def growcalls_counter(self) -> None:
            self._growcalls += 1

        def agecalls_counter(self) -> None:
            self._agecalls += 1

        def showcalls_counter(self) -> None:
            self._showcalls += 1

        def shadecalls_counter(self) -> None:
            self._shadecalls += 1

        def display_stats(self, tree: bool) -> None:
            if tree == False:
                print(f"Stats: {self._growcalls} grow, {self._agecalls} age, {self._showcalls} show")
            else:
                print(f"Stats: {self._growcalls} grow, {self._agecalls} age, {self._showcalls} show, {self._shadecalls} shade")

    @staticmethod
    def check_age(days: int) -> None:
        if days > 365:
            print(f"Is {days} days more than a year? -> True")
        else:
            print(f"Is {days} days more than a year? -> False")

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
        self._stats = Plant.Statistics()

    def show(self) -> str:
        return(print(f"{self._name}: {self._height}cm, {self._days} days old"))


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._bloomed = False

    def grow_and_bloom(self) -> None:
        self._height += 0.8
        self._bloomed = True
        print(f"[asking the {self._name.lower()} to grow and bloom]")
        self._stats.growcalls_counter()

    def show(self) -> None:
        super().show()
        if self._bloomed == True:
            print(f" Color: {self._color}\n {self._name} is blooming beautifully!")
        elif self._bloomed == False:
            print(f" Color: {self._color}\n {self._name} has not bloomed yet")
        self._stats.showcalls_counter()


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, diameter: float) -> None:
        super().__init__(name, height, days)
        self._diameter = diameter
    
    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height} long and {self._diameter}cm wide")
        self._stats.shadecalls_counter()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")
        self._stats.showcalls_counter()


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days, color)
        self.number_seeds = 0

    def grow_age_bloom(self) -> None:
        self._height += 15
        self._bloomed = True
        self._days += 10
        self.number_seeds += 42
        print(f"[make {self._name.lower()} grow, age and bloom]")
        self._stats.growcalls_counter()
        self._stats.agecalls_counter()

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.number_seeds}")


def show_statistics(plant: Plant) -> None:
    name = plant._name
    print(f"[statistics for {name}]")
    if isinstance(plant, Tree):
        plant._stats.display_stats(True)
    else:
        plant._stats.display_stats(False)


def ft_garden_analytics() -> None:
    flower = Flower("rose", 15.0, 10, "red")
    tree = Tree("oak", 200.0, 365, 5.0)
    seed = Seed("Sunflower", 80.0, 45, "yellow",)
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print()
    print("=== Flower")
    flower.show()
    show_statistics(flower)
    flower.grow_and_bloom()
    flower.show()
    show_statistics(flower)
    print()
    print("=== Tree")
    tree.show()
    show_statistics(tree)
    tree.produce_shade()
    show_statistics(tree)
    print()
    print("=== Seed")
    seed.show()
    seed.grow_age_bloom()
    seed.show()
    show_statistics(seed)
    print()
    print("=== Anonymous")




if __name__ == "__main__":
    ft_garden_analytics()