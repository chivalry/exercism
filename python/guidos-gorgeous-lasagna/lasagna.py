"""
Solution to lasagna exercise.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Return the bake time remaining.

    Return the amount of time remaining to bake the lasagna given how long it's been baking.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """
    Return the prep time in minutes.

    Return how much time it will take to prepare the lasagna for baking given how many layers.
    are required.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
