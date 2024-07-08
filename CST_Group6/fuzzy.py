import matplotlib.pyplot as plt

def get_fuzzy_rules(labels):
    """
    Function to get membership rules with 3 labels, ranges:
    - First label descends from 0 to 1
    - Second label ascends from 0 to 1 and descends from 2 to 3
    - Third label ascends from 2 to 3

    Parameters:
    ----------
    labels
        Array of 3 string labels
    
    Returns:
    ----------
    membership_rules
        Array of y values in [0] and label in [1] for each membership function (3)
    """
    if len(labels) != 3:
        raise ValueError("You need to specify 3 labels")
    fuzzy_rules = [
        (lambda x: 1.0 if x <= 0 else (1 - x) if 0 < x < 1 else 0.0, labels[0]),
        (lambda x: x if 0 < x < 1 else (1.0 if 1 <= x <= 2 else (3 - x if 2 < x < 3 else 0.0)), labels[1]),
        (lambda x: 0.0 if x <= 2 else (x - 2) if 2 <= x <= 3 else 1.0, labels[2]),
    ]
    return fuzzy_rules

# Funzione per plottare le funzioni di appartenenza
def plot_fuzzy_functions(x_values, labels, title : str, filename : str):
    """
    xvalues
        np array of values for x
    labels
        Labels for each fuzzy function (3)
    title : str
        Plot title
    filename : str
        Filename for saving the file
    """
    rules = get_fuzzy_rules(labels)
    plt.figure(figsize=(10, 6))
    for rule, label in rules:
        values = [rule(x) for x in x_values]
        plt.plot(x_values, values, label=label)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('Membership')
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)  # Salvataggio del grafico con il nome specificato
    plt.close()