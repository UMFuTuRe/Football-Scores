import json
import os

class SaveData:
    # Ruta del archivo donde se almacenarán los números de ligas
    FILE_NAME = "client_data/leagues.json"

    def __init__(self):
        self.a = "a"


    def create_leagues_document():
        with open(FILE_NAME, "w+") as file:
            json.dump([], file, indent=4) 
        file.close()
        load_leagues()

    # Función para cargar los números de las ligas desde el archivo
    def load_leagues():
        if os.path.isfile(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)
        else:
            self.create_leagues_document()

    # Función para guardar los números de las ligas en el archivo
    def saves_leagues(leagues):
        with open(self.FILE_NAME, "w") as file:
            json.dump(leagues, file, indent=4)
        file.close()

    # Función para agregar un número de liga a la lista
    def add_league(league_id):
        leagues = self.load_leagues()
        if league_id not in leagues:
            leagues.append(league_id)  
            self.saves_leagues(leagues)  

    # Función para eliminar un número de liga de la lista
    def remove_league(league_id):
        leagues = self.load_leagues() 
        if league_id in leagues:
            leagues.remove(league_id)
            self.saves_leagues(leagues)

    # Función para listar los números de las ligas guardadas
    def get_leagues():
        leagues = self.load_leagues()
        return leagues