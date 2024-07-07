from person import Person
from person import chiavi_F_FQ, chiavi_F_NA

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