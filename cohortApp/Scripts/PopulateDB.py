#import the packages required
import pandas as pd
import sqlite3


#connect to sqlite database
conn=sqlite3.connect("CDDatabase3")
#create cursor object
c = conn.cursor()

#create the table Cohorts
c.execute('CREATE TABLE IF NOT EXISTS Cohorts(Cohort_ID text, Cohort_Name text)')
conn.commit()

#create the table Learners
c.execute('CREATE TABLE IF NOT EXISTS Learners(LearnerId integer primary key ,Sno integer,Status text,Cohort text,Name text,Location text, '
          'Phone_no integer,Email text,Aptitude_score integer,Behavioral_score integer,Educational_background text,'
          'Yop integer,Last_degree_college_name text,Last_degree_percentage real,Experience text,Waiver_for_marketing '
          'text,Resume_available text,Consent_shared text,Documents_received text,Tech_nontech_background text,'
          ' FOREIGN KEY(Cohort) REFERENCES Cohorts(Cohort_ID))')
conn.commit()

#create the table Learners1
c.execute('CREATE TABLE IF NOT EXISTS Learners1(LearnerId integer primary key ,Cohort text,Name text,Location text, '
          'Phone_no integer,Email text,Aptitude_score integer,Behavioral_score integer,Tech_nontech_background text,FOREIGN KEY(Cohort) REFERENCES Cohorts(Cohort_ID))')
conn.commit()


# Define filepath, read the file content of cohort file and insert into DB table named "Cohorts".
filepath1 = '..\\Data\\Cohort_det.xlsx'
df1=pd.read_excel(filepath1)
df1.to_sql('Cohorts', conn,if_exists='replace', index=False)

# Define filepath, read the file content of cohort file and insert into 2 tables.
#  Tables named "Learners" has all the columns as in the Excel sheet
#  Tables named "Learners1" has main columns from the Excel sheet

filepath = '..\\Data\\Cohorts_test.xlsx'
f=pd.ExcelFile(filepath)

# Iterate through each worksheet
for sheet in f.sheet_names:
    # Parse data from each worksheet as a Pandas DataFrame
    df = f.parse(sheet)
    df['Cohort'] = sheet
    df.to_sql('Learners', conn, if_exists='append', index=False )

# Remove  columns as index base
    df.drop(df.columns[[0,1,9,10,11,12,13,14,15,16,17]], axis=1, inplace=True)
    df.to_sql('Learners1', conn, if_exists='append', index=False)







