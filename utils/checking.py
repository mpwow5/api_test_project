import json
from requests import Response

"""Class contains methods for checking status code and required field in responses"""


class Checking:
    """Method for checking status code in response"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f'Status code is incorrect. Status code is {response.status_code}'
        if response.status_code == status_code:
            print(f'Correct status code. Status code = {status_code}')

    """Method for checking required fields in response"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All values are presented')

    """Method for checking values of required fields in response"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{field_name} is correct')
