import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# MOVIE DATA ANALYSIS
# ============================================================

# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

file_path = "../data/imdb_top_1000.csv"

df = pd.read_csv(r"C:\Users\AFNAFATHIMA\Downloads\archive (4)\imdb_top_1000.csv")

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())


# ------------------------------------------------------------
# 2. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 3. DATA PREPROCESSING
# ------------------------------------------------------------

# Keep only rows where important columns are available
required_columns = [
    "Genre",
    "IMDB_Rating",
    "Released_Year",
    "Gross",
    "Runtime"
]

df = df.dropna(subset=required_columns)

# Convert Released_Year to numeric
df["Released_Year"] = pd.to_numeric(
    df["Released_Year"],
    errors="coerce"
)

# Convert Gross to numeric
df["Gross"] = (
    df["Gross"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["Gross"] = pd.to_numeric(
    df["Gross"],
    errors="coerce"
)

# Convert Runtime to numeric
df["Runtime"] = (
    df["Runtime"]
    .astype(str)
    .str.replace(" min", "", regex=False)
)

df["Runtime"] = pd.to_numeric(
    df["Runtime"],
    errors="coerce"
)

# Remove rows created with invalid numeric values
df = df.dropna(
    subset=[
        "Released_Year",
        "Gross",
        "Runtime"
    ]
)

print("\nAfter Data Cleaning:")
print("Dataset Shape:", df.shape)


# ============================================================
# 4. GENRE-WISE MOVIE COUNT
# ============================================================

genre_count = (
    df["Genre"]
    .value_counts()
)

print("\n======================================")
print("GENRE-WISE MOVIE COUNT")
print("======================================")

print(genre_count)


# ============================================================
# 5. AVERAGE RATING BY GENRE
# ============================================================

genre_avg_rating = (
    df.groupby("Genre")["IMDB_Rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\n======================================")
print("AVERAGE RATING BY GENRE")
print("======================================")

print(genre_avg_rating)


# ============================================================
# 6. AVERAGE REVENUE BY GENRE
# ============================================================

genre_avg_revenue = (
    df.groupby("Genre")["Gross"]
    .mean()
    .sort_values(ascending=False)
)

print("\n======================================")
print("AVERAGE REVENUE BY GENRE")
print("======================================")

print(genre_avg_revenue)


# ============================================================
# 7. BASIC MOVIE INFORMATION
# ============================================================

print("\n======================================")
print("BASIC MOVIE INFORMATION")
print("======================================")

print("Total Movies:", len(df))

print(
    "Highest Rated Movie:",
    df.loc[df["IMDB_Rating"].idxmax(), "Series_Title"]
)

print(
    "Highest Rating:",
    df["IMDB_Rating"].max()
)

print(
    "Highest Revenue Movie:",
    df.loc[df["Gross"].idxmax(), "Series_Title"]
)

print(
    "Highest Revenue:",
    df["Gross"].max()
)


# ============================================================
# 8. VISUALIZATION 1 - RATING DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["IMDB_Rating"],
    bins=15,
    kde=True
)

plt.title("Distribution of IMDb Ratings")
plt.xlabel("IMDb Rating")
plt.ylabel("Number of Movies")

plt.tight_layout()

# Display graph only
plt.show()


# ============================================================
# 9. VISUALIZATION 2 - MOVIES RELEASED BY YEAR
# ============================================================

movies_per_year = (
    df["Released_Year"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12, 6))

plt.plot(
    movies_per_year.index,
    movies_per_year.values,
    marker="o"
)

plt.title("Movies Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Movies")

plt.xticks(rotation=45)

plt.tight_layout()

# Display graph only
plt.show()


# ============================================================
# 10. VISUALIZATION 3 - GENRE-WISE AVERAGE RATING
# ============================================================

top_genres_rating = (
    genre_avg_rating
    .head(15)
    .sort_values()
)

plt.figure(figsize=(10, 7))

plt.barh(
    top_genres_rating.index,
    top_genres_rating.values
)

plt.title("Top 15 Genres by Average IMDb Rating")
plt.xlabel("Average IMDb Rating")
plt.ylabel("Genre")

plt.tight_layout()

# Display graph only
plt.show()


# ============================================================
# 11. VISUALIZATION 4 - GENRE-WISE AVERAGE REVENUE
# ============================================================

top_genres_revenue = (
    genre_avg_revenue
    .head(15)
    .sort_values()
)

plt.figure(figsize=(10, 7))

plt.barh(
    top_genres_revenue.index,
    top_genres_revenue.values
)

plt.title("Top 15 Genres by Average Revenue")
plt.xlabel("Average Revenue")
plt.ylabel("Genre")

plt.tight_layout()

# Display graph only
plt.show()


# ============================================================
# 12. FINAL MESSAGE
# ============================================================

print("\n======================================")
print("MOVIE DATA ANALYSIS COMPLETED!")
print("======================================")

print("\nAll analysis results were displayed above.")
print("All graphs were displayed on screen.")
print("No visualization files were saved.")