# %%
import pandas as pd 

# %%
df_present = pd.read_csv("pre_model_format_read.csv")
df_present

# %%
#hot code meal status and temp lunch

#first convert missing values for meal status to null
values = {'Meal Status': "Null"}
df_present = df_present.fillna(value=values)

#then hotcode
df_new = pd.get_dummies(data=df_present,columns=["Meal Status"])
df_new


#hotcode temp lunch
df_new1 = pd.get_dummies(data=df_new,columns=["Temp Lunch Status"])
df_new1

#df_new2 = df_new1.astype(int)
#df_new2

# %%
#fill in missing scores with average of the last scores
#dropped ID 309795 since it was missing all reading scores
#I did this manually in excel. Needs to be automated

# %%
#move first column to the end
cols = list(df_new1.columns.values) #Make a list of all of the columns in the df
cols.pop(cols.index('Grade_4_Present_Reading_ Percent_Score')) #Remove b from list
df_new2 = df_new1[cols+['Grade_4_Present_Reading_ Percent_Score']] #Create new dataframe with columns in the order you want
len(df_new2.columns)
df_new2


# %%
X = df_new2.iloc[:, 1:20]
y = df_new2['Grade_4_Present_Reading_ Percent_Score']

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
df1 = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
#df1=df1['Actual']*100
#df1
df1['Actual']=df1['Actual']*100
df1['Predicted']=df1['Predicted']*100
df1

# %%
df3 = pd.concat([df1,X_test], axis=1)

# %%
df3['Grade_4_last_year_Reading_Percent_Score']=df3['Grade_4_last_year_Reading_Percent_Score']*100
df3['Grade_4_Practice2018_Reading_Percent Score']=df3['Grade_4_Practice2018_Reading_Percent Score']*100
df3['Grade_4_Practice2019_Reading_Percent_Score_x']=df3['Grade_4_Practice2019_Reading_Percent_Score_x']*100
df3


# %%

df3['abs_diff'] = abs(df3['Actual'] - df3['Predicted'])
df3


# %%
#convert back one hot encoding
#I did this manually in excel 
#export to excel
df3.to_csv(r'/Users/sukanyasravasti/LR_Reading_Grade4.csv', index = False)


# %%
