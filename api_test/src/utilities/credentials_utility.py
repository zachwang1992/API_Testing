import os


class CredentialsUtility:
    @staticmethod
    def get_api_key():

        api_key = os.environ.get('API_KEY')

        if not api_key:
            raise Exception("The API credentials 'API_KEY' must be in env variable")
        else:
            return {'api_key': api_key}

    @staticmethod
    def get_account_username():

        username = os.environ.get('USERNAME')

        if not username:
            raise Exception("The account credentials 'USERNAME' must be in env variable")
        else:
            return username

    @staticmethod
    def get_account_password():

        password = os.environ.get('PASSWORD')

        if not password:
            raise Exception("The account credentials 'PASSWORD' must be in env variable")
        else:
            return password
