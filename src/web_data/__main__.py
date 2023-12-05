"""for main"""
from .earthquake_api import eda_Summary
from .web_scraping import weather_Scraper
from .earthquake_api import usgs_Earthquake_Fetcher
from .nbc_news import  sitemap_Parser

def XML():
    base_website = "https://www.nbcnews.com/"
    sitemap_parser = sitemap_Parser(base_website)
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
    earthquake_fetcher = usgs_Earthquake_Fetcher("2020-01-01", "2020-01-02")
    earthquake_data = earthquake_fetcher.fetch_data()
    data = earthquake_fetcher.parse_to_dataframe(earthquake_data)
    print("EDA start---------------------------------------")
    eda_Summary.plot_histogram(data)
    eda_Summary.plot_depth_histogram(data)
    eda_Summary.plot_latitude_longitude(data)
    eda_Summary.plot_top_places(data)
    eda_Summary.plot_magnitude_ranges(data)
    eda_Summary.plot_pairplot_numerical(data)
    eda_Summary.plot_violin_magnitude_by_depth(data)
    eda_Summary.plot_scatter_matrix_kde(data)
    eda_Summary.plot_correlation_matrix(data)

    print("EDA ends----------------------------------------")
def web_scraping():
    ## The Weather Data can be used like this by usin the below scraping tools.
    weather_url = "https://forecast.weather.gov/MapClick.php?lat=40.714530000000025&lon=-74.00711999999999"
    weather_scraper = weather_Scraper(weather_url)
    html_content = weather_scraper.fetch_html()
    weather_data = weather_scraper.scrape_weather_data(html_content)
    weather_df = weather_scraper.create_dataframe(weather_data)

    if weather_df is not None:
        print(weather_df)



main()