from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from pyowm.owm import OWM
import csv


class WeatherAgriculture:

    def __init__(self):
        self._key = '64f8b3850d870d20d50ba646d5035208'


    def get_wa_manager(self):
        owm = OWM(self._key)
        return owm.weather_manager()


    def get_wa_reg(self):
        owm = OWM(self._key)
        return owm.city_id_registry()



class AgricultureAnalyser:


    def log_temperature(self, temperature):
        if temperature < 2:
            with open("dangerous_temperature.csv", 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["Datetime", "Temperature"])

                writer.writerow({"Datetime": datetime.now(), "Temperature": temperature})

        with open("dlog_temperature.csv", 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Datetime", "Temperature"])

            writer.writerow({"Datetime": datetime.now(), "Temperature": temperature})



def temperature_check():
    wa = WeatherAgriculture()
    aa = AgricultureAnalyser()
    wm = wa.get_wa_manager()
    weather = wm.weather_at_place("Lugano").weather
    aa.log_temperature(weather.temperature('celsius')['temp'])
    print("Logged")


if __name__ == '__main__':
    temperature_check()
    scheduler = BlockingScheduler()
    scheduler.add_job(temperature_check, 'interval', hours=1)
    scheduler.start()

