# Data Engineering Assignment(Problem statement 2)


## Overview

This Python script is designed for extracting exhibitor lists from various websites, such as Archiexpo, Austgamingexpo, and KBB. The script utilizes web scraping techniques, including Selenium, BeautifulSoup, and Tesseract OCR, to gather information about companies attending events. This README provides installation steps for the required Python packages and outlines the usage of the script.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/natarajnord/Data-Engineering-Assignment
   cd Data-Engineering-Assignment
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) installed and available in your system's PATH.

## Usage

1. **Run the Script:**
   ```bash
   python main.py
   ```

2. **Follow Instructions:**
   - The script will prompt you to visit the provided URLs for Archiexpo, Austgamingexpo, and KBB.
   - It will extract exhibitor information and display the results.
   - Extracted data will be saved to a CSV file named 'company names.csv'.

3. **Verify Output:**
   - Open the generated 'company names.csv' file to inspect the extracted data.

## Additional Notes

- This script is designed for educational purposes and may require adjustments for use on other websites.
- Ensure you comply with the terms of service of the websites you are scraping.

## License

This project is licensed under the [GPL-2.0 license](LICENSE). Feel free to modify and distribute the code as per the license terms.

---

Feel free to customize this README based on your project's specific details and requirements.
