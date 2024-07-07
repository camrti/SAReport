# This file can be executed also as Main to get results of all test cases
from functions import F_SL_function, F_M_function, engagement_level

# Same mapping from main (copied for execution as main)
mappings = {
        "F_FQ": {"No activity": 0, "Low activity": 0.5, "High activity": 1},
        "F_NA": {"None": 0, "Some": 0.5, "Many": 1}
    }

# Get lists from mapping dictionary (needed for Person creation later)
chiavi_F_FQ = list(mappings["F_FQ"].keys())
chiavi_F_NA = list(mappings["F_NA"].keys())

# Person class
class Person():
    """
    A class to represent people using the platform. Only values for CST are required here (plus the name for better data inspection)
    Attributes:
    ----------
    name : str
        Person name
    F_SL
        Value for F_SL function. Call F_SL_function(x) from functions.py where x is the number of hours spent on the platform in the last 7 days
    F_FQ
        Value for F_FQ function. Use a value from the list chiavi_F_FQ above
    F_NA
        Value for F_NA function. Use a value from the list chiavi_F_NA above
    F_M
        Value for F_M function. Call F_M_function(x) form functions.py where x is the number of material used in the last 7 days

    Methods:
    ----------
    print_datas():
        Prints CST user data in the console
    get_engagement_level():
        Returns the value of engagement of the user calculated with the engagement_level() function from functions.py
    print_engagement_level
        Prints user engagement level in the console
    """
    def __init__(self, name : str, F_SL, F_FQ, F_NA, F_M):
        """
        Initialize a Person object. A Person object contains CST datas of users of the platform (plus the name)

        Parameters:
        ----------
        name : str
            Person name
        F_SL
            Value for F_SL function. Call F_SL_function(x) from functions.py where x is the number of hours spent on the platform in the last 7 days
        F_FQ
            Value for F_FQ function. Use a value from the list chiavi_F_FQ above
        F_NA
            Value for F_NA function. Use a value from the list chiavi_F_NA above
        F_M
            Value for F_M function. Call F_M_function(x) form functions.py where x is the number of material used in the last 7 days
        """
        self.name = name
        self.fsl = F_SL_function(F_SL)
        self.ffq = F_FQ
        self.fna = F_NA
        self.fm = F_M_function(F_M)

    def print_datas(self):
        """
        Prints CST user data in the console
        """
        print("Hours:",self.fsl,"\tForum Questions:",self.ffq,"\tUn-answered Questions:",self.fna,"\tMaterial Usage:",self.fm)

    def get_engagement_level(self):
        """
        Returns the value of engagement of the user calculated with the engagement_level() function from functions.py

        Returns:
        ----------
        str
            Value of engagement level of user
        """
        return engagement_level(self.fsl, self.ffq, self.fm, self.fna, mappings)
    
    def print_engagement_level(self):
        """
        Prints user engagement level in the console
        """
        print("Results for",self.name+":",self.get_engagement_level())

    def get_dashboard_mapped_engagement_level(self):
        """
        Returns the dashboard-mapped value of engagement of the user calculated with the engagement_level() function from functions.py

        Returns:
        ----------
        int
            Dashboard-mapped value of engagement level of user
        """
        return engagement_level(self.fsl, self.ffq, self.fm, self.fna, mappings, dashboardMapping=True)

def week1cases():
    """
    Runs week 1 test cases prints user names and results in the console
    """
    print("Test case week 1:")
    Test = Person("Aldo", 8, chiavi_F_FQ[2], chiavi_F_NA[1], 7)
    Test.print_engagement_level()
    Test = Person("Filippo", 24,chiavi_F_FQ[0], chiavi_F_NA[0],9)
    Test.print_engagement_level()
    Test = Person("Marta", 30,chiavi_F_FQ[2], chiavi_F_NA[2],16)
    Test.print_engagement_level()
    Test = Person("Matilde", 16,chiavi_F_FQ[1], chiavi_F_NA[0],7)
    Test.print_engagement_level()
    Test = Person("Maya", 26,chiavi_F_FQ[1], chiavi_F_NA[1],2)
    Test.print_engagement_level()
    Test = Person("Matteo", 10,chiavi_F_FQ[2], chiavi_F_NA[1],6)
    Test.print_engagement_level()

# Run test cases as main
if __name__ == "__main__":
    pass
    week1cases()