from bs4 import BeautifulSoup
import requests
import json

# URL to fetch the course data
course_url = "https://www.programiz.com/python-programming"

# Make a request to fetch the HTML content
response = requests.get(course_url)
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

# Print the structured course data
print(json.dumps(course_data, indent=4))
