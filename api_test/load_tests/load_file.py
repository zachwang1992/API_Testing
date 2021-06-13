from locust import HttpUser, task

from api_test.src.utilities.credentials_utility import CredentialsUtility

api_key_value = CredentialsUtility.get_api_key().get('api_key')


class WebsiteUser(HttpUser):
    host = 'https://api.themoviedb.org/3'

    @task
    def index(self):
        self.client.get(f'/movie/top_rated?api_key={api_key_value}', name='get top rated movies')