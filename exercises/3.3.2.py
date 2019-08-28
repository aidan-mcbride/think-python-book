def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_horiz_border_section():
    """
    Print one cell's border w/ left intersect
    """
    print('+ ', end='')
    print('- '*4, end='')

def print_cell_space_section():
    """
    print one unit tall of cell space
    A cell is four of these tall
    """
    print('| ', end='')
    print('  '*4, end='')

def print_horiz_border():
    """
    print four cells wide of border
    """
    do_four(print_horiz_border_section)
    print('+')

def print_cell_space():
    """
    Print four cells of white space, then a right border
    """
    do_four(print_cell_space_section)
    print('|')

def print_row():
    """
    Print a top border,
    then print four-tall of cell space
    """
    print_horiz_border()
    do_four(print_cell_space)

def print_grid():
    """
    Print four rows, then print a bottom border
    """
    do_four(print_row)
    print_horiz_border()

# actual final function call
print_grid()
