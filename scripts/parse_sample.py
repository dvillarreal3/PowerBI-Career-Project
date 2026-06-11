"""Simple script to parse sample CSV using clean_amount and print results."""
import csv
from src.etl_utils import clean_amount

INPUT = 'data/sample_transactions.csv'

if __name__ == '__main__':
    with open(INPUT, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw = row.get('amount')
            try:
                val = clean_amount(raw)
            except Exception as e:
                val = f'ERROR: {e}'
            print(f"id={row.get('id')}, desc={row.get('description')}, raw={raw!r}, parsed={val}")
