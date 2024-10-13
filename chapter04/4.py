
import sys

""" This is the "nester.py" module and it provides one function called print_lol()
    which prints lists that may or may not include nested lists. """

def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    """ This function takes one positional argument called "the_list", which
        is any python list (of - possibly - nested lists). Each data item in
        the provided list is (recursively) printed to the screen on it's own line. """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='', file=fh)
            print(each_item, file=fh)



man = []
other = []

try:
    data = open("sketch.txt")
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The datafile is missing!")

try:
    with open("man_data.txt", 'w') as man_file:
        print_lol(man, fh=man_file)
    with open("other_data.txt", 'w') as other_file:
        print_lol(other, fh=other_file)
except IOError as err:
    print("File error: " + str(err))




