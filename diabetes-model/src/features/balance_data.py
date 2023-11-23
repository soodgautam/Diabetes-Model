
from sklearn.utils import resample
import pandas as pd

def read_data(file_path):
    raw_df = pd.read_csv(file_path)
    return raw_df

def balance_data(df):

    df_majority = df[df.Diabetes_binary == 0]
    df_minority = df[df.Diabetes_binary == 1]

    # Upsample minority class
    df_minority_upsampled = resample(df_minority, 
                                     replace=True,     # sample with replacement
                                     n_samples=df_majority.shape[0],    # to match majority class
                                     random_state=123) # reproducible results

    # Combine majority class with upsampled minority class
    df_upsampled = pd.concat([df_majority, df_minority_upsampled])

    # Display new class counts
    print(df_upsampled.Diabetes_binary.value_counts())

    return df_upsampled

def main():
    # Read in CSV file
    df = pd.read_csv('../data/processed/selected_data.csv')

    # Balance the data
    df_balanced = balance_data(df)

    # Save the balanced data to a new CSV file
    df_balanced.to_csv('../data/processed/balanced_data.csv', index=False)

if __name__ == '__main__':
   
    main()
