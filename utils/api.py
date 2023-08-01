import requests


"""Методы для тестирования Star Wars API"""


class SW_api():

    """Получает всю информацию по персонажу Дарт Вейдер"""
    @staticmethod
    def get_darth_vader_info():
        base_url = 'https://swapi.dev'          # Базовая URL
        darth_resource = '/api/people/4'        #Ресурс метода Get для получения информации по персонажу Дарт Вейдер
        darth_url = base_url + darth_resource
        print("URL метода get_darth_vader_info : " + darth_url)

        result_get = requests.get(darth_url)
        print(result_get.text)

        return result_get


    """Метод по получению информации о фильмах"""
    @staticmethod
    def get_info_about_film(films_urls):
        list_result_film_json = []
        for film_url in films_urls:
            result_film_url = requests.get(film_url)
            result_film_json = result_film_url.json()
            print('Обработка URL фильма ' + result_film_json.get('title') + ", эпизод " + str(result_film_json.get('episode_id')))
            list_result_film_json.append(result_film_json)
        return list(list_result_film_json)


    """Метод по созданию списка персонажей учавствующих в фильмах"""
    @staticmethod
    def create_characters_list(films_json):
        characters_list_url = []
        for film in films_json:
            characters_urls = list(film.get('characters'))
            print("Создание списка персонажей из фильма: " + film.get('title'))
            for character_url in characters_urls:
                if character_url not in characters_list_url:
                    characters_list_url.append(character_url)
        return characters_list_url


    """Метод по получению информации по персонажу с созданием списка имён персонажей"""
    @staticmethod
    def create_name_list(characters_list_url):
        characters_name_list = []
        for character in characters_list_url:
            character_info = requests.get(character)
            character_info.encoding = 'utf-8'
            character_info_json = character_info.json()
            characters_name = character_info_json.get('name')
            characters_name_list.append(characters_name)
        return characters_name_list


    """Метод по сохранению списка имён персонажей в файл"""
    @staticmethod
    def create_file_with_name_list(characters_name_list):
        for character in characters_name_list:
            try:
                with open('name_list_file.txt', 'a', encoding="utf-8") as name_list_file:
                    name_list_file.write(character + '\n')
            except:
                with open('name_list_file.txt', 'w', encoding="utf-8") as name_list_file:
                    name_list_file.write(character)