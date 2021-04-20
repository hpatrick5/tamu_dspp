# %%
import pandas as pd

# %%
'''
## Data Reading

Two different dataframes for both, maths and reading data is created below.
'''

# %%
df_maths = pd.read_excel("Grade5_AI_Predictions_Final.xlsx")
df_reading = pd.read_excel("Grade5_AI_Predictions_Final.xlsx")

# %%
df_maths.head()

# %%
df_reading.head()

# %%
'''
## Class that implements the functions to pull academic achievement metrics
'''

# %%
class academic_achievement:
    def __init__(self, df, course):
        self.df = df
        self.course = course
        self.races = ["All Students", 
                      'African American', 
                      'Hispanic', 
                      "White", 
                      "American Indian", 
                      "Asian", 
                      "Pacific Islander", 
                      "Two or More"]
        
        self.target = {
            "All Students": (44, 46),
            "African American": (32, 31),
            "Hispanic": (37, 40),
            "White": (60, 59),
            "American Indian": (43, 45),
            "Asian": (74, 82),
            "Pacific Islander": (45, 50),
            "Two or More": (56, 54),
            "Econ Disadv": (33, 36),
            "EL (Current & Monitored)+": (29, 40),
            "Special Ed (Current)": (19, 23),
            "Special Ed (Former)": (36, 44),
            "Continuously Enrolled": (46, 47),
            "Non-Continuously Enrolled": (42, 45)
        }
        
        self.academic_data = dict()
        
    def get_academic_achievement_dict(self, group, data):
        target = 0
        if self.course == "ELA/Reading":
            target = self.target[group][0]
        else:
            target = self.target[group][1]

        data_dict = {
            "1. " + self.course + " Target": target,
            "2." + "Target Met": "N",
            "3." + "% at Meets GL Standard or Above": data["Percent"],
            "4." + "# at Meets GL Standard or Above": data["Meets"],
            "5." + "Total Tests (Adjusted)": data["Total"]
        }
        if data["Percent"] >= target:
            data_dict["2." + "Target Met"] = "Y"

        return data_dict
    
    def get_data_on_race(self, race):
        total_count = 0
        meet_count = 0
        for index, row in self.df.iterrows():
            row_race = row['Ethnicity']
            row_meet = row['AI Meets']
            row_master = row['AI Masters']
            if race == "All Students" or race == row_race:
                total_count += 1
                if row_meet or row_master:
                    meet_count += 1
        percent = 0
        if total_count != 0:
            percent = (meet_count/total_count)*100
        data = {"Percent": percent, "Meets": meet_count, "Total": total_count}
        return self.get_academic_achievement_dict(race, data)
    
    def get_col_stat(self, col_name, no_tag, group):
        total_count = 0
        meet_count = 0
        for index, row in self.df.iterrows():
            if col_name not in row:
                continue
            row_col_val = row[col_name]
            row_meet = row['AI Meets']
            row_master = row['AI Masters']
            if row_col_val != no_tag:
                total_count += 1
                if row_meet or row_master:
                    meet_count += 1
        percent = 0
        if total_count != 0:
            percent = (meet_count/total_count)*100
        data = {"Percent": percent, "Meets": meet_count, "Total": total_count}
        return self.get_academic_achievement_dict(group, data)
    
    def get_academic_data(self):
        index = 97
        for race in self.races:
            if str(race) == "nan":
                continue
            race_academic_data = self.get_data_on_race(race)
            self.academic_data[chr(index) + ". " + race] = race_academic_data
            index += 1
        
        econ_disadv_academic_data = self.get_col_stat("ED", "No", "Econ Disadv")
        self.academic_data[chr(index) + ". " + "Econ Disadv"] = econ_disadv_academic_data
        
        index += 1
        lep_academic_data = self.get_col_stat("LEP", "Other Non-LEP Student", "EL (Current & Monitored)+")
        self.academic_data[chr(index) + ". " + "EL (Current & Monitored)+"] = lep_academic_data
        
        index += 1
        special_ed_current_academic_data = self.get_col_stat("Special Ed Indicator", "No", "Special Ed (Current)")
        self.academic_data[chr(index) + ". " + "Special Ed (Current)"] = special_ed_current_academic_data
        
        index += 1
        special_ed_former_academic_data = self.get_col_stat("Special Ed Indicator (Former)", "No", "Special Ed (Former)")
        self.academic_data[chr(index) + ". " + "Special Ed (Former)"] = special_ed_former_academic_data
        
        continuously_enrolled_academic_data = self.get_col_stat("Continuously Enrolled", "No", "Continuously Enrolled")
        continuously_not_enrolled_academic_data = self.get_col_stat("Continuously Enrolled", "Yes", "Non-Continuously Enrolled")

        index += 1
        self.academic_data[chr(index) + ". " + "Continuously Enrolled"] = continuously_enrolled_academic_data
        index += 1
        self.academic_data[chr(index) + ". " + "Non-Continuously Enrolled"] = continuously_not_enrolled_academic_data
        
        return self.academic_data
        

