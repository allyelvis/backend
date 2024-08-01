import requests

class APIService:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def get(self, endpoint, params=None):
        response = requests.get(f'{self.base_url}/{endpoint}', headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f'{self.base_url}/{endpoint}', json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data):
        response = requests.put(f'{self.base_url}/{endpoint}', json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(f'{self.base_url}/{endpoint}', headers=self.headers)
        response.raise_for_status()
        return response.json()
