"""
RECORD CHECK  -  my version
===========================

Name  : Aryan Illathuveliyil Suseel
Lane  :  AI
Date  : 

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one messy status line and return a dict with hostname, used, total."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"]
    }


def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK based on usage percentage."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT

raw_records = []
with open("messy_records.txt") as f:
    for line in f:
        raw_records.append(line.strip())


# =============================================================== PROCESS + OUTPUT

flagged = 0

for raw in raw_records:
    try:
        record = parse_line(raw)
        status = status_of(record["used"], record["total"])
        print(record, "→", status)

        if status != "OK":
            flagged += 1
    except ValueError:
        print("Could not parse:", raw)

print()
print(f"Summary: {len(raw_records)} records, {flagged} flagged")