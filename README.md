# Credit Card Default Prediction 💳

## Welcome!  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30">

Welcome and thank you for stopping by. This project focuses on a classification problem, aiming to demonstrate the various steps involved in developing a Machine Learning pipeline (pre-implementation stage).

## Table of contents

- [Motivation](#motivation)
- [About the data](#about-the-data)
- [Results](#results)
- [Dependencies](#dependencies)
- [Using Make to Replicate Analysis](#using-make-to-replicate-analysis)
- [Contributing](#contributing)

## Motivation

The objective of the model predicting whether a credit card client will default or not using [Default of Credit Card Clients Dataset](https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset). In this data set, there are 30,000 examples and 24 features, and the goal is to estimate whether a person will default (fail to pay) their credit card bills; this column is labeled "default.payment.next.month" in the data. The rest of the columns are used as features.

## About the data

This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005. Each record in the dataset is associated with a unique identifier (id) and includes 24 attributes related to each client. Among these attributes, 3 are categorical, while 21 are numeric, encompassing both discrete and continuous values. Below is a summary of the variables of the dataset:

|variable |class     |description |
|:--------|:---------|:-----------|
|ID                            |   int64  |ID of each client|
|LIMIT_BAL                            | float64 | Amount of given credit in NT dollars (includes individual and family/supplementary credit|
| SEX                         |  int64  | Gender (1=male, 2=female)|
| EDUCATION                       |  int64 | (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)|
| MARRIAGE             | int64 |Marital status (1=married, 2=single, 3=others)|
| AGE                  | int64 | Age in years|
| PAY_0                        | int64 |Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)|
| PAY_2                       | int64|  Repayment status in August, 2005 (scale same as above)|
| PAY_3                       | int64 | Repayment status in July, 2005|
| PAY_4                           | int64 | Repayment status in June, 2005|
| PAY_5                 | int64  | Repayment status in May, 2005|
| PAY_6               | int64  | Repayment status in April, 2005|
| BILL_AMT1                     | float64 |  Amount of bill statement in September, 2005 (NT dollar)|
| BILL_AMT2               | float64 | Amount of bill statement in August, 2005 (NT dollar)|
| BILL_AMT3  | int64  | Amount of bill statement in July, 2005 (NT dollar)|
| BILL_AMT4                | float64  |Amount of bill statement in June, 2005 (NT dollar)|
| BILL_AMT5                |float64  |Amount of bill statement in May, 2005 (NT dollar)|
| BILL_AMT6                | float64  | Amount of bill statement in April, 2005 (NT dollar)|
| PAY_AMT1                | float64 |  Amount of previous payment in September, 2005 (NT dollar)|
| PAY_AMT2               | float64  |Amount of previous payment in August, 2005 (NT dollar)|
| PAY_AMT3                | float64 | Amount of previous payment in July, 2005 (NT dollar)|
| PAY_AMT4                | float64  |  Amount of previous payment in June, 2005 (NT dollar)|
| PAY_AMT5                | float64 |  Amount of previous payment in May, 2005 (NT dollar)|
| PAY_AMT6                | float64 |  Amount of previous payment in April, 2005 (NT dollar)|
| default.payment.next.month  | int64 | Default payment (1=yes, 0=no)|

The data set is public and can be found in [kaggle](https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset).

## Results

Report in process, please go to [Notebook](https://github.com/AguilarRaul/Default_class/blob/main/notebooks/complete_pipeline.ipynb) for temporary results.

## Dependencies

To run the report locally, install the project dependencies by following these steps:

1. Clone this repository to your local directory.

2. I created an environment fie: `environment.yaml`. To execute it, go to the root of this repository and run:
   
        conda env create -f environment.yaml


4. Activate it by running:

        conda activate default_credit

## Using Make to Replicate Analysis

To reproduce the report, `Makefile` automates the execution of all essential scripts for data processing, model execution, result generation, and report generation. To do so follow the steps outlined below:

After installing the [dependencies](#dependencies) listed above.

1. Open command line and navigate to the root directory the local repository.

2. Run
   
        make all

To reset the local repository to a clean state, with no intermediate files or results files:

1. Open command line and navigate to the root directory the repository.

2. Run
   
        make clean

## Contributing

Interested in contributing? We are glad you are interested, please check out the [contributing guidelines](https://github.com/AguilarRaul/Default_class/blob/main/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

This project was created by Raul Aguilar Lopez. The materials of this project are licensed under the MIT License. If re-using/re-mixing please provide attribution and link to this webpage.
