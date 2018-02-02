#test_person.py
from mock import patch
from person import Person

# mock the get_name function
#@patch('data_source.get_name') # This won't work as expected!
#@patch('Person.get_name') # this will not work - file name, not Class name
# @patch('person.get_name') # not working 

# I have to do this - test passed
@patch('person.data_source.get_name') 

def test_name(mock_get_name):
    # set a return value for our mock object
    mock_get_name.return_value = "Bob" 
    person = Person()
    name = person.name()
    assert name == "Bob"

'''
nostests test_person.py
will return error
'''
