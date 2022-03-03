class Subject:
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers():
        pass


class WeatherDataObserver:
    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()


class WeatherData(Subject):

    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def notifyObservers(self):
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()


class CurrentConditionsDisplay(WeatherDataObserver):

    def __init__(self, weatherData):
        super().__init__(weatherData)

    def display(self):
        print("Current conditions:", self.temperature,
              "F degrees and", self.humidity, "[%] humidity",
              "and pressure", self.pressure)
        print()


class StatisticsDisplay(WeatherDataObserver):
    def __init__(self, weatherData):
        super().__init__(weatherData)

        self.min_temp = float('inf')
        self.average_temp = 0
        self.max_temp = float('-inf')

        self.min_humidity = float('inf')
        self.average_humidity = 0
        self.max_humidity = float('-inf')

        self.min_pressure = float('inf')
        self.average_pressure = 0
        self.max_pressure = float('-inf')

    def calculate_stats(self):
        self.min_temp = round(min(self.min_temp, self.temperature), 2)
        self.max_temp = round(max(self.max_temp, self.temperature), 2)
        self.average_temp = round((self.max_temp + self.min_temp) / 2, 2)

        self.min_humidity = round(min(self.min_humidity, self.humidity), 2)
        self.max_humidity = round(max(self.max_humidity, self.humidity), 2)
        self.average_humidity = round(
            (self.max_humidity + self.min_humidity) / 2, 2)

        self.min_pressure = round(min(self.min_pressure, self.pressure), 2)
        self.max_pressure = round(max(self.max_pressure, self.pressure), 2)
        self.average_pressure = round(
            (self.max_pressure + self.min_pressure) / 2, 2)

    def display(self):

        self.calculate_stats()

        print("--- Statistics ---")
        print("Min temperature:", self.min_temp)
        print("Max temperature:", self.max_temp)
        print("Average temperature:", self.average_temp)

        print("Min humidity:", self.min_humidity)
        print("Max humidity:", self.max_humidity)
        print("Average humidity:", self.average_humidity)

        print("Min pressure:", self.min_pressure)
        print("Max pressure:", self.max_pressure)
        print("Average pressure:", self.average_pressure)
        print("------------------")
        print()


class ForecastDisplay(WeatherDataObserver):
    def __init__(self, weatherData):
        super().__init__(weatherData)
        self.forcast_temp = 0
        self.forcast_humidity = 0
        self.forcast_pressure = 0

    def calculate_forcast(self):
        self.forcast_temp = round(
            self.temperature + 0.11 * self.humidity + 0.22 * self.pressure, 2)
        self.forcast_humidity = round(self.humidity - 0.9 * self.humidity, 2)
        self.forcast_pressure = round(
            self.pressure + 0.1 * self.temperature - 0.21 * self.pressure, 2)

    def display(self):

        self.calculate_forcast()

        print("--- Forecast ---")
        print("Temperature:", self.forcast_temp)
        print("Humidity:", self.forcast_humidity)
        print("Pressure:", self.forcast_pressure)
        print("------------------END OF REPORT------------------")
        print()


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forcast_display = ForecastDisplay(weather_data)

        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)

        # # un-register the observer
        # weather_data.removeObserver(current_display)
        # weather_data.setMeasurements(120, 100,1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
