import pytest
import is_divisible


class TestClass:

    def test(self):
        assert is_divisible.func(3, 3, 4) == False
        assert is_divisible.func(12, 3, 4) == True
        assert is_divisible.func(8, 3, 4) == False
        assert is_divisible.func(48, 3, 4) == True


