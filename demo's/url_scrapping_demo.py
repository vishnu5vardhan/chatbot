import requests
from bs4 import BeautifulSoup
import csv
import json

# Function to read URLs from a file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

# Function to scrape content from a URL
def scrape_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract various elements
        titles = soup.find_all('title')
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        paragraphs = soup.find_all('p')
        
        # Extract meta tags
        meta_tags = {meta.get('name', meta.get('property')): meta.get('content') for meta in soup.find_all('meta')}
        
        # Extract all links
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Extract structured data (JSON-LD)
        structured_data = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                structured_data.append(json.loads(script.string))
            except json.JSONDecodeError:
                continue
        
        # Extract social media links
        social_media_links = {name: url for name, url in meta_tags.items() if 'social' in (name or '').lower()}
        
        # Extract file downloads
        file_downloads = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'))]

        # Handle potential None types
        content = {
            'url': url,
            'title': titles[0].get_text() if titles else 'NA',
            'headings': [heading.get_text() for heading in headings] if headings else ['NA'],
            'paragraphs': [paragraph.get_text() for paragraph in paragraphs] if paragraphs else ['NA'],
            'meta_tags': meta_tags or 'NA',
            'links': links or ['NA'],
            'structured_data': structured_data or 'NA',
            'social_media_links': social_media_links or 'NA',
            'file_downloads': file_downloads or ['NA']
        }
        
        print(f"Successfully scraped: {url}")
        return content

    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return None

# Read URLs from the specified file
urls_file = 'collected_urls_demo.txt'  # Change to your actual file path
urls = read_urls_from_file(urls_file)

# Scrape content from all URLs
all_content = []
for url in urls:
    content = scrape_content(url)
    if content:
        all_content.append(content)

# Save the scraped content to a CSV file
with open('scraped_content_demo.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['url', 'title', 'headings', 'paragraphs', 'meta_tags', 'links', 'structured_data', 'social_media_links', 'file_downloads']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in all_content:
        writer.writerow({
            'url': data['url'],
            'title': data['title'],
            'headings': "; ".join(data['headings']),
            'paragraphs': "; ".join(data['paragraphs']),
            'meta_tags': json.dumps(data['meta_tags']),
            'links': "; ".join(data['links']),
            'structured_data': json.dumps(data['structured_data']),
            'social_media_links': json.dumps(data['social_media_links']),
            'file_downloads': "; ".join(data['file_downloads'])
        })

print("Scraping completed and saved to scraped_content_demo.csv")
