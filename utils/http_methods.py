import requests

"""Кастомные http методы"""


class Http_methods:
    headers = {'Content-Type': 'application/json'}  # Информация передается с запросами и возращается с ответами
    cookie = ''
    # Статические методы

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result
    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result


