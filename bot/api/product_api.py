
import requests
class ProductAPI:
    def consultar_produtos(self, product_name):
        try:
            response = requests.get("http://localhost:8080/products/search", params={"productName": product_name})
            if (response.status_code == 200):
                return response.json()
        except Exception as e:
            print(f"Não consegui consultar a API de Consulta de Produtos {e}")

