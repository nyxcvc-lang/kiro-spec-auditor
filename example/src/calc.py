# REQ-101: implemented
def add(a, b):
    return a + b

# REQ-102: implemented
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("div by zero")
    return a / b

