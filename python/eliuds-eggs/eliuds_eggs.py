def egg_count(display_value):
    return len([x for x in format(display_value, 'b') if x == '1'])
