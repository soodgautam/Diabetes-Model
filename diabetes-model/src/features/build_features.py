#balance
from sklearn.feature_selection import SelectPercentile, chi2
import numpy as np
import pandas as pd

from sklearn.feature_selection import SelectPercentile, chi2
import numpy as np
import pandas as pd

def read_data(file_path):
    raw_df = pd.read_csv(file_path)
    return raw_df

def feature_selection(df):
    X = df.drop(['Diabetes_binary'], axis=1)
    y = df['Diabetes_binary']

    # Select top 75% features using chi-squared statistical test
    selector = SelectPercentile(chi2, percentile=75)
    X_new = selector.fit_transform(X, y)

    # Get feature scores and names
    scores = selector.scores_
    feature_names = X.columns

    # Create table of scores and feature names
    table = pd.DataFrame({'Feature Name': feature_names, 'Score': scores})
    table = table.sort_values('Score', ascending=False).reset_index(drop=True)

    # Print table
    print(table)

    # Get indices of selected features
    selected_features = selector.get_support(indices=True)

    # Create new DataFrame with only the selected features
    X_selected = X.iloc[:, selected_features]
    y_selected = y
    selected_df = pd.concat([X_selected, y_selected], axis=1)

    return selected_df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def main():
    file_path = "../data/processed/clean_data.csv"
    selected_file_path = "../data/processed/selected_data.csv"

    df = read_data(file_path)
    selected_df = feature_selection(df)
    save_data(selected_df, selected_file_path)
    print(f"Selected data saved to {selected_file_path}")

if __name__ == '__main__':
    main()


