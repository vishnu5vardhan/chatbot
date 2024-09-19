import requests
from bs4 import BeautifulSoup

def scrape_sitemap(url):
    """Fetch the sitemap and return all URLs (both pages and sub-sitemaps)."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap {url}: {e}")
        return [], []

    # Parse the sitemap XML
    soup = BeautifulSoup(response.content, 'xml')
    page_urls = []
    sub_sitemaps = []

    # Extract URLs from the <url> and <sitemap> tags
    for url_tag in soup.find_all('url'):
        page_urls.append(url_tag.loc.text)
    for sitemap_tag in soup.find_all('sitemap'):
        sub_sitemaps.append(sitemap_tag.loc.text)

    return page_urls, sub_sitemaps

def main():
    # List of sub-sitemaps to process
    sub_sitemaps = [
        'https://cmrtc.ac.in/sitemap-misc.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2024-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2024-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2024-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2023-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2021-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2021-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2021-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2020-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2020-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2020-06.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p1-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p2-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p3-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p4-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-post-p5-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2024-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2024-06.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2024-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2024-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2024-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2024-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2024-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2024-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p4-2024-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p5-2024-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2024-01.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-12.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-11.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-10.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-09.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2023-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2023-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p4-2023-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p5-2023-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2023-01.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-11.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-10.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-09.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2022-09.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-06.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2022-06.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2022-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2022-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p4-2022-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2022-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2022-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2022-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2022-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2022-02.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2022-01.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2022-01.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2021-12.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2021-12.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2021-12.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2021-10.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2021-09.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2021-08.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2021-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2021-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2021-01.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2020-12.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2020-09.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2020-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2020-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2020-07.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2020-06.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2020-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2020-05.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2020-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2020-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2020-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p4-2020-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p5-2020-04.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p1-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p2-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p3-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p4-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p5-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p6-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p7-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p8-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p9-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p10-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p11-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p12-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p13-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p14-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p15-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p16-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p17-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p18-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p19-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p20-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p21-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p22-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p23-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p24-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p25-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p26-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p27-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p28-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p29-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p30-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p31-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p32-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p33-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p34-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p35-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p36-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p37-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p38-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p39-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p40-2020-03.xml',
        'https://cmrtc.ac.in/sitemap-pt-page-p41-2020-03.xml',
    ]

    all_page_urls = []

    # Traverse all sub-sitemaps to gather additional URLs
    for current_sitemap in sub_sitemaps:
        print(f"Scraping sub-sitemap: {current_sitemap}")
        page_urls, new_sub_sitemaps = scrape_sitemap(current_sitemap)
        all_page_urls.extend(page_urls)

    print(f"Found {len(all_page_urls)} page URLs in total.")

    # Write all collected URLs to a file
    with open('collected_urls.txt', 'w') as f:
        for url in all_page_urls:
            f.write(url + '\n')

    print("All URLs have been written to 'collected_urls.txt'.")

if __name__ == "__main__":
    main()
