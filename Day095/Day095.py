def abbrev_name(name):
    names = name.split(' ')
    nam = '.'.join([f"{n[0]}" for n in names])
    return nam.upper()

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# Patrick Feeney => P.F