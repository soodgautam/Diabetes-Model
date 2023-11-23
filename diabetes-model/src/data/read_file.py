import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

def read_data(file_path):
    raw_df = pd.read_csv(file_path)
    return raw_df

file_path = ("../data/external/diabetes_binary_health_indicators_BRFSS2015.csv")
raw_df = read_data(file_path)


