import pytest


@pytest.fixture()
def init_xx():
    with open('./test.txt','w') as f:
        f.write('hello')


@pytest.mark.usefixtures('init_xx')
class Test_xx:
    def test_xx(self):
        with open('./test.txt', 'r') as f:
            a = f.read()
            print(a)
            assert a == 'hello'
