import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num est un nombre entier
              den est un nombre entier non nul
        POST : initialise les attributs
        RAISE : ValueError si den est egal à 0 ou si den ou si num n'est pas un entier
        """
        if not isinstance(num,int) or not isinstance(den,int):
            raise TypeError('num and den must be integers')
        if den == 0 :
            raise ValueError('den must be greater than 0')

        if den < 0:
            num = -num
            den = -den

        pgcd = math.gcd(num, den)
        self._num = num // pgcd
        self._den = den //pgcd

    @property
    def numerator(self):
        """Return the numerator of the fraction

        PRE :
        POST : retourne la valeur de l'attribut num
        """
        return self._num

    @property
    def denominator(self):
        """Return the denominator of the fraction

        PRE :
        POST : retourne la valeur de l'attribut den
        """
        return self._den


    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE :
        POST : retourne un str donnant le resultat sous forme reduite
        """
        return f"Le resultat est {self._num}/{self._den}"


    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :
        POST : renvoie un str donnant le resultat en unite + fraction ou unite si pas de reste
        """
        nbr = self._num // self._den #1
        if self._num % self._den != 0:
            fr = (self._num - (nbr * self._den))
            return f"Le resultat est {nbr} + {fr}/{self._den}"

        return f"Le resultat est {nbr}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est une fraction à additionner
         POST : retourne le resultat de cette somme de fraction
         RAISE : erreur si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError
        n = self.numerator * other.denominator + self.denominator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE : other est une fraction à soustraire
         POST : retourne le resultat de cette soustraction de fraction
         RAISE : erreur si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError("other is not a Fraction")
        n = self.numerator * other.denominator - self.denominator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

         PRE : other est une fraction à multiplier
         POST : retourne le resultat de cette multiplication de fraction
         RAISE : erreur si other n'est pas une fraction
         """
        if not isinstance(other,Fraction):
            raise TypeError("other is not a Fraction")
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

         PRE : other est une fraction à diviser
         POST : retourne le resultat de cette division de fraction
         RAISE : erreur si other n'est pas une fraction et si on veut diviser par 0
         """
        if not isinstance(other,Fraction):
            raise TypeError("other is not a Fraction")
        if other.numerator == 0:
            raise ValueError("le num doit être different de 0")
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return Fraction(n, d)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

         PRE : other est un entier à mettre en puissance
         POST : retourne le resultat de cette puissance de fraction
         RAISE : erreur si other n'est pas une entier
         """
        if not isinstance(other,int):
            raise TypeError("Exposant doit être un entier.")
        if other < 0:
            n = self.denominator ** abs(other)
            d = self.numerator ** abs(other)
            return Fraction(n, d)
        n = self.numerator ** other
        d = self.denominator ** other
        return Fraction(n, d)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est une fraction
        POST : retourne True si c'est égale sinon False
        RAISE : erreur si other n'est pas une fraction
        """
        if not isinstance(other,Fraction):
            raise TypeError("other is not a Fraction")
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE :
        POST : retourne la valeur de la fraction en décimal
        """
        return float(self.numerator/self.denominator)


    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE :
        POST : return True si c'est la fraction est égale à zero sino False
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE :
        POST : return True si c'est la fraction est entiere sinon False
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE :
        POST : return True si c'est la fraction en absolu est plus petite que 1, sinon False
        """
        return abs(self.numerator / self.denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE :
        POST : return True si le numerateur de la fraction réduite vaut 1
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other est une fraction
        POST :return True si c'est la difference des fractions est unitaire, sinon False
        RAISE : erreur si other n'est pas une fraction'
        """
        if not isinstance(other,Fraction):
            raise TypeError("other is not a Fraction")
        dif = self - other
        dif._num = abs(dif.numerator)
        return dif.is_unit()


if __name__ == '__main__':
    pass
    fraction1 = Fraction(10,20)
    print(f"1) {fraction1}")
    fraction2 = Fraction(4,3)
    print(f"2) {fraction2.as_mixed_number()}")

    fraction3 = Fraction(3,3)
    print(f"3) {fraction3.as_mixed_number()}")

    fraction4 = Fraction(1,2)

    somme = fraction1 + fraction3
    print(f"4) {somme}")
    diff = fraction1 - fraction2
    print(f"5) {diff}")
    multi = fraction1 * fraction2
    print(f"6) {multi}")
    div = fraction1 / fraction2
    print(f"7) {div}")
    puis = fraction1 ** -4
    print(f"8) {puis}")
    egal = fraction1 == fraction4
    print(f"9) {egal}")
    deci = fraction1
    print(f"10) {float(deci)}")
    print(f"11) {fraction1.is_zero()}")
    fraction5 = Fraction(0,5)
    print(f"12) {fraction5.is_zero()}")
    f6 = Fraction(8, 4)
    f7 = Fraction(1, 3)
    print(f"13) {f6.is_integer()}")
    print(f"14) {f7.is_integer()}")
    f8 = Fraction(1, 4)
    f9 = Fraction(7, 3)
    print(f"15) {f8.is_proper()}")
    print(f"16) {f9.is_proper()}")
    f1 = Fraction(7, 4)
    f2 = Fraction(9, 12)
    f3 = Fraction(-1, 3)
    print(f"17) {f1.is_adjacent_to(f2)}")
    print(f"18) {f1.is_adjacent_to(f3)}")