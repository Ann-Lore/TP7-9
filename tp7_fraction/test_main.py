import unittest
from main import Fraction
class TestMain(unittest.TestCase):
    def test_init(self):
        f1 = Fraction(10, 20)
        f2 = Fraction(-8, 6)
        f3 = Fraction(4, -3)

        self.assertEqual(f1.numerator, 1)
        self.assertEqual(f1.denominator, 2)

        self.assertEqual(f2.numerator, -4)
        self.assertEqual(f2.denominator, 3)

        self.assertEqual(f3.numerator, -4)
        self.assertEqual(f3.denominator, 3)

        with self.assertRaises(ValueError):
            Fraction(4, 0)

        with self.assertRaises(TypeError):
            Fraction(4.4, 8)

        with self.assertRaises(TypeError):
            Fraction("ug", "fdk")

    def test_str(self):
        f1 = Fraction(10, 20)

        self.assertEqual(str(f1), "Le resultat est 1/2")

    def test_as_mixed_number(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(3, 3)

        self.assertEqual(f1.as_mixed_number(), "Le resultat est 1 + 1/3" )
        self.assertEqual(f2.as_mixed_number(), "Le resultat est 1")

    def test_addition(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(3, 3)
        f3 = Fraction(-4, 7)
        self.assertEqual(str(f1 + f2), "Le resultat est 7/3")
        self.assertEqual(str(f1 + f3), "Le resultat est 16/21")

        with self.assertRaises(TypeError):
            f1 + 2

        with self.assertRaises(TypeError):
            f1 - 2.5

        with self.assertRaises(TypeError):
            f1 + "shfj"


    def test_soustraction(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(3, 3)
        f3 = Fraction(-4, 7)
        self.assertEqual(str(f1 - f2), "Le resultat est 1/3")
        self.assertEqual(str(f1 - f3), "Le resultat est 40/21")

        with self.assertRaises(TypeError):
            f1 - 2

        with self.assertRaises(TypeError):
            f1 - 2.5

        with self.assertRaises(TypeError):
            f1 - "shfj"

    def test_multiplication(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(3, 3)
        f3 = Fraction(-4, 7)
        self.assertEqual(str(f1 * f2), "Le resultat est 4/3")
        self.assertEqual(str(f1 * f3), "Le resultat est -16/21")

        with self.assertRaises(TypeError):
            f1 * 2

        with self.assertRaises(TypeError):
            f1 * 2.5

        with self.assertRaises(TypeError):
            f1 * "shfj"

    def test_division(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(3, 3)
        f3 = Fraction(-4, 7)
        f4 = Fraction(0, 3)
        self.assertEqual(str(f1 / f2), "Le resultat est 4/3")
        self.assertEqual(str(f1 / f3), "Le resultat est -7/3")

        with self.assertRaises(TypeError):
            f1 / 2

        with self.assertRaises(TypeError):
            f1 / 2.2

        with self.assertRaises(ValueError):
            f1 / f4

        with self.assertRaises(TypeError):
            f1 / "shfj"

    def test_puissance(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(21, 47)

        self.assertEqual(str(f1 ** 2), "Le resultat est 16/9")
        self.assertEqual(str(f1 ** -4), "Le resultat est 81/256")

        self.assertEqual(str(f2 ** 1), "Le resultat est 21/47")
        self.assertEqual(str(f2 ** -2), "Le resultat est 2209/441")

        with self.assertRaises(TypeError):
            f1 ** 2.2

        with self.assertRaises(TypeError):
            f1 ** 2/4

        with self.assertRaises(TypeError):
            f1 ** "shfj"

    def test_egalite(self):
        f1 = Fraction(10, 20)
        f2 = Fraction(1, 2)
        f3 = Fraction(21, 47)

        self.assertTrue(f1 == f2)
        self.assertFalse(f1 == f3)


        with self.assertRaises(TypeError):
            _ = f1 == 0.5

        with self.assertRaises(TypeError):
            _ = f1 == "shfj"

    def test_float(self):
        f1 = Fraction(10, 20)
        f2 = Fraction(1, 3)

        self.assertAlmostEqual(float(f1), 0.5, places=7)
        self.assertAlmostEqual(float(f2), 1/3, places=7)

    def test_is_zero(self):
        f1 = Fraction(0, 20)
        f2 = Fraction(1, 3)

        self.assertTrue(f1.is_zero())
        self.assertFalse(f2.is_zero())

    def test_is_integer(self):
        f1 = Fraction(8, 4)
        f2 = Fraction(1, 3)

        self.assertTrue(f1.is_integer())
        self.assertFalse(f2.is_integer())

    def test_is_proper(self):
        f1 = Fraction(1, 4)
        f2 = Fraction(7, 3)
        f3 = Fraction(-1, 3)

        self.assertTrue(f1.is_proper())
        self.assertTrue(f3.is_proper())

        self.assertFalse(f2.is_proper())

    def test_is_adjacent_to(self):
        f1 = Fraction(7, 4)
        f2 = Fraction(9, 12)
        f3 = Fraction(-1, 3)

        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertFalse(f1.is_adjacent_to(f3))

        with self.assertRaises(TypeError):
            f1.is_adjacent_to(2)

        with self.assertRaises(TypeError):
            f1.is_adjacent_to(25.6)

        with self.assertRaises(TypeError):
            f1.is_adjacent_to("njsn")


    def test_plus_petit(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(3, 3)
        f3 = Fraction(-4, 7)
        self.assertTrue(f3 < f1)
        self.assertFalse(f1 < f2)

        with self.assertRaises(TypeError):
            f1 < 1

        with self.assertRaises(TypeError):
            f1 < 0.5

        with self.assertRaises(TypeError):
            f1 < "shfj"

    def test_plus_grand(self):
        f1 = Fraction(4, 3)
        f2 = Fraction(3, 3)
        f3 = Fraction(-4, 7)
        self.assertTrue(f2 > f3)
        self.assertFalse(f3 > f1)

        with self.assertRaises(TypeError):
            f1 > 2

        with self.assertRaises(TypeError):
            f1 > 2.2

        with self.assertRaises(TypeError):
            f1 > "shfj"
