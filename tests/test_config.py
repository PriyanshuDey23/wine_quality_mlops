# configration test
# test cases
# in test_generic (# Assertion function, it should be true if test gets passed( eg :a == b ))


import pytest

class NotinRange(Exception):
    def __init__(self,   message= "Value Not In Range"):
        self.message=message
        super().__init__(self.message)



def test_generic():
    a=5
    with pytest.raises(NotinRange):
        if a not in range(10,20):
            raise NotinRange
    
