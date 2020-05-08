import pytest
from calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (-1, 0, -1),
        (0.1, 0.1, 0.2),
        (1234567890, 987654321, 2222222211)
    ])
    def test_add(self, a, b, expected):
        result = self.calc.add(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (9, 3, 3),
        (8, 3, 8/3),
        (-1, 1, -1),
        (1.1, 0.1, 11.0),
        (0, 1, 0),
        (0, 0, 0)
    ])
    def test_div(self, a, b, expected):
        if b == 0:
            try:
                self.calc.div(a, b)
            except ZeroDivisionError as e:
                assert str(e) == "division by zero"
        else:
            result = self.calc.div(a, b)
            assert result == expected


if __name__ == '__main__':
    pytest.main(['-vs','test_calc.py'])
