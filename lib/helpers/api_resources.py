import random
import yaml


class ApiResources:

    create_user = "/public/v2/users"
    get_user = "/public/v2/users/"
    headers = {"Content-Type": "application/json",
               "Authorization": "Please provide the token"}
    endpoint = "https://gorest.co.in"


    @staticmethod
    def id_generator():
        """
        To generate the random id number
        :return:
        """
        user_id = random.randint(101, 10000)
        return user_id

    @staticmethod
    def api_resources_read_url():
        """
        To read the data from the config files
        :return:
        """
        with open("api_config.yaml", encoding="utf-8") as f:
            api_data_config = yaml.safe_load(f.read())
            url = api_data_config["API"]["endpoint"]
            return url
