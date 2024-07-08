import matplotlib.pyplot as plt
import numpy as np
from functions import F_SL_function, F_M_function
from plotting import plot_step_function, plot_customised_step_function
from test_cases import week1cases, week2cases
from constants import F_FQ_labels, F_NA_labels, F_FQ_values, F_NA_values
from fuzzy import plot_fuzzy_functions as plot_ff

def main():
    # Generate graphs
    # Fuzzified forum questions
    x_values = np.linspace(0, 3.5, 50)
    plot_ff(x_values,F_FQ_labels,"Fuzzified Forum Questions","plot_fuzzy_forum_questions.png")
    # Fuzzified non answered forum questions
    plot_ff(x_values, F_NA_labels,"Fuzzified Non Answered Forum Questions","plot_fuzzy_not_answered.png")
    # F_FQ
    plot_step_function(F_FQ_labels, F_FQ_values, 'F_FQ (Questions on the forum)', 'Questions on the forum', 'plot_F_FQ.png')
    # F_NA
    plot_step_function(F_NA_labels, F_NA_values, 'F_NA (Questions without answers)', 'Questions without answers', 'plot_F_NA.png')
    # F_SL
    x_values = [0, 4, 7, 10, 14, 18, 21, 24, 28, 35]
    plot_customised_step_function(x_values,[F_SL_function(x) for x in x_values],'F_SL (Hours spent on the platform)','Hours spent on the platform','plot_F_SL.png')
    # F_M
    x_values = [0, 1, 4, 7, 9, 11, 13]
    plot_customised_step_function(x_values,[F_M_function(x) for x in x_values],'F_M (Usage of provided material)','Usage of provided material','plot_F_M.png')

    # Run test cases
    week1cases()
    week2cases()

# MAIN
if __name__ == "__main__":
    main()
