
def change(amount):
    ''' 
        given n cents, returns number of ways to make change
        based on quarters, dimes, nickels, and pennies 
    '''
    coins = [25, 10, 5, 1]
    return change_helper(amount, 0, coins)

def change_helper(amount, denom, coins):

    # only one way to make change with all pennies
    if denom == 3: return 1 

    # cannot make change with 0 value
    elif amount < 0: return 0

    denom_amount = coins[denom]

    sub_denom = change_helper(amount - denom_amount, denom, coins)
    next_denom = change_helper(amount, denom + 1, coins)
    return  sub_denom + next_denom 

    



if __name__ == "__main__":
    print change(1)
    print change(4)
    print change(10)
    print change(15)
    print change(51)
    
