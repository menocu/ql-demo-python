
def multiple_definitions_if(value, flag):

    foo = value # unnecessary assignment, foo is never read before assignment
    if flag:
        foo = "bar"
    else:
        foo = "baz"

    print foo

