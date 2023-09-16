import os
from utils import get_urls_from_xls, download_from_njstart

def scrape_and_save_data(url_objs, download_directory):
    """
    Iterates over url_objs and for each object, creates a folder named after its doc_id. 
    The contents of the folder are populated by the download_from_njstart function.

    Args:
    - url_objs (list): List of objects with keys 'url_to_scrape' and 'doc_id'.
    - download_directory (str): Base directory where data should be saved.
    
    Returns:
    None
    """

    # Iterate over each URL object
    for obj in url_objs:
        doc_id = obj['doc_id']
        url_to_scrape = obj['url_to_scrape']

        # Create a new directory for each doc_id
        doc_id_directory = os.path.join(download_directory, doc_id)
        if not os.path.exists(doc_id_directory):
            os.makedirs(doc_id_directory)

        # Download the data into the specific directory
        download_from_njstart(url_to_scrape, download_directory=doc_id_directory)


xls_file_path = '/home/localadmin/Desktop/njstartscrape/njstartscrape/bidSearchResults.xls'
download_directory = '/home/localadmin/Desktop/njstartscrape'
url_obj_to_scrape = get_urls_from_xls(xls_file_path)

# Call the function to start the scraping and saving process
scrape_and_save_data(url_obj_to_scrape, download_directory)