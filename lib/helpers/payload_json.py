import string
import random

from lib.helpers.api_resources import ApiResources


class PayloadJson(ApiResources):

    @staticmethod
    def create_new_user():
        """
        TO create json body for post request to create new user
        :return:
        """
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        id = ApiResources.id_generator()
        result_str += "@keer.example1"

        body = {
            "id": id,
            "name": "James Kapoor",
            "email": result_str,
            "gender": "male",
            "status": "active"

        }
        return body
