import pytest
from FizzBuzzer import FBGo

@pytest.mark.parametrize("x,y", [
    (4, "4"),
    (0, "FizzBuzz"),
    (-1, "-1"),
    (3, "Fizz"),
    (5, "Buzz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (21, "Fizz"),
    (30, "FizzBuzz"),
    (45, "FizzBuzz"),
    (25, "Buzz"),
    (98, "98"),
    (99, "Fizz"),
])

def test_RunAll(x, y):
    assert FBGo(x) == y
    
#eof
