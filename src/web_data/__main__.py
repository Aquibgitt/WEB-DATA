"""for main"""
from .earthquake_api import eda_Exploration
from .the_inference import inference_Analysis

from .nbc_news import  SitemapParser

def XML():
    base_website = "https://www.nbcnews.com/"
    sitemap_parser = SitemapParser(base_website)
    robots_txt = sitemap_parser.fetch_robots_txt()
    print(robots_txt)
    sitemap_parser.extract_sitemaps(robots_txt)
    sitemap_df = sitemap_parser.parse_sitemaps_to_dataframe()

    if sitemap_df is not None:
        print(sitemap_df)  # Display the rows of the DataFrame



def main():
    print("hello professor Molin")
    XML()
    earthquake_api()
    web_scraping()



def earthquake_api():
    print("EDA start---------------------------------------")
    eda_Summary.plot_histogram()
    eda_Summary.plot_depth_histogram()
    eda_Summary.plot_latitude_longitude()
    eda_Summary.plot_top_places()
    eda_Summary.plot_magnitude_ranges()
    eda_Summary.plot_pairplot_numerical()
    eda_Summary.plot_violin_magnitude_by_depth()
    eda_Summary.plot_scatter_matrix_kde()
    eda_Summary.plot_correlation_matrix()

    print("EDA ends----------------------------------------")
def web_scraping():
    ## The Weather Data can be used like this by usin the below scraping tools.
    weather_url = "https://forecast.weather.gov/MapClick.php?lat=40.714530000000025&lon=-74.00711999999999"
    weather_scraper = WeatherScraper(weather_url)
    html_content = weather_scraper.fetch_html()
    weather_data = weather_scraper.scrape_weather_data(html_content)
    weather_df = weather_scraper.create_dataframe(weather_data)

    if weather_df is not None:
        print(weather_df)



main()