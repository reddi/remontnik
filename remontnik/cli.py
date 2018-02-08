from pprint import pprint

from .opensky import find_close


def cli():
    MAX_DIST = 450000
    PARIS_LAT, PARIS_LON = (48.85341, 2.3488)

    pprint(
        find_close(
            target_lat=PARIS_LAT,
            target_lon=PARIS_LON,
            max_dist=MAX_DIST))
