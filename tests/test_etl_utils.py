from src.etl_utils import clean_amount
import pytest


def test_clean_amount_basic():
    assert clean_amount('$1,234.56') == 1234.56


def test_clean_amount_int():
    assert clean_amount(100) == 100.0


def test_clean_amount_none():
    assert clean_amount(None) is None


def test_clean_amount_empty():
    assert clean_amount('') is None


def test_clean_amount_bad():
    with pytest.raises(ValueError):
        clean_amount('abc')
