import sqlite3
import pandas as pd

# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel('tech_nontech.xlsx', sheet_name='Sheet1')

# Connect to the SQLite database
conn = sqlite3.connect('tech_nontech_Database.db')
# Create a cursor object
c = conn.cursor()

# Create a new table
c.execute('''CREATE TABLE IF NOT EXISTS Learners (
                LearnerId INTEGER PRIMARY KEY,
                Educational_background TEXT,
                Tech_nontech_background TEXT
            )''')

# Iterate over the rows in the DataFrame
for _, row in df.iterrows():
    educational_background = row['Educational Background']
    
    # Check if the educational background contains tech-related keywords
    tech_keywords = ["computer", "programming", "software", "data", "sql", "python", "information"]
    is_tech = any(keyword in str(educational_background).lower() for keyword in tech_keywords)
    
    # Update the Tech_nontech_background column accordingly
    tech_nontech = "Tech" if is_tech else "Non-Tech"
    
    # Insert the record into the database
    c.execute("INSERT INTO Learners (Educational_background, Tech_nontech_background) VALUES (?, ?)",
              (educational_background, tech_nontech))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
c.close()
conn.close()

# Connect to the SQLite database
conn = sqlite3.connect('tech_nontech_Database.db')
# Create a cursor object
c = conn.cursor()

# Execute a SELECT query to retrieve all records from the Learners table
c.execute("SELECT * FROM Learners")
rows = c.fetchall()

# Print the data
for row in rows:
    print(row)

#delete the content of the table
c.execute('DELETE FROM Learners')
conn.commit()

# Close the cursor and connection
c.close()
conn.close()
