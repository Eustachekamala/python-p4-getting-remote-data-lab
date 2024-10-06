import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send a GET request to the URL and return the response body as a JSON string."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Use get_response_body to get the response, then convert it to a Python object."""
        response_body = self.get_response_body()
        return json.loads(response_body)

# Example usage
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
data = get_requester.load_json()
print(data)