# Web scraping with docstrings.

import requests
from bs4 import BeautifulSoup
import pandas as pd

class weather_Scraper:
    def __init__(self, url):
        """
        Initialize WeatherScraper with the URL of the weather forecast page.

        Args:
        - url (str): The URL of the weather forecast page.

        Returns:
        - None
        """
        self.url = url

    def fetch_html(self):
        """
        Fetches the HTML content from the provided URL.

        Returns:
        - str: The HTML content of the webpage.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch HTML content.")
            return None

    def scrape_weather_data(self, html_content):
        """
        Scrapes weather forecast data from the provided HTML content.

        Args:
        - html_content (str): HTML content of the webpage.

        Returns:
        - list: A list of dictionaries containing weather forecast information.
        """
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            seven_day_forecast = soup.find(id='seven-day-forecast')
            forecast_items = seven_day_forecast.find_all(class_='tombstone-container')

            data = []
            for forecast in forecast_items:
                period = forecast.find(class_='period-name').get_text()
                short_desc = forecast.find(class_='short-desc').get_text()
                temp = forecast.find(class_='temp').get_text()
                data.append({'Period': period, 'Short Description': short_desc, 'Temperature': temp})

            return data
        else:
            print("No HTML content to scrape.")
            return None

    def create_dataframe(self, weather_data):
        """
        Creates a DataFrame from the weather forecast data.

        Args:
        - weather_data (list): A list of dictionaries containing weather forecast information.

        Returns:
        - DataFrame: A pandas DataFrame containing weather forecast details.
        """
        if weather_data:
            df = pd.DataFrame(weather_data)
            return df
        else:
            print("No weather data to create DataFrame.")
            return None
