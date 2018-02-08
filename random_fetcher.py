from jsonrpcclient.http_client import HTTPClient

class Random_Client(HTTPClient):
    
    def __init__(self, endpoint):
        HTTPClient.__init__(self, endpoint)
        
    def get_numbers(self, n=1000, min=0, max=9):
        params = {
            "apiKey": "0e4a2072-e364-404e-a26e-b574732a0d7d",
            "n": n,
            "min": min,
            "max": max
        }
        r = self.request('generateIntegers', params)
        return r['random']['data']

if __name__ == "__main__":
    rc = Random_Client('https://api.random.org/json-rpc/1/invoke')
    print(rc.get_numbers())