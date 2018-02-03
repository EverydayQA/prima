import mock
from pytests.lib import person
import unittest


class TestPerson(unittest.TestCase):
    """

    Here is how to mock.patch the get_name function
    @mock.patch('Person.get_name') # this will not work - file name, not Class name
    @mock.patch('person.get_name') # not working

    package_name.dir_name.file_name(person.py).func_name(get_name())
    @mock.patch('pytests.lib.person.get_name')
    """


    @mock.patch('pytests.lib.person.get_name')
    def test_name(self, mock_get_name):
        # set a return value for our mock object
        mock_get_name.return_value = "Bob"
        ps = person.Person()
        name = ps.name()
        self.assertEqual(name, "Bob")


@mock.patch('pytests.lib.person.Pet')
def test_dog_noise(mock_pet):
    # mock_pet.noise.return_value= "Meoow"
    mock_pet.return_value.noise.return_value = "Meoow"

    ps = person.Person()
    # forgot the return_value - which is what the example is for
    # assert person.pet.noise == "Meoow"
    assert ps.pet.noise.return_value == "Meoow"


@mock.patch('pytests.lib.person.noise_logger', lambda x: x)
def test_decorator():
    ps = person.Person()
    assert ps.pet.noise() == 'Woof'