# %%
'''
## Class that implements the functions to pull growth metrics
'''

# %%
class growth_status:
    def __init__(self, df, course):
        self.df = df
        self.course = course
        self.races = ["All Students", 
                      'African American', 
                      'Hispanic', 
                      "White", 
                      "American Indian", 
                      "Asian", 
                      "Pacific Islander", 
                      "Two or More"]
        
        self.target = {
            "All Students": (66, 71),
            "African American": (62, 67),
            "Hispanic": (65, 69),
            "White": (69, 74),
            "American Indian": (67, 71),
            "Asian": (77, 86),
            "Pacific Islander": (67, 74),
            "Two or More": (68, 73),
            "Econ Disadv": (64, 68),
            "EL (Current & Monitored)+": (64, 68),
            "Special Ed (Current)": (59, 61),
            "Special Ed (Former)": (65, 70),
            "Continuously Enrolled": (66, 71),
            "Non-Continuously Enrolled": (67, 70)
        }
        
        self.growth_data = dict()
    
    def get_growth_status_dict(self, group, data):
        target = 0
        if self.course == "ELA/Reading":
            target = growth_status_target[group][0]
        else:
            target = growth_status_target[group][1]

        data_dict = {
            "1." + self.course + " Target": target,
            "2." + "Target Met": "N",
            "3." + "Academic Growth Score": data["Score"],
            "4." + "Growth Points": data["Sum"],
            "5." + "Total Tests": data["Total"]
        }
        if data["Score"] >= target:
            data_dict["2." + "Target Met"] = "Y"

        return data_dict
    
    def get_data_on_race(self, race):
        total_count = 0
        growth_sum = 0
        for index, row in self.df.iterrows():
            row_race = row['Ethnicity']
            row_growth = row['Growth']
            if race is None or race == row_race:
                total_count += 1
                growth_sum += row_growth
        percent = 0
        if total_count != 0:
            percent = (growth_sum/total_count)*100
        data = {"Score": percent, "Sum": growth_sum, "Total": total_count}
        return self.get_growth_status_dict(race, data)
    
    def get_col_stat(self, col_name, no_tag, group):
        total_count = 0
        growth_sum = 0
        for index, row in self.df.iterrows():
            if col_name not in row:
                continue
            row_col_val = row[col_name]
            row_growth = row['Growth']
            if row_col_val != no_tag:
                total_count += 1
                growth_sum += row_growth
        percent = 0
        if total_count != 0:
            percent = (growth_sum/total_count)*100
        data = {"Score": percent, "Sum": growth_sum, "Total": total_count}
        return self.get_growth_status_dict(race, data)
    
    def get_growth_data(self):
        index = 97
        for race in self.races:
            if str(race) == "nan":
                continue
            race_growth_data = self.get_data_on_race(race)
            self.growth_data[chr(index) + ". " + race] = race_growth_data
            index += 1
        
        econ_disadv_growth_data = self.get_col_stat("ED", "No", "Econ Disadv")
        self.growth_data[chr(index) + ". " + "Econ Disadv"] = econ_disadv_growth_data
        
        index += 1
        lep_growth_data = self.get_col_stat("LEP", "Other Non-LEP Student", "EL (Current & Monitored)+")
        self.growth_data[chr(index) + ". " + "EL (Current & Monitored)+"] = lep_growth_data
        
        index += 1
        special_ed_current_growth_data = self.get_col_stat("Special Ed Indicator", "No", "Special Ed (Current)")
        self.growth_data[chr(index) + ". " + "Special Ed (Current)"] = special_ed_current_growth_data
        
        index += 1
        special_ed_former_growth_data = self.get_col_stat("Special Ed Indicator (Former)", "No", "Special Ed (Former)")
        self.growth_data[chr(index) + ". " + "Special Ed (Former)"] = special_ed_former_growth_data
        
        continuously_enrolled_growth_data = self.get_col_stat("Continuously Enrolled", "No", "Continuously Enrolled")
        continuously_not_enrolled_growth_data = self.get_col_stat("Continuously Enrolled", "Yes", "Non-Continuously Enrolled")

        index += 1
        self.growth_data[chr(index) + ". " + "Continuously Enrolled"] = continuously_enrolled_growth_data
        index += 1
        self.growth_data[chr(index) + ". " + "Non-Continuously Enrolled"] = continuously_not_enrolled_growth_data
        
        return self.growth_data
        

