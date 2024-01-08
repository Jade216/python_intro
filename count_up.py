def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    for num in range(start, stop+1):
        print(num)

    # why return num DOES NOT work???  if not work, can i use print? what is the difference between print and return in this case?
    


count_up(5, 7)        
