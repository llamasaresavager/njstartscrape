from selenium import webdriver
import time

url = "https://www.njstart.gov/bso/external/bidDetail.sdo?docId=24DPP00924&external=true&parentUrl=close"

# Setup the browser (you'll need the appropriate driver for this, e.g., chromedriver.exe for Chrome)
# Before launching, set the default download directory if you want the downloads to be organized
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': '/home/localadmin/Desktop/njstartscrape'}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

# Navigate to the page
browser.get(url)

# Give some time for JavaScript to load and modify the page (if necessary)
time.sleep(5)

# Identify all relevant anchor tags with href containing "javascript:downloadFile("
links = browser.find_elements_by_xpath('//a[contains(@href, "javascript:downloadFile(")]')

# Iterate over each link and click to initiate the download
for link in links:
    link.click()
    time.sleep(2)  # Allow time for the download to initiate

# Optionally close the browser after all downloads
browser.close()