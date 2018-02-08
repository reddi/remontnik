import requests

from .distance import distance


OPENSKY_URL = 'https://opensky-network.org/api/states/all'


def find_close(target_lat, target_lon, max_dist):
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
