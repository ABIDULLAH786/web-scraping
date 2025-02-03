import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.programiz.com"
ROUTES = [
    {
        "section": "Introduction",
        "lessons": [
            {
                "title": "How to Get Started With Python?",
                "url": "/python-programming/getting-started"
            },
            {
                "title": "Your First Python Program",
                "url": "/python-programming/first-program"
            },
            {
                "title": "Python Comments",
                "url": "/python-programming/comments"
            }
        ]
    },
    {
        "section": "Python Fundamentals",
        "lessons": [
            {
                "title": "Python Variables, Constants and Literals",
                "url": "/python-programming/variables-constants-literals"
            },
            {
                "title": "Python Type Conversion",
                "url": "/python-programming/type-conversion-and-casting"
            },
            {
                "title": "Python Basic Input and Output",
                "url": "/python-programming/input-output-import"
            },
            {
                "title": "Python Operators",
                "url": "/python-programming/operators"
            }
        ]
    },
    {
        "section": "Python Flow Control",
        "lessons": [
            {
                "title": "Python if...else Statement",
                "url": "/python-programming/if-elif-else"
            },
            {
                "title": "Python for Loop",
                "url": "/python-programming/for-loop"
            },
            {
                "title": "Python while Loop",
                "url": "/python-programming/while-loop"
            },
            {
                "title": "Python break and continue",
                "url": "/python-programming/break-continue"
            },
            {
                "title": "Python pass Statement",
                "url": "/python-programming/pass-statement"
            }
        ]
    },
    {
        "section": "Python Data Types",
        "lessons": [
            {
                "title": "Python Numbers, Type Conversion and Mathematics",
                "url": "/python-programming/numbers"
            },
            {
                "title": "Python List",
                "url": "/python-programming/list"
            },
            {
                "title": "Python Tuple",
                "url": "/python-programming/tuple"
            },
            {
                "title": "Python Sets",
                "url": "/python-programming/set"
            },
            {
                "title": "Python Dictionary",
                "url": "/python-programming/dictionary"
            }
        ]
    },
    {
        "section": "Python Functions",
        "lessons": [
            {
                "title": "Python Functions",
                "url": "/python-programming/function"
            },
            {
                "title": "Python Function Arguments",
                "url": "/python-programming/function-argument"
            },
            {
                "title": "Python Variable Scope",
                "url": "/python-programming/global-local-nonlocal-variables"
            },
            {
                "title": "Python Global Keyword",
                "url": "/python-programming/global-keyword"
            },
            {
                "title": "Python Recursion",
                "url": "/python-programming/recursion"
            },
            {
                "title": "Python Modules",
                "url": "/python-programming/modules"
            },
            {
                "title": "Python Package",
                "url": "/python-programming/package"
            },
            {
                "title": "Python Main function",
                "url": "/python-programming/main-function"
            }
        ]
    },
    {
        "section": "Python Files",
        "lessons": [
            {
                "title": "Python Directory and Files Management",
                "url": "/python-programming/directory"
            },
            {
                "title": "Python CSV: Read and Write CSV files",
                "url": "/python-programming/csv"
            },
            {
                "title": "Reading CSV files in Python",
                "url": "/python-programming/reading-csv-files"
            },
            {
                "title": "Writing CSV files in Python",
                "url": "/python-programming/writing-csv-files"
            }
        ]
    },
    {
        "section": "Python Exception Handling",
        "lessons": [
            {
                "title": "Python Exceptions",
                "url": "/python-programming/exceptions"
            },
            {
                "title": "Python Exception Handling",
                "url": "/python-programming/exception-handling"
            },
            {
                "title": "Python Custom Exceptions",
                "url": "/python-programming/user-defined-exception"
            }
        ]
    },
    {
        "section": "Python Object and Class",
        "lessons": [
            {
                "title": "Python Objects and Classes",
                "url": "/python-programming/class"
            },
            {
                "title": "Python Inheritance",
                "url": "/python-programming/inheritance"
            },
            {
                "title": "Python Multiple Inheritance",
                "url": "/python-programming/multiple-inheritance"
            },
            {
                "title": "Polymorphism in Python",
                "url": "/python-programming/polymorphism"
            },
            {
                "title": "Python Operator Overloading",
                "url": "/python-programming/operator-overloading"
            }
        ]
    },
    {
        "section": "Python Advanced Topics",
        "lessons": [
            {
                "title": "List comprehension",
                "url": "/python-programming/list-comprehension"
            },
            {
                "title": "Python Lambda/Anonymous Function",
                "url": "/python-programming/anonymous-function"
            },
            {
                "title": "Python Iterators",
                "url": "/python-programming/iterator"
            },
            {
                "title": "Python Generators",
                "url": "/python-programming/generator"
            },
            {
                "title": "Python Namespace and Scope",
                "url": "/python-programming/namespace"
            },
            {
                "title": "Python Closures",
                "url": "/python-programming/closure"
            },
            {
                "title": "Python Decorators",
                "url": "/python-programming/decorator"
            },
            {
                "title": "Python @property decorator",
                "url": "/python-programming/property"
            },
            {
                "title": "Python RegEx",
                "url": "/python-programming/regex"
            }
        ]
    },
    {
        "section": "Python Date and Time",
        "lessons": [
            {
                "title": "Python datetime",
                "url": "/python-programming/datetime"
            },
            {
                "title": "Python strftime()",
                "url": "/python-programming/datetime/strftime"
            },
            {
                "title": "Python strptime()",
                "url": "/python-programming/datetime/strptime"
            },
            {
                "title": "How to get current date and time in Python?",
                "url": "/python-programming/datetime/current-datetime"
            },
            {
                "title": "Python Get Current Time",
                "url": "/python-programming/datetime/current-time"
            },
            {
                "title": "Python timestamp to datetime and vice-versa",
                "url": "/python-programming/datetime/timestamp-datetime"
            },
            {
                "title": "Python time Module",
                "url": "/python-programming/time"
            },
            {
                "title": "Python sleep()",
                "url": "/python-programming/time/sleep"
            }
        ]
    },
    {
        "section": "Additional Topic",
        "lessons": [
            {
                "title": "Precedence and Associativity of Operators in Python",
                "url": "/python-programming/precedence-associativity"
            },
            {
                "title": "Python Keywords and Identifiers",
                "url": "/python-programming/keywords-identifier"
            },
            {
                "title": "Python Asserts",
                "url": "/python-programming/assert-statement"
            },
            {
                "title": "Python Json",
                "url": "/python-programming/json"
            },
            {
                "title": "Python pip",
                "url": "/python-programming/pip"
            },
            {
                "title": "Python *args and **kwargs",
                "url": "/python-programming/args-and-kwargs"
            }
        ]
    }
]

