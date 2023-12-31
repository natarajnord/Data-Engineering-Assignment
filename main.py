import csv

import requests
from bs4 import BeautifulSoup
from time import sleep  # Import the sleep function
import pytesseract
from PIL import Image
from io import BytesIO
from selenium import webdriver
from bs4 import BeautifulSoup




# For Archiexpo
def extract_company_name_from_archiexpo_selenium(url):
    company_names = []

    try:
        # Set up Selenium WebDriver
        driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in your PATH
        driver.get(url)

        # Wait for the page to load (you may need to adjust the sleep duration)
        driver.implicitly_wait(5)

        # Extract company names based on the provided CSS selector
        css_selector = 'td.xl63 a'
        extracted_company_names = extract_from_html(driver.page_source, css_selector)

        return extracted_company_names
    except Exception as e:
        print(f"Error extracting data from {url}: {e}")
        return []
    finally:
        # Close the WebDriver
        driver.quit()


# For austgaming


def extract_company_name_from_austgamingexpo(url):
    company_names = []

    try:
        # Make an HTTP request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the HTTP request
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract company names based on the provided CSS code
        company_names = [div['title'] for div in soup.select('.exhibitors__item[title]')]
    except Exception as e:
        print(f"Error extracting data from {url}: {e}")

    return company_names

#for KBB
def extract_from_html(html_content, css_selector):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.select(css_selector)
    extracted_info = [element.text.strip() for element in elements]
    return extracted_info

def extract_company_name_from_kbb_selenium(url):
    try:
        # Set up Selenium WebDriver
        driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in your PATH
        driver.get(url)

        # Wait for the page to load (you may need to adjust the sleep duration)
        driver.implicitly_wait(5)

        # Extract company names using the provided CSS selector
        css_selector = '.cmp-exhibitorlisting__listing-record-title--text'
        extracted_company_names = extract_from_html(driver.page_source, css_selector)

        return extracted_company_names
    except Exception as e:
        print(f"Error extracting data from {url}: {e}")
        return []
    finally:
        # Close the WebDriver
        driver.quit()






# Test the function



def extract_text_from_image_selenium(image_url):
    try:
        # Set up Selenium WebDriver
        driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in your PATH
        driver.get(image_url)

        # Wait for the image to load (you may need to adjust the sleep duration)
        driver.implicitly_wait(10)

        # Capture the screenshot
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(BytesIO(screenshot))

        # Use pytesseract for OCR
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ''
    finally:
        # Close the WebDriver
        driver.quit()

# Test the script with the provided websites
archiexpo_url = 'https://archiexpo.ie/a-z-listing/'
austgamingexpo_url = 'https://austgamingexpo.com/exhibitors/'
kbb_url = 'https://www.kbb.co.uk/en/exhibitors.html/'

company_names_archiexpo_selenium = extract_company_name_from_archiexpo_selenium(archiexpo_url)
company_names_austgamingexpo_selenium = extract_company_name_from_austgamingexpo(austgamingexpo_url)
company_names_kbb_selenium = extract_company_name_from_kbb_selenium(kbb_url)

# Display the results
print("Archiexpo Company Names (Selenium):")
for name in company_names_archiexpo_selenium:
    print(f"Company Name: {name}")
    print("=" * 30)

print("Austgamingexpo Company Names (Selenium):")
for name in company_names_austgamingexpo_selenium:
    print(f"Company Name: {name}")
    print("=" * 30)
print("KBB Company Names (Selenium):")
for name in company_names_kbb_selenium:
    print(f"Company Name: {name}")
    print("=" * 30)

# Save the results to a CSV file
with open('company names.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header
    csv_writer.writerow(['Website', 'Company Name'])

    # Write Archiexpo data
    for name in company_names_archiexpo_selenium:
        csv_writer.writerow(['Archiexpo', name])

    # Write Austgamingexpo data
    for name in company_names_austgamingexpo_selenium:
        csv_writer.writerow(['Austgamingexpo', name])

    # Write KBB data
    for name in company_names_kbb_selenium:
        csv_writer.writerow(['KBB', name])

# Display a message indicating that the data has been saved
print("Data has been saved to output.csv")