# tests.py
import unittest
from user_operations import base_request_user
from store_operations import base_request_store
import pprint

class TestAPIRequests(unittest.TestCase):
    def test_user_operations(self):

        user_info_1 = base_request_user.get('1', expected_error=False)
        pprint.pprint(user_info_1)
        self.assertIsNotNone(user_info_1)

        user_data = {'id': 1001, 'username': 'lulu_smith', 'email': 'lulu.smith@gmail.com'}
        user_created = base_request_user.post('', '', user_data)
        pprint.pprint(user_created)
        self.assertIsNotNone(user_created)

        user_data_updated = {'id': 1, 'username': 'lulu_smith_updated', 'email': 'lulu.smith.updated@gmail.com'}
        user_updated = base_request_user.put('1', '', user_data_updated)
        pprint.pprint(user_updated)
        self.assertIsNotNone(user_updated)

        user_deleted = base_request_user.delete('1', '')
        pprint.pprint(user_deleted)
        self.assertIsNotNone(user_deleted)

    def test_store_operations(self):

        order_info_1 = base_request_store.get('1', expected_error=False)
        pprint.pprint(order_info_1)
        self.assertIsNotNone(order_info_1)

        order_data = {'id': 1001, 'item': 'item123', 'quantity': 3}
        order_created = base_request_store.post('', 'new', order_data)
        pprint.pprint(order_created)
        self.assertIsNotNone(order_created)

        order_data_updated = {'id': 1, 'item': 'item123_updated', 'quantity': 5}
        order_updated = base_request_store.put('1', '', order_data_updated)
        pprint.pprint(order_updated)
        self.assertIsNotNone(order_updated)

        order_deleted = base_request_store.delete('1', '')
        pprint.pprint(order_deleted)
        self.assertIsNotNone(order_deleted)

if __name__ == '__main__':
    unittest.main()
