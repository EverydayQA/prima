class Dog():

     @property
     def size(self):
         return 2

     @property
     def breed(self):
        return 'c'

import pytest

cases = [{"size":9, "breed":"doberman"}, {"size":2, "breed":"pug"}]

@pytest.mark.parametrize("case", list(cases.values()), ids=list(cases.keys()))
def test_properties(case):

    dog = Dog()
    mocks = ()

    for m, v in case.items():
       mocks += (mock.patch.object(dog, m, return_value=v),)

    with mocks:
        pass
