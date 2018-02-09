import math


EARTH_RADIUS = 6372795


def distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points using Haversine formula."""

    m = math.pi / 180
    lat1 *= m
    lat2 *= m
    lon1 *= m
    lon2 *= m

    lat1_cos = math.cos(lat1)
    lat2_cos = math.cos(lat2)
    lat1_sin = math.sin(lat1)
    lat2_sin = math.sin(lat2)
    delta = lon2 - lon1
    delta_cos = math.cos(delta)
    delta_sin = math.sin(delta)

    y = math.sqrt(
        math.pow(lat2_cos * delta_sin, 2) +
        math.pow(lat1_cos * lat2_sin - lat1_sin * lat2_cos * delta_cos, 2))
    x = lat1_sin * lat2_sin + lat1_cos * lat2_cos * delta_cos

    return math.atan2(y, x) * EARTH_RADIUS
