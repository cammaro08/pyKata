import pytest
import addition_Binary

def test_add_binary():
    assert addition_Binary.add_binary(1,1) == "10"
    assert addition_Binary.add_binary(0,1) == "1"
    assert addition_Binary.add_binary(1,0) == "1"
    assert addition_Binary.add_binary(2,2) == "100"
    assert addition_Binary.add_binary(51,12) == "111111"

# Test.assert_equals(add_binary(1,1),"10")
# Test.assert_equals(add_binary(0,1),"1")
# Test.assert_equals(add_binary(1,0),"1")
# Test.assert_equals(add_binary(2,2),"100")
# Test.assert_equals(add_binary(51,12),"111111")
