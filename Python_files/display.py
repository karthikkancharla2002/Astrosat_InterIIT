import pandas as pd

file1='./Astrosat_readings_new.csv'
filedata=pd.read_csv(file1)

required_data = filedata[['Proposal_ID']]
print(required_data.head())


pid = input("Enter the required proposal ID: ")
