import pytest
import house_number

def test_house_numbers_sum():
    assert house_number.house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]) == 11
    assert house_number.house_numbers_sum([4,2,1,6,0]) == 13
    assert house_number.house_numbers_sum([4,1,2,3,0,10,2]) == 10
    assert house_number.house_numbers_sum([0,1,2,3,4,5]) == 0

# [5, 1, 2, 3, 0, 1, 5, 0, 2], 11),
#     ([4, 2, 1, 6, 0], 13),
#     ([4, 1, 2, 3, 0, 10, 2], 10),
#     ([0, 1, 2, 3, 4, 5], 0),
