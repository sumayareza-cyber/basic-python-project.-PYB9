# Student Performance Data Analysis using Matplotlib & Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample dataset
data = {
    "Name": ["Morice", "Jenny", "Robert", "David", "Jenna", "Devid", "Asha", "Michael"],
    "Math": [80, 70, 90, 70, 75, 95, 82, 65],
    "Science": [88, 77, 85, 75, 80, 92, 78, 60],
    "English": [78, 72, 80, 66, 74, 84, 82, 68],
    "Sports": [90, 85, 75, 50, 95, 80, 75, 60]
}

df = pd.DataFrame(data)

# ======================
# 1. Line Plot (Math scores trend)
# ======================
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Math"], marker="o", linestyle="-", color="b", label="Math Scores")
plt.title("Line Plot - Math Scores of Students")
plt.xlabel("Students")
plt.ylabel("Math Score")
plt.legend()
plt.show()

# ======================
# 2. Bar Plot (Average scores per subject)
# ======================
avg_scores = df[["Math","Science","English","Sports"]].mean()
plt.figure(figsize=(8,5))
sns.barplot(x=avg_scores.index, y=avg_scores.values, palette="viridis")
plt.title("Bar Plot - Average Scores per Subject")
plt.ylabel("Average Score")
plt.show()

# ======================
# 3. Pie Chart (Distribution of Sports scores)
# ======================
plt.figure(figsize=(6,6))
plt.pie(df["Sports"], labels=df["Name"], autopct="%1.1f%%", startangle=140)
plt.title("Pie Chart - Sports Scores Distribution")
plt.show()

# ======================
# 4. Box Plot (Spread of scores across subjects)
# ======================
plt.figure(figsize=(8,5))
sns.boxplot(data=df[["Math","Science","English","Sports"]], palette="Set2")
plt.title("Box Plot - Score Distribution by Subject")
plt.ylabel("Scores")
plt.show()

# ======================
# 5. Heatmap (Correlation between subjects)
# ======================
plt.figure(figsize=(6,4))
sns.heatmap(df[["Math","Science","English","Sports"]].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap - Correlation between Subjects")
plt.show()