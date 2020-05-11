import yaml
import pytest
from hamcrest import *
from calc import Calc


@pytest.fixture()
def ins_calc():
    return Calc()


class TestCalc:

    def setup(self):
        with open("steps.yaml", 'rb') as fo:
            self.steps = yaml.safe_load(fo)

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("data.yaml", 'rb'))["add"])
    def calc_add(self, ins_calc, a, b, expected):
        calc = ins_calc
        for step in self.steps:
            if "add" in step:
                # a,b 为整数或浮点数
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    result = calc.add(a, b)
                    assert result == expected
                # a,b 为其他数据类型时
                else:
                    with pytest.raises(TypeError):
                        calc.add(a, b)

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("data.yaml", 'rb'))["sub"])
    def calc_sub(self, ins_calc, a, b, expected):
        calc = ins_calc
        # a,b 为整数或浮点数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = calc.sub(a, b)
            assert result == expected
        # a,b 为其他数据类型时
        else:
            with pytest.raises(TypeError):
                calc.sub(a, b)

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("data.yaml", 'rb'))["mul"])
    def calc_mul(self, ins_calc, a, b, expected):
        calc = ins_calc
        # a,b 为整数或浮点数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = calc.mul(a, b)
            print(result)
            # 浮点数是二进制，使用close_to方法
            assert_that(result, close_to(expected, 0.01))
        # a,b 为其他数据类型时
        else:
            with pytest.raises(TypeError):
                calc.mul(a, b)

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("data.yaml", 'rb'))["div"])
    def calc_div(self, ins_calc, a, b, expected):
        calc = ins_calc
        for step in self.steps:
            if "div" in step:
                # 除数为0
                if b == 0:
                    with pytest.raises(ZeroDivisionError):
                        calc.div(a, b)
                # a,b 为整数或浮点数
                elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    result = calc.div(a, b)
                    # 除数有余数时，用close_to
                    assert_that(result, close_to(expected, 0.01))
                # a,b 为其他数据类型
                else:
                    with pytest.raises(TypeError):
                        calc.div(a, b)


if __name__ == '__main__':
    pytest.main(["-vs", "-m", "add or div", "test_calc.py"])
