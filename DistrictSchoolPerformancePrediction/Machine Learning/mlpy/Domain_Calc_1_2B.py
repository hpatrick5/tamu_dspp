import pandas as pd

#math grade 4
df_g4_math = pd.read_excel("Grade4_Compare_AI_with_Expert.xlsx", "Math_Compare_With_JC")
#23 observstions (number of rows in the df)
total_g4_math = df_g4_math.shape[0]
print(total_g4_math)

#number in approaches
df_g4_math.rename(columns={'AI predictions':'AIpred'}, inplace=True)

#number in masters (students in meets are also in masters)
g4_math_masters = df_g4_math.query('AIpred == "Masters"').AIpred.count()
print(g4_math_masters)

#number in meets
g4_math_meets = df_g4_math.query('AIpred == "Meets"').AIpred.count() + g4_math_masters
print(g4_math_meets)

g4_math_approaches = df_g4_math.query('AIpred == "Approaches"').AIpred.count() + g4_math_meets
print(g4_math_approaches)

#reading grade 4
df_g4_read = pd.read_excel("Grade4_Compare_AI_with_Expert.xlsx","Reading_Compare_with_JC")

total_g4_read = df_g4_read.shape[0]
print(total_g4_read)

#number in approaches
df_g4_read.rename(columns={'AI Predictions':'AIpred'}, inplace=True)

#number in masters (students in meets are also in masters)
g4_read_masters = df_g4_read.query('AIpred == "Masters"').AIpred.count()
print(g4_read_masters)

#number in meets
g4_read_meets = df_g4_read.query('AIpred == "Meets"').AIpred.count() + g4_read_masters
print(g4_read_meets)

#df_g4_read
g4_read_approaches = df_g4_read.query('AIpred == "Approaches"').AIpred.count() + g4_read_meets
print(g4_read_approaches)

########PLEASE NOTE GRADE 5 APPROACHES, MEETS AND MASTERS IS IN DIFFERNT FORMAT SO CALCULATIONS ARE A BIT DIFFERNT####

#math grade 5
df_g5_math = pd.read_excel("Grade5_Predictions_Final.xlsx","Grade5_Math_Predictions_Final")
total_g5_math = df_g5_math.shape[0]
print(total_g5_math)

#number in approaches
df_g5_math.rename(columns={'AI Approches':'AIapp'}, inplace=True)
g5_math_approaches = df_g5_math.query('AIapp == 1').AIapp.count()
print(g5_math_approaches)

#number in meets
df_g5_math.rename(columns={'AI Meets':'AImeets'}, inplace=True)
g5_math_meets = df_g5_math.query('AImeets == 1').AImeets.count()
print(g5_math_meets)

#number in masters (students in meets are also in masters)
df_g5_math.rename(columns={'AI Masters':'AImasters'}, inplace=True)
g5_math_masters = df_g5_math.query('AImasters == 1').AImasters.count()
print(g5_math_masters)

#reading grade 5
df_g5_read = pd.read_excel("Grade5_Predictions_Final.xlsx","Grade5_Reading_Predictions_Fina")
total_g5_read = df_g5_read.shape[0]
print(total_g5_read)

#number in approaches
df_g5_read.rename(columns={'AI Approaches':'AIapp'}, inplace=True)
g5_read_approaches = df_g5_read.query('AIapp == 1').AIapp.count()
print(g5_read_approaches)

#number in meets
df_g5_read.rename(columns={'AI Meets':'AImeets'}, inplace=True)
g5_read_meets = df_g5_read.query('AImeets == 1').AImeets.count()
print(g5_read_meets)


#number in masters (students in meets are also in masters)
df_g5_read.rename(columns={'AI Masters':'AImasters'}, inplace=True)
g5_read_masters = df_g5_read.query('AImasters == 1').AImasters.count()
print(g5_read_masters)

#percents in approaches, meets and masters for math grades 4 and 5 combined
total_math = total_g4_math + total_g5_math
print(total_math)

total_math_approaches = g4_math_approaches + g5_math_approaches
total_math_meets = g4_math_meets + g5_math_meets
total_math_masters = g4_math_masters + g5_math_masters
print(total_math_masters)

#percent math approaches
share_math_app = (total_math_approaches/total_math)*100
print("Percent Math Approaches:", share_math_app)

#percent math meets
share_math_meets = (total_math_meets/total_math)*100
print("Percent Math Meets:", share_math_meets)

#percent math masters
share_math_masters = (total_math_masters/total_math)*100
print("Percent Math Masters:", share_math_masters)


