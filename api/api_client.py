import requests
import os
from dotenv import load_dotenv
import client_data

class APIClient:
    BASE_URL = "https://v3.football.api-sports.io/"

    def __init__(self):
        self.api_key = os.getenv("API_KEY")

    def get_league(self, league_id):
        url = f"{self.BASE_URL}/leagues?id={league_id}"
        headers = {
            'x-rapidapi-host': self.BASE_URL,
            'x-rapidapi-key': self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            response.raise_for_status()
    
    def get_favourite_leagues(self):
        for league_id in get_leagues():
            result = self.get_league(league_id)
            print(f"Name: {result["response"][0]["league"]["name"]}")

    def get_leagues(self):
        url = f"{self.BASE_URL}/leagues"
        headers = {
            'x-rapidapi-host': self.BASE_URL,
            'x-rapidapi-key': self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            response.raise_for_status()