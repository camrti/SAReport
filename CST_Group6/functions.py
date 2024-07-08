# Helper functions for CST group 6
from constants import F_FQ_NA_mappings

def F_SL_function(x):
    """
    Function for returning the corresponding y value of F_SL given x

    Parameters:
    ----------
    x
        x value of function F_SL
    
    Returns:
    ----------
    y
        y value of function F_SL (or None for un-specified cases)
    """
    match x:
        case x if 0 <= x < 4:
            return 0
        case x if 4 <= x < 7:
            return 0.1
        case x if 7 <= x < 10:
            return 0.2
        case x if 10 <= x < 14:
            return 0.3
        case x if 14 <= x < 18:
            return 0.4
        case x if 18 <= x < 21:
            return 0.7
        case x if 21 <= x < 24:
            return 0.8
        case x if 24 <= x < 28:
            return 0.9
        case x if x >= 28:
            return 1
        case _:
            return None

def F_M_function(x):
    """
    Function for returning the corresponding y value of F_M given x

    Parameters:
    ----------
    x
        x value of function F_M
    
    Returns:
    ----------
    y
        y value of function F_M (or None for un-specified cases)
    """
    match x:
        case 0:
            return 0
        case x if 1 <= x < 4:
            return 0.1
        case x if 4 <= x < 7:
            return 0.4
        case x if 7 <= x < 9:
            return 0.6
        case x if 9 <= x < 11:
            return 0.8
        case x if x >= 11:
            return 1
        case _:
            return None

def engagement_level(F_SL, F_FQ, F_M, F_NA, w_SL=0.6, w_FQ=0.2, w_M=0.2, w_NA=0.1, dashboardMapping : bool=False):
    """
    Function that returns engagement level given the CST parameters and mappings (weights are declared but can be changed)

    Parameters:
    ----------
    F_SL
        y value of function F_SL
    F_FQ
        y value of function F_FQ
    F_FM
        y value of function F_FM
    F_NA
        y value of function F_NA
    w_SL
        Weight of function F_SL (default already set)
    w_FQ
        Weight of function F_FQ (default already set)
    w_M
        Weight of function F_M (default already set)
    w_NA
        Weight of function F_NAL (default already set)
    dashboardMapping : bool
        Bool to specify if you need dashboard mapping (see get_dashboard_mapping() for more info) [True] of if you need the label [False]. Default is False

    Returns:
    ----------
    E
        Engagement level
    """
    
    # Engagement level
    E = w_SL * F_SL + w_FQ * F_FQ_NA_mappings["F_FQ"][F_FQ] + w_M * F_M - w_NA * F_FQ_NA_mappings["F_NA"][F_NA]

    # Check if dashboard mapping is needed
    if dashboardMapping: return get_dashboard_mapping(E)

    if E < 0.4:
        return "Low Engagement"
    elif E < 0.7:
        return "Medium Engagement"
    else:
        return "High Engagement"
    
def get_dashboard_mapping(E):
    """
    Function to get our dashboard mapping for the Engagement value
    The mapping is this:
        - 0 if Low Engagement
        - 1 if Medium Engagement
        - 2 if High Engagement

    Parameters:
    ----------
    E
        Engagement level (numeric)
    
    Returns:
    ----------
    E
        Dashboard-mapped engagement level
    """
    if E < 0.4:
         return 0
    if E < 0.7:
        return 1
    return 2