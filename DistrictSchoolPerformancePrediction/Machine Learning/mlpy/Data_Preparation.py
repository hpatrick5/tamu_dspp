'''
# Proof of Concept for AI Turnaround Data Report - ELRC
## Data Preperation

This notebook shows how a common format data was generated from each of the individual files. From now on, this steps should not be done as these are different for each grade.

We will be standardazing each grade file format which will be the format that we output data in this file.

'''

import pandas as pd
import numpy as np
from os.path import join

'''
This is the directory that contains all the data files for all the grades from the customer.
'''

school_data_directory = "fromCustomer"

'''
### Common Files
'''

'''
The continously enrolled file recieved from the customer was for the school year 2019. However, we were looking for the data from the school year 2018. Hence, subtract 1 so that student are in the correct grade for our data.

'''

continously_enrolled_file = join(school_data_directory, "Continuously Enrolled Carmichael.xlsx")
df_continously_enrolled = pd.ExcelFile(continously_enrolled_file).parse("All Selected Records",skiprows = 2)
df_continously_enrolled = df_continously_enrolled.drop(columns=["Student Name"])
df_continously_enrolled["Grade"] = df_continously_enrolled["Grade"] - 1
df_continously_enrolled = df_continously_enrolled.rename(columns = {"Student ID" : "Local ID"})

# df_continously_enrolled.head()

economically_disadvantaged_file = join(school_data_directory, "Current ED.xlsx")
df_economically_disadvantaged = pd.ExcelFile(economically_disadvantaged_file).parse("All Selected Records",skiprows = 2)
df_economically_disadvantaged = df_economically_disadvantaged.drop(columns=["Student Name"])
df_economically_disadvantaged = df_economically_disadvantaged.rename(columns = {"Student ID" : "Local ID"})
# df_economically_disadvantaged.head()

'''
## 3rd Grade Data Preperation
'''
grade3_directory = join(school_data_directory, '3rd Grade')

grade3_math = join(grade3_directory, "3rd Grade STAAR Math Carmichael.xlsx")
df_grade3_math = pd.ExcelFile(grade3_math).parse("Sheet1", skiprows = 1)

grade3_read = join(grade3_directory, "3rd Grade STAAR RDG Carmichael.xlsx")
df_grade3_read = pd.ExcelFile(grade3_read).parse("Sheet1", skiprows = 1)

'''
### Join with the continously enrolled and economically disadvantaged lists.
'''

df_grade3_math = pd.merge(df_grade3_math, df_economically_disadvantaged[["Local ID","Meal Status"]], how='left', on = "Local ID")
df_grade3_math = pd.merge(df_grade3_math, df_continously_enrolled[["Local ID","16-17 PEIMS Campus"]], how='left', on = "Local ID")
df_grade3_math["Meal Status"].fillna("No", inplace=True)
df_grade3_math['Continously Enrolled'] = np.where(df_grade3_math['16-17 PEIMS Campus'].isnull(), "No","Yes")
df_grade3_math = df_grade3_math.drop(columns=["16-17 PEIMS Campus"])

'''
### Fix all the column names
'''

df_grade3_math[["Raw Score.4","Percent Score.4","Approaches.4", "Meets.4", "Masters.4", "Date Taken.4"]] \
= df_grade3_math[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]]

