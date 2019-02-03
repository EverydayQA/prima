import math
import vector


class TwoVectors(object):

    def __init__(self, vv, bb):
        # input is vector, not class Vector()
        self.vv = vv
        self.bb = bb
        self.vec_vv = vector.Vector(self.vv)
        self.vec_bb = vector.Vector(self.bb)

    def projection_scalar(self):
        """
        """
        scalar = self.dot_products() / self.dot_products_2vecs(self.bb, self.bb)
        return scalar

    def projection_v_onto_b(self):
        """
        A projection vector vb from vv onto bb
        should be vector bb * scalar
        """
        print('Projection')
        # do not know how to calculate scalar for vec bb
        scalar = self.projection_scalar()
        return self.vec_bb.multiply_by_scalar(scalar)

    def multiply_two_vectors(self, vv, bb):
        """
        Multiplication of 2 vectors
        """
        return [x * y for x, y in zip(vv, bb)]

    def multiply(self):
        """
        Multiplication of 2 vectors
        """
        return self.multiply_by_scalar(self.vv, self.bb)

    def add(self):
        items = []
        for x, y in zip(self.vv, self.bb):
            value = x + y
            items.append(value)
        return items

    def minus(self):
        return self.minus_2vecs(self.vv, self.bb)

    def minus_2vecs(self, vv, bb):
        items = []
        for x, y in zip(vv, bb):
            value = x - y
            items.append(value)
        return items

    def ortho_vb(self):
        print('Orthogonas')
        return self.minus_2vecs(self.vv, self.projection_v_onto_b())

    def inner_products(self):
        return self.dot_products()

    def dot_products(self):
        return self.dot_products_2vecs(self.vv, self.bb)

    def dot_products_2vecs(self, vv, bb):
        """
        Or inner products, V.B
        """
        total = 0
        for x, y in zip(vv, bb):
            total = total + (x * y)
        return total

    def area_crossed_by(self):
        print('Area')
        vec = vector.Vector(self.cross_products())
        return vec.magnitude()

    def cross_products(self):
        return self.cross_products_2vecs(self.vv, self.bb)

    def cross_products_2vecs(self, vv, bb):
        """
        Only support 3 elements vector for now
        :returns: a new vector, totally different from dot products
        """
        items = []
        index = 0
        for item in vv:
            total = self.cross_item(vv, bb, index)
            # add minus if not first and last
            if index == 1:
                total = 0 - total
            items.append(total)
            index = index + 1
        return items

    def cross_item(self, vv, bb, index):
        """
        only for 3 items vector
        """
        # vv bb should exclude current index
        nvv = list(vv)
        nbb = list(bb)
        del nvv[index]
        del nbb[index]
        total = None
        for x, y in zip(nvv, reversed(nbb)):
            if total is None:
                total = x * y
            else:
                total = total - x * y
        print('cross_item {} {} {} {}'.format(nvv, nbb, index, total))
        return total

    def get_cosine(self):
        """
        (V.B) / (|V| * |B|)
        """
        value = self.dot_products() / (self.vec_vv.magnitude() * self.vec_bb.magnitude())
        return value

    def angle_rad(self):
        value = self.get_cosine()
        return math.acos(value)

    def angle_degree(self):
        return math.degrees(self.angle_rad())


def main():

    print('\n** Dot products')
    vv = [7.887, 4.138]
    bb = [-8.802, 6.776]
    twov = TwoVectors(vv, bb)
    cc = twov.dot_products()
    print(cc)
    vv = [-5.955, -4.904, -1.874]
    bb = [-4.496, -8.755, 7.103]
    twov = TwoVectors(vv, bb)
    cc = twov.dot_products()
    print(cc)

    print('\n** Angle')
    vv = [3.183, -7.627]
    bb = [-2.668, 5.319]
    twov = TwoVectors(vv, bb)
    cc = twov.angle_rad()
    print(cc)
    vv = [7.35, 0.221, 5.188]
    bb = [2.751, 8.259, 3.985]
    twov = TwoVectors(vv, bb)
    cc = twov.angle_degree()
    print(cc)

    print('\n** Projection')
    vv = [3.039, 1.879]
    bb = [0.825, 2.036]
    twov = TwoVectors(vv, bb)
    cc = twov.projection_v_onto_b()
    print(cc)
    vv = [-9.88, -3.264, -8.159]
    bb = [-2.155, -9.353, -9.473]
    twov = TwoVectors(vv, bb)
    cc = twov.projection_v_onto_b()
    print(cc)
    cc = twov.ortho_vb()
    print(cc)
    #
    vv = [3.009, -6.172, 3.692, -2.51]
    bb = [6.404, -9.144, 2.759, 8.718]
    twov = TwoVectors(vv, bb)
    cc = twov.projection_v_onto_b()
    print(cc)
    cc = twov.ortho_vb()
    print(cc)

    print('\nCross products')
    vv = [8.462, 7.893, -8.187]
    bb = [6.984, -5.975, 4.778]
    twov = TwoVectors(vv, bb)
    cc = twov.cross_products()
    print(cc)
    vv = [-8.987, -9.838, 5.031]
    bb = [-4.268, -1.861, -8.866]
    twov = TwoVectors(vv, bb)
    cc = twov.area_crossed_by()
    print(cc)
    vv = [1.5, 9.547, 3.691]
    bb = [-6.007, 0.124, 5.772]
    twov = TwoVectors(vv, bb)
    cc = twov.area_crossed_by()
    print(cc / 2)


if __name__ == '__main__':
    main()
