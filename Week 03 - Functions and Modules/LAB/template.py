"""
RECORD CHECK  -  my version
===========================

Name  : Aryan Illathuveliyil Suseel
Lane  :  AI
Date  :

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return OVER LIMIT, WARNING or OK based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value relative to limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted record check report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value     : {value:>10.2f}")
    print(f"  Limit     : {limit:>10.2f}")
    print(f"  Difference: {difference:>+10.2f}")
    print(f"  Percent   : {percent:>10.2f} %")
    print(f"  Status    : {status}")
    print("=" * 34)
    print()


# ==================================================================== MAIN

over_limit_count = 0

while True:
    label = input("Enter a label (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)

print(f"Total records that were OVER LIMIT: {over_limit_count}")