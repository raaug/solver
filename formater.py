do_not_add_to_black = set()
# string_green assembles the regex string for green letters
def string_green(gstring):
    gstring = "{}{}{}".format( '/', gstring, '/ && ')
    return gstring.lower()


# format green assembles the raw green letter string
def format_green(green_list):
    for letter, index in green_list:
        do_not_add_to_black.update(letter)
    green = '.....'
    if len(green_list):
        for letter, index in green_list:
            green = green[:index] + letter + green[index + 1:]
    return string_green(green)


def assemble_item(item):
    rstring = '!/'
    a = item
    (letter, index) = a
    for i in range(5):
        if i != index:
            rstring += '.'
        else:
            rstring += letter
    rstring += '/ && '
    return rstring


# 'yellow' is comprised of two parts a letter that is in the answer
# but is not in the correct position
def format_yellow(yellow_list):
    for letter, index in yellow_list:
        do_not_add_to_black.update(letter)
    in_list = []
    in_string = ''
    yellow = '.....'
    yellow_not_in_pos = ''
    
    # format the yellow string
    if len(yellow_list) > 0: # yellow_list is a list of tuples
        for letter, pos in yellow_list:
            yellow = yellow[:pos] + letter + yellow[pos + 1:]
    in_list = list(set(list(yellow))) # Eliminate duplicate letters
    in_list = [c for c in in_list if c.isalpha()] # Remove non-alpha characters

    # characters that are in string but not correct location
    for c in in_list:
        in_string += f'/{c}/ && '

    for item in yellow_list:
        yellow_not_in_pos += assemble_item(item)
    
    ret_string = in_string + yellow_not_in_pos

    return ret_string


def format_black(black_list):
    ret_string = '!/['
    for letter, index in black_list:
        if letter not in do_not_add_to_black:
            ret_string += letter
    ret_string += ']/'
    return ret_string
