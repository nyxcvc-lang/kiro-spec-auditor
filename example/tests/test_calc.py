# REQ-101: tested
def test_add():
    from src.calc import add
    assert add(2, 3) == 5

# REQ-102: tested
def test_div_zero():
    from src.calc import div
    try:
        div(1, 0)
    except ZeroDivisionError:
        return
    raise AssertionError("expected ZeroDivisionError")
