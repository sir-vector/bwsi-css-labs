from labs.lab_1.lab_1c import max_subarray_sum #import function from lab

def test_normal_input(): #testing a normal input list (littered with negatives and positives)
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_negative(): #testing a list of all negatives (technically viable input)
    assert max_subarray_sum([-3,-1,-2]) == -1

def test_single_element(): #testing a list with one object
    assert max_subarray_sum([5]) == 5

def test_empty_list(): #testing an empty list
    assert max_subarray_sum([]) == 0