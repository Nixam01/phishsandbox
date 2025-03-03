import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

data0 = pd.read_csv("ml/datasets/adjusted/PhiUSIIL_Phishing_URL_Dataset_clean.csv", on_bad_lines='skip')
data = data0.drop(['URL'], axis = 1).copy()
y = data['label']
X = data.drop('label',axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)
X_train.shape, X_test.shape

tree = DecisionTreeClassifier(max_depth = 10) 
tree.fit(X_train, y_train)

y_predict = tree.predict(X_test)

acc_test_tree = accuracy_score(y_test,y_predict)
print("Decision Tree: Accuracy on test Data: {:.10f}".format(acc_test_tree))


def predict_domain(features):
    testrecord_df = pd.DataFrame(features, columns=X_train.columns)
    y_predicted_on_record = tree.predict(testrecord_df)
    print(y_predicted_on_record)