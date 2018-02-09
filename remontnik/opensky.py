import requests

from .distance import distance


OPENSKY_URL = 'https://opensky-network.org/api/states/all'


def find_close(target_lat, target_lon, max_dist):
    """Find vehicles from opensky close to target point.

    Args:
        target_lat (float): latitude of target point.
        target_lon (float): longitude of target point.
        max_dist (float): max distance from target point to vehicle.

    Returns:
        List of tuples with callsign, latitude and longitude of vehicles.
    """

    resp = requests.get(OPENSKY_URL, timeout=5)
    assert resp.status_code == 200

    states = resp.json().get('states')
    assert states is not None

    result = []
    for state in states:
        callsign, lon, lat = state[1], state[5], state[6]
        if (lon is not None and lat is not None and
                distance(lat, lon, target_lat, target_lon) <= max_dist):
            result.append((callsign, lon, lat))
    return result
