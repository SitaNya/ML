from math import sqrt, pi, acos
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
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
        new_coordinates = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = Decimal(self.magnitude())
            return self.times_scaler(Decimal('1.0') / magnitude)
        except ZeroDivisionError:
            raise self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(Decimal(u1.dot(u2)).quantize(Decimal('0.000')))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        print self.dot(v)
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def get_proj_b(self,b):
        b_normaalized=b.normalized()
        return b_normaalized.times_scaler(self.dot(b_normaalized))

    def __str__(self):
        return 'Vector: {}'.format([round(x,3) for x in self.coordinates])

    def __eq__(self, v):
        return self.coordinates == v.coordinates


v1 = Vector([3.039, 1.879])
w1 = Vector([0.825, 2.036])

v2 = Vector([-9.88, -3.264, -8.159])
w2 = Vector([-2.155, -9.353, -9.473])

v3 = Vector([3.009, -6.172, 3.692,-2.51])
w3 = Vector([6.404,-9.144,2.759,8.718])

print v1.get_proj_b(w1)

print v2.minus(v2.get_proj_b(w2))

print v3.get_proj_b(w3)
print v3.minus(v3.get_proj_b(w3))