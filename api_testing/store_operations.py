from base_request import BaseRequest
from constants import BASE_URL_STORE
import pprint


base_request_store = BaseRequest(BASE_URL_STORE)


order_info_1 = base_request_store.get('1', expected_error=False)
pprint.pprint(order_info_1)


order_data = {'id': 1001, 'item': 'item123', 'quantity': 3}
order_created = base_request_store.post('', 'new', order_data)
pprint.pprint(order_created)


order_data_updated = {'id': 1, 'item': 'item123_updated', 'quantity': 5}
order_updated = base_request_store.put('1', '', order_data_updated)
pprint.pprint(order_updated)


order_deleted = base_request_store.delete('1', '')
pprint.pprint(order_deleted)
