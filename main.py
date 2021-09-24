import pandas as pd 

# read csv file from filesystem
df = pd.read_csv('mental-health-in-tech-survey-2019.csv')



# traverse through all records of survey dataframe
# for index, record in df.iterrows():
#     print(type(record))
#     exit()


# total number of columns
print("Columns = {}".format(len(df.columns)))
print("Rows = {}".format(len(df.index)))