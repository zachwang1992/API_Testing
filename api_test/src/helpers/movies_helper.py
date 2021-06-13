import logging as logger

from api_test.src.utilities.credentials_utility import CredentialsUtility
from api_test.src.utilities.requests_utility import RequestsUtility
from api_test.src.utilities.token_approval_utility import TokenApprovalUtility


class MovieHelper:
    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_request_token(self):
        logger.info(f'creating a new request token...')

        create_token_json = self.requests_utility.get('/authentication/token/new')
        self.request_token = create_token_json.get('request_token')
        self.token_approval_utility = TokenApprovalUtility(self.request_token)
        return create_token_json

    def authorize_request_token(self):
        self.token_approval_utility.approve_token()

    def create_session_id(self):
        logger.info(f'creating a new session id...')

        payload = {'request_token': self.request_token}
        create_session_id_json = self.requests_utility.post('/authentication/session/new', payload=payload)
        self.session_id = create_session_id_json.get('session_id')
        return self.session_id

    def rate_a_movie(self, movie_id, payload=None, headers=None, parameters=None, expected_status_code=201):
        if not payload and payload != {}:
            payload = {'value': 8.5}
        if not parameters and parameters != {}:
            parameters = CredentialsUtility.get_api_key()
            parameters.update({'session_id': self.session_id})

        rate_movie_json = self.requests_utility.post(f'/movie/{movie_id}/rating', payload=payload, headers=headers,
                                                     parameters=parameters, expected_status_code=expected_status_code)

        return rate_movie_json
