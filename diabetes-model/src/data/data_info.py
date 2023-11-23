from data.read_file import *

pyfile_path = ("../data/external/diabetes_binary_health_indicators_BRFSS2015.csv")
raw_df = read_data(file_path)

print(raw_df.head())

def grab_info(raw_df):

    print("Head")
    print(raw_df.head())
    print(" ")
    print("Tail")
    print(raw_df.tail())
    print("describe")
    print(raw_df.describe())
    print("checkmissing")
    print(print(raw_df.isna().any()))
    print("check duplicates")
    duplicates = raw_df[raw_df.duplicated()]
    print("Duplicate Rows : ",len(duplicates))
    return

grab_info(read_data(file_path))
