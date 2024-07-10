# Helper functions for CST group 6
import matplotlib.pyplot as plt

def plot_customised_step_function(x_values, y_values, label : str, xlabel : str, filename : str):
    """
    Plots and saves step functions of different values (used for F_SL and F_M)

    Parameters:
    ----------
    x_values
        Array of values for x
    y_values
        Array of values for y
    label : str
        Function label (also used for title, where "Step function for " is added before this label)
    xlabel : str
        x axis label
    filename : str
        Filename for saving the file
    """
    plt.figure(figsize=(10, 6))
    plt.step(x_values, y_values, where='post', label=label, marker='o')
    plt.title('Step function for '+label)
    plt.xlabel(xlabel)
    plt.ylabel('Value')
    plt.grid(True)
    plt.ylim(0, 1.1)
    plt.yticks(sorted(set(y_values)))
    plt.xticks(x_values)
    plt.legend()
    plt.savefig(filename)
    plt.close()