from calculator import sum, minus

# FILEPATH: /home/hai/Dev/pythopn-snippet/pytest-container/test_calculator.py


def test_sum():
    assert sum(2, 3) == 5
    assert sum(-5, 10) == 5
    assert sum(0, 0) == 0


def test_minus():
    assert minus(5, 2) == 3
    assert minus(10, 5) == 5
    assert minus(0, 0) == 0


def test_fail_test_case():
    assert 1 == 1
