from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Function to save a webpage as a PDF using the print dialog
def save_page_as_pdf(url, output_pdf_path):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode (optional)
    chrome_options.add_argument('--disable-gpu')  # Disable GPU (optional)
    chrome_options.add_argument('--kiosk-printing')  # Enable silent printing
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Load the webpage
        driver.get(url)

        # Give the page time to load
        time.sleep(5)  # Adjust as necessary for slow-loading pages

        # Save the page as a PDF
        driver.execute_script('window.print();')
        
        print(f"Print dialog should appear. Save the file manually to: {output_pdf_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# URL to save as PDF
url = "https://www.programiz.com/python-programming/getting-started"  # Replace with your desired URL

# Call the function
save_page_as_pdf(url, "output.pdf")
