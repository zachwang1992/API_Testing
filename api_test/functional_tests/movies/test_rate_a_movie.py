import logging as logger
from api_test.src.helpers.movies_helper import MovieHelper
from api_test.src.utilities.credentials_utility import CredentialsUtility
from api_test.src.utilities.generic_utilities import generate_a_random_existing_movie_id, \
    generate_a_random_non_existing_session_id, generate_a_random_non_existing_api_key
from api_test.src.utilities.api_responses_utility import RateMovieResponse


class TestRateAMovie:
    def test_rate_a_movie_successfully(self):
        """
        The function tests that we send request with valid payload, parameters and headers to rate a movie successfully.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with valid payload, parameters and headers to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.SUCCESSFULLY_ADDED_RESPONSE \
               or rs_api == RateMovieResponse.SUCCESSFULLY_UPDATED_RESPONSE, \
            f'Response body of rating a movie successfully is not correct.'

    def test_rate_a_movie_without_api_key(self):
        """
        The function tests that if we send request without api key to rate a movie, the response status code is 401.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        session_id = movie_helper.create_session_id()

        logger.info(f'sending a post request without api key to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, parameters={'session_id': session_id}, expected_status_code=401)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_WITHOUT_API_KEY, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_without_session_id(self):
        """
        The function tests that if we send request without session id to rate a movie, the response status code is 401.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        session_id = movie_helper.create_session_id()

        logger.info(f'sending a post request without session id to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, parameters=CredentialsUtility.get_api_key(),
                                           expected_status_code=401)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_WITHOUT_SESSION_ID,\
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_without_api_key_and_session_id(self):
        """
        The function tests that if we send request without api key and session id to rate a movie, the response status
        code is 401.
        :return: None
        """
        movie_helper = MovieHelper()

        logger.info(f'sending a post request without api key and session id to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, parameters={}, expected_status_code=401)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_WITHOUT_API_KEY, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_with_non_existing_api_key(self):
        """
        The function tests that if we send request with non-existing api key to rate a movie, the response status
        code is 401.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        session_id = movie_helper.create_session_id()

        logger.info(f'sending a post request with non-existing api key to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        parameters = {'session_id': session_id}
        parameters.update({'api_key': generate_a_random_non_existing_api_key()})
        rs_api = movie_helper.rate_a_movie(movie_id, parameters=parameters, expected_status_code=401)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_WITHOUT_API_KEY, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_with_non_existing_session_id(self):
        """
        The function tests that if we send request with non-existing session id to rate a movie, the response status
        code is 401.
        :return: None
        """
        movie_helper = MovieHelper()

        logger.info(f'sending a post request with non-existing session id to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        non_existing_session_id = generate_a_random_non_existing_session_id()
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'session_id': non_existing_session_id})
        rs_api = movie_helper.rate_a_movie(movie_id, parameters=parameters, expected_status_code=401)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_WITHOUT_SESSION_ID, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_with_invalid_payload_including_value_not_multiple_of_half(self):
        """
        The function tests that if we send request with invalid payload including value which is not multiple of 0.5 to
        rate a movie, the response status code is 400.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with invalid payload including value which is not multiple of 0.5 to rate'
                    f' a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, payload={'value': 8.1}, expected_status_code=400)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_OF_VALUE_NOT_MULTIPLE_OF_HALF, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_with_invalid_payload_including_value_more_than_ten(self):
        """
        The function tests that if we send request with invalid payload including value more than 10 to rate a movie,
        the response status code is 400.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with invalid payload including value more than 10 to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, payload={'value': 12}, expected_status_code=400)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_OF_VALUE_MORE_THAN_TEN, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_with_invalid_payload_including_value_not_greater_than_zero(self):
        """
        The function tests that if we send request with invalid payload including value not greater than 0 to rate a
        movie, the response status code is 400.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with invalid payload including value not greater than 0 to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, payload={'value': 0}, expected_status_code=400)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_OF_VALUE_NOT_GREATER_THAN_ZERO, \
            f'Response body of rating a movie is not correct.'

    # bug
    def test_rate_a_movie_with_invalid_payload_including_value_in_string(self):
        """
        The function tests that if we send request with invalid payload including value in string to rate a movie, the
        response status code is 400.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with invalid payload including value in string to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, payload={'value': '5x'}, expected_status_code=400)

        logger.info(f'checking the response...')
        assert rs_api, f'Response body of rating a movie is empty.'
        assert not rs_api.get('success'), f'success field in the response is true'

    def test_rate_a_movie_with_invalid_payload_including_wrong_key(self):
        """
        The function tests that if we send request with invalid payload including wrong key to rate a movie, the
        response status code is 400.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with invalid payload including wrong key to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, payload={'Value': 8.5}, expected_status_code=400)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_OF_BAD_REQUEST, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_with_empty_payload(self):
        """
        The function tests that if we send request with empty payload to rate a movie, the response status code is 400.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with empty payload to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, payload={}, expected_status_code=400)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_OF_BAD_REQUEST, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_without_content_type(self):
        """
        The function tests that if we send request without content type to rate a movie, the response status code is 400.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request without content type to rate a movie...')
        movie_id = generate_a_random_existing_movie_id()
        rs_api = movie_helper.rate_a_movie(movie_id, headers={}, expected_status_code=400)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_RESPONSE_OF_BAD_REQUEST, \
            f'Response body of rating a movie is not correct.'

    def test_rate_a_movie_with_non_existing_movie_id(self):
        """
        The function tests that if we send request with non-existing movie id to rate a movie, the response status code
        is 404.
        :return: None
        """
        movie_helper = MovieHelper()
        movie_helper.create_request_token()
        movie_helper.authorize_request_token()
        movie_helper.create_session_id()

        logger.info(f'sending a post request with valid payload, parameters and headers to rate a movie...')
        movie_id = 1
        rs_api = movie_helper.rate_a_movie(movie_id, expected_status_code=404)

        logger.info(f'checking the response...')
        assert rs_api == RateMovieResponse.FAILED_REQUEST_OF_INVALID_MOVIE_ID, \
            f'Response body of rating a movie successfully is not correct.'
