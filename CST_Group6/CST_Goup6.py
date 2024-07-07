import matplotlib.pyplot as plt
from functions import F_SL_function, F_M_function
from plotting import plot_step_function, plot_customised_step_function
from test_cases import week1cases

# Explanation of context attributes:
    # F_FQ = Forum questions
    # F_NA = Forum Not answered
    # F_SL = Session Lenght
    # F_M = Material Usage

def main():
    # Mappings for F_FQ and F_NA
    mappings = {
        "F_FQ": {"No activity": 0, "Low activity": 0.5, "High activity": 1},
        "F_NA": {"None": 0, "Some": 0.5, "Many": 1}
    }
    
    # Generate graphs
    # F_FQ
    plot_step_function(list(mappings["F_FQ"].keys()), list(mappings["F_FQ"].values()), 
                       'F_FQ (Questions on the forum)', 'Questions on the forum', 'plot_F_FQ.png')
    
    # F_NA
    plot_step_function(list(mappings["F_NA"].keys()), list(mappings["F_NA"].values()), 
                       'F_NA (Questions without answers)', 'Questions without answers', 'plot_F_NA.png')
    
    # F_SL
    x_values = [0, 4, 7, 10, 14, 18, 21, 24, 28, 35]
    plot_customised_step_function(x_values,[F_SL_function(x) for x in x_values],
                                  'F_SL (Hours spent on the platform)','Hours spent on the platform','plot_F_SL.png')
    
    # F_M
    x_values = [0, 1, 4, 7, 9, 11, 13]
    plot_customised_step_function(x_values,[F_M_function(x) for x in x_values],
                                  'F_M (Usage of provided material)','Usage of provided material','plot_F_M.png')

    # Run test cases
    week1cases()

# MAIN
if __name__ == "__main__":
    main()
