import pytest
import length_and_count


def test_length():
    list = length_and_count.build_one_two_three()

    assert length_and_count.length(None) == 0, "Length of null list should be zero."
    assert(length_and_count.length(None), 0, "Length of null list should be zero.")
    assert(length_and_count.length(length_and_count.Node(99)), 1, "Length of single node list should be one.")
    assert(length_and_count.length(list), 3, "Length of the three node list should be three.")

def test_count():
    list = length_and_count.build_one_two_three()

    assert (length_and_count.count(list, 1), 1, "list should only contain one 1.")
    assert(length_and_count.count(list, 2), 1, "list should only contain one 2.")
    assert(length_and_count.count(list, 3), 1, "list should only contain one 3.")
    assert(length_and_count.count(list, 99), 0, "list should return zero for integer not found in list.")
    assert(length_and_count.count(None, 1), 0, "null list should always return count of zero.")