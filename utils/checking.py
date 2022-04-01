import json

from requests import Response

"""Методы для проверки ответов запросов"""



class Checking:

    """Метод для проверки статус кодов ответов"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f'Status code is incorrect. Status code is {response.status_code}'
        if response.status_code == status_code:
            print(f'Correct status code. Status code = {status_code}')

    """Метод проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)  # Преобразует строку в формат json
        assert list(token) == expected_value
        print('All values are presented')

    """Метод для проверки значенй обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{field_name} is correct')

