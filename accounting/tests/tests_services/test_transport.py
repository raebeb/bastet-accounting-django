from rest_framework import status
from rest_framework.test import APITestCase
import json
import requests
import unittest 
from unittest.mock import patch


from accounting.services.transport import Transport


class TransportServicesTest(unittest.TestCase):
    @patch('requests.post')
    def setUp(self, mock_post):
        self.transport = Transport()
        request = {
          'url': 'https://www.example.com/api',
          'params': {'key1': 'value1', 'key2': 'value2'},
          'headers': {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'en-US,en;q=0.5'},
          'data': {'param1': 'value1', 'param2': 'value2'},
          'cookies': {'session_id': '12345'}
        }

        response = {
          'status_code': 200,
          'url': 'https://www.example.com/api',
          'headers': { 'Content-Type': 'application/json'},
          'cookies': {'session_id': '12345'},
          'content': json.dumps({'id': 3, 'pokemon': 'pikachula'}).encode('utf-8')
        }
        
        # Generate a request
        mock_response = requests.Response()
        mock_response.status_code = response['status_code']
        mock_response.url = response['url']
        mock_response.headers = response['headers']
        mock_response.cookies = response['cookies']
        mock_response._content = response['content']

        # moquear la response
        mock_post.return_value = mock_response

        self.response = requests.post(**request)

    def test_process_headers(self):
        expected = {'user_agent': 'Mozilla/5.0', 'accept_language': 'en-US,en;q=0.5'}
        actual = Transport.process_headers(self.response.headers)
        self.assertEqual(expected, actual)

    def test_code_response(self):
        expected = {
            'code': 200,
            'url': 'https://www.example.com',
            'headers': {
                'content_type': 'application/json',
                'date': 'Tue, 03 Aug 2021 15:15:43 GMT',
                'x_frame_options': 'SAMEORIGIN',
            },
            'cookies': None,
            'body': {
              "id": 7,
              "baby_trigger_item": None,
              "chain": {
                "is_baby": False,
                "species": {
                  "name": "rattata",
                  "url": "https://pokeapi.co/api/v2/pokemon-species/19/"
                },
                "evolution_details": None,
              }
            }
        }

      
        actual = Transport.code_response(self.response, self.response.headers)
        self.assertEqual(expected, actual)
        