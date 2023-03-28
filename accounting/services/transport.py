import os
import json
from django.conf import settings
from django.utils.text import camel_case_to_spaces

class Transport:
    BASE_HEADERS = {
        'Content-Type': 'application/json'
    }

    RESPONSE_LOGGING = os.environ.get('TYPHOEUS_RESPONSE_LOGGING', 'LOG_RESPONSES')
    REQUEST_LOGGING = os.environ.get('TYPHOEUS_REQUEST_LOGGING', 'LOG_REQUESTS')

    @staticmethod
    def get(self, url, xheaders=None, params=None):
        headers = self.BASE_HEADERS.copy()
        if xheaders is not None:
            headers.update(xheaders)
        return Transport.run('get', url, headers=headers, params=params)

    @staticmethod
    def post(url, body=None, payload=None, xheaders=None, params=None):
        return Transport.put_post('post', url, body, payload, xheaders, params)

    @staticmethod
    def put(url, body=None, payload=None, xheaders=None, params=None):
        return Transport.put_post('put', url, body, payload, xheaders, params)

    @staticmethod
    def run(method, url, **kwargs):
        import requests
        from django.core.exceptions import ValidationError

        request = requests.Request(method, url, **kwargs)
        prepared_request = request.prepare()

        if Transport.REQUEST_LOGGING == 'LOG_REQUESTS':
            print(prepared_request.body)

        response = requests.Session().send(prepared_request)

        if Transport.RESPONSE_LOGGING == 'LOG_RESPONSES':
            print(f"{method.upper()}ing to {url}")

        processed_response = Transport.process(response)

        if processed_response['code'] > 300:
          print(f"Error {processed_response['code']}: {processed_response['body']}")
          return processed_response

    @staticmethod
    def put_post(method, url, body=None, payload=None, xheaders=None, params=None):
        headers = Transport.BASE_HEADERS.copy()
        if xheaders is not None:
            headers.update(xheaders)

        if body is None and payload is not None:
            body = json.dumps(payload)

        return Transport.run(method, url, headers=headers, params=params, data=body)

    @staticmethod
    def process(response):
        headers = Transport.process_headers(response.headers)
        coded_response = Transport.code_response(response, headers)
        if Transport.RESPONSE_LOGGING == 'LOG_RESPONSES':
            Transport.log_coded_response(coded_response)
        return coded_response

    @staticmethod
    def code_response(response, headers):
        response_code = response.status_code
        if response_code > 300:
            print(f"Error {response_code}: {response.text}")
        return {
            'code': response_code,
            'url': response.url,
            'headers': headers,
            'cookies': headers.get('set_cookie', None),
            'body': json.loads(response.text) if response_code < 300 else None
        }

    @staticmethod
    def parse_body(body):
        return {camel_case_to_spaces(k).replace(' ', '_'): v for k, v in body.items()}

    @staticmethod
    def log_coded_response(resp):
        print(f"Response from {resp['url']}")
        for key, value in resp.items():
            if key != 'url' and key != 'headers':
                print(f"{key.ljust(10, ' ')} : {value}")
