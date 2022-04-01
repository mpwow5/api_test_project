from utils.http_methods import Http_methods

"""Методы для тестирования API"""

BASE_URL = 'https://api-iasip.herokuapp.com/' #  Базовый URL, одинаковый для всех запросов

class Iasip_api:
    """ Метод для создания нового эпизода"""
    @staticmethod
    def create_new_episode():
        json_for_create_new_episode = {
            "episode_name": "The Gang Tries Desperately to Win an Award",
             "episode_id": 6, "season": 9,
             "number in season": 3,
             "number overall": 96,
             "IMDB rating": 9.2,
             "director": "Richie Keen",
             "writers": ["David Hornsby"],
             "original air date": {"year": 2013, "month": "September", "day": 18},
             "storyline": "Once again, Paddys is passed up by the Philadelphia Free Press annual Best Bar In "
                          "Philadelphia competition. So to win the award, the gang goes to the bar that did win the "
                          "award in an attempt to stake out the competition."
        }

        post_resource = '/api/episodes/'  #  Ресурс метода POST
        post_url = BASE_URL + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_episode)
        print(result_post.text)
        return result_post

    """Метод для проверки нового эпизода"""

    @staticmethod
    def get_new_episode(episode_id):

        get_resource = "/api/episodes/" #  Ресурс метода GET
        get_url = BASE_URL + get_resource + "?episode_id=" + str(episode_id)
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""

    @staticmethod
    def put_new_episode(episode_id):
        put_resource = "/api/episodes/"
        put_url = BASE_URL + put_resource + "?episode_id=" + str(episode_id)
        print(put_url)
        json_for_update_new_episode = {
            "IMDB rating": 9.2,
            "director": "Richie Keen"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_episode)
        print(result_put.text)
        return result_put

    """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_episode():
        delete_resource = "/api/episodes/"
        delete_url = BASE_URL + delete_resource
        json_for_delete_episode = {
            "episode_id": 6
        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_episode)
        print(delete_url)
        print(result_delete.text)
        return result_delete

