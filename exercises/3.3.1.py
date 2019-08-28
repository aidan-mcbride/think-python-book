def print_cell_border():
    print('+ ', end='')
    print('- '*4, end='')

def print_cell_space():
    print('| ', end='')
    print('  '*4, end='')

def print_grid():
    # top border
    print_cell_border()
    print_cell_border()
    print('+')
    # top row space
    print_cell_space()
    print_cell_space()
    print('|')
    print_cell_space()
    print_cell_space()
    print('|')
    print_cell_space()
    print_cell_space()
    print('|')
    print_cell_space()
    print_cell_space()
    print('|')
    # middle border
    print_cell_border()
    print_cell_border()
    print('+')
    # bottom row space
    print_cell_space()
    print_cell_space()
    print('|')
    print_cell_space()
    print_cell_space()
    print('|')
    print_cell_space()
    print_cell_space()
    print('|')
    print_cell_space()
    print_cell_space()
    print('|')
    # bottom border
    print_cell_border()
    print_cell_border()
    print('+')

print_grid()
