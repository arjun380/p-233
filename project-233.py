import pandas as pd
data = pd.read_csv('projectC233_studentData.csv')

data['Total_marks_obtained']=data.loc[:,[2,3,4]].sum(axis=1)
data.loc[data['Total_marks_obtained'] > 250, 'grade'] = 'A'
data.loc[data['Total_marks_obtained'] < 250, 'grade'] = 'B'
data['Percentage']=(data['Total_marks_obtained']/data['Overall_Total'])*100
print("report_card: \n",data)