'''
The process of initiating an action on a
server is done through HTTP requests which
are message sent by the client. The two
most commonly used HTTP requests are
GET and POST. This task involves validating
requests and parsing URL parameters as a
comma-separated string. Authentication
tokens for both GET and POST requests are
sent as a URL parameter named "token".
for validation of authentication, the tokens
must be a set of valid authenticationtokens.
in the case of a post request, a
CSRF (cross-site request forgery) token must
also be provided. A POST request is
considered  valid if Its authentication token
is valid and its CSRI token is an alphanumeric
value consisting only of lowercase letters and/or number with a
minimum length of 8. Once a request is validated, the URI parameters must be passed as a comma-seprated string.

URL parameters are identified by the portion of the url
that comes after a question mark (?)

'''

import re

def validate_request(http_method, url_params):
    # Check if authentication token is present
    if 'token' not in url_params:
        return False, "Authentication token is missing"

    # Validate authentication token
    authentication_token = url_params['token']
    if not is_valid_authentication_token(authentication_token):
        return False, "Invalid authentication token"

    if http_method == 'POST':
        # Check if CSRF token is present
        if 'csrf_token' not in url_params:
            return False, "CSRF token is missing"
        
        # Validate CSRF token
        csrf_token = url_params['csrf_token']
        if not is_valid_csrf_token(csrf_token):
            return False, "Invalid CSRF token"

    # If all validations pass, construct comma-separated string of URL parameters
    parameters_string = ",".join([f"{key}={value}" for key, value in url_params.items()])
    return True, parameters_string

def is_valid_authentication_token(token):
    # Mock implementation of token validation
    # Replace this with actual token validation logic
    valid_tokens = ['token1', 'token2', 'token3'] # Example valid tokens
    return token in valid_tokens

def is_valid_csrf_token(token):
    # Validate CSRF token format
    return bool(re.match("^[a-z0-9]{8,}$", token))

# Example HTTP request parameters
http_method = 'POST'
url_params = {'token': 'token1', 'param1': 'value1', 'param2': 'value2', 'csrf_token': 'csrf1234'}

# Validate the request and parse URL parameters
is_valid, parameters_string = validate_request(http_method, url_params)
if is_valid:
    print("Request is valid")
    print("URL parameters as comma-separated string:", parameters_string)
else:
    print("Request is not valid")
