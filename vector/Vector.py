from math import sqrt, pi


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scaler(self, c):
        new_coordinates = [c * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scaler(1. / magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalized zero coordinates")

    def size(self, v):
        new_coordinates = [x * y for x, y in zip(self.coordinates, v.coordinates)]
        return sum(new_coordinates)

    def xx(self,v):
        xxx=self.size(v)/(self.magnitude()*v.magnitude())
        return xxx

    def yy(self,v):
        xxx = self.size(v) / (self.magnitude() * v.magnitude())
        return xxx*180/pi

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

v1=Vector([7.887,4.138])
w1=Vector([-8.802,6.776])

v2=Vector([3.183,-7.627])
w2=Vector([-2.668,5.319])

v3=Vector([-5.955,-4.904,-1.874])
w3=Vector([-4.496,-8.755,7.103])

v4=Vector([7.35,0.221,5.188])
w4=Vector([2.751,8.259,3.985])

print v1.size(w1)

print v2.xx(w2)

print v3.size(w3)

print v4.yy(w4)