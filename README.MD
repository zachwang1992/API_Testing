# Bynder API Testing Assignment
## Description
The app tests the following TMDB API endpoints:  
https://developers.themoviedb.org/3/movies/get-top-rated-movies  
https://developers.themoviedb.org/3/movies/rate-movie

## Tech Stack
- Python  
- Pytest  
- requests  
- Selenium webdriver  
- Locust  
- Docker


## Test scenarios
### Endpoint 1 (get top rated movies):
- get top rated movies with a valid API key (passed)
- get top rated movies with a valid page and valid API key (passed)
- get top rated movies with an invalid page of non integer and valid API key (**failed**)
- get top rated movies with an invalid page of string and valid API key (**failed**)
- get top rated movies with a valid language and valid API key (passed)
- get top rated movies with a non-existing language and valid API key (passed)
- get top rated movies with a valid region and valid API key (passed)
- get top rated movies with an invalid region in lower case and valid API key (**failed**)
- get top rated movies with a non-existing region and valid API key (passed)
- check the consistency of total_pages and total_results for requests of different pages (**unstable, sometimes failed**)
- get top rated movies with all optional parameters and valid API key (passed)
- get top rated movies without API key (passed)
- get top rated movies with an invalid API key (passed)
 
### Endpoint 2 (rate a movie):
- rate a movie successfully with valid payload, headers and parameters (passed)
- rate a movie without api key (passed)
- rate a movie without session id (passed)
- rate a movie without api key and session id (passed)
- rate a movie with non-existing api key (passed)
- rate a movie with non-existing session id (passed)
- rate a movie with invalid payload including value which is not multiple of 0.5 (passed)
- rate a movie with invalid payload including value more than 10 (passed)
- rate a movie with invalid payload including value not greater than 0 (passed)
- rate a movie with invalid payload including value in string (**failed**)
- rate a movie with invalid payload including wrong key (passed)
- rate a movie with empty payload (passed)
- rate a movie without content type (passed)
- rate a movie non-existing movie id (passed)

Please refer to more details in test_cases.docx file.

## Load Testing
A basic load testing scenario for endpoint 1 is scripted in python and locust. The scenario parameters should be updated based on 
requirements.

Scenario:
 - total users: 1000
 - spawn rate (users spawned/second): 20
 - time: 60s

## Running the test
### Prerequisites
in linux system  
docker is installed

### Commands:
- $ sudo docker build -t api_test .
- $ sudo docker run -v "$PWD":/report/ api_test

The commands should be executed in the root directory of the repo. A html test report api_test_report.html is generated 
after test execution.  
To execute load testing, we can run command: 
- $ sudo docker run api_test locust -f api_test/load_tests/load_file.py --headless -u 1000 -r 20 -t 60s
