from utils.api import SW_api
from utils.checking import Checking

#python -m pytest -s -v

#result = ['Luke Skywalker', 'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 'Owen Lars', 'Beru Whitesun lars',
        # 'R5-D4', 'Biggs Darklighter', 'Obi-Wan Kenobi', 'Wilhuff Tarkin', 'Chewbacca', 'Han Solo', 'Greedo',
        # 'Jabba Desilijic Tiure', 'Wedge Antilles', 'Jek Tono Porkins', 'Raymus Antilles', 'Yoda', 'Palpatine',
        # 'Boba Fett', 'IG-88', 'Bossk', 'Lando Calrissian', 'Lobot', 'Ackbar', 'Mon Mothma', 'Arvel Crynyd',
        # 'Wicket Systri Warrick', 'Nien Nunb', 'Bib Fortuna', 'Anakin Skywalker', 'Nute Gunray', 'Padmé Amidala',
        # 'Ayla Secura', 'Mace Windu', 'Ki-Adi-Mundi', 'Kit Fisto', 'Eeth Koth', 'Adi Gallia', 'Saesee Tiin',
        # 'Plo Koon', 'Poggle the Lesser', 'Luminara Unduli', 'Dooku', 'Bail Prestor Organa', 'R4-P17', 'Shaak Ti',
        # 'Grievous', 'Tarfful', 'Sly Moore', 'Tion Medon']


"""Получения всей информации по персонажу Дарт Вейдер, получение и сохранение информации по персонажам которые снимались во всех фильмах с Дарт Вейдером."""

class Test_Darth_Vader_and_others():

    def test_darth_vader(self):

        print('\n    Метод GET для получения информации о Дарте Вейдере:')
        result_get = SW_api.get_darth_vader_info()
        print(result_get.status_code)
        # json_keys = json.loads(result_get.text)         #вывод всех ключей
        # print(list(json_keys))                          #
        check = result_get.json()
        json_values_films = list(check.get('films'))
        Checking.check_status_code(result_get, 200)


        print('\n    Метод GET для получения информации по фильмам в которых участвовал Дарт Вейдер:')
        list_result_film_json = SW_api.get_info_about_film(json_values_films)


        print('\n    Метод по созданию ссылок на информацию по персонажам участвующих в фильме')
        characters_list_url = SW_api.create_characters_list(list_result_film_json)


        print('\n    Метод по получению информации по персонажу с созданием списка имён персонажей')
        characters_name_list = SW_api.create_name_list(characters_list_url)


        print('\n    Метод по сохранению списка имён персонажей в файл')
        SW_api.create_file_with_name_list(characters_name_list)


        print('\n    Тестовый сценарий test_darth_vader завершён.')