def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """
    try:
        number_of_items = len(item_prices)
        # If the number of items is greater than 3- loop runs. Loop get the smallest number in the list.
        if number_of_items >= 3:
            min_num = min(item_prices)
            # Check for less than 0 numbers
            if min_num < 0:
                raise ValueError('There are negative numbers, please try again')
            return min_num
            # If items are less than 3 no discount applied. None is returned to the call
        return None
    except TypeError:
        return None

if __name__ == '__main__':
    main()