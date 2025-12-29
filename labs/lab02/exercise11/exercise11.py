def is_valid_multiple(amount):
    """
    Checks if the amount is a multiple of RM10.
    """
    if amount % 10 == 0 :
        return True
    else: 
        return False

def is_balance_sufficient(amount, balance):
    """
    Checks if the balance is enough for the withdrawal.
    """
    if balance >= amount :
        return True
    else:
        return False

def process_withdrawal(amount, balance):
    """
    Processes the withdrawal.
    Returns the new balance if successful.
    Returns "Invalid Amount" if not a multiple of 10.
    Returns "Insufficient Funds" if balance is too low.
    """
    balance = 
    if is_valid_multiple(amount) == False:
        return "Invalid Amount"

    if is_balance_sufficient(amount, balance) == False:
        return "Insufficient Funds"

    # Withdrawal successful
    return balance - amount
