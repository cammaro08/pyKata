import pytest
import get_nth_node

def test_get_nth():
    list = get_nth_node.build_one_two_three()

    assert(get_nth_node.get_nth(list, 0).data, 1, "First node should be located at index 0.")
    assert(get_nth_node.get_nth(list, 1).data, 2, "Second node should be located at index 1.")
    assert(get_nth_node.get_nth(list, 2).data, 3, "Third node should be located at index 2.")

    # raise (Exception): assert lambda: get_nth_node.get_nth(list, 3))
    # raise("Invalid index value should throw error.", lambda: get_nth_node.get_nth(list, 3))
    # raise("Invalid index value should throw error.", lambda: get_nth_node.get_nth(list, -1))
    # raise("Invalid index value should throw error.", lambda: get_nth_node.get_nth(list, 100))
    # raise("None linked list should throw error.", lambda: get_nth_node.get_nth(None, 0))
