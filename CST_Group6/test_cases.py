from person import Person
import csv

def week1cases():
    """
    Runs week 1 test cases prints user names and results in the console
    """
    print("Test case week 1:")
    with open("users_context_attributes.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            user = Person(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]))
            user.print_engagement_level()

def week2cases():
    """
    Runs week 2 test cases prints user names and results in the console
    """
    print("Test case week 2:")
    with open("week2CST.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            user = Person(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]))
            user.print_engagement_level()

# Run test cases as main
if __name__ == "__main__":
    pass
    week1cases()
    week2cases()