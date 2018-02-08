import math

from remontnik.distance import distance


def test_distance_equal():
    assert math.isclose(
        distance(4.1028, 49.0572, 4.1028, 49.0572),
        0.0,
        rel_tol=1e-3)


def test_distance_different():
    assert math.isclose(
        distance(35.7153, -78.9809, 51.6147, 4.4685),
        6561920.630975546,
        rel_tol=1e-3)