df_grade3_math[["Raw Score.5","Percent Score.5","Approaches.5", "Meets.5", "Masters.5", "Date Taken.5"]] \
= df_grade3_math[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3" , "Date Taken.3"]]

df_grade3_math[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]] \
= df_grade3_math[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1", "Date Taken.1"]]

df_grade3_math[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1", "Date Taken.1"]]  = "-"
df_grade3_math[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3", "Date Taken.3"]]  = "-"

df_grade3_column_order = ['Local ID', 'Special Ed Indicator', 'LEP', 'Ethnicity', 'Meal Status', 'Continously Enrolled', \
'Raw Score', 'Percent Score', 'Approaches', 'Meets', 'Masters', 'Date Taken', \
'Raw Score.1', 'Percent Score.1', 'Approaches.1', 'Meets.1','Masters.1', 'Date Taken.1', \
'Raw Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2', 'Masters.2', 'Date Taken.2', \
'Raw Score.3', 'Percent Score.3', 'Approaches.3', 'Meets.3', 'Masters.3', 'Date Taken.3', \
'Raw Score.4','Percent Score.4', 'Approaches.4', 'Meets.4', 'Masters.4', 'Date Taken.4', \
'Raw Score.5', 'Percent Score.5', 'Approaches.5','Meets.5', 'Masters.5', 'Date Taken.5']

df_temp = pd.DataFrame({'a':[np.nan]})
df_temp.to_csv((join(grade3_directory, "__3rd Grade STAAR Math Carmichael Final.csv")), index=False, header = None)
df_grade3_math.to_csv((join(grade3_directory, "__3rd Grade STAAR Math Carmichael Final.csv")),mode = 'a', columns = df_grade3_column_order)

'''
### Merge the continoulsy enrolled and economically disadvantaged data.
'''

df_grade3_read = pd.merge(df_grade3_read, df_economically_disadvantaged[["Local ID","Meal Status"]], how='left', on = "Local ID")
df_grade3_read = pd.merge(df_grade3_read, df_continously_enrolled[["Local ID","16-17 PEIMS Campus"]], how='left', on = "Local ID")
df_grade3_read["Meal Status"].fillna("No", inplace=True)
df_grade3_read['Continously Enrolled'] = np.where(df_grade3_read['16-17 PEIMS Campus'].isnull(), "No","Yes")
df_grade3_read = df_grade3_read.drop(columns=["16-17 PEIMS Campus"])

df_grade3_read[["Raw Score.4","Percent Score.4","Approaches.4", "Meets.4", "Masters.4", "Date Taken.4"]] \
= df_grade3_read[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]]

df_grade3_read[["Raw Score.5","Percent Score.5","Approaches.5", "Meets.5", "Masters.5", "Date Taken.5"]] \
= df_grade3_read[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3" , "Date Taken.3"]]

df_grade3_read[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]] \
= df_grade3_read[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1", "Date Taken.1"]]

df_grade3_read[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1", "Date Taken.1"]]  = "-"
df_grade3_read[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3", "Date Taken.3"]]  = "-"

df_temp = pd.DataFrame({'a':[np.nan]})
df_temp.to_csv((join(grade3_directory, "__3rd Grade STAAR RDG Carmichael Final.csv")), index=False, header = None)
df_grade3_read.to_csv((join(grade3_directory, "__3rd Grade STAAR RDG Carmichael Final.csv")),mode='a', columns = df_grade3_column_order)

'''
## 4th Grade Preparation
'''

grade4_directory = join(school_data_directory, '4th Grade')
grade4_previous_year = join(grade4_directory,'3rd 2018 RDG Math STAAR Data.xlsx')
grade4_final_year = join(grade4_directory,'4th 2019 RDG Math STAAR Data.xlsx')
grade4_mock_1 = join(grade4_directory,'4th Gr. Fall 2018 Practice STAAR.xlsx')
grade4_mock_2 = join(grade4_directory,'4th Gr. Spring 2019 Practice STAAR.xlsx')

df_grade4_previous_year = pd.ExcelFile(grade4_previous_year).parse("ABC Order", skiprows = 1).drop(columns="Student Name")
df_grade4_final_year = pd.ExcelFile(grade4_final_year).parse("Sheet1", skiprows = 1).drop(columns="Student Name")
df_grade4_mock_1 = pd.ExcelFile(grade4_mock_1).parse("Sheet1", skiprows = 1).drop(columns="Student Name")
df_grade4_mock_2 = pd.ExcelFile(grade4_mock_2).parse("Sheet1", skiprows = 1).drop(columns="Student Name")

'''
### Fix the column names for each of the 4th Grade data
'''

df_grade4_final_year = df_grade4_final_year.drop(columns=['Scale Score', 'Scale Score.1', 'Scale Score.2', 'Scale Score.3'])

df_grade4_previous_year = df_grade4_previous_year.drop(columns=['Sped Indicator', 'LEP', 'Gender', 'Ethnicity'])
df_grade4_previous_year.columns = ['Local ID', 'Raw Score',
       'Scale Score', 'Percent Score', 'Approaches', 'Meets',
       'Masters', 'Raw Score.1', 'Scale Score.1', 'Percent Score.1',
       'Approaches.1', 'Meets.1', 'Masters.1', 'Raw Score.2',
       'Scale Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2',
       'Masters.2', 'Raw Score.3', 'Scale Score.3', 'Percent Score.3',
       'Approaches.3', 'Meets.3', 'Masters.3']
df_grade4_previous_year = df_grade4_previous_year.drop(columns=['Scale Score', 'Scale Score.1', 'Scale Score.2', 'Scale Score.3'])

df_grade4_mock_1 = df_grade4_mock_1.drop(columns=['Special Ed Indicator', 'LEP', 'Ethnicity'])
df_grade4_mock_1.columns = ['Local ID', 'Raw Score',
       'Percent Score', 'Approaches', 'Meets',
       'Masters', 'Date Taken', 'Raw Score.1', 'Percent Score.1',
       'Approaches.1', 'Meets.1', 'Masters.1',
       'Date Taken.1', 'Raw Score.2', 'Percent Score.2',
       'Approaches.2', 'Meets.2', 'Masters.2',
       'Date Taken.2']

df_grade4_mock_2 = df_grade4_mock_2.drop(columns=['Special Ed Indicator', 'LEP', 'Ethnicity'])
df_grade4_mock_2.columns = ['Local ID', 'Raw Score',
       'Percent Score', 'Approaches', 'Meets',
       'Masters', 'Date Taken', 'Raw Score.1', 'Percent Score.1',
       'Approaches.1', 'Meets.1', 'Masters.1',
       'Date Taken.1', 'Raw Score.2', 'Percent Score.2',
       'Approaches.2', 'Meets.2', 'Masters.2',
       'Date Taken.2']

'''
### Merge the continously enrolled and economically disadvantaged data
'''

df_grade4_final_year = pd.merge(df_grade4_final_year, df_economically_disadvantaged[["Local ID","Meal Status"]], how='left', on = "Local ID")
df_grade4_final_year = pd.merge(df_grade4_final_year, df_continously_enrolled[["Local ID","16-17 PEIMS Campus"]], how='left', on = "Local ID")
df_grade4_final_year["Meal Status"].fillna("No", inplace=True)
df_grade4_final_year['Continously Enrolled'] = np.where(df_grade4_final_year['16-17 PEIMS Campus'].isnull(), "No","Yes")
df_grade4_final_year = df_grade4_final_year.drop(columns=["16-17 PEIMS Campus"])

'''
### Merge all the exam data
'''

df_grade4_final_year = pd.merge(df_grade4_final_year, df_grade4_previous_year, how = 'left', on = "Local ID", suffixes = ["","_prev"])
df_grade4_final_year = pd.merge(df_grade4_final_year, df_grade4_mock_1, how = 'left', on = "Local ID", suffixes = ["","_mock1"])
df_grade4_final_year = pd.merge(df_grade4_final_year, df_grade4_mock_2, how = 'left', on = "Local ID", suffixes = ["","_mock2"])

'''
### Prepare math data.
'''

df_grade4_math = df_grade4_final_year.copy()
drop_list_math = ["Raw Score", "Percent Score", "Approaches", "Meets",  "Masters", "Date Taken"]
drop_list_math.extend(["Raw Score.1", "Percent Score.1", "Approaches.1", "Meets.1",  "Masters.1", "Date Taken.1"])
drop_list_math.extend(["Raw Score.2_prev", "Percent Score.2_prev", "Approaches.2_prev", "Meets.2_prev",  "Masters.2_prev"])
drop_list_math.extend(["Raw Score.3_prev", "Percent Score.3_prev", "Approaches.3_prev", "Meets.3_prev",  "Masters.3_prev"])
drop_list_math.extend(["Raw Score_mock1", "Percent Score_mock1", "Approaches_mock1", "Meets_mock1",  "Masters_mock1", "Date Taken_mock1"])
drop_list_math.extend(["Raw Score_mock2", "Percent Score_mock2", "Approaches_mock2", "Meets_mock2",  "Masters_mock2", "Date Taken_mock2"])
drop_list_math.extend(["Raw Score.1_mock1", "Percent Score.1_mock1", "Approaches.1_mock1", "Meets.1_mock1",  "Masters.1_mock1", "Date Taken.1_mock1"])
drop_list_math.extend(["Raw Score.1_mock2", "Percent Score.1_mock2", "Approaches.1_mock2", "Meets.1_mock2",  "Masters.1_mock2", "Date Taken.1_mock2"])

df_grade4_math = df_grade4_math.drop(columns=drop_list_math)

df_grade4_math[["Raw Score.6","Percent Score.6","Approaches.6", "Meets.6", "Masters.6", "Date Taken.6"]] \
= df_grade4_math[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]]

df_grade4_math[["Raw Score.7","Percent Score.7","Approaches.7", "Meets.7", "Masters.7", "Date Taken.7"]] \
= df_grade4_math[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3" , "Date Taken.3"]]

df_grade4_math[["Raw Score","Percent Score","Approaches", "Meets", "Masters"]] \
= df_grade4_math[["Raw Score.1_prev","Percent Score.1_prev","Approaches.1_prev", "Meets.1_prev", "Masters.1_prev"]]

df_grade4_math[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1"]] \
= df_grade4_math[["Raw Score_prev","Percent Score_prev","Approaches_prev", "Meets_prev", "Masters_prev"]]

df_grade4_math[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]] \
= df_grade4_math[["Raw Score.2_mock1","Percent Score.2_mock1","Approaches.2_mock1", "Meets.2_mock1", "Masters.2_mock1", "Date Taken.2_mock1"]]

df_grade4_math[["Raw Score.4","Percent Score.4","Approaches.4", "Meets.4", "Masters.4", "Date Taken.4"]] \
= df_grade4_math[["Raw Score.2_mock2","Percent Score.2_mock2","Approaches.2_mock2", "Meets.2_mock2", "Masters.2_mock2", "Date Taken.2_mock2"]]

df_grade4_math[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3", "Date Taken.3"]]  = "-"
df_grade4_math[["Raw Score.5","Percent Score.5","Approaches.5", "Meets.5", "Masters.5", "Date Taken.5"]]  \
= pd.DataFrame([['-'] * 6], index=df_grade4_math.index)

drop_remaining = ["Raw Score.1_prev","Percent Score.1_prev","Approaches.1_prev", "Meets.1_prev", "Masters.1_prev", \
                 "Raw Score_prev","Percent Score_prev","Approaches_prev", "Meets_prev", "Masters_prev",\
                 "Raw Score.2_mock1","Percent Score.2_mock1","Approaches.2_mock1", "Meets.2_mock1", "Masters.2_mock1", "Date Taken.2_mock1",\
                 "Raw Score.2_mock2","Percent Score.2_mock2","Approaches.2_mock2", "Meets.2_mock2", "Masters.2_mock2", "Date Taken.2_mock2"]

df_grade4_math = df_grade4_math.drop(columns = drop_remaining)

df_grade4_column_order = ['Local ID', 'Special Ed Indicator', 'LEP', 'Ethnicity', 'Meal Status', 'Continously Enrolled', \
'Raw Score', 'Percent Score', 'Approaches', 'Meets', 'Masters', \
'Raw Score.1', 'Percent Score.1', 'Approaches.1', 'Meets.1','Masters.1', \
'Raw Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2', 'Masters.2', 'Date Taken.2', \
'Raw Score.3', 'Percent Score.3', 'Approaches.3', 'Meets.3', 'Masters.3', 'Date Taken.3', \
'Raw Score.4','Percent Score.4', 'Approaches.4', 'Meets.4', 'Masters.4', 'Date Taken.4', \
'Raw Score.5', 'Percent Score.5', 'Approaches.5','Meets.5', 'Masters.5', 'Date Taken.5',\
'Raw Score.6','Percent Score.6', 'Approaches.6', 'Meets.6', 'Masters.6', 'Date Taken.6', \
'Raw Score.7','Percent Score.7', 'Approaches.7', 'Meets.7', 'Masters.7', 'Date Taken.7']

df_temp = pd.DataFrame({'a':[np.nan]})
df_temp.to_csv((join(grade4_directory, "__4th Grade STAAR Math Carmichael Final.csv")), index=False, header = None)
df_grade4_math.to_csv((join(grade4_directory, "__4th Grade STAAR Math Carmichael Final.csv")),mode='a', columns = df_grade4_column_order)

'''
### Prepare Reading Data
'''
keep_list_read = drop_list_math.copy()
keep_list_read.extend(['Local ID', 'Special Ed Indicator', 'LEP', 'Ethnicity','Meal Status', 'Continously Enrolled'])
df_grade4_read = df_grade4_final_year[keep_list_read].copy()

df_grade4_read[["Raw Score.6","Percent Score.6","Approaches.6", "Meets.6", "Masters.6", "Date Taken.6"]] \
= df_grade4_read[["Raw Score","Percent Score","Approaches", "Meets", "Masters", "Date Taken"]]

df_grade4_read[["Raw Score.7","Percent Score.7","Approaches.7", "Meets.7", "Masters.7", "Date Taken.7"]] \
= df_grade4_read[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1" , "Date Taken.1"]]

df_grade4_read[["Raw Score","Percent Score","Approaches", "Meets", "Masters"]] \
= df_grade4_read[["Raw Score.3_prev","Percent Score.3_prev","Approaches.3_prev", "Meets.3_prev", "Masters.3_prev"]]

df_grade4_read[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1"]] \
= df_grade4_read[["Raw Score.2_prev","Percent Score.2_prev","Approaches.2_prev", "Meets.2_prev", "Masters.2_prev"]]

df_grade4_read[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]] \
= df_grade4_read[["Raw Score_mock1","Percent Score_mock1","Approaches_mock1", "Meets_mock1", "Masters_mock1", "Date Taken_mock1"]]

df_grade4_read[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3", "Date Taken.3"]]  \
= df_grade4_read[["Raw Score.1_mock1","Percent Score.1_mock1","Approaches.1_mock1", "Meets.1_mock1", "Masters.1_mock1", "Date Taken.1_mock1"]]

df_grade4_read[["Raw Score.4","Percent Score.4","Approaches.4", "Meets.4", "Masters.4", "Date Taken.4"]] \
= df_grade4_read[["Raw Score_mock2","Percent Score_mock2","Approaches_mock2", "Meets_mock2", "Masters_mock2", "Date Taken_mock2"]]

df_grade4_read[["Raw Score.5","Percent Score.5","Approaches.5", "Meets.5", "Masters.5", "Date Taken.5"]]  \
= df_grade4_read[["Raw Score.1_mock2","Percent Score.1_mock2","Approaches.1_mock2", "Meets.1_mock2", "Masters.1_mock2", "Date Taken.1_mock2"]]

drop_remaining = ["Raw Score.3_prev","Percent Score.3_prev","Approaches.3_prev", "Meets.3_prev", "Masters.3_prev",\
                 "Raw Score.2_prev","Percent Score.2_prev","Approaches.2_prev", "Meets.2_prev", "Masters.2_prev",\
                 "Raw Score_mock1","Percent Score_mock1","Approaches_mock1", "Meets_mock1", "Masters_mock1", "Date Taken_mock1",\
                 "Raw Score.1_mock1","Percent Score.1_mock1","Approaches.1_mock1", "Meets.1_mock1", "Masters.1_mock1", "Date Taken.1_mock1",
                 "Raw Score_mock2","Percent Score_mock2","Approaches_mock2", "Meets_mock2", "Masters_mock2", "Date Taken_mock2",
                 "Raw Score.1_mock2","Percent Score.1_mock2","Approaches.1_mock2", "Meets.1_mock2", "Masters.1_mock2", "Date Taken.1_mock2"]

df_grade4_read = df_grade4_read.drop(columns = drop_remaining)

df_temp = pd.DataFrame({'a':[np.nan]})
df_temp.to_csv((join(grade4_directory, "__4th Grade STAAR RDG Carmichael Final.csv")), index=False, header = None)
df_grade4_read.to_csv((join(grade4_directory, "__4th Grade STAAR RDG Carmichael Final.csv")),mode='a', columns = df_grade4_column_order)

'''
## 5th Grade Preparation
'''

grade5_directory = join(school_data_directory, '5th Grade')
grade5_previous_year = join(grade5_directory,'Carmichael fourth grade end of year 2018.xlsx')
grade5_read = join(grade5_directory,'Carmichael fifth grade 2019 (reading).xlsx')
grade5_math = join(grade5_directory,'2019 STAAR Math Data.xlsx')

df_grade5_previous_year = pd.ExcelFile(grade5_previous_year).parse("Sheet1", skiprows = 1)
df_grade5_read = pd.ExcelFile(grade5_read).parse("Sheet1", skiprows = 1)
df_grade5_math = pd.ExcelFile(grade5_math).parse("Sheet1", skiprows = 1)

df_grade5_previous_year.columns = ['Local ID', 'Special Ed Indicator', 'LEP', 'Ethnicity', 'Raw Score', \
       'Percent Score', 'Approaches', 'Meets', 'Masters',\
       'Date Taken', 'Raw Score.1', 'Percent Score.1',\
       'Approaches.1', 'Meets.1', 'Masters.1', 'Date Taken.1',\
       'Raw Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2',\
       'Masters.2', 'Date Taken.2', 'Raw Score.3', 'Percent Score.3',\
       'Approaches.3', 'Meets.3', 'Masters.3', 'Date Taken.3']

df_grade5_previous_year = df_grade5_previous_year.drop(columns = ['Special Ed Indicator', 'LEP', 'Ethnicity'])
df_grade5_previous_year_read = df_grade5_previous_year.copy()
df_grade5_previous_year_read = df_grade5_previous_year_read.drop(columns= ['Raw Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2',\
       'Masters.2', 'Date Taken.2', 'Raw Score.3', 'Percent Score.3', 'Approaches.3', 'Meets.3', 'Masters.3', 'Date Taken.3'])

df_grade5_previous_year_math = df_grade5_previous_year.copy()

df_grade5_previous_year_math[["Raw Score","Percent Score","Approaches", "Meets", "Masters", "Date Taken"]] \
= df_grade5_previous_year_math[["Raw Score.2","Percent Score.2","Approaches.2", "Meets.2", "Masters.2", "Date Taken.2"]]

df_grade5_previous_year_math[["Raw Score.1","Percent Score.1","Approaches.1", "Meets.1", "Masters.1", "Date Taken.1"]] \
= df_grade5_previous_year_math[["Raw Score.3","Percent Score.3","Approaches.3", "Meets.3", "Masters.3" , "Date Taken.3"]]

df_grade5_previous_year_math = df_grade5_previous_year_math.drop(columns= ['Raw Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2',\
       'Masters.2', 'Date Taken.2', 'Raw Score.3', 'Percent Score.3', 'Approaches.3', 'Meets.3', 'Masters.3', 'Date Taken.3'])

df_grade5_read = df_grade5_read.drop(columns =  ['Raw Score.6', 'Percent Score.6', 'Approaches Grade Level.6', 'Satisfactory.2', \
       'Meets.5', 'Date Taken.6', 'Raw Score.7', 'Percent Score.7', \
       'Approaches Grade Level.7', 'Satisfactory.3', 'Meets.6', 'Date Taken.7', \
       'Raw Score.8', 'Percent Score.8', 'Approaches Grade Level.8',\
       'Satisfactory.4', 'Meets.7', 'Date Taken.8'])

df_grade5_read.columns = ['Local ID', 'Special Ed Indicator', 'LEP', 'Ethnicity', \
                          'Raw Score.2', 'Percent Score.2','Approaches.2', 'Meets.2', 'Masters.2', 'Date Taken.2',\
                          'Raw Score.3', 'Percent Score.3','Approaches.3', 'Meets.3', 'Masters.3', 'Date Taken.3',\
                          'Raw Score.4', 'Percent Score.4', 'Approaches.4', 'Meets.4', 'Masters.4', 'Date Taken.4',\
                          'Raw Score.5', 'Percent Score.5', 'Approaches.5', 'Meets.5', 'Masters.5', 'Date Taken.5',\
                          'Raw Score.6', 'Percent Score.6', 'Approaches.6', 'Meets.6', 'Masters.6', 'Date Taken.6',\
                          'Raw Score.7', 'Percent Score.7', 'Approaches.7', 'Meets.7', 'Masters.7', 'Date Taken.7']

df_grade5_read = pd.merge(df_grade5_read, df_grade5_previous_year_read, how = 'left', on = "Local ID", suffixes = ["","_prev"])

df_grade5_read = pd.merge(df_grade5_read, df_economically_disadvantaged[["Local ID","Meal Status"]], how='left', on = "Local ID")
df_grade5_read = pd.merge(df_grade5_read, df_continously_enrolled[["Local ID","16-17 PEIMS Campus"]], how='left', on = "Local ID")
df_grade5_read["Meal Status"].fillna("No", inplace=True)
df_grade5_read['Continously Enrolled'] = np.where(df_grade5_read['16-17 PEIMS Campus'].isnull(), "No","Yes")
df_grade5_read = df_grade5_read.drop(columns=["16-17 PEIMS Campus"])

grade5_column_order = ['Local ID', 'Special Ed Indicator', 'LEP', 'Ethnicity', 'Meal Status', 'Continously Enrolled', \
'Raw Score', 'Percent Score', 'Approaches', 'Meets', 'Masters', 'Date Taken', \
'Raw Score.1','Percent Score.1', 'Approaches.1', 'Meets.1', 'Masters.1','Date Taken.1' \
'Raw Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2', 'Masters.2', 'Date Taken.2',\
'Raw Score.3', 'Percent Score.3', 'Approaches.3','Meets.3', 'Masters.3', 'Date Taken.3',\
'Raw Score.4', 'Percent Score.4', 'Approaches.4', 'Meets.4', 'Masters.4', 'Date Taken.4',\
'Raw Score.5', 'Percent Score.5', 'Approaches.5', 'Meets.5', 'Masters.5', 'Date Taken.5',\
'Raw Score.6', 'Percent Score.6', 'Approaches.6', 'Meets.6', 'Masters.6', 'Date Taken.6',\
'Raw Score.7', 'Percent Score.7', 'Approaches.7','Meets.7', 'Masters.7', 'Date Taken.7']

df_temp = pd.DataFrame({'a':[np.nan]})
df_temp.to_csv((join(grade5_directory, "__5th Grade STAAR RDG Carmichael Final.csv")), index=False, header = None)
df_grade5_read.to_csv((join(grade5_directory, "__5th Grade STAAR RDG Carmichael Final.csv")),mode='a', columns = grade5_column_order)

'''
### Math Grade5
'''

df_grade5_math = df_grade5_math.drop(columns =  [\
       'Raw Score.4', 'Percent Score.4', 'Approaches Grade Level.4', 'meets',\
       'Masters.2', 'Date Taken.4', 'Raw Score.5', 'Percent Score.5',\
       'Approaches Grade Level.5', 'Meets.5', 'Masters.3', 'Date Taken.5',\
       'Raw Score.6', 'Percent Score.6', 'Approaches Grade Level.6', 'Meets.6',\
       'Masters.4', 'Date Taken.6'])

df_grade5_math.columns = ['Local ID', 'Special Ed Indicator', 'LEP', 'Ethnicity',\
'Raw Score.2', 'Percent Score.2', 'Approaches.2', 'Meets.2', 'Masters.2', 'Date Taken.2',\
'Raw Score.4', 'Percent Score.4', 'Approaches.4', 'Meets.4', 'Masters.4', 'Date Taken.4',\
'Raw Score.6', 'Percent Score.6', 'Approaches.6', 'Meets.6', 'Masters.6', 'Date Taken.6',\
'Raw Score.7', 'Percent Score.7', 'Approaches.7','Meets.7', 'Masters.7', 'Date Taken.7']

df_grade5_math[['Raw Score.3', 'Percent Score.3', 'Approaches.3','Meets.3', 'Masters.3', 'Date Taken.3']] = \
    pd.DataFrame([['-'] * 6], index=df_grade5_math.index)

df_grade5_math[['Raw Score.5', 'Percent Score.5', 'Approaches.5', 'Meets.5', 'Masters.5', 'Date Taken.5']] = \
    pd.DataFrame([['-'] * 6], index=df_grade5_math.index)

df_grade5_math = pd.merge(df_grade5_math, df_grade5_previous_year_math, how = 'left', on = "Local ID", suffixes = ["","_prev"])

df_grade5_math = pd.merge(df_grade5_math, df_economically_disadvantaged[["Local ID","Meal Status"]], how='left', on = "Local ID")
df_grade5_math = pd.merge(df_grade5_math, df_continously_enrolled[["Local ID","16-17 PEIMS Campus"]], how='left', on = "Local ID")
df_grade5_math["Meal Status"].fillna("No", inplace=True)
df_grade5_math['Continously Enrolled'] = np.where(df_grade5_math['16-17 PEIMS Campus'].isnull(), "No","Yes")
df_grade5_math = df_grade5_math.drop(columns=["16-17 PEIMS Campus"])

df_temp = pd.DataFrame({'a':[np.nan]})
df_temp.to_csv((join(grade5_directory, "__5th Grade STAAR Math Carmichael Final.csv")), index=False, header = None)
df_grade5_math.to_csv((join(grade5_directory, "__5th Grade STAAR Math Carmichael Final.csv")),mode='a', columns = grade5_column_order)