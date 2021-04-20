# %%
import pandas as pd 
import numpy as np

# %%
df = pd.read_csv("grade5_iter1_mean_impute_onehot_math.csv")

# %%
df

# %%
#not including dependent variable (i.e. final STARR test in last column)
X = df.iloc[:, 1:12]
y = df['percent_score_f']

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
df1

# %%
df3 = pd.concat([df1,X_test], axis=1)

# %%
df3

# %%
df3.to_csv(r'/Users/sukanyasravasti/LR_Math_Grade5.csv', index = False)

# %%
df3['abs_diff'] = abs(df3['Actual'] - df3['Predicted'])

# %%
df3 

# %%
df3.hist(column = 'abs_diff')

# %%
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from numpy import mean
from numpy import std


# %%
df_rf = pd.read_csv("grade5_iter1_mean_impute_onehot_math.csv")

# %%
drop_indices = np.random.choice(df_rf.index, 10, replace=False)
df_rf_test = df_rf.loc[drop_indices]
df_rf = df_rf.drop(drop_indices)

# %%
model = RandomForestRegressor(random_state=1)

# %%
cv = LeaveOneOut()

# %%
scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)

# %%
scores = abs(scores)
print(scores)

# %%
print('MAE: %.3f (%.3f)' % (mean(scores), std(scores)))

# %%
from sklearn.model_selection import RandomizedSearchCV

# %%
random_grid = { 'bootstrap': [True, False],
 'max_depth': [5,10,15],
 'max_features': ['auto', 'sqrt'],
 'min_samples_leaf': [1, 2, 4],
 'min_samples_split': [2, 5, 10],
 'n_estimators': [20,40,60,80]}

# %%
rf_random = RandomizedSearchCV(estimator = model, param_distributions = random_grid, n_iter = 10, cv = cv, verbose=2, random_state=42, n_jobs = -1)

# %%
rf_random.fit(X, y)

# %%
rf_random.best_params_
