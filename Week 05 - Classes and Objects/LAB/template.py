"""
RECORD CHECK  -  my version
===========================

Name  : Aryan Illathuveliyil Suseel
Lane  :  AI      
Date  :

Run it:   python template.py
"""

# ====================================================================== CLASS

class Record:
    """A single measurement with a label, value and limit."""

    over_limit_count = 0          # class-level running total

    def __init__(self, label, value, limit):
        """Store label, value and limit on the object."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on the percentage of the limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("records.txt")


# ==================================================================== OUTPUT

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")
    print("=" * 34)

print()
print(f"Total records OVER LIMIT: {Record.over_limit_count}")