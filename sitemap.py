#downloading sitemap file

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry # type: ignore

# URL of the sitemap
sitemap_url = 'https://cmrtc.ac.in/sitemap.xml'

# Set headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Create a session
session = requests.Session()

# Define retry strategy
retry = Retry(
    total=5,                  # Total retry attempts
    backoff_factor=1,          # Wait 1 second between retries, then 2 seconds, etc.
    status_forcelist=[500, 502, 503, 504],  # Retry for these HTTP status codes
)

# Mount it for HTTPAdapter to handle retries
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

try:
    # Send a GET request with headers and retry mechanisms
    response = session.get(sitemap_url, headers=headers, timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        # Specify the file name to save the sitemap
        file_name = 'sitemap.xml'
        
        # Open the file in write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        
        print(f"Sitemap downloaded and saved as {file_name}")
    else:
        print(f"Failed to download the sitemap: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
