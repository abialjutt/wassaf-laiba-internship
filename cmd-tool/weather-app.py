import requests
import datetime
import typer 
from decouple import config

class Request_handler:
    apiKey : str
    baseUrl : str
    def __init__(self) -> None:
        self.apiKey = config('SECRET_KEY')
        self.baseURL = config('BASE_URL')

    def startdate(startdate):
        datesplit = startdate.split('-')
        dt = datetime.datetime(int(datesplit[0]), int(datesplit[1]), int(datesplit[2]))
        return dt.timestamp()

    def enddate(enddate):
        datesplit = enddate.split('-')
        dt = datetime.datetime(int(datesplit[0]), int(datesplit[1]), int(datesplit[2]))
        return dt.timestamp()

    def completeURL(self, cityName: str):
        cityname = cityName
        complete_URL = self.baseURL + cityname + "&appid=" + self.apiKey
        return complete_URL

class Interface():
    app =  typer.Typer()
    # request_handler = Request_handler()


    @app.command()
    def weather_info(cityname: str):
        request_handler = Request_handler()
        res = requests.get(request_handler.completeURL(cityname))
        data = res.json()
        print("Main Weather: ", data["weather"][0]["main"])
        print("Temperature: ", data["main"]["temp"])
        print("Visibility: ", data["visibility"])


    app()