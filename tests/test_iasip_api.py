import json, time

from utils.api import Iasip_api
from requests import Response
from utils.checking import Checking
"""Создание, изменение и удаление нового эпизода"""


class Test_create_episode:

    def test_create_new_episode(self):
        print("Метод POST")
        result_post: Response = Iasip_api.create_new_episode()
        check_post = result_post.json()
        episode_id = check_post.get('episode_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'episode_id'])
        Checking.check_json_value(result_post, 'status', 'Episode added')


        print("Метод GET POST")
        result_get: Response = Iasip_api.get_new_episode(episode_id)
        Checking.check_status_code(result_get, 200)

        time.sleep(5)

        print("Метод PUT")
        result_put: Response = Iasip_api.put_new_episode(episode_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['message'])
 
        print("Метод GET PUT")
        result_get: Response = Iasip_api.get_new_episode(episode_id)
        Checking.check_status_code(result_get, 200)


        print("Метод DELETE")
        result_delete: Response = Iasip_api.delete_new_episode()
        Checking.check_status_code(result_delete, 200)

        print("Метод GET DELETE")
        result_get: Response = Iasip_api.get_new_episode(episode_id)
        Checking.check_status_code(result_get, 404)
