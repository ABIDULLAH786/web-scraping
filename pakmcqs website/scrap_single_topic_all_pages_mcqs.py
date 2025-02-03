import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_mcqs(url, start_idx):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    if soup.title.text == "Page not found - PakMcqs":
        print("Page title: ", soup.title.text)
        return None, start_idx

    all_mcqs = soup.find_all("article", class_="l-post grid-post grid-card-post")
    print("all_mcqs: ", len(all_mcqs))
    mcq_list = []
    for mcq in all_mcqs:
        item = {}
        item["#Sr."] = start_idx
        item["question"] = mcq.find('h2').text.strip()
        
        options_container = mcq.find("div", class_="excerpt")
        options_html = options_container.find('p')
        options = options_html.get_text(separator="\n").strip().split('\n')
        options = [opt.strip() for opt in options if opt.strip()]  # Remove empty options and strip extra spaces
        options = [opt[3:].strip() if len(opt) > 1 and opt[1] == '.' else opt for opt in options]  # Remove option labels

        # Ignore the options if the correct one is not found and place the cell empty
        correct_option_text = ""
        if options_html.find('strong') is not None:
            correct_option_text = options_html.find('strong').text.strip()
            correct_option_text = correct_option_text[3:].strip() if len(correct_option_text) > 1 and correct_option_text[1] == '.' else correct_option_text  # Remove option labels from correct option

        # Assign options to respective columns
        item["A"] = options[0] if len(options) > 0 else ""
        item["B"] = options[1] if len(options) > 1 else ""
        item["C"] = options[2] if len(options) > 2 else ""
        item["D"] = options[3] if len(options) > 3 else ""

        # Determine the correct option letter
        if correct_option_text == item["A"]:
            item["Ans"] = "A"
        elif correct_option_text == item["B"]:
            item["Ans"] = "B"
        elif correct_option_text == item["C"]:
            item["Ans"] = "C"
        elif correct_option_text == item["D"]:
            item["Ans"] = "D"
        else:
            item["Ans"] = ""

        if item["Ans"]:  # Only save MCQs that have an answer
            mcq_list.append(item)
        start_idx += 1
    print(f"\tTotal MCQS on current page is: ", len(mcq_list))
    return mcq_list, start_idx

current_page = 1
proceed = True
all_mcqs_data = []
start_idx = 1

while proceed:
    print("=> Scraping page: " + str(current_page))
    url = f"https://pakmcqs.com/category/pak-study-mcqs/page/{current_page}"
    mcqs_data, start_idx = scrape_mcqs(url, start_idx)
    # print("\t--> Scraping page data: ", len(mcqs_data))
    if mcqs_data is None:
        proceed = False
    else:
        all_mcqs_data.extend(mcqs_data)
        current_page += 1

# Create a DataFrame
df = pd.DataFrame(all_mcqs_data)

# Save the DataFrame to an Excel file
df.to_excel("mcqs.xlsx", index=False)

print("Scraping complete. Data saved to mcqs.xlsx.")
