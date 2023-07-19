import requests
import smtplib

MY_EMAIL = "nazutesting@gmail.com"
MY_PASSWORD = "Test2022"


REC_EMAIL = ["dongareshreyash20@gmail.com", "ssdon2002@gamil.com"]

length = len(REC_EMAIL)
for i in range(length):
    x = REC_EMAIL[i]
    REC_EMAIL_ALL = x

    api_key = "f75be6737774cb02b4add2c3d3fc6ef7"
    end_point = "https://api.openweathermap.org/data/2.5/onecall"
    weather_params = {
        "lat":18.5196,
        "lon":73.8553,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }

    responce = requests.get(end_point, params=weather_params)
    responce.raise_for_status()
    # print(responce.status_code)
    weather_data = responce.json()
    weather_slice = weather_data["hourly"][:12]


    will_rain = False
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=REC_EMAIL_ALL,
                    msg="Please carry yourself an Umbrella\n\n Have a nice day!!"
                )

        else:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=REC_EMAIL_ALL,
                    msg="Subject: Weather Info\n\nIt's gonna be a bright sunny day, as per the day cycle.\n\n Following data is valid till 6:00 pm \n\n Have a nice day!!"
                )
