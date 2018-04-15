def print_formatted(number):
    w = len("{0:b}".format(number))
    for i in range(1,number+1):
        b = "{0:{w}b}".format(i,w=w)
        h = "{0:{w}X}".format(i,w=w)
        o = "{0:{w}o}".format(i,w=w)
        d = "{0:{w}d}".format(i,w=w)
        print(d+" "+o+" "+h+" "+b)
