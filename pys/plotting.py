import polars as pl
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def age_plot(polars_df):
    # Convert the 'smokes' column to a category type if it's not already
    df = polars_df.to_pandas()
    df['alive'] = df['alive'].map({1: 'Alive', 0: 'Dead'})
    df["smokes"] = df["smokes"].astype("category")

    # Create the boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="smokes", y="age", data=df)
    plt.title("Age vs Smoking Status")
    plt.xlabel("Smoker Status")
    plt.ylabel("Age")
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x="alive", y="age", data=df)
    plt.title("Age vs Outcome (Alive/Dead)")
    plt.xlabel("Outcome")
    plt.ylabel("Age")
    plt.show()

def age_distribution_plot(polars_df):
    df = polars_df.to_pandas()
    df["smokes"] = df["smokes"].astype("category")
    
    # Plot the KDE plot for age distribution by smoking status
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x="age", hue="smokes", fill=True, common_norm=False)
    
    # Add labels and title
    plt.title("Age Distribution by Smoking Status")
    plt.xlabel("Age")
    plt.ylabel("Density")
    plt.legend(title="Smoking Status", labels=["Smoker", "Non-Smoker"])
    
    # Show the plot
    plt.show()

def salary_plot(polars_df):
    # Convert the 'smokes' column to a category type if it's not already
    df = polars_df.to_pandas()
    df['alive'] = df['alive'].map({1: 'Alive', 0: 'Dead'})
    df["smokes"] = df["smokes"].astype("category")

    # Create the boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="smokes", y="salary", data=df)
    plt.title("Salary vs Smoking Status")
    plt.xlabel("Smoker Status")
    plt.ylabel("Age")
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x="alive", y="salary", data=df)
    plt.title("Salary vs Outcome (Alive/Dead)")
    plt.xlabel("Outcome")
    plt.ylabel("Age")
    plt.show()

def gender_count_plot(polars_df):
    # Convert the 'smokes' and 'alive' columns to appropriate categories
    df = polars_df.to_pandas()
    df["smokes"] = df["smokes"].astype("category")
    df["alive"] = df["alive"].map({1: "Alive", 0: "Dead"})
    df["gender"] = df["gender"].astype("category")

    # Count plot for Gender by Smoking Status
    plt.figure(figsize=(8, 6))
    sns.countplot(x="smokes", hue="gender", data=df)
    plt.title("Gender Distribution by Smoking Status")
    plt.xlabel("Smoking Status")
    plt.ylabel("Count")
    plt.show()

    # Count plot for Gender by Outcome (Alive/Dead)
    plt.figure(figsize=(8, 6))
    sns.countplot(x="alive", hue="gender", data=df)
    plt.title("Gender Distribution by Outcome (Alive/Dead)")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.show()