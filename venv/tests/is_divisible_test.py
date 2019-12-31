import pytest
import is_divisible


class TestClass:

    def test1(self):
        pass

    def test2(self):
        assert is_divisible.add_func(2, 3, 1) == 6

    def test3(self):
        assert is_divisible.func2(2) == 5
        assert is_divisible.add_func(1, 1, 1) == 2

    def test4(self):
        assert is_divisible.func2(3) == 1


    # Test.assert_equals(is_divisible(3,3,4),False)
    # Test.assert_equals(is_divisible(12,3,4),True)
    # Test.assert_equals(is_divisible(8,3,4),False)
    # Test.assert_equals(is_divisible(48,3,4),True)
