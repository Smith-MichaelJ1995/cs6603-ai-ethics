import pandas as pd
import matplotlib.pyplot as plt

# read csv file from filesystem
df = pd.read_csv('mental-health-in-tech-survey-2019.csv')

# Protected Class Variable 1: Race
dfCaucasian
dfBlack
dfHispanic
dfAsian
dfMixed

# traverse through all records of survey dataframe
#for index, record in df.iterrows():
#    print(record)
#    if "what" in record:
#        print(record)


# total number of columns
print("Columns = {}".format(len(df.columns)))
print("Rows = {}".format(len(df.index)))