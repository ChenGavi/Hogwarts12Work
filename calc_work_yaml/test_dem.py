import yaml
import pytest
from hamcrest import *
from calc import Calc


@pytest.fixture()
def ins_calc():
    return Calc()


class TestCalc:
    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("data.yaml", 'rb'))["add"]["data"])
    def calc_add(self, ins_calc, a, b, expected):
        calc = ins_calc
        with open("data.yaml", 'rb') as fo:
            steps = yaml.safe_load(fo)["add"]["steps"]
        for step in steps:
            if isinstance(step,dict):
                # 获取
                    if str(type(a)) in step["data type"] and str(type(a)) in step["data type"]:
                        result = calc.add(a, b)
                # 断言
                if
                # 捕获错误
        # a,b 为整数或浮点数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = calc.add(a, b)
            assert result == expected
        # a,b 为其他数据类型时
        else:
            with pytest.raises(TypeError):
                calc.add(a, b)