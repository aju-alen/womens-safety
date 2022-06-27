import pandas as pd
from imblearn.over_sampling import SMOTE
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

df=pd.read_csv("dataset.csv")
print(df.head(10))
print(df.shape)
print(df["label"].value_counts())
data=df.dropna()
# print(df.shape)
labels=data["label"]
data.drop('label', axis=1, inplace=True)
print(data.head(10))
print(labels.head(10))
sm = SMOTE(random_state = 2)
Xdata, Ydata = sm.fit_resample(data, labels)

with open('smotesample.pickle', 'wb') as f:
    pickle.dump(sm, f)

print(Xdata.shape)
print(Ydata.shape)
print(Ydata.value_counts())

print(Ydata)

X_train, X_test, y_train, y_test = train_test_split(Xdata, Ydata, test_size = 0.3, random_state = 0)
# X_train=X_train.to_numpy
# X_test=X_test.to_numpy
scaler = MinMaxScaler()
X_train=scaler.fit_transform(X_train)
with open('scaler.pickle', 'wb') as f:
    pickle.dump(scaler, f)
X_test=scaler.transform(X_test)

lr = LogisticRegression(solver='lbfgs', max_iter=1000)
  
# train the model on train set
lr.fit(X_train, y_train.ravel())

with open('LR_model.pickle', 'wb') as f:
    pickle.dump(lr, f)

predictions = lr.predict(X_test)
print(predictions)
score=accuracy_score(y_test, predictions)
print("accuracy score==>",score)