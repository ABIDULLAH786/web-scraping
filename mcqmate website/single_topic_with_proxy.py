import requests
from bs4 import BeautifulSoup
import csv
import re
from itertools import cycle

# Base URL of the topic
base_url = "https://mcqmate.com/topic/computer-networks/"

# List of proxies
proxies_list = [
    # "206.189.130.107:8080",
    # "15.207.196.77:3128",
    # "103.76.253.66:3129",
    "103.174.102.127:80",
    "103.155.54.26:83",
    "103.51.21.250:83",
    "103.78.170.13:83",
    "182.72.203.246:80",
    "103.125.154.233:8080",
    "103.243.114.206:8080",
    "103.134.165.38:8080",
    "59.92.70.176:3127",
    "103.242.119.88:80",
    "103.206.208.135:55443",
    "103.180.73.107:8080",
    "103.160.207.49:32650",
    "103.82.157.102:8080",
]
proxies_cycle = cycle(proxies_list)  # Cycle through proxies

def extract_topic_name(url):
    match = re.search(r'topic/([^?]+)', url)
    if match:
        return match.group(1).replace('-', '_')
    return "mcqs"

def scrape_page(page_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Rotate through proxies
        proxy = next(proxies_cycle)
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }

        print(f"Using proxy: {proxy}")
        response = requests.get(page_url, headers=headers, proxies=proxies, timeout=10, verify=False)

        if response.status_code != 200:
            print(f"Failed to retrieve page {page_url} with proxy {proxy}")
            return [], False

        soup = BeautifulSoup(response.content, 'html.parser')
        current_url = response.url
        # Check if the page URL is the same as the current URL to detect redirection
        if page_url != current_url:
            return [], False

        mcq_tables = soup.find_all('table', class_='w-full mcq_table')

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
    except Exception as e:
        print(f"Error for page {page_url} with proxy {proxy}: {e}")
        return [], False

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
    topic_name = extract_topic_name(base_url)
    print("Topic Name: %s" % topic_name)

    mcqs = scrape_topic(base_url)
    print("MCQs: %s" % len(mcqs))

    filename = f"{topic_name}_mcqs.csv"
    save_to_csv(mcqs, filename)
    print(f"Saved {len(mcqs)} MCQs to {filename}")
