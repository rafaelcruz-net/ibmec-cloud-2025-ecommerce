
import requests
class ProductAPI:
    def consultar_api(self):
        try:
            response = requests.get("http://localhost:8080/products")
            if (response.status_code == 200):
                data = response.json()[0]
                return data
        except Exception as e:
            print(f"Deu ruim ao consultar a API de produtos {e}")

