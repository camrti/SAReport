# Helper functions for CST group 6
import matplotlib.pyplot as plt

def plot_step_function(labels, values, title, xlabel, filename):
    """
    Plots and saves step functions (used for F_FQ and F_NA)

    Parameters:
    ----------
    labels
        x labels (for values)
    values
        x values
    title
        Plot title
    xlabel
        x axis label
    filename
        filename for saving the file
    """
    plt.figure(figsize=(10, 6))
    plt.step(labels, values, where='post', label=title, marker='o')
    plt.title(f'Step function for {title}')
    plt.xlabel(xlabel)
    plt.ylabel('Value')
    plt.grid(True)
    plt.ylim(0, 1.1)
    plt.yticks(sorted(set(values)))  # Mostra solo i valori assunti dalla funzione
    plt.xticks(labels)  # Mostra solo i valori effettivamente assunti dalla funzione sull'asse X
    plt.legend()
    plt.savefig(filename)  # Salvataggio del grafico con il nome specificato
    plt.close()  # Chiude il grafico per liberare memoria

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
        filename for saving the file
    """
    plt.figure(figsize=(10, 6))
    plt.step(x_values, y_values, where='post', label=label, marker='o')
    plt.title('Step function for '+label)
    plt.xlabel(xlabel)
    plt.ylabel('Value')
    plt.grid(True)
    plt.ylim(0, 1.1)
    plt.yticks(sorted(set(y_values)))  # Mostra solo i valori assunti dalla funzione
    plt.xticks(x_values)  # Mostra solo i valori effettivamente assunti dalla funzione sull'asse X
    plt.legend()
    plt.savefig(filename)  # Salvataggio del grafico con il nome specificato
    plt.close()  # Chiude il grafico per liberare memoria
