from bs4 import BeautifulSoup
import re

def chunk_pdfminer_html_grouped_with_metadata(html_path, group_size=3):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    divs = soup.find_all('div')

    page_pattern = re.compile(r'page\s+(\d+)', re.I)
    chunks = []

    current_page = None
    paragraph_num = 0
    paragraph_divs = []  

    all_paragraphs = [] 

    def flush_paragraph():
        nonlocal paragraph_divs, paragraph_num, current_page, all_paragraphs
        if paragraph_divs:
            paragraph_num += 1
            all_paragraphs.append({
                "page": current_page,
                "paragraph_num": paragraph_num,
                "divs": paragraph_divs
            })
            paragraph_divs = []

    for div in divs:
        text = div.get_text(separator=' ', strip=True).lower()
        match = page_pattern.search(text)
        if match:
            flush_paragraph()
            current_page = int(match.group(1))
            paragraph_num = 0 
            continue


        paragraph_divs.append(div)

    flush_paragraph()

    for para in all_paragraphs:
        divs_in_para = para["divs"]
        total_chunks_in_paragraph = (len(divs_in_para) + group_size - 1) // group_size
        for i in range(0, len(divs_in_para), group_size):
            group = divs_in_para[i:i+group_size]
            texts = [d.get_text(separator=' ', strip=True) for d in group if d.get_text(strip=True)]
            if texts:
                chunk = {
                    "page": para["page"],
                    "paragraph_num": para["paragraph_num"],
                    "chunks_in_paragraph": total_chunks_in_paragraph,
                    "heading": f"Page {para['page']} - Paragraph {para['paragraph_num']} - Chunk {(i // group_size) + 1} of {total_chunks_in_paragraph}",
                    "content": texts
                }
                chunks.append(chunk)

    return chunks


def save_chunks_to_file(chunks, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for idx, chunk in enumerate(chunks, 1):
            f.write(f"--- Chunk {idx} ---\n")
            f.write(f"Page: {chunk['page']}\n")
            f.write(f"Paragraph number: {chunk['paragraph_num']}\n")
            f.write(f"Chunks in paragraph: {chunk['chunks_in_paragraph']}\n")
            f.write(f"Heading: {chunk['heading']}\n\n")
            f.write("Content:\n")
            for paragraph in chunk["content"]:
                f.write(paragraph + "\n")
            f.write("\n----------------\n\n")


if __name__ == "__main__":
    chunks = chunk_pdfminer_html_grouped_with_metadata("output_cleaned.html")
    save_chunks_to_file(chunks, "output_chunks_semantic.txt")
    print(f"Saved {len(chunks)} chunks with metadata to 'output_chunks_semantic.txt'")
