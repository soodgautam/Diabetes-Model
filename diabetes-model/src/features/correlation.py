import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_correlation_matrix(df):
    plt.figure(figsize=(15,15))
    correlation_mat = df.corr()
    sns.heatmap(correlation_mat, annot = True)


    plt.savefig("../reports/figures/correlationMatrix.png")
    
    plt.show()





def correlation_with_diabetes(df):
    plt.figure(figsize=(15,15))
    df2 = df.copy()
    x = df2.drop("Diabetes_binary", axis=1).apply(lambda x: x.corr(df.Diabetes_binary))
    plt.plot(x)
 
    #plt.hlines(y=0, xmin=4, xmax=20, linewidth=2, color='r')
    plt.hlines(y=0, xmin=0, xmax=16, linewidth=2, color='r')
    plt.xticks(rotation = 90)

    plt.savefig("../reports/figures/correlationWithDiabetes.png")
    plt.show()


def main():
    df = pd.read_csv('../data/processed/clean_data.csv')
    plot_correlation_matrix(df)
    correlation_with_diabetes(df)

if __name__ == '__main__':

    main()