class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates cannot be empty')
        except TypeError:
            raise TypeError('The coordinates must be interable')
    def __str__(self):
        return 'Vector {0}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        return [x+y for x, y in zip(self.coordinates, v.coordinates)]

    def subtraction(self, v):
        return [x-y for x, y in zip(self.coordinates, v.coordinates)]
    def scale(self, scale):
        return [x*scale for x in self.coordinates]

    def manitude(self, delta):
        return math.sqrt( math.fsum([math.pow(x) for x in delta]) )

    def normalize(self):
        pass
vec = Vector([1, 2, 3])
print vec
print str(vec)
vec2 = Vector([1,2,3])
vec3 = Vector([2,3,1])
print vec.__eq__(vec3)
print vec.__eq__(vec2)

coord = [1.671, -1.012, -0.318]
vec = Vector(coord)
coord_scaled = vec.scale(7.41)
print coord_scaled
c1 = [7.119, 8.215]
c2 = [-8.223, 0.878]
vec1 = Vector(c1)
vec2 = Vector(c2)
vec_sub = vec1.subtraction(vec2)
print vec_sub
c1 = [8.218, -9.341]
c2 = [-1.129, 2.111]
vec1 = Vector(c1)
vec2 = Vector(c2)
add = vec1.add(vec2)
print add

