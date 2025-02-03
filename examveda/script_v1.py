import requests
from bs4 import BeautifulSoup

def check_for_sections(base_url):
    """Check if multiple sections exist."""
    response = requests.get(base_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Look for the section container
    section_container = soup.select_one('div.page-content.chapter-section')
    if not section_container:
        print("No sections found. Default single section assumed.")
        return 1  # Default single section

    # Count the number of sections
    sections = section_container.find_all('a')
    total_sections = len(sections)
    print(f"Total sections found: {total_sections}")
    return total_sections

def scrape_section_pages(base_url, section_number=None):
    """Iterate through pages of a section and scrape data."""
    page_number = 1
    while True:
        # Construct URL based on section and page numbers
        if section_number:
            section_url = f"{base_url}?section={section_number}&page={page_number}"
        else:
            section_url = f"{base_url}?page={page_number}"

        print(f"Visiting: {section_url}")
        response = requests.get(section_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for question articles
        question_articles = soup.select('article.question.single-question.question-type-normal')
        if not question_articles:
            print(f"No questions found on page {page_number}. Stopping.")
            break

        mcqs_list = []
        # Process each question article
        for question in question_articles:
            item = {}
            question_number = question.select_one('.question-number')
            question_text = question.select_one('h2')
            answer_container = question.select_one('.answer_container .page-content')

            if question_number and question_text:
                # print("question: ", question)
                question_number = question_number.text.strip()
                question_text = question_text.text.strip()
                # print(f"Question {question_number}: {question_text}")
                item["question"] = question_text

                options = question.select('.question-inner .question-options p')
                print("Options: ", len(options))
                # Assign options to respective columns
                item["A"] = options[0].select_one('label:nth-of-type(2)').text.strip() if len(options) > 0 else ""
                item["B"] = options[1].select_one('label:nth-of-type(2)').text.strip() if len(options) > 1 else ""
                item["C"] = options[2].select_one('label:nth-of-type(2)').text.strip() if len(options) > 2 else ""
                item["D"] = options[3].select_one('label:nth-of-type(2)').text.strip() if len(options) > 3 else ""
                print("item: ", item)
                # for option in options:
                #     label = option.select_one('label[for]')
                #     if label:
                #         print(f"- {label.text.strip()}")

                # Extract answer and solution
                if answer_container:
                    solution = answer_container.select_one('div:nth-of-type(2)').select_one("strong")
                    if solution:
                        solution_text = solution.text.strip()
                        item["Ans"] = solution_text
                        print(f"Solution: {solution_text}")
            else:
                print("Ad or empty content found, skipping.")

        # Process the questions
        # for question in questions:
        #     raw_question_num = question.select_one('.question-number')
        #     print("raw_question_num: ", raw_question_num)
        #     question_number = raw_question_num.text.strip()
        #     print("actual Question Number: ", question_number)
        #     question_text = question.select_one('h2').text.strip()
        #     print(f"Question {question_number}: {question_text}")

        # 
        page_number += 1
        print("Updating page number to : ", page_number)

def main():
    base_url = "https://www.examveda.com/civil-engineering/practice-mcq-question-on-theory-of-structures"

    # Step 1: Check for sections
    total_sections = check_for_sections(base_url)

    # Step 2: Scrape pages for each section
    if total_sections == 1:
        print("Scraping default single section...")
        scrape_section_pages(base_url)
    else:
        for section_number in range(1, total_sections + 1):
            print(f"Scraping section {section_number}...")
            scrape_section_pages(base_url, section_number)

if __name__ == "__main__":
    main()
