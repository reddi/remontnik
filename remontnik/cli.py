import argparse
from pprint import pprint

from .opensky import find_close


MAX_DIST = 450000
PARIS_LAT, PARIS_LON = (48.85341, 2.3488)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('lat', type=float, default=PARIS_LAT)
    parser.add_argument('lon', type=float, default=PARIS_LON)
    parser.add_argument('dist', type=int, default=MAX_DIST)
    args = parser.parse_args()

    pprint(
        find_close(
            target_lat=args.lat,
            target_lon=args.lon,
            max_dist=args.dist))
