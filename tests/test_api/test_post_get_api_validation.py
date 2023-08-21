import requests

from lib.helpers.api_resources import ApiResources
from lib.helpers.payload_json import PayloadJson
from utilities.utils import Utils

log = Utils.custom_logger()

log.info("Validate the post and get api calls")
def test_post_get_api_validation_case():
    url = ApiResources.endpoint
    log.info("Step 1: create and hit the post request api")
    create_user_response = requests.post(url + ApiResources.create_user,
                                         json=PayloadJson.create_new_user(),
                                         headers=ApiResources.headers, )
    log.info("Step 2: Validate the response status code for post request")
    assert create_user_response.status_code == 201
    log.info("Step 3: Validate the get request")
    get_user_details_response = requests.get(url + ApiResources.get_user,
                                             params={'id': create_user_response.json()["id"]},
                                             headers=ApiResources.headers, )
    log.info("Step 4: Validate the get request response status code")
    assert get_user_details_response.status_code == 200
