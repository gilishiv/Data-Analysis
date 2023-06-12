import PopulateDB
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("CDDatabase3")
# Create a cursor object
c = conn.cursor()

# Function to get the Learner's details according to Aptitude score

def get_aptitude_sc():
    Apt_score_oper= input("\n Enter the option for aptitude Score operator (1 for Equal, 2 for Greater than , 3 for Less than):")
    flag = 0

    # Execute the SELECT statement based on the user input
    if Apt_score_oper == "1":
        Apt_score = input("\n Enter the aptitude Score: ")
        c.execute(f"SELECT LearnerId, Cohort, Name, Location, Phone_no, Email, Aptitude_score FROM Learners1 WHERE Aptitude_score= '{Apt_score}'")
        Apt_score_oper_E="equal to "
        flag = 1
    elif Apt_score_oper == "2":
        Apt_score = input("\n Enter the aptitude Score: ")
        c.execute(f"SELECT LearnerId, Cohort, Name, Location, Phone_no, Email, Aptitude_score FROM Learners1 WHERE Aptitude_score >'{Apt_score}'")
        Apt_score_oper_E = "greater than "
        flag = 1
    elif Apt_score_oper == "3":
        Apt_score = input("\n Enter the aptitude Score: ")
        c.execute(f"SELECT LearnerId, Cohort, Name, Location, Phone_no, Email, Aptitude_score FROM Learners1  WHERE Aptitude_score < '{Apt_score}'")
        Apt_score_oper_E = "less than "
        flag = 1
    else:
        print("invalid option.")

    if flag == 1:
    # Fetch all the results
        result = c.fetchall()

    # Display the results
        print(f"Display all values in the DB where Aptitude score is  {Apt_score_oper_E} '{Apt_score}':")
        for row in result:
            print(row)

# Function to get the Learner's details according to Behavioural score

def get_behavioural_score():
    Beh_score_oper=input("\n Enter the option for behavioural Score operator (1 for Equal, 2 for Greater than , 3 for Less than):")
    flag = 0
    # Execute the SELECT statement based on the user input
    if Beh_score_oper == "1":
        Beh_score = input("\n Enter the behavioural Score: ")
        c.execute(f"SELECT LearnerId, Cohort, Name, Location, Phone_no, Email, Behavioral_score FROM Learners1 WHERE Behavioral_score= '{Beh_score}'")
        Beh_score_oper_E="equal to "
        flag = 1
    elif Beh_score_oper == "2":
        Beh_score = input("\n Enter the behavioural Score: ")
        c.execute(f"SELECT LearnerId, Cohort, Name, Location, Phone_no, Email, Behavioral_score FROM Learners1 WHERE Behavioral_score > '{Beh_score}'")
        Beh_score_oper_E = "greater than "
        flag = 1
    elif Beh_score_oper == "3":
        Beh_score = input("\n Enter the behavioural Score: ")
        c.execute(f"SELECT LearnerId, Cohort, Name, Location, Phone_no, Email, Behavioral_score FROM Learners1 WHERE Behavioral_score < '{Beh_score}'")
        Beh_score_oper_E = "less than "
        flag = 1
    else:
        print("invalid option.")

    if flag == 1:
    # Fetch all the results
        result = c.fetchall()

    # Display the results
        print(f"Display all values in the DB where Behavioural score is  {Beh_score_oper_E} '{Beh_score}':")
        for row in result:
            print(row)

# Function to get the Learner's details based on their Location

def get_location():
    # User input for location
    location_input = input("\n Enter the location (1 for London, 2 for Newcastle, 3 for Sunderland): ")
    flag=0
    # Execute the SELECT statement based on the user input
    if location_input == "1":
        c.execute("SELECT * FROM Learners1 WHERE Location LIKE 'London%'")
        location_name = "London"
        flag=1
    elif location_input == "2":
        c.execute("SELECT * FROM Learners1 WHERE Location LIKE 'Newcastle%'")
        location_name = "Newcastle"
        flag = 1
    elif location_input == "3":
        c.execute("SELECT * FROM Learners1 WHERE Location LIKE 'Sunderland%'")
        location_name = "Sunderland"
        flag = 1
    else:
        print("Invalid location input.")

    if flag == 1 :
    # Fetch all the results
        result = c.fetchall()

    # Display the results
        print(f"Display all values in the DB where Location starts with '{location_name}':")
        for row in result:
            print(row)

# Function to get the Learner's details based on thier Cohort

def get_cohort():
    cohort_value = input("\n Enter the option for Cohort (1 for UKNEW6 , 2 for UKSUN1, 3 for UKEDI6, 4 for UKNEW8, 5 for UKEXE1, 6 for UKEXE2, 7 for UKNEW7, 8 for USWAS15 ): ")
    flag = 0
    # Execute the SELECT statement based on the user input
    if cohort_value == "1":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'UKNEW6'")
        coh_name = "UKNEW6"
        flag = 1
    elif cohort_value == "2":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'UKSUN1'")
        coh_name = "UKSUN1"
        flag = 1
    elif cohort_value == "3":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'UKEDI6'")
        coh_name = "UKEDI6"
        flag = 1
    elif cohort_value == "4":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'UKNEW8'")
        coh_name = "UKNEW8"
        flag = 1
    elif cohort_value == "5":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'UKEXE1'")
        coh_name = "UKEXE1"
        flag = 1
    elif cohort_value == "6":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'UKEXE2'")
        coh_name = "UKEXE2"
        flag = 1
    elif cohort_value == "7":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'UKNEW7'")
        coh_name = "UKNEW7"
        flag = 1
    elif cohort_value == "8":
        c.execute("SELECT * FROM Learners1 WHERE Cohort = 'USWAS15'")
        coh_name = "USWAS15"
        flag = 1
    else:
        print("Invalid location input.")

    if flag == 1:
    # Fetch all the results
        result = c.fetchall()

    # Display the results
        print(f"Display all values in the DB of the Cohort '{coh_name}':")
        for row in result:
                print(row)



# Function to call the different function based on user input

def search():
    if field == "1":
        get_aptitude_sc()
    elif field == "2":
        get_behavioural_score()
    elif field == "3":
        get_location()
    elif field == "4":
        get_cohort()
    else:
        print("invalid option.")

# Function to display message for invalid input

def invalid():
    if search1 == "0":
        print("Thank you")
        exit()
    elif search1 != "1":
        print("invalid option")
        exit()

# Display the Learner details based on user input

search1 = input("\n Do you want to look at the Learner's details?( 1 for yes and 0 for No): ")
invalid()

while (search1 == "1"):
    field = input(
        "\n Enter the option by which you want to display the Learner's details (1 for Aptitude score, 2 for Behavioural score, 3 for Location, 4 for Cohort): ")
    search()
    search1 = input("\n Do you want to look at the Learner's details?( 1 for yes and 0 for No): ")
    invalid()







# Close the cursor and connection
c.close()
conn.close()
