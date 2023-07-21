import count
# write 2 tests for this function that test if the function works for integers as well as strings.

def test_count_zeros():
    assert count.count([0,0,0], 0) == 3

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3

# The count which was imported is the file count.py, so you have to specify which function from count.py to use.
# This is done by using count.count().

# run the command:
# python3 -m pytest

# Should be able to see the tests have passed.
