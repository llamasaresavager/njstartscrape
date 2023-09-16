import xlrd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

url = "https://www.njstart.gov/bso/external/bidDetail.sdo?docId=24DPP00924&external=true&parentUrl=close"

# Constants for the browser setup
BINARY_LOCATION = '/home/localadmin/Documents/chromiumdriver/chrome-linux64/chrome'
DOWNLOAD_DIRECTORY = '/home/localadmin/Desktop/njstartscrape'


def download_from_njstart(url, binary_location=BINARY_LOCATION, download_directory=DOWNLOAD_DIRECTORY, close_browser_after=True):
    """
    Downloads files and saves the HTML from the given njstart URL.

    Args:
    - url (str): The URL to scrape.
    - binary_location (str): Location of the Chrome binary.
    - download_directory (str): Directory where files and HTML should be saved.
    - close_browser_after (bool, optional): Flag to decide whether to close the browser after downloading. Defaults to True.

    Returns:
    None
    """
    
    # Setup the browser with given preferences
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = binary_location
    prefs = {'download.default_directory': download_directory}
    chrome_options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(options=chrome_options)

    # Navigate to the page
    browser.get(url)

    # Give some time for JavaScript to load and modify the page
    time.sleep(5)

    # Identify all relevant anchor tags with href containing "javascript:downloadFile("
    links = browser.find_elements(by=By.XPATH, value='//a[contains(@href, "javascript:downloadFile(")]')

    # Iterate over each link and click to initiate the download
    for link in links:
        link.click()
        time.sleep(2)  # Allow time for the download to initiate

    # Save the HTML content of the page
    html_content = browser.page_source
    with open(os.path.join(download_directory, "page_source.html"), 'w', encoding='utf-8') as file:
        file.write(html_content)

    if close_browser_after:
        browser.close()

def get_urls_from_xls(xls_file_path):
    # Array to store the results
    urls_to_scrape_data = []

    # Read the .xls file
    workbook = xlrd.open_workbook(xls_file_path)
    sheet = workbook.sheet_by_index(0)

    # Iterate through all the values in column A starting at A2
    for row in range(1, sheet.nrows):  # 1 to skip the header
        doc_id = sheet.cell_value(row, 0)  # 0 refers to column A
        url_to_scrape = f"https://www.njstart.gov/bso/external/bidDetail.sdo?docId={doc_id}&external=true&parentUrl=close"
        # Appending the object with url_to_scrape and doc_id
        urls_to_scrape_data.append({"url_to_scrape": url_to_scrape, "doc_id": doc_id})

    return urls_to_scrape_data
