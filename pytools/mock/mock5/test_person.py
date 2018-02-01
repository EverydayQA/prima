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

# this patch only file.Class - not the normal one file.method()
@patch('person.Pet')
def test_dog_noise(mock_pet):
    #mock_pet.noise.return_value= "Meoow"
    mock_pet.return_value.noise.return_value= "Meoow"

    person = Person()
    # forgot the return_value - which is what the example is for
    #assert person.pet.noise == "Meoow"
    assert person.pet.noise.return_value == "Meoow"

@patch('person.noise_logger',lambda x: x)
def test_decorator():
    person = Person()
    assert person.pet.noise() == 'Woof'

'''
the -s switch to tell to print to stdout
nostests-s test_person.py
will return error
'''
