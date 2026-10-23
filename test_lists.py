import lists


def test_clamp():
    assert lists.clamp([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == ['low', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'high']


def test_reverse():
    assert lists.reverse([1,2,3]) == [3,2,1]
    assert lists.reverse([1,2,1,3,4,5]) == [5,4,3,1,2,1]
