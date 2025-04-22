import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

data0 = pd.read_csv("ml/datasets/adjusted/PhiUSIIL_Phishing_URL_Dataset_clean.csv", on_bad_lines='skip')
data = data0.drop(['URL'], axis = 1).copy()
y = data['label']
X = data.drop('label',axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)

tree = DecisionTreeClassifier(max_depth = 10) 
tree.fit(X_train, y_train)

y_predict = tree.predict(X_test)

def predict_domain(features, url):
    record = pd.Series(features)
    record = record.iloc[1:]
    record_df = pd.DataFrame([record.values], columns=X_train.columns)
    y_predicted_on_record = tree.predict(record_df)
    if y_predicted_on_record == 1:
        print('URL ' + url + ' is legitimate')
    else:
        print('URL ' + url + ' is likely a phishing')