# %%
'''
## Class that implements the functions to pull success metrics
'''
class success_status:
    def __init__(self, df1, df2):
        self.df = df1
        self.df = self.df.append(df2)
        self.races = ["All Students", 
                      'African American', 
                      'Hispanic', 
                      "White", 
                      "American Indian", 
                      "Asian", 
                      "Pacific Islander", 
                      "Two or More"]
        
        self.target = {
            "All Students": 47,
            "African American": 36,
            "Hispanic": 41,
            "White": 58,
            "American Indian": 46,
            "Asian": 73,
            "Pacific Islander": 48,
            "Two or More": 55,
            "Econ Disadv": 38,
            "EL (Current & Monitored)+": 37,
            "Special Ed (Current)": 23,
            "Special Ed (Former)": 43,
            "Continuously Enrolled": 48,
            "Non-Continuously Enrolled": 45
        }

        self.success_data = dict()
    
    def get_student_success_status_dict(self, group, data):
        target = self.target[group]
        data_dict = {
            "1." + "Target": target,
            "2." + "Target Met": "N",
            "3." + "STAAR Component Score": data["Average"],
            "4." + "% at Approaches GL Standard or Above": data["Approaches Percent"],
            "5." + "% at Meets GL Standard or Above": data["Meets Percent"],
            "6." + "% at Masters GL Standard": data["Masters Percent"],
            "7." + "Total Tests": data["Total"]
        }
        if data["Average"] >= target:
            data_dict["2." + "Target Met"] = "Y"

        return data_dict
    
    def get_data_on_race(self, race):
        total_count = 0
        meet_count = 0
        approach_count = 0
        master_count = 0
        for index, row in self.df.iterrows():
            row_race = row['Ethnicity']
            row_approaches = row['AI Approaches']
            row_meet = row['AI Meets']
            row_master = row['AI Masters']
            if race is None or race == row_race:
                total_count += 1
                if row_approaches:
                    approach_count += 1
                elif row_meet:
                    approach_count += 1
                    meet_count += 1
                elif row_master:
                    approach_count += 1
                    meet_count += 1
                    master_count += 1
        master_percent = 0
        meet_percent = 0
        approach_percent = 0
        if total_count != 0:
            master_percent = (master_count/total_count)*100
            meet_percent = (meet_count/total_count)*100
            approach_percent = (approach_count/total_count)*100
            
        average = (master_percent + meet_percent + approach_percent)/3
        
        data = {"Total": total_count, 
                "Masters Percent": master_percent, 
                "Meets Percent": meet_percent, 
                "Approaches Percent": approach_percent, 
                "Average": average}
        
        return self.get_student_success_status_dict(race, data)
    
    def get_col_stat(self, col_name, no_tag, group):
        total_count = 0
        meet_count = 0
        approach_count = 0
        master_count = 0
        for index, row in self.df.iterrows():
            if col_name not in row:
                continue
            row_col_val = row[col_name]
            row_approaches = row['AI Approaches']
            row_meet = row['AI Meets']
            row_master = row['AI Masters']
            if row_col_val != no_tag:
                total_count += 1
                if row_approaches:
                    approach_count += 1
                elif row_meet:
                    approach_count += 1
                    meet_count += 1
                elif row_master:
                    approach_count += 1
                    meet_count += 1
                    master_count += 1
                    
        master_percent = 0
        meet_percent = 0
        approach_percent = 0
        if total_count != 0:
            master_percent = (master_count/total_count)*100
            meet_percent = (meet_count/total_count)*100
            approach_percent = (approach_count/total_count)*100
            
        average = (master_percent + meet_percent + approach_percent)/3
        
        data = {"Total": total_count, 
                "Masters Percent": master_percent, 
                "Meets Percent": meet_percent, 
                "Approaches Percent": approach_percent, 
                "Average": average}
        
        return self.get_student_success_status_dict(race, data)
    
    def get_success_data(self):
        index = 97
        for race in self.races:
            if str(race) == "nan":
                continue
            race_success_data = self.get_data_on_race(race)
            self.success_data[chr(index) + ". " + race] = race_success_data
            index += 1
        
        econ_disadv_success_data = self.get_col_stat("ED", "No", "Econ Disadv")
        self.success_data[chr(index) + ". " + "Econ Disadv"] = econ_disadv_success_data
        
        index += 1
        lep_success_data = self.get_col_stat("LEP", "Other Non-LEP Student", "EL (Current & Monitored)+")
        self.success_data[chr(index) + ". " + "EL (Current & Monitored)+"] = lep_success_data
        
        index += 1
        special_ed_current_success_data = self.get_col_stat("Special Ed Indicator", "No", "Special Ed (Current)")
        self.success_data[chr(index) + ". " + "Special Ed (Current)"] = special_ed_current_success_data
        
        index += 1
        special_ed_former_success_data = self.get_col_stat("Special Ed Indicator (Former)", "No", "Special Ed (Former)")
        self.success_data[chr(index) + ". " + "Special Ed (Former)"] = special_ed_former_success_data
        
        continuously_enrolled_success_data = self.get_col_stat("Continuously Enrolled", "No", "Continuously Enrolled")
        continuously_not_enrolled_success_data = self.get_col_stat("Continuously Enrolled", "Yes", "Non-Continuously Enrolled")

        index += 1
        self.success_data[chr(index) + ". " + "Continuously Enrolled"] = continuously_enrolled_success_data
        index += 1
        self.success_data[chr(index) + ". " + "Non-Continuously Enrolled"] = continuously_not_enrolled_success_data
        
        return self.success_data
        

