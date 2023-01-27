class MathOperations:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print('Операция сложения')
        return self.value + other.value

    def __sub__(self, other):
        print('Операция вычитания')
        return self.value - other.value

    def __mul__(self, other):
        print('Операция умножения')
        return self.value * other.value

    def __truediv__(self, other):
        print('Операция деления')
        return self.value / other.value

a = MathOperations(50)
b = MathOperations(2)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

