#!/usr/bin/python
import unittest
import mock
class AddressByPhoneTestCase(unittest.TestCase):
    def test_no_content_found_with_mock(self):
        print "this function will mock Contact model get_by_phone to return none"
        with mock.patch('user_directory.models.Contact') as fake_contact:
            print "fake_contact_id ", id(fake_contact)
            conf = { 'get_by_phone.return_value': None }
            fake_contact.configure_mock(**conf)
            resp = self.client.get(reverse('get_address_by_phone'), {'phone_no' : 1234567891})
            self.assertTrue(resp.status_code == 204)

    def test_success_with_mock(self):
        print  "this function will test the address by phone view after mocking model"
        with mock.patch('user_directory.models.Contact') as fake_contact:
            print "fake_contact_id ", id(fake_contact)
            contact_obj = Contact(recent_address_id = 123, best_address_id = 456)
            conf = { 'get_by_phone.return_value': contact_obj }
            fake_contact.configure_mock(**conf)
            resp = self.client.get(reverse('get_address_by_phone'), {'phone_no' : 1234567891})
            resp_body = json.loads(resp.content)
            self.assertTrue(resp_body == {  'recent_address_id' : 123, 
                                            'frequent_address_id' : 456
                                        }
                        )
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AddressByPhoneTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

