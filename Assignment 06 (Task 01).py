import math

class NDimensionalVector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"NDimensionalVector{self.components}"

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        components = list(self.components)
        components[index] = value
        self.components = tuple(components)


    def __eq__(self, other):
        return self.components == other.components

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return NDimensionalVector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return NDimensionalVector(*(x - y for x, y in zip(self.components, other.components)))

    def __mul__(self, scalar):
        return NDimensionalVector(*(x * scalar for x in self.components))

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def dot_product(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(x * y for x, y in zip(self.components, other.components))
    
    def __neg__(self):
        return NDimensionalVector(*(-x for x in self.components))

    def __iter__(self):
        return iter(self.components)
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def __ne__(self, other):
        return not self == other

def main():
    #Test case for 1-D Vector
    v = NDimensionalVector(28)
    v0 = NDimensionalVector(10)
    print("Vector:", v)
    print("Vector 0:", v0)
    print("Magnitude of Vector:", round(v.magnitude()))
    print("Magnitude of Vector 0:", round(v0.magnitude()))
    print("Dot Product of Vector and Vector 0:", v.dot_product(v0))
    print("Sum of Vector and Vector 0:", v+v0)
    print("Difference of Vector and Vector 0:", v-v0)

    #Test case for 4-D Vector 
    v1 = NDimensionalVector(89, 28, 81, 94)
    v2 = NDimensionalVector(19, 10, 11, 12)
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Magnitude of Vector 1:", round(v1.magnitude()))
    print("Magnitude of Vector 2:", round(v2.magnitude()))
    print("Dot Product of Vector 1 and Vector 2:", v1.dot_product(v2))
    print("Sum of Vector 1 and Vector 2:", v1 + v2)
    print("Difference of Vector 1 and Vector 2:", v1 - v2)

    #Test case for 2-D Vector
    v3 = NDimensionalVector(92, 94)
    v4 = NDimensionalVector(4, 10)
    print("Vector 3:", v3)
    print("Vector 4:", v4)
    print("Magnitude of Vector 3:", round(v3.magnitude()))
    print("Magnitude of Vector 4:", round(v4.magnitude()))
    print("Dot Product of Vector 3 and Vector 4:", v3.dot_product(v4))
    print("Sum of Vector 3 and Vector 4:", v3 + v4)
    print("Difference of Vector 3 and Vector 4:", v3 - v4)

    #Test case for 3-D Vector
    v5 = NDimensionalVector(89, 92, 81)
    v6 = NDimensionalVector(4, 5, 19)
    print("Vector 5:", v5)
    print("Vector 6:", v6)
    print("Magnitude of Vector 5:", round(v5.magnitude()))
    print("Magnitude of Vector 6:", round(v6.magnitude()))
    print("Dot Product of Vector 5 and Vector 6:", v5.dot_product(v6))
    print("Sum of Vector 5 and Vector 6:", v5 + v6)
    print("Difference of Vector 5 and Vector 6:", v5 - v6)

    #Test case for 5-D Vector
    v7 = NDimensionalVector(89, 28, 32, 81, 94)
    v8 = NDimensionalVector(5, 19, 10, 11, 12)
    print("Vector 7:", v7)
    print("Vector 8:", v8)
    print("Magnitude of Vector 7:", round(v7.magnitude()))
    print("Magnitude of Vector 8:", round(v8.magnitude()))
    print("Dot Product of Vector 7 and Vector 8:", v7.dot_product(v8))
    print("Sum of Vector 7 and Vector 8:", v7 + v8)
    print("Difference of Vector 7 and Vector 8:", v7 - v8)

if __name__=="__main__":
    main()