OUTPUT_DIR = "programiz_offline"

def download_page(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Save the HTML file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(soup))

        # Download CSS and JS files
        for tag in soup.find_all(["link", "script"]):
            src = tag.get("src") or tag.get("href")
            if src and not src.startswith("http"):
                src_url = f"{BASE_URL}{src}"
                download_resource(src_url, os.path.join(os.path.dirname(output_path), os.path.basename(src)))

    else:
        print(f"Failed to download {url}: Status Code {response.status_code}")

def download_resource(url, output_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed to download resource {url}: Status Code {response.status_code}")
    except Exception as e:
        print(f"Error downloading resource {url}: {e}")

def save_course_content(routes):
    for section in routes:
        section_name = section["section"].replace(" ", "_")
        section_dir = os.path.join(OUTPUT_DIR, section_name)
        os.makedirs(section_dir, exist_ok=True)

        for lesson in section["lessons"]:
            lesson_url = f"{BASE_URL}{lesson['url']}"
            lesson_title = lesson["title"].replace(" ", "_").replace("?", "")
            lesson_path = os.path.join(section_dir, f"{lesson_title}.html")

            print(f"Downloading {lesson['title']}...")
            download_page(lesson_url, lesson_path)

if __name__ == "__main__":
    save_course_content(ROUTES)
    print("Download complete.")
