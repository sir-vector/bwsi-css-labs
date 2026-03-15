from labs.lab_1.lab_1d import two_sum #importing the sum function from lab

def test_normal_input(): #testing a normal input of a list with positive integers
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_negative_numbers(): #testing with negative numbers in a list
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3]

def test_same_number_twice(): #testing the same number being used twice
    assert two_sum([3, 3, 4], 6) == [0, 1]