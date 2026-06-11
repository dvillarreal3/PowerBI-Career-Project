import pytest
from src.etl_utils import clean_amount

@pytest.mark.parametrize("input_val,expected", [
    ("$1,234.56", 1234.56),
    ("1,234.56", 1234.56),
    ("-1,234.56", -1234.56),
    ("(1,234.56)", -1234.56),
    ("$ -1,234.56", -1234.56),
    ("  1234.56 ", 1234.56),
    (1234.56, 1234.56),
    (None, None),
    ("EUR 1.234,56", 1234.56),
    ("1.234,56 €", 1234.56),
    ("USD 1,234", 1234.0),
    ("1 234,56", 1234.56),
    ("1\u00A0234,56", 1234.56),
    ("+1,234.56", 1234.56),
    ("($1,234.56)", -1234.56),
    ("( $ 1,234.56 )", -1234.56),
    ("¥1,234", 1234.0),
    ("1,234.567", 1234.567),
])
def test_clean_amount_various(input_val, expected):
    assert clean_amount(input_val) == expected


def test_clean_amount_raises_on_bad():
    with pytest.raises(ValueError):
        clean_amount('abc')
