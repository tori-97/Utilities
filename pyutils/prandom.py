import random

def randint(start: int, end: int):
    """
        * Returns random integer from a range 
    """
    return random.randint(start, end)

def randfloat(start: float, end: float):
    """
        * Returns random float from a range
    """
    return random.uniform(start, end)