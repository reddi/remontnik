import pytest
import requests_mock

from remontnik.opensky import find_close, OPENSKY_URL


def test_find_close_empty():
    with requests_mock.mock() as m:
        m.get(OPENSKY_URL, json={'states': []}, status_code=200)
        assert find_close(target_lat=0, target_lon=0, max_dist=1) == []


def test_find_close_zero():
    with requests_mock.mock() as m:
        m.get(
            OPENSKY_URL,
            json={'states': [('x', 'x', 'x', 'x', 'x', 1.23, None)]},
            status_code=200)

        assert find_close(
            target_lat=1.23,
            target_lon=4.56,
            max_dist=123456) == []


def test_find_close_zero():
    with requests_mock.mock() as m:
        m.get(
            OPENSKY_URL,
            json={
                'states': [
                    ('x', 'x', 'x', 'x', 'x', 139.8277, 35.4777),
                    ('x', 'x', 'x', 'x', 'x', -3.0339, 47.5231)]},
            status_code=200)

        assert find_close(
            target_lat=-93.2104,
            target_lon=44.687,
            max_dist=100000) == []


def test_find_close_one():
    with requests_mock.mock() as m:
        m.get(
            OPENSKY_URL,
            json={
                'states': [
                    ('x', 'cs0', 'x', 'x', 'x', -37.7944, 123.44),
                    ('x', 'cs1', 'x', 'x', 'x', -3.0339, 47.5231)]},
            status_code=200)

        assert find_close(
            target_lat=122.16,
            target_lon=-36.0953,
            max_dist=230000) == [('cs0',  -37.7944, 123.44)]


def test_find_close_http_error():
    with requests_mock.mock() as m:
        m.get(OPENSKY_URL, json={'states': []}, status_code=500)
        with pytest.raises(AssertionError):
            find_close(0, 0, 0)


def test_find_close_incorrect_resp():
    with requests_mock.mock() as m:
        m.get(OPENSKY_URL, json={'foo': 'bar'}, status_code=200)
        with pytest.raises(AssertionError):
            find_close(0, 0, 0)
