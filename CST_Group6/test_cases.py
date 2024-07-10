from person import Person
import csv

def runCases(filepath : str,weekNum : int = None):
    """
    Runs week 1 test cases prints user names and results in the console

    Parameters:
    ----------
    filepath : str
        String containing the name of the csv file with the records to analyze
    weekNum : int
        Week number to print in console (default = None. None value with print a "Rusults:" string)
    """
    if weekNum is not None:
        print(f"Test case week {weekNum}:")
    else:
        print("Results:")
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            user = Person(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]))
            user.print_engagement_level()

# Run test cases as main
if __name__ == "__main__":
    pass
    runCases("users_context_attributes.csv",1)
    runCases("week2CST.csv",2)