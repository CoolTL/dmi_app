from PySide6.QtWidgets import QApplication
from model.weather_model import WeatherModel
from view.weather_view import WeatherView
from controller.weather_controller import WeatherController
import sys

def main():
    app = QApplication(sys.argv)

    view = WeatherView()
    model = WeatherModel()
    controller = WeatherController(model, view)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
