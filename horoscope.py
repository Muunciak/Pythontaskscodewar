import requests
import pyaztro


def Horoscope():
    sign = input("Sign: ")
    day = input("Day: ")
    params = (
        ('sign', sign),
        ('day', day)
    )

    url = "https://aztro.sameerkumar.website/"
    response = requests.post(url, params=params).json()
    print(response)


Horoscope()
