# EARTHQUAKE_API_Aquib_Hussain 

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

class USGSEarthquakeFetcher:
    """
    A class to fetch and analyze earthquake data from the USGS database.

    Attributes:
    - start_date (str): The start date for querying earthquake data.
    - end_date (str): The end date for querying earthquake data.
    """
    def __init__(self, start_date, end_date):
        """
        Initialize the USGSEarthquakeFetcher class with start and end dates.

        Args:
        - start_date (str): The start date for querying earthquake data (YYYY-MM-DD format).
        - end_date (str): The end date for querying earthquake data (YYYY-MM-DD format).
        """
        self.base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
        self.start_date = start_date
        self.end_date = end_date

    def fetch_data(self):
        """
        Fetch earthquake data from the USGS API.

        Returns:
        - JSON: JSON data containing earthquake information.
        """
        params = {
            "format": "geojson",
            "starttime": self.start_date,
            "endtime": self.end_date
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from USGS Earthquake API.")
            return None

    def parse_to_dataframe(self, data):
        """
        Parse earthquake JSON data to a pandas DataFrame.

        Args:
        - data (JSON): JSON data containing earthquake information.

        Returns:
        - DataFrame: DataFrame containing parsed earthquake data.
        """
        if data:
            features = data.get('features')
            if features:
                all_data = []
                for feature in features:
                    properties = feature.get('properties')
                    geometry = feature.get('geometry')
                    if properties and geometry:
                        quake_data = {
                            'Magnitude': properties.get('mag'),
                            'Place': properties.get('place'),
                            'Latitude': geometry.get('coordinates')[1],
                            'Longitude': geometry.get('coordinates')[0],
                            'Depth': geometry.get('coordinates')[2]
                        }
                        all_data.append(quake_data)
                if all_data:
                    df = pd.DataFrame(all_data)
                    return df
        print("No earthquake data found.")
        return None

# To fetch the EarthQuake Data 
earthquake_fetcher = USGSEarthquakeFetcher("2020-01-01", "2020-01-02")
earthquake_data = earthquake_fetcher.fetch_data()
earthquake_df = earthquake_fetcher.parse_to_dataframe(earthquake_data)

if earthquake_df is not None:
    print(earthquake_df)  # Display the rows of the DataFrame

# Performing the EDA first 
    class EDA:
        # Display basic information about the DataFrame
        def display_basic_info():
            """
            Display basic information about the given DataFrame.

            Args:
            - dataframe (DataFrame): The DataFrame for which basic information is to be displayed.


            """
            print(f"Shape of the DataFrame: {earthquake_df.shape}")
            print("\nInfo about the DataFrame:")
            print(earthquake_df.info())
            print("\nSummary statistics:")
            print(earthquake_df.describe())
            # Check for missing values
            print(earthquake_df.isnull().sum())

        def plot_histogram():
            """
            Plot a histogram for a specified column in the DataFrame.

            Args:
            - dataframe (DataFrame): The DataFrame containing the data.
            - column (str): The column name for which the histogram will be plotted.
            - bins (int): Number of bins for the histogram (default is 20).


            """
            plt.hist(earthquake_df['Magnitude'], bins=20)
            plt.xlabel('Magnitude')
            plt.ylabel('Frequency')
            plt.title(f'Histogram of Magnitude')
            plt.show()


        def plot_depth_histogram():
            """
            Plot a histogram for the 'Depth' column in the DataFrame.

            Args:
            - dataframe (DataFrame): The DataFrame containing the earthquake data.
            - bins (int): Number of bins for the histogram (default is 20).

            """
            plt.hist(earthquake_df['Depth'], bins=20)
            plt.xlabel('Depth')
            plt.ylabel('Frequency')
            plt.title('Histogram of Depth')
            plt.show()

        # plot_depth_histogram(earthquake_df, bins=20)


        def plot_latitude_longitude():
            """
            Plot a scatter plot for Latitude vs Longitude.

            Args:
            - dataframe (DataFrame): The DataFrame containing Latitude and Longitude data.

            """
            plt.scatter(earthquake_df['Longitude'], earthquake_df['Latitude'], alpha=0.5)
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.title('Earthquake Locations')
            plt.show()

        def plot_top_places():
            """
            Plot the top earthquake occurrence places in a horizontal bar plot.

            Args:
            - dataframe (DataFrame): The DataFrame containing earthquake data.
            - num_places (int): Number of top places to display (default is 10).

            """
            top_places = earthquake_df['Place'].value_counts().iloc[10 - 1::-1]
            plt.figure(figsize=(10, 5))
            top_places.plot(kind='barh')
            plt.xlabel('Frequency')
            plt.ylabel('Place')
            plt.title(f'Top {10} Earthquake Occurrence Places')
            plt.show()

        def plot_magnitude_ranges():
            """
            Plot the count of earthquakes within different magnitude ranges.

            Args:
            - dataframe (DataFrame): The DataFrame containing earthquake data.
            - bins (list): List of bin edges for magnitude ranges (default is [0, 3, 5, 7, 9]).
            - labels (list): Labels for the magnitude ranges (default is ['0-3', '3-5', '5-7', '7-9']).

            """
            magnitude_bins = pd.cut(earthquake_df['Magnitude'], bins=[0, 3, 5, 7, 9], labels=['0-3', '3-5', '5-7', '7-9'])
            magnitude_bins.value_counts().sort_index().plot(kind='bar')
            plt.xlabel('Magnitude Range')
            plt.ylabel('Frequency')
            plt.title('Count of Earthquakes by Magnitude Range')
            plt.show()

        def plot_pairplot_numerical():
            """
            Create a pairplot of selected numerical features.

            Args:
            - dataframe (DataFrame): The DataFrame containing earthquake data.
            - columns (list): List of columns to include in the pairplot.

            """
            sns.pairplot(earthquake_df[['Magnitude', 'Depth', 'Latitude', 'Longitude']])
            plt.title('Pairplot of Numerical Features')
            plt.show()



        def plot_violin_magnitude_by_depth():
            """
            Create a violin plot to visualize the distribution of Magnitude by Depth.

            Args:
            - dataframe (DataFrame): The DataFrame containing earthquake data.
            - x_column (str): The column representing the x-axis (default is 'Depth').
            - y_column (str): The column representing the y-axis (default is 'Magnitude').

            """
            plt.figure(figsize=(8, 6))
            sns.violinplot(x='Depth', y='Magnitude', data=earthquake_df)
            plt.xlabel('Depth')
            plt.ylabel('Magnitude')
            plt.title('Violin Plot of Magnitude by Depth')
            plt.show()


        def plot_scatter_matrix_kde():
            """
            Create a scatter matrix with KDEs for selected numerical columns.

            Args:
            - dataframe (DataFrame): The DataFrame containing earthquake data.
            - columns (list): List of columns to include in the scatter matrix.

            """
            sns.pairplot(earthquake_df[['Magnitude', 'Depth', 'Latitude', 'Longitude']], kind='kde')
            plt.suptitle('Scatter Matrix with KDEs', y=1.02)
            plt.show()


        #Plotting the Correlation Matrix 

        def plot_correlation_matrix():
            """
            Create a heatmap for the correlation matrix between selected numerical columns.

            Args:
            - dataframe (DataFrame): The DataFrame containing earthquake data.
            - columns (list): List of columns to include in the correlation matrix.
            """
            numeric_cols = earthquake_df[['Magnitude', 'Depth', 'Latitude', 'Longitude']]
            correlation_matrix = numeric_cols.corr()
            plt.figure(figsize=(8, 6))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
            plt.title('Correlation Matrix Heatmap')
            plt.show()

