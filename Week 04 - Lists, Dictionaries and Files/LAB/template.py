"""
RECORD CHECK  -  my version
===========================

Name  : Aryan Illathuveliyil Suseel
Lane  :  AI
Date  :

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return difference, percent and status for a value against its limit."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


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


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            record = {
                "label": parts[0],
                "value": float(parts[1]),
                "limit": float(parts[2])
            }
            records.append(record)
    return records


# ====================================================================== STORE

records = load_records("records.txt")


# =============================================================== PROCESS + OUTPUT

over_limit_count = 0
results = []          # for writing to the output file

for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent, status = check_record(value, limit)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)
    results.append(f"{label},{status}")

# Write results to a new file
with open("results.txt", "w") as file:
    for line in results:
        file.write(line + "\n")

print(f"Total records that were OVER LIMIT: {over_limit_count}")
print("Results also saved to results.txt")