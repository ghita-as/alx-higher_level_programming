#!/usr/bin/python3
def magic_calculation(a, b):
    # Dummy import for bytecode compatibility
    import magic_calculation_102

    # Import add and sub functions
    add, sub = magic_calculation_102.add, magic_calculation_102.sub

    # Check if a is less than b
    if a < b:
        # Calculate c by adding a and b
        c = add(a, b)

        # Iterate over the range (4, 6) and add to c
        for i in range(4, 6):
            c = add(c, i)

        return c
    else:
        # If a is not less than b, perform sub(a, b)
        return sub(a, b)
