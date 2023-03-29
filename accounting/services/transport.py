import json
import os

from django.utils.text import camel_case_to_spaces


class Transport:
    """
    Transport is a wrapper around the requests library that provides
    a consistent interface for making requests to thrid party services.
    """
    BASE_HEADERS = {
        'Content-Type': 'application/json'
    }

    RESPONSE_LOGGING = os.environ.get('TYPHOEUS_RESPONSE_LOGGING', 'LOG_RESPONSES')
    REQUEST_LOGGING = os.environ.get('TYPHOEUS_REQUEST_LOGGING', 'LOG_REQUESTS')

    @staticmethod
    def get(url: str, xheaders:dict=None, params:dict =None) -> dict[str, any]:
        """
        Prepare the data to make the get request
        :param url: url to make the request to
        :param xheaders: extra headers to add to the request
        :param params: params to add to the request
        :return: call to Transport.run() with the provided arguments
        """
        headers = Transport.BASE_HEADERS.copy()
        if xheaders is not None:
            headers.update(xheaders)
        return Transport.run('get', url, headers=headers, params=params)

    @staticmethod
    def post(url: str, body:dict=None, payload:dict=None, xheaders:dict=None, params:dict=None) -> dict[str, any]:
        """
        Prepare the data to make the post request
        :param url: url to make the request to
        :param body: body to send with the request
        :param payload: payload to send with the request
        :param xheaders: extra headers to add to the request
        :param params: params to add to the request
        :return: call to Transport.put_post() with the provided arguments
        """
        return Transport.put_post('post', url, body, payload, xheaders, params)

    @staticmethod
    def put(url: str, body:dict=None, payload:dict=None, xheaders:dict=None, params:dict=None) -> dict[str, any]:
        """
        Prepare the data to make the put request
        :param url: url to make the request to
        :param body: body to send with the request
        :param payload: payload to send with the request
        :param xheaders: extra headers to add to the request
        :param params: params to add to the request
        :return: call to Transport.put_post() with the provided arguments
        """
        return Transport.put_post('put', url, body, payload, xheaders, params)

    @staticmethod
    def run(method: str, url:str, **kwargs) -> dict[str, any]:
        """
        Execute the request for the provided method and url.
        :param method: HTTP method to use
        :param url: url to make the request to
        :param kwargs: additional arguments to pass to the request
        :return: Response processed by Transport.process()
        """
        import requests

        request = requests.Request(method, url, **kwargs)
        prepared_request = request.prepare()

        if Transport.REQUEST_LOGGING == 'LOG_REQUESTS':
            print(prepared_request.body)

        response = requests.Session().send(prepared_request)

        if Transport.RESPONSE_LOGGING == 'LOG_RESPONSES':
            print(f"{method.upper()}ing to {url}")

        processed_response = Transport.process(response)
        import pdb;
        pdb.set_trace()
        if processed_response['code'] > 300:
            print(f"Error {processed_response['code']}: {processed_response['body']}")
        return processed_response

    @staticmethod
    def put_post(method: str, url: str, body:dict=None, payload:dict=None, xheaders:dict=None, params:dict=None):
        """
        Prepare the data to make the put or post request
        :param method: HTTP method to use (put or post)
        :param url: url to make the request to
        :param body: body to send with the request
        :param payload: payload to send with the request
        :param xheaders: extra headers to add to the request
        :param params: params to add to the request
        :return: call to Transport.run() with the provided arguments
        """
        headers = Transport.BASE_HEADERS.copy()
        if xheaders is not None:
            headers.update(xheaders)

        if body is None and payload is not None:
            body = json.dumps(payload)

        return Transport.run(method, url, headers=headers, params=params, data=body)

    @staticmethod
    def process_headers(headers: dict[str, str]) -> dict[str, str]:
        """
        Process the headers returned by the request and return a dictionary with the headers in a more usable format.
        :param headers: headers returned by the request
        :return: headers in a more usable format
        """
        return {
            camel_case_to_spaces(k).replace(' ', '_'): v.strip()
            for k, v in headers.items()
            if isinstance(v, str) and v.strip()
        }

    @staticmethod
    def process(response: dict[str, any]) -> dict[str, any]:
        """
        Process the response from the request and return a dictionary with the response in a more usable format.
        :param response:
        :return: response in a more usable format
        """
        headers = Transport.process_headers(response.headers)

        coded_response = Transport.code_response(response, headers)
        if Transport.RESPONSE_LOGGING == 'LOG_RESPONSES':
            Transport.log_coded_response(coded_response)
        return coded_response

    @staticmethod
    def code_response(response:dict, headers:dict) -> dict[str, any]:
        """
        Process the response from the request and return a dictionary with the response in a more usable format.
        :param response: response from the request
        :param headers: headers from the request
        :return: dict with the response in a more usable format
        """
        response_code = response.status_code
        if response_code > 300:
            print(f"Error {response_code}: {response.text}")
        return {
            'code': response_code,
            'url': response.url,
            'headers': headers,
            'cookies': headers.get('set_cookie', None),
            'body': response.json() if response_code < 300 else None
        }

    @staticmethod
    def parse_body(body:dict) -> dict[str, any]:
        """
        Parse the body of the request and return a dictionary with the body in a more usable format.
        :param body: body of the request
        :return: dict with the body in a more usable format
        """
        return {camel_case_to_spaces(k).replace(' ', '_'): v for k, v in body.items()}

    @staticmethod
    def log_coded_response(resp:dict) -> None:
        """
        Log the response from the request.
        :param resp: response from the request
        :return: None
        """
        print(f"Response from {resp['url']}")
        for key, value in resp.items():
            if key != 'url' and key != 'headers':
                print(f"{key.ljust(10, ' ')} : {value}")
