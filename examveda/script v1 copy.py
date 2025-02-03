import requests
from bs4 import BeautifulSoup
import pandas as pd

import requests
from requests.exceptions import ConnectionError, Timeout

def checkConnection(base_url):
    try:
        response = requests.get(base_url, timeout=10)  # Add a timeout
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.content
    except ConnectionError:
        print("Failed to connect to the server. Please check your internet or the URL.")
    except Timeout:
        print("Request timed out. Please try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def get_sections_and_pages(base_url):
    """
    Extract sections and pages from the base URL.
    """
    sections_pages = []
    
    print("Connection response...")
    checkConnection(base_url)
    response = requests.get(base_url) 
    print("response of html is received...")
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract sections
    sections = soup.select('.page-content.chapter-section a')
    for section in sections:
        section_url = section['href']
        section_number = section_url.split('=')[-1] if 'section=' in section_url else '1'

        # Find the number of pages for this section
        current_page = 1
        while True:
            page_url = f"{section_url}&page={current_page}" if current_page > 1 else section_url
            page_response = requests.get(page_url)
            page_soup = BeautifulSoup(page_response.text, 'html.parser')

            if not page_soup.select('article.question.single-question'):
                break  # No more questions, stop pagination

            sections_pages.append((section_number, current_page, page_url))
            current_page += 1

    return sections_pages

def extract_mcqs(page_url):
    """
    Extract MCQs, options, answers, and explanations from a page.
    """
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    questions = soup.select('article.question.single-question')

    mcqs = []
    for question in questions:
        question_number = question.select_one('.question-number').text.strip()
        question_text = question.select_one('.question-main').text.strip()

        options = []
        for option in question.select('.question-options p label[for]'):
            options.append(option.text.strip()[2:].strip())  # Remove "A.", "B.", etc.

        answer = question.select_one('input[type="hidden"][id^="answer"]')['value']
        answer_text = f"Option {['A', 'B', 'C', 'D'][int(answer)-1]}"

        explanation = "No explanation given"
        explanation_div = question.select_one('.answer_container .page-content div')
        if explanation_div:
            explanation = explanation_div.text.strip()

        mcqs.append([question_number, question_text] + options + [answer_text, explanation])

    return mcqs

def save_to_excel(data, filename):
    """
    Save extracted data to an Excel file.
    """
    columns = ['Serial Number', 'Question', 'Option A', 'Option B', 'Option C', 'Option D', 'Answer', 'Explanation']
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    base_url = "https://www.examveda.com/civil-engineering/practice-mcq-question-on-theory-of-structures/"
    print("Getting Sections...")
    sections_pages = get_sections_and_pages(base_url)

    print("sections_pages length: ", len(sections_pages))
    all_mcqs = []
    for section, page, url in sections_pages:
        print(f"Scraping Section {section}, Page {page}...")
        mcqs = extract_mcqs(url)
        all_mcqs.extend(mcqs)

    save_to_excel(all_mcqs, "MCQs.xlsx")

if __name__ == "__main__":
    main()
