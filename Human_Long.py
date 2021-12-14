import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import re
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import r2_score,mean_squared_error
from tensorflow import keras
import os.path

from sklearn import model_selection, datasets
from sklearn.tree import DecisionTreeClassifier
import joblib
import pickle

sd = pd.read_csv("test21.csv",encoding='latin1')

print(pd.isnull(sd).sum().sum())


print(sd.REPORTING_AREA.dtype)

off_code_count =sd.OFFENSE_CODE.value_counts()
off_group_count = sd.OFFENSE_CODE_GROUP.value_counts()
off_des_count = sd.OFFENSE_DESCRIPTION.value_counts()
district_count = sd.DISTRICT.value_counts()
report_area_count = sd.REPORTING_AREA.value_counts()
year_count = sd.YEAR.value_counts()
month_count = sd.MONTH.value_counts()
day_count = sd.DAY_OF_WEEK.value_counts()
hour_count = sd.HOUR.value_counts()
street_count = sd.STREET.value_counts()


X = sd.drop('SHOOTING',1)

X['REPORTING_AREA'] = X['REPORTING_AREA'].replace(" ","0")

Y = X.dropna(how = 'any')

Y = Y.drop(['INCIDENT_NUMBER','OCCURRED_ON_DATE','Location'], axis =1)

Y['MONTH']= Y['MONTH'].astype(float)

Y['OFFENSE_CODE_GROUP'] = Y['OFFENSE_CODE_GROUP'].replace(['Missing Person Located','Missing Person Reported','Prostitution',
                                                           'Verbal Disputes','Disorderly Conduct','Harassment','Offenses Against Child / Family'],'Humanity related')

Y = Y[Y.OFFENSE_CODE_GROUP == 'Humanity related']

target_long = Y.iloc[:,[12]]

Y = Y.drop(['OFFENSE_CODE','OFFENSE_DESCRIPTION','Lat','Long','YEAR'],axis =1)

features =pd.get_dummies(Y, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )

# dumping the featrues count for later use in GUI

feat_dummies = "Feat_human.joblib"
feat_nodummies = "Feat_human_nodummy.joblib"

joblib.dump(features,feat_dummies)
joblib.dump(Y,feat_nodummies)

# model for Lat

X_train, X_test, Y_train, Y_test = train_test_split(features, target_long,test_size = 0.25)


print(X_train.shape)   
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

i = 8

Long_model = tree.DecisionTreeRegressor(max_depth =i)

Long_model.fit(X_train,Y_train)

Y_predict = Long_model.predict(X_test)

r2Sore =r2_score(Y_test,Y_predict)
mse = mean_squared_error(Y_test,Y_predict)
print('\n r2Sore FOR LONG for tree depth :',i,' is : ',r2Sore)
print ('\n mse FOR LONG for tree depth :',i,' is : ',mse)

# saving models

# filename = "Human_Long.joblib"
# joblib.dump(Long_model,filename)

