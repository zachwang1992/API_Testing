import string

from api_test.src.utilities.credentials_utility import CredentialsUtility
from api_test.src.utilities.requests_utility import RequestsUtility
import random


def generate_a_random_existing_page_number():
    total_pages = RequestsUtility().get('/movie/top_rated').get('total_pages')
    random_page = random.randint(1, total_pages)
    return random_page


def generate_a_random_existing_movie_id():
    random_page = generate_a_random_existing_page_number()
    parameters = CredentialsUtility.get_api_key()
    parameters.update({'page': random_page})
    movie_id = RequestsUtility().get('/movie/top_rated', parameters=parameters).get('results')[0].get('id')
    return movie_id


def generate_a_random_non_existing_session_id():
    session_id_length = 40
    random_session_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=session_id_length))
    return random_session_id


def generate_a_random_non_existing_api_key():
    session_id_length = 32
    random_session_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=session_id_length))
    return random_session_id
