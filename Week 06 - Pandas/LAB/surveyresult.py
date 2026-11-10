
import pandas as pd
import matplotlib.pyplot as plt  

# 1. Load and look
df = pd.read_csv("survey_results.csv")
print(df.head())
print(df.dtypes)
print(len(df))

# 2. Measure the gap (percentage unanswered)
unanswered = len(df[df["answered"] == 0])
percent_unanswered = (unanswered / len(df)) * 100
print(f"Unanswered: {percent_unanswered:.1f}%")

# 3. Filter it clean (only answered == 1)
clean = df[df["answered"] == 1].copy()

# 4. Group it – average score per category
avg_by_category = clean.groupby("category")["score"].mean()
print(avg_by_category)

# 5. Sort it – strongest category
print(avg_by_category.sort_values(ascending=False))

# 6. Classify it – Pass / Fail
clean["result"] = clean["score"].apply(lambda s: "Pass" if s >= 60 else "Fail")
print(clean[["category", "score", "result"]])

# 7. Chart it
clean["result"].value_counts().plot(kind="bar")
plt.title("Pass vs Fail Counts")
plt.ylabel("Number of responses")
plt.tight_layout()
plt.savefig("pass_fail_chart.png")
plt.show()

# 8. Save it
clean.to_csv("survey_results_clean.csv", index=False)

