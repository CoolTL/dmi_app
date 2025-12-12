import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal

class WeatherView(QWidget):

    dataRequested = Signal()  # signal, når brugeren klikker på knappen

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DMI Weather App")
        self.setMinimumSize(600, 600)

        self.layout = QVBoxLayout()
        self.label = QLabel("Tryk for at hente data fra DMI")
        self.button = QPushButton("Hent temperaturer")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # Opret Cartopy-kort
        self.fig = plt.figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        self.ax.set_extent([8, 15, 54.5, 58])
        self.ax.coastlines()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

        # Signal-slot forbindelse
        self.button.clicked.connect(self.dataRequested.emit)

    def plot_temperature_points(self, df):
        """Plot temperaturdata """
        
