from utils.api import Iasip_api
from requests import Response

"""Создание, изменение и удаление нового эпизода"""


class Test_create_episode:

    def test_create_new_episode(self):
        print("Метод POST")
        result_post: Response = Iasip_api.create_new_episode()
        check_post = result_post.json()
        # episode_id = check_post.get('episode_id') #  Необходимо поправить API - возврашать значение только созданного
        # эпизода
        episode_id = '6'  # Временная заглушка

        print("Метод GET POST")
        result_get: Response = Iasip_api.get_new_episode(episode_id)

        print("Метод PUT")
        result_post: Response = Iasip_api.put_new_episode(episode_id)

        print("Метод GET PUT")
        result_get: Response = Iasip_api.get_new_episode(episode_id)

        print("Метод DELETE")
        result_delete: Response = Iasip_api.delete_new_episode()

        print("Метод GET DELETE")
        result_get: Response = Iasip_api.get_new_episode(episode_id)
