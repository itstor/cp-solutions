def print_nums(*args):
    max = -999
    l = 0
    for i in args:
        if max < len(str(i)):
            max = len(str(i))
    l = max

    return "\n".join(str(i).zfill(l) for i in args)
