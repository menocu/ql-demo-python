import lib.classes

def good_raise():
    raise lib.classes.AnExceptionClass()

def bad_raise():
    # this will raise a TypeError in python 3
    # rather than the intended error
    raise lib.classes.ARandomClass()

try:
    good_raise()
except lib.classes.AnExceptionClass:
    print("except succeeded")

try:
    bad_raise()
# This except also fails in python3
except lib.classes.ARandomClass:
    print("except succeeded")