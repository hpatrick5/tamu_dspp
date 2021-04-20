# %%
import pandas as pd 
import numpy as np

# %%
df_present = pd.read_csv("Carmichael_grade3_math_meanImpute_ED_CE.csv")
df_present

# %%
#hot code 

df1 = pd.get_dummies(data=df_present,columns=["LEP"])
df1

df2 = pd.get_dummies(data=df1,columns=["Ethnicity"])
df2

df3 = df2.rename(columns={'Special Ed Indicator': 'Special_Ed_Ind'})
df3

df4 = df3.rename(columns={'Meal Status': 'Meal_Stat'})
df4

#change to binary
df4['Special_Ed_Ind']= df4.Special_Ed_Ind.map(dict(Yes=1, No=0))
df4

df4['CE']= df4.CE.map(dict(yes=1, no=0))
df4

mapping = {'01 - Free': 1, '02 - Reduced': 1, 'no': 0}
df4 = df4.replace({'Meal_Stat': mapping})
df4


# %%
#move first column to the end
cols = list(df4.columns.values) #Make a list of all of the columns in the df
cols.pop(cols.index('Percent Score final')) #Remove b from list
df5 = df4[cols+['Percent Score final']] #Create new dataframe with columns in the order you want
#len(df_new2.columns)
df5


# %%
ID = df5.iloc[:, 0:1]
X = df5.iloc[:, 0:15]
y = df5['Percent Score final']

# %%
ID

# %%
X

# %%
y

# %%
from sklearn.model_selection import train_test_split

# %%
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 10)

# %%
X_train

# %%
X_test

# %%
y_test

# %%
from sklearn.linear_model import LinearRegression
clf = LinearRegression()

# %%
clf.fit(X_train,y_train)

# %%
y_pred = clf.predict(X_test)

# %%
clf.score(X_test, y_test)

# %%
df6 = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})


# %%
df6 = pd.concat([df6,X_test], axis=1)
df6

# %%

df6['abs_diff'] = abs(df6['Actual'] - df6['Predicted'])
df6


# %%
#convert back one hot encoding
#I did this manually in excel 
#export to excel
df6.to_csv(r'/Users/sukanyasravasti/LR_Math_Grade3.csv', index = False)


# %%
