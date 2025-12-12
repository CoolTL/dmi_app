class WeatherController:
    """
    Controller-laget binder signaler fra View til Model.
    Håndterer dataflow og opdaterer GUI.
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Signal-slot forbindelser
        self.view.dataRequested.connect(self.update_plot)

    def update_plot(self):
        """Kaldes når brugeren trykker på knappen"""
        df = self.model.get_temperature_data()
        self.view.plot_temperature_points(df)
