import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from data.read_file import *

def cleaner(raw_df):

    duplicates = raw_df[raw_df.duplicated()]
    print("Duplicate Rows : ",len(duplicates))
    print(duplicates.head())

    df = raw_df.drop_duplicates(inplace=True)
    df = raw_df.dropna(inplace=True)
    print("woks")

    df = raw_df.to_csv("../data/processed/clean_data.csv")
    return df

cleaner(read_data(file_path))
