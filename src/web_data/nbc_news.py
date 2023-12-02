# NBC NEWS WITH DOCSTRINGS_

import requests
from io import StringIO
import pandas as pd
from urllib.parse import urljoin
from xml.etree import ElementTree as ET

class sitemap_Parser:
    """
    A Class to fetch the Data from NBC News .com
    """
    def __init__(self, base_url):
        """
        Initializes the SitemapParser with the base URL.

        Args:
        - base_url (str): The base URL of the website.

        Returns:
        - None
        """
        self.base_url = base_url
        self.sitemaps = []

    def fetch_robots_txt(self):
        """
        Fetches the robots.txt file from the base URL.

        Returns:
        - str: The content of the robots.txt file.
        """
        robots_url = urljoin(self.base_url, '/robots.txt')
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def extract_sitemaps(self, robots_txt):
        """
        Extracts the URLs of sitemaps from the robots.txt file.

        Args:
        - robots_txt (str): The content of the robots.txt file.

        Returns:
        - None
        """
        if robots_txt:
            lines = robots_txt.split('\n')
            for line in lines:
                if line.startswith('Sitemap:'):
                    parts = line.split(': ')
                    if len(parts) == 2:
                        self.sitemaps.append(parts[1].strip())
        else:
            print("Failed to fetch robots.txt")

    def parse_sitemaps_to_dataframe(self):
        """
        Parses the sitemap URLs and extracts data into a DataFrame.

        Returns:
        - DataFrame: A pandas DataFrame containing extracted data from sitemaps.
        """
        if not self.sitemaps:
            print("No sitemaps found.")
            return None

        all_data = []
        for sitemap_url in self.sitemaps:
            response = requests.get(sitemap_url)
            if response.status_code == 200:
                sitemap_content = response.text
                root = ET.fromstring(sitemap_content)
                for element in root.iter():
                    if element.tag.endswith('loc'):
                        all_data.append({'URL': element.text})

        if all_data:
            df = pd.DataFrame(all_data)
            return df
        else:
            print("No data found in sitemaps.")
            return None
