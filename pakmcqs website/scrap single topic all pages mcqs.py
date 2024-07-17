import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_mcqs(url, start_idx):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    if soup.title.text == "Page not found - PakMcqs":
        return None, start_idx

    all_mcqs = soup.find_all("header", class_="entry-header entry-header-index")
    mcq_list = []

    for idx, mcq in enumerate(all_mcqs, start=1):
        item = {}
        item["#Sr."] = start_idx
        item["question"] = mcq.find('a').text.strip()
        
        options_html = mcq.find('p')
        options = options_html.get_text(separator="\n").strip().split('\n')
        options = [opt.strip() for opt in options if opt.strip()]  # Remove empty options and strip extra spaces
        options = [opt[3:].strip() if opt[1] == '.' else opt for opt in options]  # Remove option labels like "A.", "B."
        
        correct_option_text = ""
        if options_html.find('strong') is not None:
            correct_option_text = options_html.find('strong').text.strip()
            correct_option_text = correct_option_text[3:].strip() if correct_option_text[1] == '.' else correct_option_text  # Remove option labels from correct option

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
        
        mcq_list.append(item)
        start_idx += 1
    
    return mcq_list, start_idx

current_page = 1
proceed = True
all_mcqs_data = []
start_idx = 1

while proceed:
    print("Scraping page: " + str(current_page))
    url = f"https://pakmcqs.com/category/software-engineering-mcqs/software-engineering-types/page/{current_page}"
    mcqs_data, start_idx = scrape_mcqs(url, start_idx)
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
