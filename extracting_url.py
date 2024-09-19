#extracting URL's from site map

import requests
from bs4 import BeautifulSoup

# List of sub-sitemaps
sub_sitemaps = [
    'https://cmrtc.ac.in/sitemap-misc.xml',
    'https://cmrtc.ac.in/sitemap-pt-post-p1-2024-07.xml',
    'https://cmrtc.ac.in/sitemap-pt-post-p1-2024-04.xml',
    # Add other sub-sitemap URLs here
]

def scrape_sitemap(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap {url}: {e}")
        return []

    # Parse the sitemap XML
    soup = BeautifulSoup(response.content, 'xml')
    urls = []

    # Extract URLs from the <url> tags
    for url_tag in soup.find_all('url'):
        urls.append(url_tag.loc.text)

    return urls

# Scrape each sub-sitemap and collect URLs
all_urls = []
for sub_sitemap in sub_sitemaps:
    print(f"Scraping sub-sitemap: {sub_sitemap}")
    urls = scrape_sitemap(sub_sitemap)
    all_urls.extend(urls)

print(f"Found {len(all_urls)} URLs in total.")

# Now scrape each URL to get the title
for url in all_urls:
    print(f"Scraping {url}...")
    try:
        page_response = requests.get(url)
        page_response.raise_for_status()
        page_soup = BeautifulSoup(page_response.content, 'html.parser')
        title = page_soup.title.string if page_soup.title else 'No title found'
        print(f"Scraped {url} - Title: {title}")
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
    except Exception as e:
        print(f"Error processing {url}: {e}")
