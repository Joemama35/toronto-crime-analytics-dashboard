import pandas as pd
import matplotlib.pyplot as plt

# Load summary data
crime_by_year = pd.read_csv("Data/crime_by_year.csv")
crime_by_type = pd.read_csv("Data/crime_by_type.csv")
top_neighbourhoods = pd.read_csv("Data/top_neighbourhoods.csv")

# -----------------------
# Crime by Year
# -----------------------
plt.figure(figsize=(10,5))
plt.plot(crime_by_year["Year"], crime_by_year["Crime_Count"], marker="o")
plt.title("Total Crime by Year")
plt.xlabel("Year")
plt.ylabel("Crime Count")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/crime_by_year.png")
plt.close()

# -----------------------
# Crime by Type
# -----------------------
plt.figure(figsize=(10,5))
plt.bar(crime_by_type["Crime_Type"], crime_by_type["Crime_Count"])
plt.title("Crime by Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/crime_by_type.png")
plt.close()

# -----------------------
# Top 10 Neighbourhoods
# -----------------------
plt.figure(figsize=(12,6))
plt.barh(
    top_neighbourhoods["Neighbourhood"],
    top_neighbourhoods["Crime_Count"]
)
plt.title("Top 10 Neighbourhoods by Crime")
plt.tight_layout()
plt.savefig("images/top_neighbourhoods.png")
plt.close()

print("Charts created successfully!")