from bs4 import BeautifulSoup

# HTML content to parse
html_content = """<div class="contents landing_ad-wrapper">
        <div class="container">
          <div class="row">
            <div class="col-sm-12">
              <h2 id="guide">Beginner's Guide to Python</h2>

<p>These tutorials will provide you with a solid foundation in Python and prepare you for your career goals.</p>

<div class="faq-section">
  <div class="accordion">
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Introduction</div>
      </div>
      <div class="accordion-body" style="height: 0.970874px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/getting-started">How to Get Started With Python?</a></p>
          <p><a href="/python-programming/first-program">Your First Python Program</a></p>
          <p><a href="/python-programming/comments">Python Comments</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item accordion__nodes--is-active">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Fundamentals</div>
      </div>
      <div class="accordion-body" style="height: 178px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/variables-constants-literals">Python Variables, Constants and Literals</a></p>
          <p><a href="/python-programming/type-conversion-and-casting">Python Type Conversion</a></p>
          <p><a href="/python-programming/input-output-import">Python Basic Input and Output</a></p>
          <p><a href="/python-programming/operators">Python Operators</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Flow Control</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/if-elif-else">Python if...else Statement</a></p>
          <p><a href="/python-programming/for-loop">Python for Loop</a></p>
          <p><a href="/python-programming/while-loop">Python while Loop</a></p>
          <p><a href="/python-programming/break-continue">Python break and continue</a></p>
          <p><a href="/python-programming/pass-statement">Python pass Statement</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Data Types</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/numbers">Python Numbers, Type Conversion and Mathematics</a></p>
          <p><a href="/python-programming/list">Python List</a></p>
          <p><a href="/python-programming/tuple">Python Tuple</a></p>
          <p><a href="/python-programming/set">Python Sets</a></p>
          <p><a href="/python-programming/dictionary">Python Dictionary</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Functions</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/function">Python Functions</a></p>
          <p><a href="/python-programming/function-argument">Python Function Arguments</a></p>
          <p><a href="/python-programming/global-local-nonlocal-variables">Python Variable Scope</a></p>
          <p><a href="/python-programming/global-keyword">Python Global Keyword</a></p>
          <p><a href="/python-programming/recursion">Python Recursion</a></p>
          <p><a href="/python-programming/modules">Python Modules</a></p>
          <p><a href="/python-programming/package">Python Package</a></p>
          <p><a href="/python-programming/main-function">Python Main function</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Files</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/directory">Python Directory and Files Management</a></p>
          <p><a href="/python-programming/csv">Python CSV: Read and Write CSV files</a></p>
          <p><a href="/python-programming/reading-csv-files">Reading CSV files in Python</a></p>
          <p><a href="/python-programming/writing-csv-files">Writing CSV files in Python</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Exception Handling</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/exceptions">Python Exceptions</a></p>
          <p><a href="/python-programming/exception-handling">Python Exception Handling</a></p>
          <p><a href="/python-programming/user-defined-exception">Python Custom Exceptions</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Object and Class</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/class">Python Objects and Classes</a></p>
          <p><a href="/python-programming/inheritance">Python Inheritance</a></p>
          <p><a href="/python-programming/multiple-inheritance">Python Multiple Inheritance</a></p>
          <p><a href="/python-programming/polymorphism">Polymorphism in Python</a></p>
          <p><a href="/python-programming/operator-overloading">Python Operator Overloading</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Advanced Topics</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/list-comprehension">List comprehension</a></p>
          <p><a href="/python-programming/anonymous-function">Python Lambda/Anonymous Function</a></p>
          <p><a href="/python-programming/iterator">Python Iterators</a></p>
          <p><a href="/python-programming/generator">Python Generators</a></p>
          <p><a href="/python-programming/namespace">Python Namespace and Scope</a></p>
          <p><a href="/python-programming/closure">Python Closures</a></p>
          <p><a href="/python-programming/decorator">Python Decorators</a></p>
          <p><a href="/python-programming/property">Python @property decorator</a></p>
          <p><a href="/python-programming/regex">Python RegEx</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Python Date and Time</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/datetime">Python datetime</a></p>
          <p><a href="/python-programming/datetime/strftime">Python strftime()</a></p>
          <p><a href="/python-programming/datetime/strptime">Python strptime()</a></p>
          <p><a href="/python-programming/datetime/current-datetime">How to get current date and time in Python?</a></p>
          <p><a href="/python-programming/datetime/current-time">Python Get Current Time</a></p>
          <p>
            <a href="/python-programming/datetime/timestamp-datetime">Python timestamp to datetime and vice-versa</a>
          </p>
          <p><a href="/python-programming/time">Python time Module</a></p>
          <p><a href="/python-programming/time/sleep">Python sleep()</a></p>
        </div>
      </div>
    </div>
    <div class="accordion__nodes accordion-item">
      <div class="accordion-header">
        <svg class="programiz-icon accordion-header__icon">
          <use xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right"></use>
        </svg>
        <div class="accordion-header__title">Additional Topic</div>
      </div>
      <div class="accordion-body" style="height: 0px;">
        <div class="editor-contents--accordion">
          <p><a href="/python-programming/precedence-associativity">Precedence and Associativity of Operators in Python</a></p>
          <p><a href="/python-programming/keywords-identifier">Python Keywords and Identifiers</a></p>
          <p><a href="/python-programming/assert-statement">Python Asserts</a></p>
          <p><a href="/python-programming/json">Python Json</a></p>
          <p><a href="/python-programming/pip">Python pip</a></p>
          <p><a href="/python-programming/args-and-kwargs">Python *args and **kwargs</a></p>
        </div>
      </div>
    </div>
  </div>
</div>
            </div>
          </div>

                      <div class="cornerstone_sidebar">
                
    
    
    
    <div id="programizcom47951"></div>
<div id="programizcom47950" style="place-content: space-evenly; flex-direction: column;"></div>

<style>
#programizcom47951, #programizcom47950 {
    display: none;
}

@media(min-width: 1024px) { #programizcom47951 {display: block;}}
@media(min-width: 1300px) { #programizcom47951 {display: none;} #programizcom47950{display: block; }   }

</style>

                </div>
                  </div>
      </div>"""  # Replace with the provided HTML

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Container for the course data
course_data = []

# Find all accordion nodes
accordion_items = soup.find_all('div', class_='accordion__nodes')
link_urls = []
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
import json
print(json.dumps(course_data, indent=4))

# print("data: ", course_data)
