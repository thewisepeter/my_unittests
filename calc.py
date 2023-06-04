def add(x, y):
    """adds numbers"""
    return (x + y)


def subtract(x, y):
    """subtracts numbers"""
    return (x - y)


def multiply(x, y):
    """multiplies"""
    return (x * y)


def divide(x, y):
    """divide function"""
    if y == 0:
        raise ValueError('Can\'t divide by zero!')
    return (x / y)
