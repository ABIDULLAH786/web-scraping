import pdfkit
import requests
from bs4 import BeautifulSoup
import json 
# Base URL for the course
base_url = "https://www.programiz.com"
course_url = "/python-programming"

# Make a request to fetch the HTML content of the main course page
response = requests.get(base_url + course_url)
if response.status_code != 200:
    print(f"Failed to fetch the page: {response.status_code}")
    exit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Container for the course data
course_data = []

# Find the main container with the specified classes
main_container = soup.find('div', class_='contents landing_ad-wrapper')
if not main_container:
    print("The specified container was not found on the page.")
    exit()

# Find all accordion nodes within the container
accordion_items = main_container.find_all('div', class_='accordion__nodes')

# Iterate over each accordion item to extract data
for item in accordion_items:
    # Extract the section title
    header = item.find('div', class_='accordion-header__title')
    section_title = header.get_text(strip=True) if header else ""

    # Extract all links under this section
    links = item.find_all('a')
    lessons = [
        {
            'title': link.get_text(strip=True),
            'url': link['href']
        }
        for link in links
    ]

    # Add to course data
    course_data.append({
        'section': section_title,
        'lessons': lessons
    })

# Save the webpage as a PDF for each section
for section in course_data:
    for lesson in section['lessons']:
        lesson_url = base_url + lesson['url'] if not lesson['url'].startswith('http') else lesson['url']
        print("fetching lesson...")
        lesson_response = requests.get(lesson_url)
        # print("response ", *lesson_response)

        if lesson_response.status_code != 200:
            print(f"Failed to fetch lesson: {lesson['title']} ({lesson_url})")
            continue

        # Save the page as a PDF using pdfkit
        filename = f"{section['section'].replace(' ', '_')}_{lesson['title'].replace(' ', '_')}.pdf"
        try:
            print("try to download the page: ", lesson_url)
            # print("try to download the page: ", lesson_response.text)
            pdfkit.from_string(lesson_response.text, filename)
            print(f"PDF saved: {filename}")
        except Exception as e:
            print(f"Failed to save PDF for {lesson['title']}: {e}")
