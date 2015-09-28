#Example of class which represents complex number.
#This class can be used in virtual environment with following commands:
#>>> import Complex as cplx
#>>> z = cplx.Complex(2,3)
class Complex:
    def __init__(self, re, im):
        self.r = re
        self.i = im

    def add(self, z):
        re = self.r + z.r
        im = self.i + z.i
        return Complex(re, im)

    def multiply(self, z):
        re = self.r*z.r - self.i*z.i
        im = self.i*z.r + self.r*z.i
        return Complex(re, im)

    def toString(self):
        return "%f + %f i" % (self.r, self.i)

#z1 = Complex(1,2)
#z2 = Complex(-3, 5)

#z = z1.add(z2)
#print z.toString()

#z = z1.multiply(z2)
#print z.toString()

