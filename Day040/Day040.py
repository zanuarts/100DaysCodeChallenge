# https://stackoverflow.com/questions/60017186/delete-occurrences-of-an-element-if-it-occurs-more-than-n-times-in-python

def delete_nth(order, max_e):
    # Get a new list that we will return
    result = []

    # Get a dictionary to count the occurences
    occurrences = {}

    # Loop through all provided numbers
    for n in order:

        # Get the count of the current number, or assign it to 0
        count = occurrences.setdefault(n, 0)

        # If we reached the max occurence for that number, skip it
        if count >= max_e:
            continue

        # Add the current number to the list
        result.append(n)

        # Increase the 
        occurrences[n] += 1

    # We are done, return the list
    return result