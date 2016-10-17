
def multiple_definitions(value):

    foo = 123 # unnecessary assignment, value 123 is never read
    if value:
        foo = "bar"
    else:
        foo = "baz"

    print foo
