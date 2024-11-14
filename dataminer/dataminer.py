import requests
import os
import csv
class DataMiner:
    def __init__(self, urls, output_format='csv', output_file='output.csv'):
        self.urls = urls
        self.output_format = output_format
        self.output_file = output_file

    def fetch_csv(self, url):
        """Fetches the CSV content from the URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def save_to_csv(self, csv_content):
        """Saves the CSV content to a file."""
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        output_path = os.path.join(download_folder, 'walmart_store_openings.csv')

        print(f"Saving file to: {output_path}")
        
        try:
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)

            with open(output_path, mode='w', newline='', encoding='utf-8') as file:
                file.write(csv_content)

            print(f"Data saved to {output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")

    def run(self):
        """Runs the data mining process."""
        for url in self.urls:
            print(f"Processing URL: {url}")
            csv_content = self.fetch_csv(url)
            if csv_content:
                self.save_to_csv(csv_content)


if __name__ == '__main__':
    target_url = 'https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv'
    dataminer = DataMiner([target_url], output_format='csv', output_file='walmart_store_openings.csv')
    dataminer.run()
