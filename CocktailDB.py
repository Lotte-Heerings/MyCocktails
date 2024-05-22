import requests
from typing import List, Dict, Any


class CocktailDB:
    API_BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1/"

    def zoek_op_ingredient(self, ingredient: str) -> List[Dict[str, Any]]:
        endpoint = f"{self.API_BASE_URL}/filter.php?i={ingredient}"
        response = self._api_oproep_maken(endpoint)
        if response and response.get("drinks"):
            return response["drinks"]
        else:
            print("Geen cocktails gevonden met dit ingrediënt.")
            return []

    def get_random_cocktail(self) -> Dict[str, Any]:
        endpoint = f"{self.API_BASE_URL}/random.php"
        response = self._api_oproep_maken(endpoint)
        if response and response.get("drinks"):
            return response["drinks"][0]
        else:
            print("Er is een error opgetreden bij get_random_cocktail.")
            return {}

    def get_cocktail_details(self, naam: str) -> List[Dict[str, Any]]:
        endpoint = f"{self.API_BASE_URL}/search.php?s={naam}"
        response = self._api_oproep_maken(endpoint)
        if response and response.get("drinks"):
            return response["drinks"]
        else:
            print("Geen cocktails gevonden met deze naam.")
            return []

    #DRY!
    def _api_oproep_maken(self, endpoint: str) -> Dict[str, Any]:
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Fout bij het maken van API-oproep in CocktailDB.py: {e}")
            return None
