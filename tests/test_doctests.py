import doctest
import src.etl_utils as etl


def test_doctests():
    res = doctest.testmod(etl, verbose=False)
    assert res.failed == 0
