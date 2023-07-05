import numpy as np
import pandas as pd
import os

# Reading the data

train_df = pd.read_csv("data/clean/train.csv")
test_df = pd.read_csv("data/clean/test.csv")


def calculate_longest_unpaid_streak(df):
    """
    Calculates the longest unpaid streak for each row in the DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame containing payment and bill amounts.

    Returns:
        pandas.DataFrame: DataFrame with an additional column 'longest_unpaid_streak',
                          representing the longest unpaid streak for each row.
    """
    df["longest_unpaid_streak"] = df.loc[:, "PAY_0":"PAY_6"].max(axis=1)
    return df


def calculate_total_bill(df):
    """
    Calculates the total bill amount for each row in the DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame containing bill amounts.

    Returns:
        pandas.DataFrame: DataFrame with an additional column 'total_bill',
                          representing the total bill amount for each row.
    """
    df["total_bill"] = df.loc[:, "BILL_AMT1":"BILL_AMT6"].sum(axis=1)
    return df


def calculate_total_paid(df):
    """
    Calculates the total paid amount for each row in the DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame containing payment amounts.

    Returns:
        pandas.DataFrame: DataFrame with an additional column 'total_paid',
                          representing the total paid amount for each row.
    """
    df["total_paid"] = df.loc[:, "PAY_AMT1":"PAY_AMT6"].sum(axis=1)
    return df


def calculate_avg_pay_ratio(df):
    """
    Calculates the average payment ratio for each row in the DataFrame.

    The average payment ratio is calculated as the average of the payment amounts
    divided by the bill amounts for a specific time period.

    Args:
        df (pandas.DataFrame): Input DataFrame containing payment and bill amounts.

    Returns:
        pandas.DataFrame: DataFrame with an additional column 'avg_pay_ratio',
                          representing the average payment ratio for each row.
    """
    np_pay_amt = np.array(df.loc[:, "PAY_AMT1":"PAY_AMT5"])
    np_bill_amt = np.array(df.loc[:, "BILL_AMT2":"BILL_AMT6"])
    avg_pay_ratio = np.average(
        np.divide(
            np_pay_amt,
            np_bill_amt,
            out=np.ones_like(np_pay_amt),
            where=np_bill_amt != 0,
        ),
        axis=1,
    )
    df["avg_pay_ratio"] = avg_pay_ratio
    return df


# Apply transformations to train_df
train_df = calculate_longest_unpaid_streak(train_df)
train_df = calculate_total_bill(train_df)
train_df = calculate_total_paid(train_df)
train_df = calculate_avg_pay_ratio(train_df)

# Apply transformations to test_df
test_df = calculate_longest_unpaid_streak(test_df)
test_df = calculate_total_bill(test_df)
test_df = calculate_total_paid(test_df)
test_df = calculate_avg_pay_ratio(test_df)


dirs = ["data/clean/train_f_eng.csv", "data/clean/test_f_eng.csv"]

for i in dirs:
    directory = os.path.dirname(i)
    os.makedirs(directory, exist_ok=True)

# Write CSV files
train_df.to_csv("data/clean/train_f_eng.csv")
test_df.to_csv("data/clean/test_f_eng.csv")
