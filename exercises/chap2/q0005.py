
#!/usr/bin/python

def numbering(xs):
    '''
    numbering
    wrong idea to have side effetc. i.e.
    for i in range(len(xs)):
        xs[i] = (i, xs[i])
    return xs 
    '''
    return list(enumerate(xs))
