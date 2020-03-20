import math


class Vector(object):

    def __init__(self, vec):
        self.vec = vec
        print(self.vec)

    def unit_vector(self):
        """
        Unit Vector -- vector/magnitude
        """
        print('Unit Vector')
        items = []
        for item in self.vec:
            value = item / self.length()
            items.append(float(value))
        return items

    def length(self):
        return self.magnitude()

    def magnitude(self):
        total = 0
        for item in self.vec:
            total = total + item ** 2
        return math.sqrt(total)

    def multiply_by_scalar(self, scalar):
        """
        Scalar
        """
        print('scalar {}'.format(scalar))
        return [item * scalar for item in self.vec]


def main():

    # Scalar
    print("\n** Scalar")
    veca = [1.671, -1.012, -0.318]
    scalar = 7.41
    va = Vector(veca)
    print(va.magnitude())
    print(va.unit_vector())
    mscalar = va.multiply_by_scalar(scalar)
    print(mscalar)

    print('\n** Magnitude')
    vv = [-0.221, 7.437]
    vec = Vector(vv)
    print(vec.magnitude())

    vv = [8.813, -1.331, -6.247]
    vec = Vector(vv)
    print(vec.magnitude())

    print('\n** Unit Vector')
    vv = [5.581, -2.136]
    vec = Vector(vv)
    print(vec.unit_vector())

    vv = [1.996, 3.108, -4.554]
    vec = Vector(vv)
    print(vec.unit_vector())


if __name__ == '__main__':
    main()
