import unittest
from fibonacci import fib


class TestStringMethods(unittest.TestCase):
    def test_first_value_is_0(self):
        self.assertEqual(next(fib()), 0)

    def test_first_10_values_are_correct(self):
        values = []
        n = 0
        for v in fib():
            values.append(v)
            if n == 10:
                break
            n += 1

        self.assertEqual(values, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_yields_no_values_when_zero_values_requested(self):
        values = list(fib(0))

        self.assertEqual(values, [])

    def test_yields_first_value_when_only_1_value_requested(self):
        values = list(fib(1))

        self.assertEqual(values, [0])

    def test_yields_requested_number_of_values(self):
        values = list(fib(42))

        self.assertEqual(len(values), 42)

    def test_value_for_of_100th_term_is_correct(self):
        value = list(fib(100 + 1))[-1]

        self.assertEqual(value, 354224848179261915075)

    def test_value_for_step_1000th_term_is_correct(self):
        value = list(fib(1000 + 1))[-1]

        self.assertEqual(
            value,
            43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875,
        )


if __name__ == "__main__":
    unittest.main()
