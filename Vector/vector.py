# import sys
import math


class Point():
    """ Creates a point in 3D space"""

    def __init__(self, x, y=0, z=0):
        """ for 2D system keep only define x,y"""
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        return(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2
                         + (self.z - other.z)**2))

    def __str__(self):
        # precision = 3
        dummy = (round(self.x, 3), round(self.y, 3), round(self.z, 3))
        output = '(' + ','.join(map(str, dummy)) + ')'
        return(output)

    @classmethod
    def fromRadial(cls, radius, phi=90, theta=0):
        """ phi is polar angle or inclination i.e angle with positive z-axis
            theta is azimuthal angle i.e angle with positive x-axis
            both the angles are in degrees"""
        phi = math.radians(phi)
        theta = math.radians(theta)
        xCord = radius * math.sin(phi) * math.cos(theta)
        yCord = radius * math.sin(phi) * math.sin(theta)
        zCord = radius * math.cos(phi)
        return(cls(xCord, yCord, zCord))


class Vector(Point):
    """ Mathematical vector model """

    def __init__(self, x, y=0, z=0):
        super().__init__(x, y, z)

    def magnitude(self):
        return(self.distance(Point(0, 0, 0)))

    def dirCos(self):
        return(math.degrees(math.acos(self.x / self.magnitude())),
               math.degrees(math.acos(self.y / self.magnitude())),
               math.degrees(math.acos(self.z / self.magnitude())))

    def __str__(self):
        if self.x >= 0:
            xCord = str(self.x) + 'i'
        else:
            xCord = '-' + str(abs(self.x)) + 'i'
        if self.y >= 0:
            yCord = '+' + str(self.y) + 'j'
        else:
            yCord = '-' + str(abs(self.y)) + 'j'
        if self.z >= 0:
            zCord = '+' + str(self.z) + 'k'
        else:
            zCord = '-' + str(abs(self.z)) + 'k'
        output = xCord + yCord + zCord
        return(output)

    def __add__(self, other):
        xCord = self.x + other.x
        yCord = self.y + other.y
        zCord = self.z + other.z
        return(Vector(xCord, yCord, zCord))

    def __sub__(self, other):
        xCord = self.x - other.x
        yCord = self.y - other.y
        zCord = self.z - other.z
        return(Vector(xCord, yCord, zCord))

    def __len__(self):
        count = 0
        if self.x != 0:
            count += 1
        if self.y != 0:
            count += 1
        if self.z != 0:
            count += 1
        return(count)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return(True)
        return(False)

    def isCollinear(self, other):
        if self.dirCos() == other.dirCos():
            return(True)
        return(False)

    def dot(self, other):
        xCord = self.x * other.x
        yCord = self.y * other.y
        zCord = self.z * other.z
        return(xCord + yCord + zCord)

    def scalarMul(self, k):
        return(Vector(k * self.x, k * self.y, k * self.z))

    def __mul__(self, other):
        xCord = self.y * other.z - self.z * other.y
        yCord = self.z * other.x - self.x * other.z
        zCord = self.x * other.y - self.y * other.x
        return(Vector(xCord, yCord, zCord))

    def unitVect(self):
        return(Vector(self.x / self.magnitude(), self.y / self.magnitude(),
                      self.z / self.magnitude()))

#
# A = Vector(2, 4, 8)
# B = Vector(10, 5, 7)
# print(A * B)
# print(type(A))


class Line(Point):

    """ only 2D implementation as of now"""

    def __init__(self, point1, point2):
        if point1.z != 0 or point2.z != 0:
            print('2D only')
        # Creates line equation as ax + by + c = 0
        # a is x coefficient, b is y coefficient, c is constant
        self.a = point1.y - point2.y
        self.b = point2.x - point1.x
        self.c = point1.x * point2.y - point1.y * point2.x

    def __str__(self):
        if self.a > 0:
            xCoeff = str(self.a) + 'x'
        elif self.a == 0:
            xCoeff = ''
        else:
            xCoeff = '-' + str(abs(self.a)) + 'x'
        if self.b > 0:
            yCoeff = ' + ' + str(self.b) + 'y'
        elif self.b == 0:
            yCoeff = ''
        else:
            yCoeff = ' - ' + str(abs(self.b)) + 'y'
        if self.c > 0:
            constant = ' +' + str(self.c)
        elif self.c == 0:
            constant = ''
        else:
            constant = ' -' + str(abs(self.c))
        output = xCoeff + yCoeff + constant + ' = 0'
        return(output)


A = Point(2, 3)
B = Point(4, 7)
L = Line(A, B)
print(L)


if __name__ == '__main__':
    print('this is for testing purposes')
