
#Defining the variable with the name of the text file we're referencing
log_file = open("um-server-01.txt")

#Defining the function for sales_report using the variable above as a parameter
def sales_reports(log_file):

  #Running a "for loop" for each line within the log file where the loops goes through each line & day
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        #with a condition "if" day equals to Mon print line
        if day == "Mon":
            print(line)

#Calling the function
sales_reports(log_file)
