import requests
from bs4 import BeautifulSoup

current_page = 1
proceed = True

while proceed:
    url = "https://pakmcqs.com/category/software-engineering-mcqs/basics-of-software-engineering/page/" + str(current_page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("Title: " + str(soup.title))

    if soup.title.text == "Page not found - PakMcqs":
        proceed = False
    else:
        all_mcqs = soup.find_all("header", class_="entry-header entry-header-index")

        # Extracting each MCQ's info with all options and the correct option
        for mcq in all_mcqs:
            item = {}
            item["question"] = mcq.find('a').text.strip()
            
            options_html = mcq.find('p')
            options = options_html.get_text(separator="\n").strip().split('\n')
            correct_option = options_html.find('strong').text.strip()
            
            item["options"] = options
            item["correct_option"] = correct_option
            
            print("Question:", item["question"])
            print("Options:", item["options"])
            print("Correct Option:", item["correct_option"])
            print("\n")
            
    current_page += 1
