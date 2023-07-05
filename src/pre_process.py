import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Reading the data and displaying the first few rows
def_data = pd.read_csv("data/raw/UCI_Credit_Card.csv")

# Pre processing, intial waringling
def_data = def_data.rename(
    columns={"default.payment.next.month": "default"}
)  # renaming target

df = def_data[
    def_data.loc[:, "BILL_AMT1":"BILL_AMT6"].sum(axis=1) != 0
]  # removing peple with no bill amount

df = df.drop(columns=["SEX"])  # remove sex column for potential bias

train_df, test_df = train_test_split(
    df, test_size=0.2, random_state=573
)  # data split


# Pre processing, after EDA
def recategorize_column(df, column, to_replace, replacement):
    df[column] = df[column].replace(to_replace, replacement)


# Recategorize education and marriage columns in train_df
recategorize_column(train_df, "EDUCATION", [0, 5, 6], 4)
recategorize_column(train_df, "MARRIAGE", 0, 3)

# Recategorize education and marriage columns in test_df
recategorize_column(test_df, "EDUCATION", [0, 5, 6], 4)
recategorize_column(test_df, "MARRIAGE", 0, 3)

dirs = ["data/clean/train.csv", "data/clean/test.csv"]

for i in dirs:
    directory = os.path.dirname(i)
    os.makedirs(directory, exist_ok=True)

# Write CSV files
train_df.to_csv("data/clean/train.csv")
test_df.to_csv("data/clean/test.csv")