# %%
'''
## Metric Extraction
'''

# %%
## Academic Data for reading and maths
academic_data_reading = academic_achievement(df_reading, "ELA/Reading").get_academic_data()
academic_data_maths = academic_achievement(df_maths, "Maths").get_academic_data()

## Growth Data for reading and maths
growth_data_reading = growth_status(df_reading, "ELA/Reading").get_growth_data()
growth_data_maths = growth_status(df_maths, "Maths").get_growth_data()

## Overall Success Data
success_data = success_status(df_reading, df_maths).get_success_data()

# %%
'''
### Consolidating the entire data into a single dataframe
'''

# %%
certificate_df = pd.DataFrame(index =['Academic Achievement Status'])
certificate_df = certificate_df.append(pd.DataFrame.from_dict(academic_data_reading))
certificate_df = certificate_df.append(pd.DataFrame.from_dict(academic_data_maths))

certificate_df = certificate_df.append(pd.DataFrame(index =['Growth Status']))
certificate_df = certificate_df.append(pd.DataFrame.from_dict(growth_data_reading))
certificate_df = certificate_df.append(pd.DataFrame.from_dict(growth_data_maths))

certificate_df = certificate_df.append(pd.DataFrame(index =['Student Success Status']))
certificate_df = certificate_df.append(pd.DataFrame.from_dict(success_data))

# %%
certificate_df.head()

# %%
certificate_df.to_csv("certificate.csv")

# %%
'''
### STAAR Performance Certificate
'''

# %%
