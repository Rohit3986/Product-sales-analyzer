# -*- coding: utf-8 -*-
"""big_market_sales.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JvCyOV2JBf4YmF-uDlfN0edj-lZRpPEa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data1=pd.read_csv('Train.csv')

data1.head()

data1.isnull().sum()

data1.shape

sns.kdeplot(data1.Item_Weight)
plt.show()

sns.distplot(data1.Item_Weight)
plt.show()

data1.describe()

data1.Item_Weight=data1.Item_Weight.fillna(data1.Item_Weight.mean())

data1.isnull().sum()

data1.Outlet_Size.mode()

data1.Outlet_Size.value_counts()

data1["Outlet_Size"]=data1["Outlet_Size"].fillna(value="Medium")

data1.Outlet_Size.isnull().sum()

data1.Outlet_Size.value_counts()

data1.isnull().sum()

data1

data1.Item_Identifier.unique

data1.Outlet_Identifier.unique

data1=data1.drop(columns='Item_Identifier',axis=1)

data1.shape

data1=data1.drop(columns='Outlet_Identifier',axis=1)

data1.shape

"""EDA USING DTAIL"""

!pip install dtale

import dtale

data2=pd.DataFrame(data1)

dtale.instances()

import dtale.app as dtale_app

dtale_app.USE_COLAB=True

dtale.show(data2)

sns.heatmap(data2.corr(),annot=True)
plt.show()

from sklearn.preprocessing import LabelEncoder

lr=LabelEncoder()

data3=pd.get_dummies(data2,columns=["Outlet_Type"],drop_first=True)

data3.head()

data3=data3.apply(lr.fit_transform)

data3.head()

from sklearn.model_selection import train_test_split

X=data3.drop(columns="Item_Outlet_Sales",axis=1)

X.head()

Y=data3["Item_Outlet_Sales"]

X.shape

Y.shape

Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.2,random_state=51)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

Xtrain_std=sc.fit_transform(Xtrain)

Xtest_std=sc.transform(Xtest)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(Xtrain_std,Ytrain)

lr.predict(Xtest_std)

Ytest

lr.score(Xtest_std,Ytest)

from sklearn.ensemble import  RandomForestRegressor

rf=RandomForestRegressor()

rf.fit(Xtrain_std,Ytrain)

rf.score(Xtest_std,Ytest)

"""here we can maximixe our accuracy by doing hyper parameter tuning in random forest regrresor

"""

from sklearn.model_selection import GridSearchCV

model=RandomForestRegressor()

n_estimators=[10,100,1000]
criterion=["mse", "mae"]
max_depth=range(1,31)
min_samples_leaf=np.linspace(0.1,1)
max_features = ["auto", "sqrt", "log2"]

grid=dict(n_estimators=n_estimators,criterion=criterion,max_depth=max_depth,max_features=max_features)

gridsrchforeset=GridSearchCV(estimator=model,param_grid=grid,scoring='f1',cv=3)

gridsrchforeset.fit(Xtrain_std,Ytrain)

