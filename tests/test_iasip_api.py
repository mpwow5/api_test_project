from requests import Response
from utils.api import Iasip_api
from utils.checking import Checking

"""Test checks creating, updating and delete new episode
    1. Create new episode - Episode created
    2. Update new episode - Episode updated
    3. Delete new episode - Episode deleted"""


class Test_create_episode:

    def test_create_new_episode(self):
        print("Creating new episode - POST")
        result_post: Response = Iasip_api.create_new_episode()
        check_post = result_post.json()
        episode_id = check_post.get('episode_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'episode_id'])
        Checking.check_json_value(result_post, 'status', 'Episode added')

        print("Checking new episode - GET")
        result_get: Response = Iasip_api.get_new_episode(episode_id)
        Checking.check_status_code(result_get, 200)

        print("Updating new episode - PUT")
        result_put: Response = Iasip_api.put_new_episode(episode_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['message'])

        print("Checking new episode - GET")
        result_get: Response = Iasip_api.get_new_episode(episode_id)
        Checking.check_status_code(result_get, 200)

        print("Deleting new episode - DELETE")
        result_delete: Response = Iasip_api.delete_new_episode()
        Checking.check_status_code(result_delete, 200)

        print("Checking new episode - GET")
        result_get: Response = Iasip_api.get_new_episode(episode_id)
        Checking.check_status_code(result_get, 404)
