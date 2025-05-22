from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re

def extract_paragraphs_with_metadata(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    divs = soup.find_all('div')
    page_pattern = re.compile(r'page\s+(\d+)', re.I)

    current_page = None
    paragraph_num = 0
    paragraph_divs = []

    all_paragraphs = []

    def flush_paragraph():
        nonlocal paragraph_divs, paragraph_num, current_page
        if paragraph_divs:
            paragraph_num += 1
            para_text = "\n".join(div.get_text(separator=' ', strip=True) for div in paragraph_divs if div.get_text(strip=True))
            all_paragraphs.append({
                "page": current_page,
                "paragraph_num": paragraph_num,
                "text": para_text
            })
            paragraph_divs = []

    for div in divs:
        text = div.get_text(separator=' ', strip=True)
        if not text:
            continue

        match = page_pattern.search(text)
        if match:
            flush_paragraph()  
            current_page = int(match.group(1))
            paragraph_num = 0
            continue

        paragraph_divs.append(div)

    flush_paragraph()

    return all_paragraphs


def chunk_text_with_metadata(paragraphs, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )

    chunks = []
    for para in paragraphs:
        para_chunks = splitter.split_text(para["text"])
        total_chunks = len(para_chunks)
        for idx, chunk_text in enumerate(para_chunks, 1):
            chunks.append({
                "page": para["page"],
                "paragraph_num": para["paragraph_num"],
                "chunks_in_paragraph": total_chunks,
                "chunk_index": idx,
                "text": chunk_text
            })
    return chunks


def save_chunks_to_file(chunks, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for chunk in chunks:
            f.write(f"--- Chunk {chunk['chunk_index']} of {chunk['chunks_in_paragraph']} ---\n")
            f.write(f"Page: {chunk['page']}\n")
            f.write(f"Paragraph number: {chunk['paragraph_num']}\n\n")
            f.write(chunk['text'].strip() + "\n\n")
            f.write("-------------------------\n\n")


if __name__ == "__main__":
    html_path = "output_cleaned.html"
    output_txt_path = "output_chunk_recursive_with_metadata.txt"

    paragraphs = extract_paragraphs_with_metadata(html_path)
    chunks = chunk_text_with_metadata(paragraphs)
    save_chunks_to_file(chunks, output_txt_path)

    print(f"Saved {len(chunks)} chunks with metadata to: {output_txt_path}")
