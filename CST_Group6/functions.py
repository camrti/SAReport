# Helper functions for CST group 6

def F_SL_function(x):
    """
    Function for returning the corresponding y value of F_SL given x

    Parameters:
    ----------
    x
        x value
    
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
        x value
    
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
        
def F_FQ_function(x):
    """
    Function for returning the corresponding y value of F_FQ given x

    Parameters:
    ----------
    x
        x value
    
    Returns:
    ----------
    y
        y value of function F_FQ (or None for un-specified cases)
    """
    if x<=0: return 0
    if 0<x<=3: return 0.5
    if x>3: return 1
    return None


def engagement_level(F_SL, F_FQ, F_M, F_NA, w_SL=0.56, w_FQ=0.12, w_M=0.32, w_NA=0.10, returnValue : bool=False):
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
    returnValue : bool
        Bool to specify if the function should return the engagement value (0->1) and not the Label

    Returns:
    ----------
    E
        Engagement level
    """
    
    # Engagement level
    E = w_SL * F_SL + w_FQ * F_FQ + w_M * F_M - w_NA * F_NA

    # Check if dashboard mapping is needed
    if returnValue: return round(E,2)

    if E < 0.4:
        return "Low Engagement"
    elif E < 0.7:
        return "Medium Engagement"
    else:
        return "High Engagement"
