import sys
from PyQt5.QtWidgets import QApplication
#from ui.main_window import MainWindow
from api.api_client import APIClient

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Instanciar el cliente de la API
    api_client = APIClient()
    print(api_client.get_favourite_leagues())

    # Crear la ventana principal y pasarle el cliente de la API
    #main_window = MainWindow(api_client)
    #main_window.show()

    sys.exit(app.exec_())