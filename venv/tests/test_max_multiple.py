import pytest
import max_multiple

def test_max_multiple():
    assert max_multiple.max_multiple(2,7) == 6
    assert max_multiple.max_multiple(3, 10) == 9
    assert max_multiple.max_multiple(7, 17) == 14
    assert max_multiple.max_multiple(10, 50) == 50
    assert max_multiple.max_multiple(37, 200) == 185
    assert max_multiple.max_multiple(7, 100) == 98


# Test.describe("Basic tests")
# Test.assert_equals(max_multiple(2,7),6)
# Test.assert_equals(max_multiple(3,10),9)
# Test.assert_equals(max_multiple(7,17),14)
# Test.assert_equals(max_multiple(10,50),50)
# Test.assert_equals(max_multiple(37,200),185)
# Test.assert_equals(max_multiple(7,100),98)
# print("<COMPLETEDIN::>")
