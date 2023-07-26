a = 1
b = 2

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b

if __name__ == "__main__":
    result = add(a, b)
    print("{a} + {b} = {result}".format(a,b,result))
