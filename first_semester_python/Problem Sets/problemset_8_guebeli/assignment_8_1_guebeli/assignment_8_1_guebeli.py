from random import randint


class Vector:
    values = [0.0, 0.0, 0.0]
    name = ""

    def __init__(self, name, values=None, random=False):
        if values is None:
            values = [0.0, 0.0, 0.0]
        self.name = name
        if random:
            self.values = self.get_random_vector()
        else:
            self.set_vector(values)

    def get_random_vector(self):
        return [float(randint(-100, 100)), float(randint(-100, 100)), float(randint(-100, 100))]

    def set_vector(self, values):
        for k in range(len(values)):
            try:
                self.values[k] = float(values[k])
            except ValueError:
                self.values[k] = 0.0

    def print(self):
        print(f"{self.name} = ({self.values[0]}, {self.values[1]}, {self.values[2]})")

    def sum(self, vector2):
        new_vector = Vector(self.name + "+" + vector2.name, [0.0, 0.0, 0.0])

        new_vector.values[0] = self.values[0] + vector2.values[0]
        new_vector.values[1] = self.values[1] + vector2.values[1]
        new_vector.values[2] = self.values[2] + vector2.values[2]

        print(f"{self.name} + {vector2.name} = ({new_vector.values[0]}, {new_vector.values[1]}, {new_vector.values[2]})")
        return new_vector

    def multiply(self, factor):
        new_vector = Vector(str(factor) + self.name, [0.0, 0.0, 0.0])

        new_vector.values[0] = self.values[0] * factor
        new_vector.values[1] = self.values[1] * factor
        new_vector.values[2] = self.values[2] * factor

        print(f"{factor} * {self.name} = ({new_vector.values[0]}, {new_vector.values[1]}, {new_vector.values[2]})")
        return new_vector

    def cross_product(self, vector2):
        new_vector = Vector(self.name + "x" + vector2.name, [0.0, 0.0, 0.0])
        new_vector.values[0] = (self.values[1] * vector2.values[2]) - (self.values[2] * vector2.values[1])
        new_vector.values[1] = (self.values[2] * vector2.values[0]) - (self.values[0] * vector2.values[2])
        new_vector.values[2] = (self.values[0] * vector2.values[1]) - (self.values[1] * vector2.values[0])

        print(f"{self.name} x {vector2.name} = ({new_vector.values[0]}, {new_vector.values[1]}, {new_vector.values[2]})")
        return new_vector


if __name__ == '__main__':
    v1 = Vector("v1", [], True)
    v2 = Vector("v2", [5, -4, 5.5])
    v1.print()
    v2.print()
    v3 = v1.sum(v2)
    v2.print()
    v4 = v1.multiply(4)
    v2.print()
    v5 = v1.cross_product(v2)



