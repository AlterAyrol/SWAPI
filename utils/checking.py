from requests import Response
import json


"""Методы для проверки ответов на запросы"""


class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if status_code == response.status_code:
            print("Успешно! Статус код = " + str(response.status_code))
        else:
            print("Провал!!! Статус код = " + str(response.status_code))