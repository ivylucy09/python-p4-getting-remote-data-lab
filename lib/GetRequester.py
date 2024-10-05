import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Changed from response.text to response.content

    def load_json(self):
        # Parse the response body as JSON and return it
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)
        except json.JSONDecodeError:
            return None
