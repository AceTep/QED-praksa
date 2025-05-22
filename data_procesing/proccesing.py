from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
from bs4 import BeautifulSoup
import re

def pdf_to_clean_html(pdf_path, html_output_path):
    output_string = StringIO()
    laparams = LAParams()

    with open(pdf_path, 'rb') as pdf_file:
        extract_text_to_fp(
            pdf_file,
            output_string,
            laparams=laparams,
            output_type='html',
            codec=None,
            maxpages=30,
            page_numbers=range(30)
        )

    soup = BeautifulSoup(output_string.getvalue(), 'html.parser')

    for tag in soup.find_all(string=re.compile(r'OceanofPDF\.com', re.IGNORECASE)):
        parent = tag.find_parent()
        if parent:
            parent.decompose()

    for span in soup.find_all("span"):
        style = span.get("style", "")
        is_empty = not span.get_text(strip=True)
        if (
            "position:absolute" in style and
            "border" in style and
            is_empty
        ):
            span.decompose()

    title_pattern = re.compile(r"A GUIDE TO THE GUIDE")
    found = False

    for element in soup.body.find_all(recursive=False):
        if title_pattern.search(element.get_text()):
            found = True
            break
        else:
            element.decompose()

    if not found:
        print("A GUIDE TO THE GUIDE not found in the first 50 pages.")

    start_pattern = re.compile(r'^THE HITCHHIKER’S GUIDE TO THE GALAXY$')
    end_pattern = re.compile(r'^1')

    elements = soup.body.find_all(recursive=False)
    start_index = end_index = None

    for i, el in enumerate(elements):
        text = el.get_text(strip=True)
        if start_index is None and start_pattern.match(text):
            start_index = i
        elif start_index is not None and end_index is None and end_pattern.match(text):
            end_index = i
            break

    if start_index is not None and end_index is not None and start_index < end_index - 1:
        for el in elements[start_index + 1:end_index]:
            el.decompose()
    else:
        print("⚠️ Warning: Couldn't find valid range between start and end markers.")

    with open(html_output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(str(soup))

pdf_to_clean_html('knjiga.pdf', 'output_cleaned.html')