#percents in approaches, meets and masters for reading grades 4 and 5 combined
total_read = total_g4_read + total_g5_read
total_read_approaches = g4_read_approaches + g5_read_approaches
total_read_meets = g4_read_meets + g5_read_meets
total_read_masters = g4_read_masters + g5_read_masters
#print(total_read)

#percent read approaches
share_read_app = (total_read_approaches/total_read)*100
print("Percent Read Approaches:", share_read_app)

#percent read meets
share_read_meets = (total_read_meets/total_read)*100
print("Percent Read Meets", share_read_meets)

#percent math masters
share_read_masters = (total_read_masters/total_read)*100
print("Percent Read Masters", share_read_masters)

#take average for math
math_average_raw = (share_math_app + share_math_meets + share_math_masters)/3
print("raw math",math_average_raw )

#take average for read
math_average_read = (share_read_app + share_read_meets + share_read_masters)/3
print("raw read",math_average_read)

#from conversion tool https://rptsvr1.tea.texas.gov/perfreport/account/2019/scaling_tool.html
#math scaled = 80 (B)
#read scaled = 78 (C)

#domain 2B calculation
#get percentage of economically disadvantaged students for grade 4 math
df_g4_math = pd.read_excel("Grade4_Compare_AI_with_Expert.xlsx", "Math_Compare_With_JC")
df_g4_math.rename(columns={'Meal Status':'MealStat'}, inplace=True)
g4_math_econ_dis = df_g4_math.query('MealStat == "Reduced"').MealStat.count()
#print(g4_math_econ_dis)
g4_math_econ_dis = df_g4_math.query('MealStat == "Free"').MealStat.count() + g4_math_econ_dis
print(g4_math_econ_dis)
total_g4_math = df_g4_math.shape[0]
#g4_math_percent_disadvantaged = (g4_math_econ_dis/total_g4_math)*100
##print(g4_math_percent_disadvantaged)

#get percentage of economically disadvantaged students for grade 4 reading
df_g4_read = pd.read_excel("Grade4_Compare_AI_with_Expert.xlsx", "Reading_Compare_with_JC")
df_g4_read.rename(columns={'Meal Status':'MealStat'}, inplace=True)
g4_read_econ_dis = df_g4_read.query('MealStat == "Reduced"').MealStat.count()
g4_read_econ_dis = df_g4_read.query('MealStat == "Free"').MealStat.count() + g4_read_econ_dis
print(g4_read_econ_dis)
total_g4_read = df_g4_read.shape[0]
#g4_read_percent_disadvantaged = (g4_read_econ_dis/total_g4_read)*100
#print(g4_read_percent_disadvantaged)

#get percentage of economically disadvantaged students for grade 5 math
df_g5_math = pd.read_excel("Grade5_Predictions_Final.xlsx", "Grade5_Math_Predictions_Final")
g5_math_econ_dis = df_g5_math.query('ED == "02-Reduced"').ED.count()
#print(g5_math_econ_dis)
g5_math_econ_dis = df_g5_math.query('ED == "01-Free"').ED.count() + g5_math_econ_dis
print(g5_math_econ_dis)
total_g5_math = df_g5_math.shape[0]
g5_math_percent_disadvantaged = (g5_math_econ_dis/total_g5_math)*100
#print(g5_math_percent_disadvantaged)


#get percentage of economically disadvantaged students for grade 5 reading
df_g5_read = pd.read_excel("Grade5_Predictions_Final.xlsx", "Grade5_Reading_Predictions_Fina")
df_g5_read.rename(columns={'Meal Status':'MealStat'}, inplace=True)
g5_read_econ_dis = df_g5_read.query('MealStat == "02-Reduced"').MealStat.count()
g5_read_econ_dis = df_g5_read.query('MealStat == "01-Free"').MealStat.count() + g5_read_econ_dis
print(g5_read_econ_dis)
total_g5_read = df_g5_read.shape[0]
g5_read_percent_disadvantaged = (g5_read_econ_dis/total_g5_read)*100
#print(g5_read_percent_disadvantaged)


#########Total percent of economically disadvantaged##################
#Reading
percent_ED_read = ((g4_read_econ_dis + g5_read_econ_dis) / (total_g4_read+total_g5_read))*100
print("Percent ED Read",percent_ED_read)

#Math
percent_ED_math = ((g4_math_econ_dis + g5_math_econ_dis) / (total_g4_math+total_g5_math))*100
print("Percent ED Math",percent_ED_math)


#### 2B from https://rptsvr1.tea.texas.gov/perfreport/account/2019/scaling_tool.html####

#math
#90 (A) (inputs: raw math 49 from domain 1 ,percent_ED_math ) ##note input is raw score, not scaled

#read
#89 (B) (inputs: raw read 47 from domain 1 ,percent_ED_read ) ##note input is raw score, not scaled

#2A calculation