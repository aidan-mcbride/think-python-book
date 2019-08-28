def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(func, arg):
    """
    run a function four times with the given argument
    """
    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print_twice, 'spam')

do_four(print_twice, 'spam')
