import json
import logging as logger
import os

import requests

from api_test.src.configs.hosts_config import API_HOSTS
from api_test.src.utilities.credentials_utility import CredentialsUtility


class RequestsUtility:
    def __init__(self):

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def get(self, endpoint, parameters=CredentialsUtility.get_api_key(), expected_status_code=200):

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, params=parameters)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'GET API response: {self.rs_json}')

        return self.rs_json

    def post(self, endpoint, payload=None, headers=None, parameters=CredentialsUtility.get_api_key(), expected_status_code=200):

        if not headers and headers != {}:
            headers = {'Content-Type': 'application/json'}

        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, params=parameters)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'GET API response: {self.rs_json}')

        return self.rs_json

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Bad Status code.' \
          f'Expected {self.expected_status_code}, Actual status code: {self.status_code},' \
          f'URL: {self.url}, Response Json: {self.rs_json}'