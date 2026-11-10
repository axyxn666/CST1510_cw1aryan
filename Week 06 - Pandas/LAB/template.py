"""
RECORD CHECK  -  my version
===========================

Name  : Aryan Illathuveliyil Suseel
Lane  :  AI
Date  : 

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
df = pd.read_csv("records_sample.csv")

# ================================================================= PROCESS
df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)

# ================================================================== OUTPUT
print(df)                              # all rows

print("\nNon-OK rows:")
print(df[df["status"] != "OK"])        # only WARNING / OVER LIMIT

print("\nCount per status:")
print(df.groupby("status").size())     # counts

df.to_csv("cleaned_records.csv", index=False)   # save full result

# bar chart of counts
counts = df["status"].value_counts()
counts.plot(kind="bar", title="Status Counts")
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig("status_chart.png")
plt.show()