import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

from sklearn.preprocessing import StandardScaler
class DataSplitter:

    def __init__(self, test_size=0.2, random_state=42):
        self.test_size = test_size
        self.random_state = random_state

    
    def split_data(self, df, target_col):
        X = df.drop(target_col, axis=1)
        y = df[target_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)

        return X_train, X_test, y_train, y_test




class DataScaler:
    def __init__(self):
        self.scalar = StandardScaler()


    def fit_transform(self, X_train, X_test):
        X_train_scaled = self.scalar.fit_transform(X_train)
        X_test_scaled = self.scalar.transform(X_test)

        return X_train_scaled, X_test_scaled
    

class LogRegModel:
    def __init__(self):
        self.lr = LogisticRegression()
 
    def train(self, X_train_scaled, y_train):
        self.lr.fit(X_train_scaled, y_train)
        
    def predict(self, X_test_scaled):
        return self.lr.predict(X_test_scaled)
    
    def evaluate(self, X_test_scaled, y_test):
        accuracy = self.lr.score(X_test_scaled, y_test)
        print(f"Accuracy: {accuracy:.4f}")
  
        y_pred = self.lr.predict(X_test_scaled)
        cm = confusion_matrix(y_test, y_pred)
        print(f"Confusion Matrix:\n{cm}")

    
class GausClassifier:
    def __init__(self):
        self.clf = GaussianNB()

    def train(self, X_train_scaled, y_train):
        self.clf.fit(X_train_scaled, y_train)
        
    def predict(self, X_test_scaled):
        return self.clf.predict(X_test_scaled)
    
    def evaluate(self, X_test_scaled, y_test):
        accuracy = self.clf.score(X_test_scaled, y_test)
        print(f"Accuracy: {accuracy:.4f}")
        y_pred = self.clf.predict(X_test_scaled)
        cm = confusion_matrix(y_test, y_pred)
        print(f"Confusion Matrix:\n{cm}")
    
class RandForClassifier:

    def __init__(self):
        self.clf = RandomForestClassifier(n_estimators=100, criterion= 'gini')

    def train(self, x_train_scaled, y_train):
        self.clf.fit(x_train_scaled, y_train)

    def predict(self, X_test_scaled):
        return self.clf.predict(X_test_scaled)
    
    def evaluate(self, X_test_scaled, y_test):
        accuracy = self.clf.score(X_test_scaled, y_test)
        print(f"Accuracy: {accuracy:.4f}")

        y_pred = self.clf.predict(X_test_scaled)
        cm = confusion_matrix(y_test, y_pred)
        print(f"Confusion Matrix:\n{cm}")

from sklearn.tree import DecisionTreeClassifier

class DecTreeClassifier:
    def __init__(self, criterion='gini', max_depth=None, random_state=None):
        self.clf = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, random_state=random_state)
        
    def train(self, X_train_scaled, y_train):
        self.clf.fit(X_train_scaled, y_train)
        
    def predict(self, X_test_scaled):
        return self.clf.predict(X_test_scaled)
    
    def evaluate(self, X_test_scaled, y_test):
        accuracy = self.clf.score(X_test_scaled, y_test)
        print(f"Accuracy: {accuracy:.4f}")

        y_pred = self.clf.predict(X_test_scaled)
        cm = confusion_matrix(y_test, y_pred)

        print(f"Confusion Matrix:\n{cm}")

    
def main():
    file_path = "../data/processed/balanced_data.csv"
    df = pd.read_csv(file_path)
    #df.drop("Unnamed: 0")
    target_col = 'Diabetes_binary'
    
    data_splitter = DataSplitter()
    X_train, X_test, y_train, y_test = data_splitter.split_data(df, target_col)

    data_scaler = DataScaler()
    X_train_scaled, X_test_scaled = data_scaler.fit_transform(X_train, X_test)

        
    logreg_model = LogRegModel()
    logreg_model.train(X_train_scaled, y_train)

    y_pred = logreg_model.predict(X_test_scaled)
    print("Logistic Regression Accuracy:", (y_test == y_pred).mean())
   
    print("Logistic Regression Score: ")
    logreg_model.evaluate(X_test_scaled, y_test)


    GNB_classifier = GausClassifier()
    GNB_classifier.train(X_train_scaled, y_train)



    y_pred = GNB_classifier.predict(X_test_scaled)
    print("GNB Accuracy:", (y_test == y_pred).mean())
    print("GNB score")
    GNB_classifier.evaluate(X_test_scaled, y_test)


    RF_classifier = RandForClassifier()
    RF_classifier.train(X_train_scaled, y_train)


    y_pred = RF_classifier.predict(X_test_scaled)
    print("Random Forrest Accuracy:", (y_test == y_pred).mean())

    RF_classifier.evaluate(X_test_scaled, y_test)




    DTreeClassifier = DecTreeClassifier()
    DTreeClassifier.train(X_train_scaled, y_train)

    y_pred = DTreeClassifier.predict(X_test_scaled)
    print("Decision Tree Accuracy:", (y_test == y_pred).mean())

    print(DTreeClassifier.evaluate(X_test_scaled, y_test))



if __name__ == '__main__':
    main()
