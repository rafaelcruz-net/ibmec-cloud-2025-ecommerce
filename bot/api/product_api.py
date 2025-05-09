import requests
from config import DefaultConfig

class ProductAPI:
    def __init__(self):
        self.config = DefaultConfig()
        self.base_url = f"{self.config.URL_PREFIX}/products"

    def get_products(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return response.json()[0]
        else:
            return None
