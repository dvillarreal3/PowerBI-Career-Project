"""
Simple ETL utility functions for learning exercises.

This module includes clean_amount for parsing monetary strings into floats. Docstring examples are included for doctest validation.
"""

import re
from typing import Optional, Union


def clean_amount(s: Optional[Union[str, int, float]]) -> Optional[float]:
    """Convert monetary strings (many locales) or numeric types to float.

    Examples
    --------
    >>> clean_amount('$1,234.56')
    1234.56
    >>> clean_amount('(1,234.56)')
    -1234.56
    >>> clean_amount('1.234,56')
    1234.56
    >>> clean_amount('EUR 1.234,56')
    1234.56
    >>> clean_amount(None) is None
    True

    Supports:
      - Currency symbols/prefixes/suffixes (USD, €, ¥, £, etc.)
      - Thousands separators (comma, dot, space, NBSP)
      - Decimal separators both '.' and ',' with heuristics
      - Accounting parentheses for negatives, e.g. '(1,234.56)'
      - Leading '+' or '-' signs

    Heuristics (simple):
      - If both '.' and ',' appear and '.' comes before ',', treat '.' as thousands and ',' as decimal (e.g. '1.234,56').
      - If only ',' appears and the fraction part length is 2, treat ',' as decimal.
      - If only ',' appears and fraction length is 3, treat ',' as thousands.

    Returns float or None for empty inputs. Raises ValueError for unparseable strings.
    """
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return float(s)

    s = str(s).strip()
    if s == "":
        return None

    # Normalize non-breaking spaces to regular spaces
    s = s.replace('\u00A0', ' ')

    # Detect accounting-style parentheses indicating negative values
    is_negative = False
    if s.startswith('(') and s.endswith(')'):
        is_negative = True
        s = s[1:-1].strip()

    # Remove surrounding plus sign
    if s.startswith('+'):
        s = s[1:].strip()

    # Remove currency codes/letters (e.g., USD, EUR) and leading/trailing currency symbols
    # Keep digits, dot, comma, minus and spaces
    s = re.sub(r"[A-Za-z€£¥₹$]+", '', s).strip()

    # Remove spaces used as thousand separators (e.g., '1 234,56')
    s = re.sub(r'(?<=\d)[ \t](?=\d)', '', s)

    # If both '.' and ',' present, decide which is decimal
    if '.' in s and ',' in s:
        if s.find('.') < s.find(','):
            # '1.234,56' -> remove dots, replace comma with dot
            s = s.replace('.', '').replace(',', '.')
        else:
            # '1,234.56' -> remove commas
            s = s.replace(',', '')
    elif ',' in s and '.' not in s:
        # Only comma present: decide by fraction length
        parts = s.split(',')
        if len(parts) >= 2 and len(parts[-1]) == 2:
            # likely decimal separator
            s = s.replace(',', '.')
        else:
            # likely thousands separator
            s = s.replace(',', '')

    # Remove any remaining characters except digits, dot and minus
    cleaned = re.sub(r"[^0-9.\-]", '', s)
    if cleaned in ("", ".", "-"):
        raise ValueError(f"Cannot parse amount: {s}")

    try:
        value = float(cleaned)
    except ValueError:
        raise ValueError(f"Cannot parse amount: {s}")

    return -value if is_negative else value
