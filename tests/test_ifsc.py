from ifsclookup import get_ifsc


def test_ifsc_function():
    result = get_ifsc("SBIN0005943")
    assert isinstance(result, dict)