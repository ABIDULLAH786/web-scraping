import requests
from bs4 import BeautifulSoup
import csv
import re

def extract_topic_name(url):
    match = re.search(r'topic/([^?]+)', url)
    if match:
        return match.group(1).replace('-', '_')
    return "mcqs"

def scrape_page(page_url):
    response = requests.get(page_url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_url}")
        return [], False

    soup = BeautifulSoup(response.content, 'html.parser')
    current_url = response.url

    # Check if the page URL is the same as the current URL to detect redirection
    if page_url != current_url:
        return [], False

    mcq_tables = soup.find_all('table', class_='w-full mcq_table')
    
    # Check if there are no MCQ tables found, indicating an invalid or empty page
    if not mcq_tables:
        return [], False

    mcqs = []

    for table in mcq_tables:
        question = table.find('h2').get_text(strip=True)
        options_rows = table.find('tbody').find_all('tr')
        options = [row.find_all('td')[1].get_text(strip=True) for row in options_rows]
        answer_text = table.find('tfoot').find('td').get_text(strip=True).split('Answer»')[-1].strip()
        
        # Determine the correct answer (A, B, C, or D)
        answer = ""
        for i, option in enumerate(options):
            if option in answer_text:
                answer = chr(65 + i)  # Convert index 0, 1, 2, 3 to 'A', 'B', 'C', 'D'

        # Ensure there are exactly 4 options
        options += [''] * (4 - len(options))

        mcqs.append({
            'question': question,
            'A': options[0],
            'B': options[1],
            'C': options[2],
            'D': options[3],
            'Ans': answer
        })

    return mcqs, True

def scrape_topic(base_url):
    all_mcqs = []
    page = 1
    while True:
        page_url = f"{base_url}{page}"
        mcqs, valid_page = scrape_page(page_url)
        if not valid_page:
            print(f"Reached non-existent page or end of pagination at page {page}. Stopping.")
            break
        all_mcqs.extend(mcqs)
        print(f"Scraped page {page}")
        page += 1

    return all_mcqs

def save_to_csv(mcqs, filename):
    fieldnames = ['question', 'A', 'B', 'C', 'D', 'Ans']
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(mcqs)

if __name__ == "__main__":
    topic_urls = [
        "https://mcqmate.com/topic/data-communication-and-networking?page=",
        "https://mcqmate.com/topic/computer-networking?page=",
        "https://mcqmate.com/topic/operating-system?page=",
        "https://mcqmate.com/topic/basics-of-database-management-system-dbms?page=",
        "https://mcqmate.com/topic/database-management-system?page=",
        "https://mcqmate.com/topic/advanced-database-management-systems?page=",
        "https://mcqmate.com/topic/data-structures?page=",
        "https://mcqmate.com/topic/design-and-analysis-of-algorithms?page=",
        "https://mcqmate.com/topic/basics-of-operating-system?page=",
        # Add more topic URLs as needed
    ]
    
    for base_url in topic_urls:
        topic_name = extract_topic_name(base_url)
        mcqs = scrape_topic(base_url)
        filename = f"{topic_name}_mcqs.csv"
        save_to_csv(mcqs, filename)
        print(f"Saved {len(mcqs)} MCQs to {filename}")
