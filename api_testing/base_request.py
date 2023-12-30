import requests
import pprint


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, data=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

            # log
            pprint.pprint(f'{request_type} example')
            pprint.pprint(response.url)
            pprint.pprint(response.status_code)
            pprint.pprint(response.reason)
            pprint.pprint(response.text)
            pprint.pprint(response.json())
            pprint.pprint('**********')
            return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        return response.json()['message']

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']


BASE_URL_USER = 'https://petstore.swagger.io/v2/user'
base_request_user = BaseRequest(BASE_URL_USER)

BASE_URL_STORE = 'https://petstore.swagger.io/v2/store'
base_request_store = BaseRequest(BASE_URL_STORE)

user_info = base_request_user.get('username', '1')
pprint.pprint(user_info)

user_data = {'username': 'lulu_smith', 'email': 'lulu.smith@gmail.com'}
user_id = base_request_user.post('', user_data)
user_info = base_request_user.get(user_id)
assert user_data['username'] == user_info['username']

request_id_user = base_request_user.delete('1')
user_info_deleted = base_request_user.get(request_id_user, expected_error=True)
pprint.pprint(user_info_deleted)
