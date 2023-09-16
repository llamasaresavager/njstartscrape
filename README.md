# NJStart Scraper

A web scraping tool built in Python to scrape bid details from [NJStart](https://www.njstart.gov/) and save them into categorized folders.

## Features
- Scrape bid details using the Selenium web driver.
- Extract URLs from an `.xls` file to get document IDs.
- Download files and save the HTML content of bid detail pages.
- Organize downloads into folders named by their respective document IDs.

## Dependencies

- `xlrd`: For reading `.xls` files.
- `selenium`: For automating web browser interaction.

## Setup & Usage

### 1. Setup

Clone the repository:

```bash
git clone https://github.com/your_github_username/njstartscraper.git
cd njstartscraper
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Chrome Driver

Ensure you have the correct [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) version for your Chrome browser. Adjust the `BINARY_LOCATION` in the `utils.py` file to the path of your `chromedriver`.

### 3. Usage

To use the scraper:

1. Place the `.xls` file with document IDs into the designated path (default is `/home/localadmin/Desktop/njstartscrape/njstartscrape/bidSearchResults.xls`).
2. Run `main.py`:

```bash
python main.py
```
