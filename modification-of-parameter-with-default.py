
def safe_method(foo, bar=[]):

    for x in bar:
        foo += x

    return foo

def unsafe_method(foo, bar=[]):

    bar.append('baz')

    for x in bar:
        foo += x

    return foo

