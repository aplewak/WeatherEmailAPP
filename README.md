Weather Email Reporter

A small Python application that retrieves weather data from the Open-Meteo API, processes and formats the response, and emails a weather report using Red Mail and Gmail SMTP.

Features

Retrieves current weather conditions from an external REST API.

Processes JSON responses and extracts relevant weather measurements.

Formats timestamps into a human-readable date and time.

Generates a readable email report containing temperature, humidity, and wind speed.

Sends email notifications to configured recipients.

Uses environment variables to manage email credentials and configuration.

Technologies

Python

Requests

Open-Meteo Forecast API

Red Mail

Gmail SMTP

python-dotenv

Requirements

Python 3.10 or later

A Gmail account configured for app-password authentication

A Gmail app password with two-step verification enabled

Setup

Clone the repository:

git clone https://github.com/aplewak/weather-email-app.git
cd weather-email-app

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

.env file 

GMAILUSERNAME=your_email@gmail.com
GMAILPASSKEY=XXXX XXXX XXXX XXXX
GMAILRECIPIENTS=recipient@example.com,

Run the application:

python pythonSnippet.py

Configuration

The application uses environment variables for Gmail authentication and recipient configuration. The .env file is included but not filled in for secruity purposes.

Weather data is retrieved from the Open-Meteo API. The example uses geographic coordinates to determine the forecast location.

Purpose

This project demonstrates basic API integration, JSON data processing, date formatting, environment-based configuration, and automated email delivery in Python.

Author

Andrew Plewak