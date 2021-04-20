# %%
import pandas as pd 
import numpy as np

# %%
'''
##Preprocessing-Grade4
'''

# %%
df = pd.read_excel("Preprocessed_File.xlsx",sheet_name="Sheet3")

# %%
df

# %%
df[df['Raw_Score_8'] == 'None']

# %%
df.drop(['Local ID'],axis = 1,inplace = True)

# %%
##Checking for no. of records which are not useful
df[(df['Raw_Score_7'] == 'None') & (df['Raw_Score_8'] == 'None') & (df['Raw_Score_9'] == 'None') & (df['Raw_Score_10'] == 'None')]

# %%
## Converting Nones for table seperation
df['Raw_Score_7'] = df['Raw_Score_7'].replace("None",0)
df['Percent Score_7'] = df['Percent Score_7'].replace("None",0)
df['Raw_Score_8'] = df['Raw_Score_8'].replace("None",0)
df['Percent Score_8'] = df['Percent Score_8'].replace("None",0)
df['Raw_Score_9'] = df['Raw_Score_9'].replace("None",0)
df['Percent Score_9'] = df['Percent Score_9'].replace("None",0)
df['Raw_Score_10'] = df['Raw_Score_10'].replace("None",0)
df['Percent Score_10'] = df['Percent Score_10'].replace("None",0)
df['Raw_Score_11'] = df['Raw_Score_11'].replace("None",0)
df['Percent Score_11'] = df['Percent Score_11'].replace("None",0)
df['Raw_Score_12'] = df['Raw_Score_12'].replace("None",0)
df['Percent Score_12'] = df['Percent Score_12'].replace("None",0)


# %%
##Prioritizing Test Taken Dates. Most recent test scores are given most priority
df['Date Taken_7'] = 5
df['Date Taken_8'] = 4
df['Date Taken_9'] = 5 
df['Date Taken_10'] = 4
df['Date Taken_11'] = 3
df['Date Taken_12'] = 3 

# %%
df_numeric = df.select_dtypes(include = ['int','float'])

# %%
df_categor = df.select_dtypes(exclude = ['int','float'])

# %%
df = pd.get_dummies(data=df,columns=df_categor.columns)

# %%
df

# %%
