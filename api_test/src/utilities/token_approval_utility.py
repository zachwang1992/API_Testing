import logging as logger

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from api_test.src.utilities.credentials_utility import CredentialsUtility

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
BASE_URL = 'https://www.themoviedb.org/authenticate/'


class TokenApprovalUtility:
    def __init__(self, request_token):
        self.request_token = request_token

    def approve_token(self):
        logger.info(f'approving request token...')

        browser = webdriver.Chrome(options=chrome_options)
        auth_page = AuthenticatePage(browser, self.request_token)
        auth_page.open()
        auth_page.click_log_in_button()
        auth_page.fill_username_and_password()
        auth_page.click_log_in_button_again()
        auth_page.approve_token()
        auth_page.quit()

    def deny_token(self):
        browser = webdriver.Chrome(options=chrome_options)
        auth_page = AuthenticatePage(browser, self.request_token)
        auth_page.open()
        auth_page.click_log_in_button()
        auth_page.fill_username_and_password()
        auth_page.click_log_in_button_again()
        auth_page.deny_token()
        auth_page.quit()


class Locators:
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="main"]/section/div/div/div[1]')
    USERNAME_FIELD = (By.CSS_SELECTOR, 'input#username.k-textbox')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input#password.k-textbox')
    SECOND_LOG_IN_BUTTON = (By.CSS_SELECTOR, 'input#login_button.k-button.k-primary')
    APPROVE_BUTTON = (By.CSS_SELECTOR, 'button#allow_authentication.k-button.k-primary')
    DENY_BUTTON = (By.CSS_SELECTOR, 'button#deny_authentication.k-button')


class AuthenticatePage:
    def __init__(self, browser, request_token):
        self.browser = browser
        self.request_token = request_token

    @property
    def url(self):
        return f'{BASE_URL}{self.request_token}'

    def open(self):
        self.browser.get(self.url)

    def click_log_in_button(self):
        self.browser.find_element(*Locators.LOG_IN_BUTTON).click()

    def fill_username_and_password(self):
        self.browser.find_element(*Locators.USERNAME_FIELD).send_keys(CredentialsUtility.get_account_username())
        self.browser.find_element(*Locators.PASSWORD_FIELD).send_keys(CredentialsUtility.get_account_password())

    def click_log_in_button_again(self):
        self.browser.find_element(*Locators.SECOND_LOG_IN_BUTTON).click()

    def approve_token(self):
        self.browser.find_element(*Locators.APPROVE_BUTTON).click()

    def deny_token(self):
        self.browser.find_element(*Locators.DENY_BUTTON).click()

    def quit(self):
        self.browser.quit()
