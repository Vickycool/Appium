import pytest


class Test_xx:
    @pytest.mark.parametrize('a', [1, 2])
    def test_01(self, a):

        assert a == "1"
