class GetTopRatedMoviesResponse:
    INVALID_API_KEY_RESPONSE = {
        "status_code": 7,
        "status_message": "Invalid API key: You must be granted a valid key.",
        "success": False
    }
    LOWER_CASE_REGION_RESPONSE = {
        "page": 1,
        "results": [],
        "total_pages": 0,
        "total_results": 0
    }
    NON_EXISTING_REGION_RESPONSE = {
        "page": 1,
        "results": [],
        "total_pages": 0,
        "total_results": 0
    }


class RateMovieResponse:
    SUCCESSFULLY_ADDED_RESPONSE = {
        "success": True,
        "status_code": 1,
        "status_message": "Success."
    }
    SUCCESSFULLY_UPDATED_RESPONSE = {
        "success": True,
        "status_code": 12,
        "status_message": "The item/record was updated successfully."
    }
    FAILED_RESPONSE_WITHOUT_API_KEY = {
        "status_code": 7,
        "status_message": "Invalid API key: You must be granted a valid key.",
        "success": False
    }
    FAILED_RESPONSE_WITHOUT_SESSION_ID = {
        "success": False,
        "status_code": 3,
        "status_message": "Authentication failed: You do not have permissions to access the service."
    }
    FAILED_RESPONSE_OF_VALUE_NOT_MULTIPLE_OF_HALF = {
        "success": False,
        "status_code": 18,
        "status_message": "Value invalid: Values must be a multiple of 0.50."
    }
    FAILED_RESPONSE_OF_VALUE_MORE_THAN_TEN = {
        "success": False,
        "status_code": 18,
        "status_message": "Value too high: Value must be less than, or equal to 10.0."
    }
    FAILED_RESPONSE_OF_VALUE_NOT_GREATER_THAN_ZERO = {
        "success": False,
        "status_code": 18,
        "status_message": "Value too low: Value must be greater than 0.0."
    }
    FAILED_RESPONSE_OF_BAD_REQUEST = {
        "success": False,
        "status_code": 5,
        "status_message": "Invalid parameters: Your request parameters are incorrect."
    }
    FAILED_REQUEST_OF_INVALID_MOVIE_ID = {
    "success": False,
    "status_code": 34,
    "status_message": "The resource you requested could not be found."
}