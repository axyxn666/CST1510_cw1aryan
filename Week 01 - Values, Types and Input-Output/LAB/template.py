"""
RECORD CHECK  -  my version
===========================

Name  : Aryan Illathuveliyil Suseel
Lane  :  AI
Date  :

Run it:   python template.py
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("Enter a label (name, hostname, or IP): ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.

difference = first - second
percent = (first / second) * 100


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  First     : {first:>10.2f}")
print(f"  Second    : {second:>10.2f}")
print(f"  Difference: {difference:>+10.2f}")
print(f"  Percent   : {percent:>10.2f} %")
print(f"  Note      : first is {percent:.1f}% of second")

print("=" * 34)