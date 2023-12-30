from base_request import BaseRequest
from constants import BASE_URL_USER
import pprint


base_request_user = BaseRequest(BASE_URL_USER)


user_info_1 = base_request_user.get('1', expected_error=False)
pprint.pprint(user_info_1)

user_data = {'id': 1001, 'username': 'lulu_smith', 'email': 'lulu.smith@gmail.com'}
user_created = base_request_user.post('', '', user_data)
pprint.pprint(user_created)


user_data_updated = {'id': 1, 'username': 'lulu_smith_updated', 'email': 'lulu.smith.updated@gmail.com'}
user_updated = base_request_user.put('1', '', user_data_updated)
pprint.pprint(user_updated)


user_deleted = base_request_user.delete('1', '')
pprint.pprint(user_deleted)
