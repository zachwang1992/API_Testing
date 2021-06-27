import logging as logger
from api_test.src.utilities.credentials_utility import CredentialsUtility
from api_test.src.utilities.generic_utilities import generate_a_random_existing_page_number, \
    generate_a_random_non_existing_api_key
from api_test.src.utilities.requests_utility import RequestsUtility
from api_test.src.utilities.api_responses_utility import GetTopRatedMoviesResponse
from langdetect import detect


class TestGetTopRatedMovies:
    def test_get_top_rated_movies_with_valid_api_key(self):
        """
        The function tests that if we send a get request with valid api key to get top rated movies, we get
        a response with status code 200, page 1 and language in English by default.
        :return: None
        """

        logger.info(f'sending a get api request with valid api key to get top rated movies...')
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated')
        page = rs_api.get('page')
        overview = rs_api.get('results')[0].get('overview')

        logger.info(f'checking the response...')
        assert rs_api, f'Response of listing top rated movies is empty.'
        assert page == 1, f'Default page in response is {page}, which is supposed to be 1'
        assert detect(overview) == 'en'

    def test_get_top_rated_movies_with_page(self):
        """
        The function tests that if we send a get request with a valid page and valid api key to get top rated
        movies, we get a response with status code 200 and the page in the request.
        :return: None
        """

        logger.info(f'sending a get api request with a valid page and valid api key to get top rated movies...')
        parameters = CredentialsUtility.get_api_key()
        random_page_number = generate_a_random_existing_page_number()
        parameters.update({'page': random_page_number})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)
        page = rs_api.get('page')

        logger.info(f'checking the response...')
        assert rs_api, f'Response of list top rated movies is empty.'
        assert page == random_page_number, f'Page in response is {page}, which is supposed to be {random_page_number}'

    # bug
    def test_get_top_rated_movies_with_invalid_page_in_non_integer(self):
        """
        The function tests that if we send a get request with an invalid page of non integer and valid api
        key to get top rated movies, we get a response with status code 400.
        :return: None
        """

        logger.info(f'sending a get api request with an invalid page of non integer and valid api key to get top rated'
                    f' movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'page': 1.5})
        req_helper = RequestsUtility()

        logger.info(f'checking the response...')
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters, expected_status_code=400)

    # bug
    def test_get_top_rated_movies_with_invalid_page_in_string(self):
        """
        The function tests that if we send a get request with an invalid page of string and valid api key to
        get top rated movies, we get a response with status code 400.
        :return: None
        """

        logger.info(f'sending a get api request with an invalid page of string and valid api key to get top rated'
                    f' movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'page': 'abcd'})
        req_helper = RequestsUtility()

        logger.info(f'checking the response...')
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters, expected_status_code=400)

    def test_get_top_rated_movies_with_language(self):
        """
        The function tests that if we send a get request with a valid language and valid api key to get top
        rated movies, we get a response with status code 200 and results in the language in the request.
        :return: None
        """

        logger.info(f'sending a get api request with a valid language and valid api key to get top rated movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'language': 'nl'})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)
        page = rs_api.get('page')
        overview = rs_api.get('results')[0].get('overview')

        logger.info(f'checking the response...')
        assert rs_api, f'Response of listing top rated movies is empty.'
        assert page == 1, f'Default page in response is {page}, which is supposed to be 1'
        assert detect(overview) == 'nl', f'overview field is not in language nl'

    def test_get_top_rated_movies_with_non_existing_language(self):
        """
        The function tests that if we send a get request with a non-existing language and valid api key to
        get top rated movies, we get a response with status code 200 and results in the language en.
        :return: None
        """

        logger.info(f'sending a get api request with a non-existing language and valid api key to get top rated movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'language': 'xx'})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)
        page = rs_api.get('page')
        overview = rs_api.get('results')[0].get('overview')

        logger.info(f'checking the response...')
        assert rs_api, f'Response of listing top rated movies is empty.'
        assert page == 1, f'Default page in response is {page}, which is supposed to be 1'
        assert detect(overview) == 'en', f'overview field is not in language en'

    def test_get_top_rated_movies_with_region(self):
        """
        The function tests that if we send a get request with a valid region and valid api key to get top
        rated movies, we get a response with status code 200 and the results filtered by region in the request.
        :return: None
        """

        logger.info(f'sending a get api request with a valid region and valid api key to get top rated movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'region': 'US'})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)
        page = rs_api.get('page')

        logger.info(f'checking the response...')
        assert rs_api, f'Response of listing top rated movies is empty.'
        assert page == 1, f'Default page in response is {page}, which is supposed to be 1'

    # bug
    def test_get_top_rated_movies_with_region_in_lower_case(self):
        """
        The function tests that if we send a get request with an invalid region in lowercase and valid api
        key to get top rated movies, we get a response with status code 200 and the results field is empty.
        :return: None
        """

        logger.info(f'sending a get api request with an invalid region in lowercase and valid api key to get top rated'
                    f' movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'region': 'us'})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)

        logger.info(f'checking the response...')
        assert rs_api == GetTopRatedMoviesResponse.LOWER_CASE_REGION_RESPONSE, f'Response body is not correct'

    def test_get_top_rated_movies_with_non_existing_region(self):
        """
        The function tests that if we send a get request with a non-existing region and valid api key to get
        top rated movies, we get a response with status code 200 and the results field is empty.
        :return: None
        """

        logger.info(f'sending a get api request with a non-existing region and valid api key to get top rated movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'region': 'USS'})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)

        logger.info(f'checking the response...')
        assert rs_api == GetTopRatedMoviesResponse.NON_EXISTING_REGION_RESPONSE, f'Response body is not correct'

    def test_total_pages_and_total_results_fields_are_consistent(self):
        """
        The function tests that if we send multiple get requests with valid api key and different pages to
        get top rated movies, the fields total_pages and total_results are consistent.
        :return: None
        """

        logger.info(f'sending the first api request...')
        req_helper = RequestsUtility()
        rs_api_1 = req_helper.get('/movie/top_rated')
        total_pages_1 = rs_api_1.get('total_pages')
        total_results_1 = rs_api_1.get('total_results')

        logger.info(f'sending the second api request...')
        parameters = CredentialsUtility.get_api_key()
        random_page_number = generate_a_random_existing_page_number()
        parameters.update({'page': random_page_number})
        req_helper = RequestsUtility()
        rs_api_2 = req_helper.get('/movie/top_rated', parameters=parameters)
        total_pages_2 = rs_api_2.get('total_pages')
        total_results_2 = rs_api_2.get('total_results')

        logger.info(f'checking the responses...')
        assert total_pages_1 == total_pages_2, f'total_pages field is inconsistent'
        assert total_results_1 == total_results_2, f'total_results field is inconsistent'

    def test_get_top_rated_movies_with_all_optional_parameters(self):
        """
        The function tests that if we send a get request with a all optional parameters and valid api key to
        get top rated movies, we get a response with status code 200 .
        :return: None
        """

        logger.info(f'sending a get api request with all optional parameters and valid api key to get top rated movies...')
        parameters = CredentialsUtility.get_api_key()
        parameters.update({'language': 'nl'})
        parameters.update({'region': 'US'})
        random_page_number = generate_a_random_existing_page_number()
        parameters.update({'page': random_page_number})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)
        page = rs_api.get('page')
        overview = rs_api.get('results')[0].get('overview')

        logger.info(f'checking the response...')
        assert rs_api, f'Response of listing top rated movies is empty.'
        assert page == random_page_number, f'Default page in response is {page}, which is supposed to be {random_page_number}'
        assert detect(overview) == 'nl', f'overview field is not in language nl'

    def test_get_top_rated_movies_without_api_key(self):
        """
        The function tests that if we send a get request without api key to get top rated movies, we get a
        response with status code 401.
        :return: None
        """

        logger.info(f'sending a get api request without api key to get top rated movies...')
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=None, expected_status_code=401)

        logger.info(f'checking the response...')
        assert rs_api == GetTopRatedMoviesResponse.INVALID_API_KEY_RESPONSE, f'Response body is not correct'

    def test_get_top_rated_movies_with_invalid_api_key(self):
        """
        The function tests that if we send a get request with an invalid api key to get top rated movies, we
        get a response with status code 401.
        :return: None
        """

        logger.info(f'sending a get api request with an invalid api key to get top rated movies...')
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=generate_a_random_non_existing_api_key(),
                                expected_status_code=401)

        logger.info(f'checking the response...')
        assert rs_api == GetTopRatedMoviesResponse.INVALID_API_KEY_RESPONSE, f'Response body is not correct'

    def test_get_top_rated_movies_with_page_bigger_than_total_pages(self):
        """
        The function tests that if we send a get request with a page bigger than total pages and valid api
        key to get top rated movies, we get a response with status code 200 and empty results field in the request.
        :return: None
        """

        logger.info(f'sending a get api request with a valid page and valid api key to get top rated movies...')
        parameters = CredentialsUtility.get_api_key()
        total_pages = RequestsUtility().get('/movie/top_rated').get('total_pages')
        parameters.update({'page': total_pages+1})
        req_helper = RequestsUtility()
        rs_api = req_helper.get('/movie/top_rated', parameters=parameters)
        page = rs_api.get('page')
        results = rs_api.get('results')

        logger.info(f'checking the response...')
        assert rs_api, f'Response of list top rated movies is empty.'
        assert page == total_pages+1, f'Page in response is {page}, which is supposed to be {total_pages+1}'
        assert not results, f'results field is not empty'

