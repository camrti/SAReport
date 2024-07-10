# This file can be executed also as Main to get results of all test cases
from functions import F_SL_function, F_M_function, F_FQ_function, engagement_level

# Person class
class Person():
    """
    A class to represent people using the platform. Only values for CST are required here (plus the name for better data inspection)

    Attributes:
    ----------
    name : str
        Person name
    F_SL
        Value for F_SL function. Calls F_SL_function(x) from functions.py where x is the number of hours spent on the platform in the last 7 days
    F_FQ
        Value for F_FQ function. Calls F_FQ_function(x) from functions.py where x is the number of questions asked on the forum in the last 7 days
    F_NA
        Value for F_NA function. Calls F_FQ_function(x) from functions.py where x is the number of unanswered questions asked on the forum in the last 7 days
    F_M
        Value for F_M function. Calls F_M_function(x) from functions.py where x is the number of material used in the last 7 days

    Methods:
    ----------
    print_datas():
        Prints CST user data in the console
    get_engagement_level():
        Returns the level of engagement of the user calculated with the engagement_level() function from functions.py
    print_engagement_level():
        Prints user engagement level in the console
    get_engagement_value():
        Returns the value of engagement (0->1) of the user calculated with the engagement_level() function from functions.py

    """
    def __init__(self, name : str, F_SL, F_FQ, F_NA, F_M):
        """
        Initializes a Person object. A Person object contains CST datas of users of the platform (plus the name)

        Parameters:
        ----------
        name : str
            Person name
        F_SL
            Value for F_SL function. Calls F_SL_function(x) from functions.py where x is the number of hours spent on the platform in the last 7 days
        F_FQ
            Value for F_FQ function. Calls F_FQ_function(x) from functions.py where x is the number of questions asked on the forum in the last 7 days
        F_NA
            Value for F_NA function. Calls F_FQ_function(x) from functions.py where x is the number of unanswered questions asked on the forum in the last 7 days
        F_M
            Value for F_M function. Calls F_M_function(x) from functions.py where x is the number of material used in the last 7 days
        """
        self.name = name
        self.fsl = F_SL_function(F_SL)
        self.ffq = F_FQ_function(F_FQ)
        self.fna = F_FQ_function(F_NA)
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
        return engagement_level(self.fsl, self.ffq, self.fm, self.fna)
    
    def print_engagement_level(self):
        """
        Prints user engagement level in the console
        """
        print("Results for",self.name+":",self.get_engagement_level())

    def get_engagement_value(self):
        """
        Returns the value of engagement (0->1) of the user calculated with the engagement_level() function from functions.py

        Returns:
        ----------
        float
            Engagement value
        """
        return engagement_level(self.fsl, self.ffq, self.fm, self.fna, returnValue=True)
