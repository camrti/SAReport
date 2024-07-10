import matplotlib.pyplot as plt # Specified because it is used in plot functions
from functions import F_SL_function, F_M_function, F_FQ_function
from plotting import plot_customised_step_function
from test_cases import runCases

def main():
    # Generate graphs
    # F_FQ
    x_values = [0,1,2,3,4,5]
    plot_customised_step_function(x_values, [F_FQ_function(x) for x in x_values],'F_FQ (Questions on the forum)','Questions on the forum','plot_F_FQ.png')
    # F_NA
    plot_customised_step_function(x_values, [F_FQ_function(x) for x in x_values],'F_NA (Questions without answers)','Questions without answers','plot_F_NA.png')
    # F_SL
    x_values = [0, 4, 7, 10, 14, 18, 21, 24, 28, 35]
    plot_customised_step_function(x_values,[F_SL_function(x) for x in x_values],'F_SL (Hours spent on the platform)','Hours spent on the platform','plot_F_SL.png')
    # F_M
    x_values = [0, 1, 4, 7, 9, 11, 13]
    plot_customised_step_function(x_values,[F_M_function(x) for x in x_values],'F_M (Usage of provided material)','Usage of provided material','plot_F_M.png')

    # Run test cases
    runCases("users_context_attributes.csv",1)
    runCases("week2CST.csv",2)

# MAIN
if __name__ == "__main__":
    main()
