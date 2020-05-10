import pytest
from calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (-1, 0, -1),
        (0.1, 0.1, 0.2),
        (1234567890, 987654321, 2222222211),
        ("a", 1, 'can only concatenate str (not "int") to str'),
        ([1], 1, 'can only concatenate list (not "int") to list'),
        ({1}, 1, "unsupported operand type(s) for +: 'set' and 'int'"),
        ((1,), 1, 'can only concatenate tuple (not "int") to tuple'),
        (None, 1, "unsupported operand type(s) for +: 'NoneType' and 'int'")
    ])
    def test_add1(self, a, b, expected):
        # a,b 为整数或浮点数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = self.calc.add(a, b)
            assert result == expected
        # a,b 为其他数据类型时
        else:
            with pytest.raises(TypeError):
                self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expected", [
        (9, 3, 3),
        (8, 3, 8/3),
        (-1, 1, -1),
        (1.1, 0.1, 11.0),
        (0, 1, 0),
        (987654310, 123456789, 987654310/123456789),
        (0, 0, "division by zero"),
        ("a", 1, "unsupported operand type(s) for /: 'str' and 'int'"),
        ([1], 1, "unsupported operand type(s) for /: 'list' and 'int'"),
        ({1}, 1, "unsupported operand type(s) for /: 'set' and 'int'"),
        ((1,), 1, "unsupported operand type(s) for /: 'tuple' and 'int'"),
        (None, 1, "unsupported operand type(s) for /: 'NoneType' and 'int'"),
    ])
    def test_div(self, a, b, expected):
        # 除数为0
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                self.calc.div(a, b)
        # a,b 为整数或浮点数
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = self.calc.div(a, b)
            assert result == expected
        # a,b 为其他数据类型
        else:
            with pytest.raises(TypeError):
                self.calc.div(a, b)


if __name__ == '__main__':
    pytest.main(['-vs','test_calc.py'])
