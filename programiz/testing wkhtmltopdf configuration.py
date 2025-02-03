import pdfkit

# Specify the full path to wkhtmltopdf executable
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Replace this with the correct path

# Configure pdfkit to use this path
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Example usage of pdfkit
html_content = "https://www.programiz.com/python-programming"  # Your HTML content
editor_contents_html = """<div class="contents">
    <div class="container">
        <div class="row">
            <div class="col-sm-12 d-md-flex">
                <div class="right-bar">
                    <div class="editor-contents">
                        <h1>Python if...else Statement</h1>
                        <div id="node-64" class="node node-python clearfix" about="/python-programming/if-elif-else"
                            typeof="sioc:Item foaf:Document">
                            <div class="content">
                                <p id="introduction">In computer programming, the <code>if</code> statement is a
                                    conditional statement. It is used to execute a block of code only when a specific
                                    condition is met. For example, </p>

                                <p>Suppose we need to assign different grades to students based on their scores.</p>

                                <ol>
                                    <li>If a student scores above <strong>90</strong>, assign grade <strong>A</strong>
                                    </li>
                                    <li>If a student scores above <strong>75</strong>, assign grade <strong>B</strong>
                                    </li>
                                    <li>If a student scores above <strong>65</strong>, assign grade <strong>C</strong>
                                    </li>
                                </ol>

                                <p>These conditional tasks can be achieved using the <code>if</code> statement.</p>

                                <hr>
                                <h2 id="if">Python if Statement</h2>


                                <p>An <code>if</code> statement executes a block of code only when the specified
                                    condition is met. </p>

                                <p><strong>Syntax</strong></p>

                                <pre style="max-height: 600px;"><code class="python hljs"><span class="hljs-keyword">if</span> condition:
    <span class="hljs-comment"># body of if statement</span></code></pre>

                                <p>Here, <strong>condition</strong> is a boolean expression, such as
                                    <code>number &gt; 5</code>, that evaluates to either <code>True</code> or
                                    <code>False</code>.
                                </p>

                                <ul>
                                    <li>If <code>condition</code> evaluates to <code>True</code>, the body of the
                                        <code>if</code> statement is executed.
                                    </li>
                                    <li>If <code>condition</code> evaluates to <code>False</code>, the body of the
                                        <code>if</code> statement will be skipped from execution.
                                    </li>
                                </ul>

                                <p>Let's look at an example.</p>

                                <figure><img src="/sites/tutorial2program/files/python-if.png"
                                        title="Working of if Statement" alt="Working of if Statement" width=""
                                        height="">
                                    <figcaption>Working of if Statement</figcaption>
                                </figure>

                                <hr>
                                <h3 id="example">Example: Python if Statement</h3>

                                <div class="code-editor">
                                    <div class="code-editor__area">
                                        <div class="pre-code-wrapper">
                                            <div title="Click to copy" class="copy-code-button"></div>
                                            <pre class="python-exec"
                                                style="max-height: 600px;"><code class="python hljs">number = int(<span class="hljs-keyword">input</span>(<span class="hljs-string">'Enter a number: '</span>))

<span class="hljs-comment"># check if number is greater than 0</span>
<span class="hljs-keyword">if</span> number &gt; <span class="hljs-number">0</span>:
    <span class="hljs-keyword">print</span>(<span class="hljs-string">f'<span class="hljs-subst">{number}</span> is a positive number.'</span>)

<span class="hljs-keyword">print</span>(<span class="hljs-string">'A statement outside the if statement.'</span>)</code></pre>
                                        </div>
                                    </div>
                                    <div class="code-editor__action">
                                        <a href="/python-programming/online-compiler"
                                            class="btn btn--outlined-dark btn--smallest d-flex align-items-center run-code-button"
                                            target="_blank">
                                            Run Code <svg class="programiz-icon programiz-icon--small ml-2x">
                                                <use
                                                    xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevrons-right">
                                                </use>
                                            </svg>
                                        </a>
                                    </div>
                                </div>

                                <p><strong>Sample Output 1</strong></p>

                                <pre><samp>Enter a number: 10
10 is a positive number.
A statement outside the if statement.</samp></pre>

                                <p>If user enters <strong>10</strong>, the condition <code>number &gt; 0</code>
                                    evaluates to <code>True</code>. Therefore, the body of <code>if</code> is executed.
                                </p>


                                <p><strong>Sample Output 2</strong></p>

                                <pre><samp>Enter a number: -2
A statement outside the if statement.</samp></pre>

                                <p>If user enters <strong>-2</strong>, the condition <code>number &gt; 0</code>
                                    evaluates to <code>False</code>. Therefore, the body of <code>if</code> is skipped
                                    from execution.</p>

                                <hr>

                                <h3>Indentation in Python</h3>

                                <p>Python uses indentation to define a block of code, such as the body of an
                                    <code>if</code> statement. For example,
                                </p>

                                <div class="code-editor">
                                    <div class="code-editor__area">
                                        <div class="pre-code-wrapper">
                                            <div title="Click to copy" class="copy-code-button"></div>
                                            <pre class="python-exec" style="max-height: 600px;"><code class="python hljs">x = <span class="hljs-number">1</span>
total = <span class="hljs-number">0</span>

<span class="hljs-comment"># start of the if statement</span>
<span class="hljs-keyword">if</span> x != <span class="hljs-number">0</span>:
    total += x
    <span class="hljs-keyword">print</span>(total)  
<span class="hljs-comment"># end of the if statement</span>

<span class="hljs-keyword">print</span>(<span class="hljs-string">"This is always executed."</span>)</code></pre>
                                        </div>
                                    </div>
                                    <div class="code-editor__action">
                                        <a href="/python-programming/online-compiler"
                                            class="btn btn--outlined-dark btn--smallest d-flex align-items-center run-code-button"
                                            target="_blank">
                                            Run Code <svg class="programiz-icon programiz-icon--small ml-2x">
                                                <use
                                                    xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevrons-right">
                                                </use>
                                            </svg>
                                        </a>
                                    </div>
                                </div>

                                <p>Here, the body of <code>if</code> has two statements. We know this because two
                                    statements (immediately after <code>if</code>) start with indentation.</p>

                                <p>We usually use four spaces for indentation in Python, although any number of spaces
                                    works as long as we are consistent.</p>

                                <p>You will get an error if you write the above code like this:</p>

                                <div class="code-editor">
                                    <div class="code-editor__area">
                                        <div class="pre-code-wrapper">
                                            <div title="Click to copy" class="copy-code-button"></div>
                                            <pre class="python-exec" style="max-height: 600px;"><code class="python hljs"><span class="hljs-comment"># Error code</span>
x = <span class="hljs-number">1</span>
total = <span class="hljs-number">0</span>
        
<span class="hljs-keyword">if</span> x != <span class="hljs-number">0</span>:
total += x
<span class="hljs-keyword">print</span>(total)</code></pre>
                                        </div>
                                    </div>
                                    <div class="code-editor__action">
                                        <a href="/python-programming/online-compiler"
                                            class="btn btn--outlined-dark btn--smallest d-flex align-items-center run-code-button"
                                            target="_blank">
                                            Run Code <svg class="programiz-icon programiz-icon--small ml-2x">
                                                <use
                                                    xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevrons-right">
                                                </use>
                                            </svg>
                                        </a>
                                    </div>
                                </div>

                                <p>Here, we haven't used indentation after the <code>if</code> statement. In this case,
                                    Python thinks our <code>if</code> statement is empty, which results in an error.</p>

                                <hr>
                               
                                <figure><img src="/sites/tutorial2program/files/python-if-else.png"
                                        title="Working of if…else Statement" alt="Working of if…else Statement" width=""
                                        height="">
                                    <figcaption>Working of if…else Statement</figcaption>
                                </figure>
                                <div class="faq-section">
                                    <h2 class="section-title faq-section__title">More on Python if…else Statement
                                    </h2>
                                    <div class="container">
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="faq-area">
                                                    <div class="accordion">
                                                        <div class="accordion__nodes">
                                                            <div class="accordion-header"><span
                                                                    class="accordion-header__title">Compact
                                                                    <code>if</code> Statement

                                                                </span><svg
                                                                    class="programiz-icon accordion-header__icon">
                                                                    <use
                                                                        xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevron-right">
                                                                    </use>
                                                                </svg></div>
                                                            <div class="accordion-body">
                                                                <div class="editor-contents--accordion">
                                                                    <p>In certain situations, the <code>if</code>
                                                                        statement can be simplified into a single line.
                                                                        For example,</p>

                                                                    <div class="code-editor">
                                                                        <div class="code-editor__area">
                                                                            <div class="pre-code-wrapper">
                                                                                <div title="Click to copy"
                                                                                    class="copy-code-button"></div>
                                                                                <pre class="python-exec"
                                                                                    style="max-height: 600px;"><code class="python hljs">number = <span class="hljs-number">10</span>

<span class="hljs-keyword">if</span> number &gt; <span class="hljs-number">0</span>:
    <span class="hljs-keyword">print</span>(<span class="hljs-string">'Positive'</span>)</code></pre>
                                                                            </div>
                                                                        </div>
                                                                        <div class="code-editor__action">
                                                                            <a href="/python-programming/online-compiler"
                                                                                class="btn btn--outlined-dark btn--smallest d-flex align-items-center run-code-button"
                                                                                target="_blank">
                                                                                Run Code <svg
                                                                                    class="programiz-icon programiz-icon--small ml-2x">
                                                                                    <use
                                                                                        xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevrons-right">
                                                                                    </use>
                                                                                </svg>
                                                                            </a>
                                                                        </div>
                                                                    </div>

                                                                    <p>This code can be compactly written as</p>

                                                                    <div class="code-editor">
                                                                        <div class="code-editor__area">
                                                                            <div class="pre-code-wrapper">
                                                                                <div title="Click to copy"
                                                                                    class="copy-code-button"></div>
                                                                                <pre class="python-exec"
                                                                                    style="max-height: 600px;"><code class="python hljs">number = <span class="hljs-number">10</span>

<span class="hljs-keyword">if</span> number &gt; <span class="hljs-number">0</span>: <span class="hljs-keyword">print</span>(<span class="hljs-string">'Positive'</span>)</code></pre>
                                                                            </div>
                                                                        </div>
                                                                        <div class="code-editor__action">
                                                                            <a href="/python-programming/online-compiler"
                                                                                class="btn btn--outlined-dark btn--smallest d-flex align-items-center run-code-button"
                                                                                target="_blank">
                                                                                Run Code <svg
                                                                                    class="programiz-icon programiz-icon--small ml-2x">
                                                                                    <use
                                                                                        xlink:href="/sites/all/themes/programiz/assets/feather-sprite.svg#chevrons-right">
                                                                                    </use>
                                                                                </svg>
                                                                            </a>
                                                                        </div>
                                                                    </div>

                                                                    <p>This one-liner approach retains the same
                                                                        functionality but in a more concise format.</p>

                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <hr>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>"""
try:
    pdfkit.from_string(editor_contents_html, 'output.pdf', configuration=config)
except Exception as e:
    print("Error in saving file: ", e)