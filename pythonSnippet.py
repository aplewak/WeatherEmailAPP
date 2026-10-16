# OVERVIEW
# Created by Andrew Plewak on 2024-06-19
# APPLICATION: 
# Email recipients the local current weather report for UB 
# Fill out the intended .env parameters and run program via command line: python pythonSnippet.py


import os
from pathlib import Path
from redmail import EmailSender
from dotenv import load_dotenv
import requests
from datetime import datetime

# CONSTANTS
load_dotenv(Path(__file__).parent / ".env2")  # Load environment variables from .env file

# Reference the GMAILPASSKEY/ GMAILUSERNAME environment variables, this is a two step verification app password generated from your Google account
password = os.getenv("GMAILPASSKEY")
username = os.getenv("GMAILUSERNAME")
recipients = os.getenv("GMAILRECIPIENTS")

# FUCTION DEFINITIONS
def get_weather_data(lat:float,lng:float ):
    params = {
        "latitude": lat,
        "longitude": lng,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "temperature_unit": "fahrenheit"
    }

    url = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    # also available besides current. daily,hourly,minutely_15,past_days
    return response.json()["current"]


# MAIN EXECUTION

weather = get_weather_data(43.001,-78.790)

emailContents = "UB Weather Update:\n\n"

convertedDate = datetime.fromisoformat(
    weather["time"]
).strftime("%B %d, %Y")
print(convertedDate)



if not password:
    raise RuntimeError("GMAILPASSKEY environment variable is not set")
if not username:
    raise RuntimeError("GMAILUSERNAME environment variable is not set")

try:
    # check if the password is correct by attempting to connect to the SMTP server
    gmail = EmailSender(
        username=username,
        password=password,
        host="smtp.gmail.com",
        port=587,
    )

    textContent = (
    "\n\nHappy Friday,"
    "\nIn preparation for Tuesday's interview at 2 PM, I've created this small application to notify the intended recipients."
    "\nI currently do not feel comfortable making my personal full-stack application hosted on GitLab public."
    "\nHowever, during the interview, I'm happy to provide an overview/demo covering the UI, middle-tier/API, and SQL database layers."
    "\nThis simple weather email application is available to view on GitHub:"
    "\nhttps://github.com/aplewak/WeatherEmailAPP"
    "\nAttached is the updated Skill Assesment"
    "\n\n Have a good weekend,"
    "\n Andrew Plewak"
    )
    
    htmlContents = f"""
        <div style="font-family: Arial, sans-serif; color: #333;">
            <h2 style="color: #174a6e;">🌤️ UB Weather Update on {convertedDate}</h2>
            <hr>

            <table style="width: 100%; text-align: center;">
                <tr>
                    <td style="padding: 10px;">
                        <h2>🌡️</h2>
                        <h3>{weather['temperature_2m']} °F</h3>
                        <p>Temperature</p>
                    </td>
                    <td style="padding: 10px;">
                        <h2>💧</h2>
                        <h3>{weather['relative_humidity_2m']}%</h3>
                        <p>Humidity</p>
                    </td>
                    <td style="padding: 10px;">
                        <h2>💨</h2>
                        <h3>{weather['wind_speed_10m']} mph</h3>
                        <p>Wind Speed</p>
                    </td>
                </tr>
            </table>
            <hr>
            <div style="white-space: pre-line; line-height: 1.6;">
                {textContent}
            </div>

            <hr>
            <p style="color: #777; font-size: 12px;">
                Weather data provided by Open-Meteo.
            </p>
        </div>
        """

    gmail.send(
        subject="A local UB Weather Update",
        receivers=[recipients],
        text="test",
        html=htmlContents,
        attachments=[str(Path(__file__).parent / "EASSA.xlsx")]
    )
except Exception as e:
    print(f"Failed to send email: {e}")




