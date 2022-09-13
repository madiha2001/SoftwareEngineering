# from code.add import add

def add(a, b):
    return a + b

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_answer_addition():
    assert add(5, 3) == 8
