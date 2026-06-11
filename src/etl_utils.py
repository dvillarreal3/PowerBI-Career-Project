"""
Simple ETL utility functions for learning exercises.
"""

import re
from typing import Optional


def clean_amount(s) -> Optional[float]:
    """Convert monetary strings (e.g. '$1,234.56', '1,234.56') or numeric types to float.

    Returns:
        float value or None if input is None or empty string.
    Raises:
        ValueError for unparseable strings.
    """
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return float(s)
    s = str(s).strip()
    if s == "":
        return None
    # Remove currency symbols and thousands separators, keep digits, dot, minus
    cleaned = re.sub(r"[^0-9.\-]", "", s)
    try:
        return float(cleaned)
    except ValueError:
        raise ValueError(f"Cannot parse amount: {s}")
