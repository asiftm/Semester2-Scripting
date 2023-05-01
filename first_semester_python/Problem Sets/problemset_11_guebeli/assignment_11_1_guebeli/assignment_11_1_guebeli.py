

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


class Fraction:

    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator


    def sum(self, fract):
        return Fraction(self.nominator*fract.denominator + self.denominator*fract.nominator,
                        self.denominator*fract.denominator)


    def product(self, fract):
        return Fraction(self.nominator*fract.nominator, self.denominator * fract.denominator)


    def opposite(self):
        return Fraction(-1*self.nominator,self.denominator)


    def inverse(self):
        return Fraction(self.denominator,self.nominator)


    def prettify(self):
        self.simplify()
        text = ""
        if self.nominator != 0:
            text += str(self.nominator)
            if self.denominator != 1:
                text += f"/{self.denominator}"
        else:
            text = "0"
        return text


    def simplify(self):
        d = gcd(self.nominator, self.denominator)
        self.nominator = self.nominator/d
        self.denominator = self.denominator/d



if __name__ == '__main__':
    f1 = Fraction(-1, -3)
    f2 = Fraction(8, 6)

    print(f1.prettify())
    print(f2.prettify())

    print(f"Opposite of f1 = {(f1.opposite()).prettify()}")
    print(f"Inverse of f1 = {(f1.inverse()).prettify()}")

    print(f"f1 + f2 = {(f1.sum(f2)).prettify()}")
    print(f"f1 + f2 = {(f1.product(f2)).prettify()}")


